"""
FastAPI Backend: Main application with /api/chat, /chatkit, and /health endpoints.
"""
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from pydantic import BaseModel
import logging

from src.config.settings import settings
from src.rag.agent import query_agent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ChatKit disabled to prevent Gemini quota issues
CHATKIT_AVAILABLE = False
logger.info("ChatKit disabled - only /api/chat endpoint available")

# Initialize rate limiter
limiter = Limiter(key_func=get_remote_address)

# Create FastAPI app
app = FastAPI(
    title="RAG Chatbot API",
    description="Retrieval-Augmented Generation chatbot for Physical AI & Humanoid Robotics book",
    version="1.0.0"
)

# Add rate limiter to app state
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# ChatKit disabled - no initialization needed
chatkit_server = None


# Pydantic models
class ChatRequest(BaseModel):
    """Request model for /api/chat endpoint."""
    query: str
    selection_text: str = None


class ChatResponse(BaseModel):
    """Response model for /api/chat endpoint."""
    answer: str


@app.get("/health")
async def health():
    """
    Health check endpoint.

    Returns:
        dict: Health status
    """
    return {"status": "healthy"}


@app.post("/api/chat", response_model=ChatResponse)
@limiter.limit(settings.RATE_LIMIT)
async def chat(request: Request, body: ChatRequest):
    """
    Handle chat queries with RAG.

    Args:
        request: FastAPI request object (for rate limiting)
        body: ChatRequest with query and optional selection_text

    Returns:
        ChatResponse with answer
    """
    logger.info(f"Received query: {body.query[:50]}...")

    try:
        # Query agent
        answer =await query_agent(body.query, body.selection_text)

        return ChatResponse(answer=answer)

    except Exception as e:
        logger.error(f"Error in /api/chat: {e}")
        return ChatResponse(answer=f"I encountered an error: {str(e)}")


# ChatKit endpoint removed to prevent Gemini quota issues


@app.on_event("startup")
async def startup_event():
    """Run on application startup."""
    logger.info("="*80)
    logger.info("RAG CHATBOT API STARTED")
    logger.info(f"Collection: {settings.COLLECTION_NAME}")
    logger.info(f"Rate Limit: {settings.RATE_LIMIT}")
    logger.info(f"CORS Origins: {settings.CORS_ORIGINS}")
    logger.info("="*80)


@app.on_event("shutdown")
async def shutdown_event():
    """Run on application shutdown."""
    logger.info("RAG CHATBOT API STOPPED")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
