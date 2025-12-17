"""
Configuration settings loaded from environment variables.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    """Application settings loaded from environment variables."""

    # Cohere API
    COHERE_API_KEY: str = os.getenv("COHERE_API_KEY", "")

    # Qdrant Cloud
    QDRANT_URL: str = os.getenv("QDRANT_URL", "")
    QDRANT_API_KEY: str = os.getenv("QDRANT_API_KEY", "")

    # Gemini API
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

    # App Configuration
    COLLECTION_NAME: str = os.getenv("COLLECTION_NAME", "hackathon_book")
    SITEMAP_URL: str = os.getenv(
        "SITEMAP_URL",
        "https://samiceto.github.io/hackathon_book/sitemap.xml"
    )

    # Gemini Configuration
    GEMINI_BASE_URL: str = "https://generativelanguage.googleapis.com/v1beta/openai/"
    GEMINI_MODEL: str = "gemini-2.5-flash"

    # Cohere Configuration
    COHERE_EMBED_MODEL: str = "embed-english-v3.0"
    COHERE_EMBED_INPUT_TYPE_DOCUMENT: str = "search_document"
    COHERE_EMBED_INPUT_TYPE_QUERY: str = "search_query"

    # Qdrant Configuration
    QDRANT_VECTOR_SIZE: int = 1024
    QDRANT_DISTANCE: str = "Cosine"
    QDRANT_SEARCH_LIMIT: int = 5

    # Text Chunking Configuration
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200

    # Rate Limiting
    RATE_LIMIT: str = "10/minute"

    # CORS
    CORS_ORIGINS: list = [
        "https://samiceto.github.io",
        "http://localhost:3000"
    ]

    def validate(self):
        """Validate that all required environment variables are set."""
        required_vars = {
            "COHERE_API_KEY": self.COHERE_API_KEY,
            "QDRANT_URL": self.QDRANT_URL,
            "QDRANT_API_KEY": self.QDRANT_API_KEY,
            "GEMINI_API_KEY": self.GEMINI_API_KEY,
        }

        missing = [key for key, value in required_vars.items() if not value]

        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}"
            )


# Global settings instance
settings = Settings()
