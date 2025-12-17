"""
RAG Ingestion Pipeline: Sitemap crawling, text extraction, chunking, embedding, and Qdrant storage.
"""
import re
import xml.etree.ElementTree as ET
from typing import List, Dict, Generator
import requests
from bs4 import BeautifulSoup
from langchain_text_splitters import RecursiveCharacterTextSplitter
import cohere
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import uuid
import logging

from src.config.settings import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_all_urls(sitemap_url: str) -> List[str]:
    """
    Parse sitemap.xml and extract all URLs.

    Args:
        sitemap_url: URL to sitemap.xml

    Returns:
        List of URLs extracted from sitemap
    """
    try:
        response = requests.get(sitemap_url, timeout=10)
        response.raise_for_status()

        # Parse XML
        root = ET.fromstring(response.content)

        # Extract URLs from <loc> tags
        # Handle namespace if present
        namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = []

        for url in root.findall('.//ns:loc', namespaces):
            url_text = url.text.strip()
            # Filter out non-content URLs (tags, categories, etc.)
            if not any(x in url_text for x in ['/tags/', '/categories/', '/search']):
                urls.append(url_text)

        logger.info(f"Extracted {len(urls)} URLs from sitemap")
        return urls

    except Exception as e:
        logger.error(f"Error fetching sitemap: {e}")
        return []


