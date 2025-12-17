"""
ChatKitServer: Wrapper for integrating our RAG agent with ChatKit frontend.
"""
import logging
from typing import AsyncIterator, Any
from datetime import datetime
from chatkit.server import ChatKitServer
from chatkit.types import (
    ThreadMetadata,
    UserMessageItem,
    ThreadStreamEvent,
    HiddenContextItem,
    WidgetItem,
)
from chatkit.actions import Action
from chatkit.agents import AgentContext, stream_agent_response
from chatkit.memory import InMemoryStore
from agents import Runner

from src.rag.agent import agent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RagChatKitServer(ChatKitServer):
    """
    ChatKit server implementation for Physical AI RAG chatbot.
    Wraps our existing agent with ChatKit protocol for frontend integration.
    """

    def __init__(self):
        """Initialize ChatKit server with in-memory store."""
        # Use InMemoryStore for simplicity (no persistent storage needed)
        store = InMemoryStore()
        super().__init__(store, attachment_store=None)
        logger.info("RagChatKitServer initialized")

    async def action(
        self,
        thread: ThreadMetadata,
        action: Action[str, Any],
        sender: WidgetItem | None,
        context: Any,
    ) -> AsyncIterator[ThreadStreamEvent]:
        """
        Handle custom actions from the frontend (e.g., text selection).

        Args:
            thread: Thread metadata
            action: Custom action with type and payload
            sender: Widget that sent the action (if any)
            context: Request context

        Yields:
            ThreadStreamEvent: Events to send to frontend
        """
        if action.type == "text_selection":
            # Store selected text as HiddenContextItem for next message
            selected_text = action.payload.get("text", "")
            logger.info(f"Received text selection: {selected_text[:100]}...")

            # Add HiddenContextItem to thread so agent can access it
            hidden = HiddenContextItem(
                id=self.store.generate_item_id("message", thread, context),
                thread_id=thread.id,
                created_at=datetime.now(),
                content=f"SELECTED_TEXT: {selected_text}"
            )
            await self.store.add_thread_item(thread.id, hidden, context)

            logger.info("Text selection stored as HiddenContextItem")
            # Don't yield any events - this is silent
            return

        # Unknown action type
        logger.warning(f"Unknown action type: {action.type}")
        return

    async def respond(
        self,
        thread: ThreadMetadata,
        input: UserMessageItem | None,
        context: Any,
    ) -> AsyncIterator[ThreadStreamEvent]:
        """
        Process user message and stream agent response as ChatKit events.

        Args:
            thread: Thread metadata (conversation context)
            input: User message item (contains query and optional selection)
            context: Request context (FastAPI request object, etc.)

        Yields:
            ThreadStreamEvent: ChatKit events for streaming to frontend
        """
        logger.info(f"Processing request for thread: {thread.id}")

        # Create AgentContext for ChatKit integration
        agent_context = AgentContext(
            thread=thread,
            store=self.store,
            request_context=context,
        )

        # Convert ChatKit input to agent input
        if input:
            # Extract user query from UserMessageItem
            user_query = ""
            if input.content:
                for content_item in input.content:
                    if hasattr(content_item, 'text'):
                        user_query += content_item.text

            # Check for recent HiddenContextItem with selected text
            selection_text = None
            try:
                # Get recent thread items to look for HiddenContextItem
                thread_items = await self.store.get_thread_items(thread.id, context)

                # Look for most recent HiddenContextItem with SELECTED_TEXT
                for item in reversed(thread_items.data):
                    if isinstance(item, HiddenContextItem):
                        content = str(item.content)
                        if content.startswith("SELECTED_TEXT: "):
                            selection_text = content.replace("SELECTED_TEXT: ", "")
                            logger.info(f"Found selected text: {selection_text[:100]}...")
                            # Remove the HiddenContextItem after using it (one-time use)
                            await self.store.delete_thread_item(thread.id, item.id, context)
                            break
            except Exception as e:
                logger.warning(f"Error retrieving HiddenContextItem: {e}")

            # Prepend selection context if found
            if selection_text:
                user_query = f"Selected text: {selection_text}\n\nQuestion: {user_query}"

            logger.info(f"User query: {user_query[:100]}...")

            # Run agent with streaming
            result = Runner.run_streamed(
                agent,
                user_query,
                context=agent_context,
            )

            # Stream agent response as ChatKit events
            async for event in stream_agent_response(agent_context, result):
                yield event
        else:
            # No input provided - this shouldn't happen in normal flow
            logger.warning("No input provided to respond method")
            return
