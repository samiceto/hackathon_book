"""
Ingestion script: Run RAG pipeline to ingest book content into Qdrant.

Usage:
    python scripts/ingest_book.py
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.rag.ingestion import ingest_book
from src.config.settings import settings


if __name__ == "__main__":
    print("="*80)
    print("BOOK INGESTION PIPELINE")
    print("="*80)
    print(f"Sitemap URL: {settings.SITEMAP_URL}")
    print(f"Collection Name: {settings.COLLECTION_NAME}")
    print(f"Qdrant URL: {settings.QDRANT_URL}")
    print("="*80)
    print()

    # Run ingestion
    ingest_book(
        sitemap_url=settings.SITEMAP_URL,
        collection_name=settings.COLLECTION_NAME
    )
