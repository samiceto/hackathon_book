"""
Query Embedding & Retrieval: Embed queries and retrieve relevant chunks from Qdrant.
"""
from typing import List
import cohere
from qdrant_client import QdrantClient
import logging

from src.config.settings import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Lazy initialization of clients
_co_client = None
_qdrant_client = None


def get_cohere_client() -> cohere.Client:
    """Get or create Cohere client."""
    global _co_client
    if _co_client is None:
        _co_client = cohere.Client(settings.COHERE_API_KEY)
    return _co_client


def get_qdrant_client() -> QdrantClient:
    """Get or create Qdrant client."""
    global _qdrant_client
    if _qdrant_client is None:
        _qdrant_client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY
        )
    return _qdrant_client


def get_embedding(query: str) -> List[float]:
    """Embed query text using Cohere."""
    co_client = get_cohere_client()
    try:
        response = co_client.embed(
            texts=[query],
            model=settings.COHERE_EMBED_MODEL,
            input_type=settings.COHERE_EMBED_INPUT_TYPE_QUERY
        )
        return response.embeddings[0]
    except Exception as e:
        logger.error(f"Error embedding query: {e}")
        return [0.0] * settings.QDRANT_VECTOR_SIZE


def retrieve(query: str) -> str:
    """
    Retrieve relevant book content for the query.

    Args:
        query: User question

    Returns:
        Concatenated text from top relevant chunks
    """
    embedding = get_embedding(query)
    qdrant_client = get_qdrant_client()

    try:
        # Latest Qdrant client method
        results = qdrant_client.query_points(
            collection_name=settings.COLLECTION_NAME,
            query=embedding,
            limit=settings.QDRANT_SEARCH_LIMIT
        )

        chunks = [point.payload["text"] for point in results.points]
        formatted_text = "\n\n---\n\n".join(chunks)

        logger.info(f"Retrieved {len(chunks)} chunks for query: {query[:50]}...")
        return formatted_text

    except Exception as e:
        logger.error(f"Error retrieving from Qdrant: {e}")
        return ""