def extract_text_from_url(url: str) -> str:
    """
    Fetch HTML from URL and extract main content text.

    Args:
        url: URL to fetch

    Returns:
        Extracted plain text content
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.content, 'lxml')

        # Remove navigation, headers, footers, scripts, styles
        for tag in soup(['nav', 'header', 'footer', 'script', 'style', 'aside']):
            tag.decompose()

        # Extract main content (try common selectors)
        main_content = None
        for selector in ['article', 'main', '.content', '#content']:
            main_content = soup.select_one(selector)
            if main_content:
                break

        # Fall back to body if no main content found
        if not main_content:
            main_content = soup.body

        # Get text
        if main_content:
            text = main_content.get_text(separator='\n', strip=True)
            # Clean up extra whitespace
            text = re.sub(r'\n\s*\n', '\n\n', text)
            return text

        return ""

    except Exception as e:
        logger.error(f"Error extracting text from {url}: {e}")
        return ""


def chunk_text_generator(text: str, url: str) -> Generator[Dict, None, None]:
    """
    Chunk text into smaller pieces with overlap.

    Args:
        text: Text to chunk
        url: Source URL for metadata

    Yields:
        Dict with chunk text and metadata
    """
    # Handle very large texts by splitting first if needed
    max_text_length = 50000  # 50k chars max per text

    if len(text) > max_text_length:
        # Split into smaller sections
        sections = []
        for i in range(0, len(text), max_text_length):
            sections.append(text[i:i + max_text_length])
    else:
        sections = [text]

    # Initialize text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
        length_function=len,
    )

    chunk_index = 0
    total_chunks = 0

    # First pass to count total chunks
    for section in sections:
        chunks = text_splitter.split_text(section)
        total_chunks += len(chunks)

    # Second pass to yield chunks with metadata
    for section in sections:
        chunks = text_splitter.split_text(section)

        for chunk in chunks:
            yield {
                "text": chunk,
                "url": url,
                "chunk_index": chunk_index,
                "total_chunks": total_chunks
            }
            chunk_index += 1


def embed_chunks(chunks: List[str], co_client: cohere.Client) -> List[List[float]]:
    """
    Embed text chunks using Cohere.

    Args:
        chunks: List of text chunks to embed
        co_client: Cohere client

    Returns:
        List of embedding vectors (1024-dim)
    """
    if not chunks:
        return []

    # Cohere allows max 96 texts per request
    batch_size = 96
    all_embeddings = []

    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]

        try:
            response = co_client.embed(
                texts=batch,
                model=settings.COHERE_EMBED_MODEL,
                input_type=settings.COHERE_EMBED_INPUT_TYPE_DOCUMENT
            )
            all_embeddings.extend(response.embeddings)

        except Exception as e:
            logger.error(f"Error embedding batch {i//batch_size}: {e}")
            # Return zeros for failed batch
            all_embeddings.extend([[0.0] * settings.QDRANT_VECTOR_SIZE] * len(batch))

    return all_embeddings


def create_collection(collection_name: str, qdrant_client: QdrantClient):
    """
    Create Qdrant collection if it doesn't exist.

    Args:
        collection_name: Name of collection to create
        qdrant_client: Qdrant client
    """
    try:
        # Check if collection exists
        collections = qdrant_client.get_collections().collections
        if any(c.name == collection_name for c in collections):
            logger.info(f"Collection '{collection_name}' already exists")
            return

        # Create collection
        qdrant_client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=settings.QDRANT_VECTOR_SIZE,
                distance=Distance.COSINE
            )
        )
        logger.info(f"Created collection '{collection_name}'")

    except Exception as e:
        logger.error(f"Error creating collection: {e}")
        raise


def save_chunks_to_qdrant(
    chunks: List[Dict],
    embeddings: List[List[float]],
    collection_name: str,
    qdrant_client: QdrantClient
):
    """
    Upload chunks with embeddings to Qdrant.

    Args:
        chunks: List of chunk dictionaries with metadata
        embeddings: List of embedding vectors
        collection_name: Qdrant collection name
        qdrant_client: Qdrant client
    """
    if len(chunks) != len(embeddings):
        raise ValueError(f"Chunks ({len(chunks)}) and embeddings ({len(embeddings)}) length mismatch")

    # Batch upload (100 vectors at a time)
    batch_size = 100
    total_uploaded = 0

    for i in range(0, len(chunks), batch_size):
        batch_chunks = chunks[i:i + batch_size]
        batch_embeddings = embeddings[i:i + batch_size]

        points = []
        for chunk, embedding in zip(batch_chunks, batch_embeddings):
            point = PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={
                    "text": chunk["text"],
                    "url": chunk["url"],
                    "chunk_index": chunk["chunk_index"],
                    "total_chunks": chunk["total_chunks"]
                }
            )
            points.append(point)

        try:
            qdrant_client.upsert(
                collection_name=collection_name,
                points=points
            )
            total_uploaded += len(points)
            logger.info(f"Uploaded batch {i//batch_size + 1}: {total_uploaded}/{len(chunks)} chunks")

        except Exception as e:
            logger.error(f"Error uploading batch {i//batch_size}: {e}")

    logger.info(f"Total uploaded: {total_uploaded} chunks")


def ingest_book(sitemap_url: str, collection_name: str):
    """
    Main ingestion function: orchestrate entire RAG pipeline.

    Args:
        sitemap_url: URL to sitemap.xml
        collection_name: Qdrant collection name
    """
    # Validate settings
    settings.validate()

    # Initialize clients
    co_client = cohere.Client(settings.COHERE_API_KEY)
    qdrant_client = QdrantClient(
        url=settings.QDRANT_URL,
        api_key=settings.QDRANT_API_KEY
    )

    # Create collection
    create_collection(collection_name, qdrant_client)

    # Get all URLs
    logger.info(f"Fetching URLs from sitemap: {sitemap_url}")
    urls = get_all_urls(sitemap_url)

    if not urls:
        logger.error("No URLs found in sitemap")
        return

    total_chunks = 0
    failed_urls = []

    # Process each URL
    for idx, url in enumerate(urls, 1):
        logger.info(f"Processing URL {idx}/{len(urls)}: {url}")

        try:
            # Extract text
            text = extract_text_from_url(url)
            if not text:
                logger.warning(f"No text extracted from {url}")
                failed_urls.append(url)
                continue

            # Chunk text
            chunks = list(chunk_text_generator(text, url))
            if not chunks:
                logger.warning(f"No chunks generated from {url}")
                failed_urls.append(url)
                continue

            # Embed chunks
            chunk_texts = [c["text"] for c in chunks]
            embeddings = embed_chunks(chunk_texts, co_client)

            # Save to Qdrant
            save_chunks_to_qdrant(chunks, embeddings, collection_name, qdrant_client)

            total_chunks += len(chunks)
            logger.info(f"Completed {url}: {len(chunks)} chunks (total: {total_chunks})")

        except Exception as e:
            logger.error(f"Error processing {url}: {e}")
            failed_urls.append(url)

    # Summary
    logger.info("="*80)
    logger.info("INGESTION COMPLETE")
    logger.info(f"Total URLs processed: {len(urls)}")
    logger.info(f"Total chunks ingested: {total_chunks}")
    logger.info(f"Failed URLs: {len(failed_urls)}")
    if failed_urls:
        logger.info(f"Failed URL list: {failed_urls}")
    logger.info("="*80)
