"""
FastAPI Backend: Main application with /api/chat, /chatkit, and /health endpoints.
"""
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, Response
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from pydantic import BaseModel
import logging

from src.config.settings import settings
from src.rag.agent import query_agent
from src.api.chatkit_server import RagChatKitServer
from chatkit.server import StreamingResult

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

# Initialize ChatKit server
chatkit_server = RagChatKitServer()


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


@app.post("/chatkit")
@limiter.limit(settings.RATE_LIMIT)
async def chatkit_endpoint(request: Request):
    """
    ChatKit protocol endpoint for frontend integration.
    Processes ChatKit requests and returns streaming or JSON responses.

    Args:
        request: FastAPI request object (contains ChatKit protocol payload)

    Returns:
        StreamingResponse (SSE) or Response (JSON)
    """
    logger.info("Processing ChatKit request")

    try:
        # Process ChatKit request
        payload = await request.body()
        result = await chatkit_server.process(payload, {"request": request})

        # Return streaming response for SSE or JSON response
        if isinstance(result, StreamingResult):
            logger.info("Returning streaming response (SSE)")
            return StreamingResponse(result, media_type="text/event-stream")
        else:
            logger.info("Returning JSON response")
            return Response(content=result.json, media_type="application/json")

    except Exception as e:
        logger.error(f"Error in /chatkit endpoint: {e}")
        return Response(
            content=f'{{"error": "Internal server error: {str(e)}"}}',
            media_type="application/json",
            status_code=500
        )


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
