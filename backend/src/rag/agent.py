"""
OpenAI Agent with Gemini LLM: Agent setup with retrieval tool for RAG question answering.
"""
import asyncio
import logging
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, function_tool

from src.config.settings import settings
from src.rag.retrieval import retrieve as retrieval_retrieve

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Gemini client as AsyncOpenAI provider
gemini_provider = AsyncOpenAI(
    api_key=settings.GEMINI_API_KEY,
    base_url=settings.GEMINI_BASE_URL
)
print("gemini key",settings.GEMINI_API_KEY)
# Wrap provider in OpenAIChatCompletionsModel
gemini_model = OpenAIChatCompletionsModel(
    model=settings.GEMINI_MODEL,
    openai_client=gemini_provider
)

# Agent instructions
AGENT_INSTRUCTIONS = """
You are an AI tutor for the Physical AI & Humanoid Robotics textbook.
To answer the user question, first call the tool `retrieve` with the user query.
Use ONLY the returned content from `retrieve` to answer.
If the answer is not in the retrieved content, say "I don't know".
"""


@function_tool
def retrieve(query: str) -> str:
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


# Create agent with Gemini model and retrieve tool
agent = Agent(
    name="Physical AI Tutor",
    instructions=AGENT_INSTRUCTIONS,
    model=gemini_model,
    tools=[retrieve]
)


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
        # Run agent asynchronously
        result = await _run_agent_async(context)
        logger.info(f"Generated answer for query: {user_query[:50]}...")
        return result

    except Exception as e:
        logger.error(f"Error querying agent: {e}")
        return f"I encountered an error processing your question: {str(e)}"


async def _run_agent_async(user_input: str) -> str:
    """
    Run agent asynchronously using Runner.

    Args:
        user_input: User query with optional selection context

    Returns:
        Agent's final output
    """
    result = await Runner.run(agent, user_input)
    return result.final_output
    

