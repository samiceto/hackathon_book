"""
OpenAI Agent with Gemini LLM: Direct API implementation for RAG question answering.
"""
import json
import logging
from openai import AsyncOpenAI

from src.config.settings import settings
from src.rag.retrieval import retrieve as retrieval_retrieve

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Gemini client as AsyncOpenAI provider
gemini_client = AsyncOpenAI(
    api_key=settings.GEMINI_API_KEY,
    base_url=settings.GEMINI_BASE_URL
)

# Agent instructions
AGENT_INSTRUCTIONS = """You are an AI tutor for the Physical AI & Humanoid Robotics textbook.
To answer the user question, first call the tool `retrieve` with the user query.
Use ONLY the returned content from `retrieve` to answer.
If the answer is not in the retrieved content, say "I don't know"."""

# Tool definition for OpenAI function calling
RETRIEVE_TOOL = {
    "type": "function",
    "function": {
        "name": "retrieve",
        "description": "Retrieve relevant book content for the query",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "User question or search query"
                }
            },
            "required": ["query"]
        }
    }
}


def retrieve_tool(query: str) -> str:
    """
    Retrieve relevant book content for the query.

    Args:
        query: User question or search query

    Returns:
        Concatenated text from top relevant chunks
    """
    try:
        result = retrieval_retrieve(query)
        logger.info(f"Retrieved content for query: {query[:50]}...")
        return result if result else "No relevant content found."
    except Exception as e:
        logger.error(f"Error in retrieve tool: {e}")
        return f"Error retrieving content: {str(e)}"


async def query_agent(user_query: str, selection_text: str = None) -> str:
    """
    Query the agent with optional selection context.

    Args:
        user_query: User question
        selection_text: Optional highlighted text from book

    Returns:
        Agent response
    """
    # Prepend selection context if provided
    if selection_text:
        context = f"Selected text: {selection_text}\n\nQuestion: {user_query}"
    else:
        context = user_query

    try:
        # Run agent with function calling
        result = await _run_agent_with_tools(context)
        logger.info(f"Generated answer for query: {user_query[:50]}...")
        return result

    except Exception as e:
        logger.error(f"Error querying agent: {e}")
        return f"I encountered an error processing your question: {str(e)}"


async def _run_agent_with_tools(user_input: str, max_iterations: int = 5) -> str:
    """
    Run agent with OpenAI function calling loop.

    Args:
        user_input: User query with optional selection context
        max_iterations: Maximum number of function call iterations

    Returns:
        Agent's final output
    """
    messages = [
        {"role": "system", "content": AGENT_INSTRUCTIONS},
        {"role": "user", "content": user_input}
    ]

    for iteration in range(max_iterations):
        # Call Gemini via OpenAI-compatible API
        response = await gemini_client.chat.completions.create(
            model=settings.GEMINI_MODEL,
            messages=messages,
            tools=[RETRIEVE_TOOL],
            tool_choice="auto"
        )

        message = response.choices[0].message
        messages.append(message.model_dump(exclude_unset=True))

        # Check if agent wants to call a function
        if message.tool_calls:
            for tool_call in message.tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)

                logger.info(f"Agent calling tool: {function_name} with args: {function_args}")

                # Execute the retrieve tool
                if function_name == "retrieve":
                    tool_result = retrieve_tool(function_args["query"])
                else:
                    tool_result = f"Unknown tool: {function_name}"

                # Add tool response to messages
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": tool_result
                })
        else:
            # No more tool calls - return final response
            return message.content or "I don't have an answer."

    # Max iterations reached
    logger.warning(f"Agent reached max iterations ({max_iterations})")
    return "I apologize, but I couldn't complete the task within the allowed steps."


# Create a dummy agent object for backwards compatibility (if needed elsewhere)
class Agent:
    """Dummy agent class for compatibility."""
    name = "Physical AI Tutor"
    instructions = AGENT_INSTRUCTIONS

agent = Agent()
