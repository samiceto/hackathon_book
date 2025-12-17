# Implementation Plan: Physical AI & Humanoid Robotics Book (Spec 1 Only)

**Feature**: Physical AI & Humanoid Robotics: From Simulated Brains to Walking Bodies
**Feature Branch**: `002-physical-ai-course`
**Created**: 2025-12-12
**Status**: Draft

---

## Chapter Structure & Overview

### Part I: Foundations
- Chapter 1: Introduction to Physical AI and Humanoid Robotics
- Chapter 2: Core Concepts in Robot Middleware
- Chapter 3: Human-Centered Design Principles

### Part II: Simulation Awareness
- Chapter 4: Digital Twins and Physics Simulation Concepts
- Chapter 5: Conceptual Overview of Simulation Technologies

### Part III: Perception & Cognitive Models
- Chapter 6: Sensor Integration and Data Processing
- Chapter 7: Basic Cognitive Models for Humanoids
- Chapter 8: Human-Robot Interaction Principles

### Part IV: Locomotion & Control Concepts
- Chapter 9: Introduction to Movement Control
- Chapter 10: Balance and Stability Concepts
- Chapter 11: Path Planning and Navigation Basics

### Part V: Conceptual Capstone
- Chapter 12: Integrating Physical AI Components
- Chapter 13: Ethical Considerations and Future Outlook

---

## Timeline (Conceptual Focus)

1. Draft Part I – Foundations: 2 weeks
2. Draft Part II – Simulation Awareness: 3 weeks
3. Draft Part III – Perception & Cognitive Models: 3 weeks
4. Draft Part IV – Locomotion & Control Concepts: 3 weeks
5. Draft Part V – Conceptual Capstone: 2 weeks
6. Review, Edit, and Compile Full Book: 2 weeks

---

## Risk Mitigation (Book-Focused)

- **Conceptual Gaps**: Use iterative reviews and expert feedback to ensure completeness.
- **Exercise Relevance**: Pilot exercises with target audience or colleagues to ensure they are understandable without hardware.
- **Timeliness**: Maintain consistent writing schedule to meet deadlines.
- **Clarity & Accuracy**: Technical advisors review chapters for correctness of high-level concepts.

---

# Spec 2: Integrated RAG Chatbot for Book

**Feature Extension**: `002-physical-ai-chatbot`
**Created**: 2025-12-16
**Status**: Draft
**Purpose**: Develop and embed a RAG chatbot directly inside the published book to answer reader questions using book content.

---

## Summary

This implementation plan covers the development of a Retrieval-Augmented Generation (RAG) chatbot embedded in the Physical AI & Humanoid Robotics book. The chatbot will:
- Retrieve answers strictly from the book's text using RAG
- Support text selection-based questions ("Ask about this selection")
- Operate entirely on free-tier infrastructure (Qdrant Cloud, free hosting)
- Integrate with existing ChatKit js frontend
- Use FastAPI backend with Gemini LLM for generation

**Technical Approach**:
1. Ingest book content from sitemap.xml
2. Chunk, embed (Cohere), and store in Qdrant Cloud Free Tier
3. Build OpenAI Agent SDK-based agent with Gemini LLM and retrieval tool
4. Integrate with ChatKit Python + FastAPI backend
5. Connect to existing ChatKit js frontend

---

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**:
- FastAPI (backend framework)
- Qdrant Client (vector storage)
- Cohere (embeddings: `embed-english-v3.0`)
- OpenAI Agent SDK (agent framework)
- Google Generative AI (Gemini LLM: `gemini-2.5-flash`)
- ChatKit Python (backend integration)
- BeautifulSoup4 / lxml (content extraction)
- python-dotenv (environment variables)

**Storage**:
- Qdrant Cloud Free Tier (vector database for embeddings)
- No persistent storage of user queries or PII

**Testing**: pytest (unit, integration, contract tests)
**Target Platform**: Linux server (free-tier hosting: Render, Railway, or similar)
**Project Type**: Web application (backend + frontend integration)
**Performance Goals**:
- <3s end-to-end query response time
- <500ms retrieval from Qdrant
- <2s LLM generation time

**Constraints**:
- Free-tier infrastructure only (Qdrant Cloud Free Tier, free hosting)
- No API key exposure client-side
- No PII storage
- Rate limiting: 10 requests/minute per IP
- Qdrant Free Tier: 1GB storage, 1M vectors max

**Scale/Scope**:
- ~200 book pages → ~500-1000 chunks
- Expected traffic: <100 users/day initially
- Max 10k queries/month (well within free tiers)

---

## Constitution Check (Phase 2)

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Core Principles (Phase 2 - from constitution.md)

- [x] **Content-accurate answers**: All responses rely strictly on book text + optional user-highlighted selections
- [x] **Lightweight, cost-efficient design**: Operates entirely within free-tier or near-zero-cost infrastructure

### Technical Standards (Phase 2 - from constitution.md)

- [x] **RAG Pipeline Requirements**: Text chunking, embeddings (Cohere), Qdrant Cloud Free Tier, retrieval → LLM generation
- [x] **Backend Requirements**: FastAPI, free-tier hosting, handles retrieval + context construction + model calls
- [x] **Frontend Integration Requirements**: ChatKit js (already integrated), embed widget/iframe, support highlight → "Ask about this selection"
- [x] **Security Requirements**: API keys server-side only, rate limiting per IP/session, no PII storage
- [x] **Reproducibility**: Single GitHub repo + `docker-compose.yml`

### Constraints (Phase 2 - from constitution.md)

- [x] **Hosting Constraints**: Free-tier or near-zero-cost hosting only
- [x] **Technical Constraints**: FastAPI backend on free-tier services only
- [x] **Security Constraints**: No user PII stored, API keys never client-side
- [x] **No Authentication**: Usable without login, account creation, or OAuth

**Constitution Status**: ✅ All checks pass. No violations to justify.

---

## Project Structure

### Documentation (this feature)

```text
specs/002-physical-ai-course/
├── spec.md              # Feature specification (Spec 2 section)
├── plan.md              # This file (Spec 2 section)
├── research.md          # Phase 0 output (Spec 2 section to be added)
├── data-model.md        # Phase 1 output (Spec 2 section to be added)
├── contracts/           # Phase 1 output (API contracts)
│   └── rag-api.yaml     # OpenAPI spec for RAG endpoints
└── tasks.md             # Phase 2 output (to be generated by /sp.tasks)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── ingestion.py        # Sitemap crawling, chunking, embedding, Qdrant ingestion
│   │   ├── retrieval.py        # Query embedding + Qdrant retrieval
│   │   └── agent.py            # OpenAI Agent SDK setup with Gemini LLM
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py             # FastAPI app entry point
│   │   ├── routes.py           # API endpoints (query, health check)
│   │   └── middleware.py       # Rate limiting, CORS, security headers
│   └── config/
│       ├── __init__.py
│       └── settings.py         # Environment variables, API keys
├── tests/
│   ├── unit/
│   │   ├── test_ingestion.py
│   │   ├── test_retrieval.py
│   │   └── test_agent.py
│   ├── integration/
│   │   ├── test_rag_pipeline.py
│   │   └── test_api_endpoints.py
│   └── contract/
│       └── test_api_contract.py
├── scripts/
│   └── ingest_book.py          # One-time ingestion script
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env.example

project/                        # ALREADY EXISTS - Docusaurus site (frontend)
├── src/
│   └── components/
│       └── ChatBot/            # ChatKit js integration already exists here
│           ├── ChatBot.js
│           └── chatbot.css
├── docusaurus.config.js
├── package.json
└── (existing Docusaurus structure)

specs/
└── 002-physical-ai-course/
    ├── spec.md
    ├── plan.md
    ├── research.md
    ├── data-model.md
    ├── contracts/
    └── tasks.md
```

**Structure Decision**: Web application with backend + frontend separation.
- **backend/** (NEW - to be created): FastAPI backend handling RAG pipeline, agent, and API endpoints
- **project/** (ALREADY EXISTS): Docusaurus site with ChatKit js integration already in place
- No separate `frontend/` folder needed - `project/` serves as the frontend

---

## Complexity Tracking

> No violations of Constitution Check. This section is empty.

---

## Phase 0: Research & Clarifications

### Research Tasks

#### 1. Sitemap Crawling & Content Extraction
**Decision**: Use `requests` + `BeautifulSoup4` for sitemap parsing and content extraction
**Rationale**:
- Sitemap.xml provides structured URL list
- BeautifulSoup4 handles HTML parsing efficiently
- Simple, no need for heavy frameworks like Scrapy

**Alternatives Considered**:
- Scrapy: Overkill for single sitemap crawling
- Manual crawling: Error-prone, not maintainable

**Implementation Details**:
- Parse sitemap.xml to extract all URLs
- Fetch each page HTML
- Extract main content (skip navigation, headers, footers)
- Handle encoding and special characters

---

#### 2. Text Chunking Strategy
**Decision**: Recursive character splitting with 1000-char chunks, 200-char overlap
**Rationale**:
- 1000 chars ≈ 250 tokens (within Cohere embedding limits)
- 200-char overlap preserves context across chunks
- Handles code blocks, lists, and paragraphs gracefully

**Alternatives Considered**:
- Sentence-based chunking: Can split code examples awkwardly
- Fixed-size chunking (no overlap): Loses context at boundaries

**Implementation Details**:
- Use LangChain `RecursiveCharacterTextSplitter`
- Preserve metadata: URL, chunk index, total chunks per page
- Handle edge case: very large pages (split into smaller chunks if >10k chars)

---

#### 3. Cohere Embeddings Configuration
**Decision**: Use `embed-english-v3.0` model with `search_document` input type
**Rationale**:
- `embed-english-v3.0` is Cohere's latest and most accurate model
- `search_document` optimized for indexing (vs `search_query` for queries)
- 1024 dimensions (good balance of accuracy and storage)

**Alternatives Considered**:
- OpenAI embeddings: More expensive, no free tier
- Sentence Transformers: Self-hosted, but increases infrastructure complexity

**Implementation Details**:
- Batch embed chunks (max 96 texts/request to stay within Cohere limits)
- Cache embeddings to avoid re-processing during development
- Use `search_query` input type for user queries (different from `search_document`)

---

#### 4. Qdrant Cloud Configuration
**Decision**: Qdrant Cloud Free Tier with `Cosine` similarity
**Rationale**:
- Free Tier: 1GB storage, 1M vectors (sufficient for ~500-1000 chunks)
- Cosine similarity is standard for text embeddings
- Managed service (no infrastructure overhead)

**Alternatives Considered**:
- Self-hosted Qdrant: Adds infrastructure cost and complexity
- Pinecone: No generous free tier
- Chroma: Self-hosted only (no managed option)

**Implementation Details**:
- Create collection: `hackathon_book` with 1024-dim vectors
- Store metadata: `url`, `chunk_index`, `text`
- Index for fast retrieval (HNSW algorithm by default)

---

#### 5. OpenAI Agent SDK with Gemini LLM
**Decision**: Use OpenAI Agent SDK with Gemini 2.5 Flash via OpenAI-compatible API
**Rationale**:
- Gemini 2.5 Flash: Fast, affordable, high-quality responses
- OpenAI Agent SDK: Provides tool calling, structured workflows
- Gemini offers OpenAI-compatible API endpoint

**Alternatives Considered**:
- LangChain Agents: More complex, heavier framework
- Direct Gemini API: No tool calling framework, manual orchestration

**Implementation Details**:
- Set Gemini base URL: `https://generativelanguage.googleapis.com/v1beta/openai/`
- Model: `gemini-2.5-flash`
- Disable tracing: `set_tracing_disabled(disabled=True)`
- Define retrieval tool with function calling

---

#### 6. Rate Limiting Strategy
**Decision**: SlowAPI with 10 requests/minute per IP
**Rationale**:
- Prevents abuse while allowing legitimate usage
- IP-based (no authentication required)
- SlowAPI integrates seamlessly with FastAPI

**Alternatives Considered**:
- Redis-based rate limiting: Adds infrastructure dependency
- No rate limiting: Risk of abuse and cost overruns

**Implementation Details**:
- Use `slowapi` library
- Limit: `10/minute` per IP
- Return 429 status code with `Retry-After` header

---

#### 7. ChatKit Integration
**Decision**: Use ChatKit Python backend with FastAPI endpoint
**Rationale**:
- ChatKit Python provides FastAPI integration out-of-box
- Frontend (ChatKit js) already integrated
- Simplifies backend-frontend connection

**Alternatives Considered**:
- Custom WebSocket implementation: More complex, reinventing wheel
- REST-only (no streaming): Poor UX for long responses

**Implementation Details**:
- Install `chatkit` Python package
- Create `/api/chat` endpoint
- Stream responses to frontend
- Support text selection context via request body

---

### Phase 0 Output: research.md

**Action**: Create `specs/002-physical-ai-course/research.md` with all decisions documented above.

---

## Phase 1: Architecture & Design

### 1. Data Model

#### Entities

**1. BookChunk**
```python
class BookChunk:
    id: str                    # UUID
    url: str                   # Source page URL
    text: str                  # Chunk text content
    chunk_index: int           # Index within page
    total_chunks: int          # Total chunks for this page
    embedding: List[float]     # 1024-dim vector (Cohere embed-english-v3.0)
    metadata: dict             # Additional metadata (page title, section, etc.)
```

**2. QueryRequest**
```python
class QueryRequest:
    query: str                 # User question
    selection_text: str | None # Optional highlighted text
    session_id: str | None     # Optional session tracking (not stored)
```

**3. QueryResponse**
```python
class QueryResponse:
    answer: str                # LLM-generated answer
    sources: List[Source]      # Retrieved chunks with URLs
    confidence: float          # Retrieval confidence score
```

**4. Source**
```python
class Source:
    url: str                   # Source page URL
    text: str                  # Chunk text
    relevance_score: float     # Similarity score
```

---

### 2. System Architecture

```text
┌─────────────────┐
│  Docusaurus     │
│  Book Site      │
│  (Frontend)     │
└────────┬────────┘
         │ ChatKit js widget
         │ POST /api/chat
         ▼
┌─────────────────────────────────────────┐
│           FastAPI Backend               │
│                                         │
│  ┌──────────────────────────────────┐  │
│  │  Rate Limiter (10 req/min/IP)   │  │
│  └──────────────┬───────────────────┘  │
│                 ▼                       │
│  ┌──────────────────────────────────┐  │
│  │  /api/chat Endpoint              │  │
│  │  - Receive query + selection     │  │
│  │  - Call agent.query()            │  │
│  │  - Stream response to frontend   │  │
│  └──────────────┬───────────────────┘  │
│                 ▼                       │
│  ┌──────────────────────────────────┐  │
│  │  OpenAI Agent (Gemini 2.5 Flash) │  │
│  │  - Tool: retrieve()              │  │
│  │  - Instructions: answer from     │  │
│  │    retrieved content only        │  │
│  └──────────────┬───────────────────┘  │
│                 ▼                       │
│  ┌──────────────────────────────────┐  │
│  │  Retrieval Module                │  │
│  │  1. Embed query (Cohere)         │  │
│  │  2. Query Qdrant (top 5)         │  │
│  │  3. Return chunks as text        │  │
│  └──────────────┬───────────────────┘  │
└─────────────────┼───────────────────────┘
                  ▼
         ┌────────────────┐
         │ Qdrant Cloud   │
         │ Free Tier      │
         │ (Vector Store) │
         └────────────────┘

Ingestion Pipeline (one-time):
┌──────────────────┐
│ Sitemap.xml      │
│ https://...      │
│ /sitemap.xml     │
└────────┬─────────┘
         ▼
┌────────────────────────┐
│ Ingestion Script       │
│ 1. get_all_urls()      │
│ 2. extract_text()      │
│ 3. chunk_text()        │
│ 4. embed (Cohere)      │
│ 5. save_to_qdrant()    │
└────────────────────────┘
```

---

### 3. API Contracts

**File**: `specs/002-physical-ai-course/contracts/rag-api.yaml`

```yaml
openapi: 3.0.0
info:
  title: RAG Chatbot API
  version: 1.0.0
  description: API for book content question answering

servers:
  - url: https://api.example.com
    description: Production server
  - url: http://localhost:8000
    description: Local development

paths:
  /api/chat:
    post:
      summary: Submit a question to the chatbot
      description: Query the book content using RAG
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - query
              properties:
                query:
                  type: string
                  description: User question
                  example: "What is Physical AI?"
                selection_text:
                  type: string
                  nullable: true
                  description: Optional highlighted text for context
                  example: "Physical AI involves embodied agents..."
      responses:
        '200':
          description: Successful response with answer
          content:
            application/json:
              schema:
                type: object
                properties:
                  answer:
                    type: string
                    description: LLM-generated answer
                  sources:
                    type: array
                    items:
                      type: object
                      properties:
                        url:
                          type: string
                        text:
                          type: string
                        relevance_score:
                          type: number
        '429':
          description: Rate limit exceeded
          headers:
            Retry-After:
              schema:
                type: integer
              description: Seconds to wait before retry
        '500':
          description: Internal server error

  /health:
    get:
      summary: Health check endpoint
      responses:
        '200':
          description: Service is healthy
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    example: "healthy"
```

---

### 4. Quickstart Guide

**File**: `specs/002-physical-ai-course/quickstart.md`

```markdown
# RAG Chatbot Quickstart

## Prerequisites
- Python 3.11+
- Qdrant Cloud Free Tier account
- Cohere API key (free tier)
- Gemini API key (free tier)

## Environment Setup


2. .env file already available
## Ingestion (One-Time)

```bash
cd backend
python scripts/ingest_book.py
```

This will:
- Fetch all pages from sitemap.xml
- Chunk text (1000 chars, 200 overlap)
- Embed with Cohere
- Store in Qdrant Cloud

## Run Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn src.api.main:app --reload
```

Backend runs at `http://localhost:8000`

## Test API

```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "What is Physical AI?"}'
```

## Deploy

```bash
docker-compose up -d
```

Deploys to free-tier hosting (Render).
```

---

## Phase 2: Implementation Plan

### Step 1: RAG Ingestion Pipeline

**File**: `backend/src/rag/ingestion.py`

**Functions to Implement**:

1. **`get_all_urls(sitemap_url: str) -> List[str]`**
   - Parse sitemap.xml
   - Extract all `<loc>` URLs
   - Filter out non-content URLs (e.g., /tags/, /categories/)

2. **`extract_text_from_url(url: str) -> str`**
   - Fetch HTML with `requests`
   - Parse with BeautifulSoup4
   - Extract main content (e.g., `<article>`, `<main>`)
   - Strip navigation, headers, footers
   - Return plain text

3. **`chunk_text_generator(text: str, url: str) -> Generator[Dict, None, None]`**
   - Use `RecursiveCharacterTextSplitter` (1000 chars, 200 overlap)
   - Handle memory: yield chunks instead of loading all at once
   - Metadata: `url`, `chunk_index`, `total_chunks`
   - Handle large pages: split if >10k chars

4. **`embed_chunks(chunks: List[str]) -> List[List[float]]`**
   - Call Cohere API with `embed-english-v3.0`
   - Batch: max 96 chunks per request
   - Input type: `search_document`
   - Return 1024-dim vectors

5. **`create_collection(collection_name: str)`**
   - Create Qdrant collection: `hackathon_book`
   - Vector size: 1024
   - Distance: `Cosine`
   - Skip if exists

6. **`save_chunks_to_qdrant(chunks: List[Dict])`**
   - Upload chunks with embeddings to Qdrant
   - Metadata: `url`, `text`, `chunk_index`
   - Batch upload: 100 vectors at a time

7. **`ingest_book(sitemap_url: str, collection_name: str)`** (Main function)
   - Call `get_all_urls()`
   - For each URL: `extract_text_from_url()` → `chunk_text_generator()` → `embed_chunks()` → `save_chunks_to_qdrant()`
   - Progress logging
   - Error handling: skip failed URLs, log errors

**Configuration**:
```python
sitemap_url = "https://samiceto.github.io/hackathon_book/sitemap.xml"
collection_name = "hackathon_book"
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
embed_model = "embed-english-v3.0"
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
```

---

### Step 2: OpenAI Agent Setup with Gemini LLM

**File**: `backend/src/rag/agent.py`

**Implementation**:

1. **Setup Gemini Client**:
   ```python
   from openai import OpenAI
   from openai_agent_sdk import set_tracing_disabled

   set_tracing_disabled(disabled=True)

   client = OpenAI(
       base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
       api_key=os.getenv("GEMINI_API_KEY")
   )
   ```

2. **Define Retrieval Tool**:
   ```python
   def retrieve(query: str) -> str:
       """
       Retrieve relevant book content for the query.

       Args:
           query: User question

       Returns:
           Concatenated text from top 5 relevant chunks
       """
       # Embed query with Cohere (input_type="search_query")
       embedding = get_embedding(query)

       # Query Qdrant
       results = qdrant_client.search(
           collection_name="hackathon_book",
           query_vector=embedding,
           limit=5
       )

       # Format results
       chunks = [hit.payload["text"] for hit in results]
       return "\n\n---\n\n".join(chunks)
   ```

3. **Create Agent**:
   ```python
   from openai_agent_sdk import Agent

   agent = Agent(
       model="gemini-2.5-flash",
       client=client,
       tools=[retrieve],
       instructions="""
       You are an AI tutor for the Physical AI & Humanoid Robotics textbook.
       To answer the user question, first call the tool `retrieve` with the user query.
       Use ONLY the returned content from `retrieve` to answer.
       If the answer is not in the retrieved content, say "I don't know".
       """
   )
   ```

4. **Query Function**:
   ```python
   def query_agent(user_query: str, selection_text: str | None = None) -> str:
       """
       Query the agent with optional selection context.

       Args:
           user_query: User question
           selection_text: Optional highlighted text

       Returns:
           Agent response
       """
       # Prepend selection context if provided
       if selection_text:
           context = f"Selected text: {selection_text}\n\nQuestion: {user_query}"
       else:
           context = user_query

       # Run agent
       response = agent.run(context)
       return response.text
   ```

---

### Step 3: FastAPI Backend + ChatKit Integration

**File**: `backend/src/api/main.py`

**Implementation**:

1. **FastAPI App Setup**:
   ```python
   from fastapi import FastAPI, Request
   from fastapi.middleware.cors import CORSMiddleware
   from slowapi import Limiter, _rate_limit_exceeded_handler
   from slowapi.util import get_remote_address
   from slowapi.errors import RateLimitExceeded

   limiter = Limiter(key_func=get_remote_address)
   app = FastAPI()
   app.state.limiter = limiter
   app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

   # CORS for frontend
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["https://samiceto.github.io", "http://localhost:3000"],
       allow_methods=["POST", "GET"],
       allow_headers=["*"],
   )
   ```

2. **Chat Endpoint**:
   ```python
   from pydantic import BaseModel
   from src.rag.agent import query_agent

   class ChatRequest(BaseModel):
       query: str
       selection_text: str | None = None

   class ChatResponse(BaseModel):
       answer: str

   @app.post("/api/chat", response_model=ChatResponse)
   @limiter.limit("10/minute")
   async def chat(request: Request, body: ChatRequest):
       """
       Handle chat queries.
       """
       answer = query_agent(body.query, body.selection_text)
       return ChatResponse(answer=answer)
   ```

3. **Health Check**:
   ```python
   @app.get("/health")
   async def health():
       return {"status": "healthy"}
   ```

4. **ChatKit Integration** (if using ChatKit Python):
   ```python
   from chatkit import ChatKit

   chatkit = ChatKit(
       agent=query_agent,
       streaming=True
   )

   app.mount("/chatkit", chatkit.get_app())
   ```

---

### Step 4: Frontend Integration (ChatKit js)

**File**: `project/src/components/ChatBot/ChatBot.js` (already exists)

**Verification**:
- Confirm ChatKit js is configured to call `/api/chat`
- Test "Ask about this selection" flow
- Ensure API endpoint is correct

**No code changes needed** if ChatKit js already integrated correctly.

---

### Step 5: Environment Configuration

**File**: `backend/.env.example`

```bash
# Cohere API
COHERE_API_KEY=your_cohere_api_key_here

# Qdrant Cloud
QDRANT_URL=https://your-cluster.qdrant.io
QDRANT_API_KEY=your_qdrant_api_key_here

# Gemini API
GEMINI_API_KEY=your_gemini_api_key_here

# App Config
COLLECTION_NAME=hackathon_book
SITEMAP_URL=https://samiceto.github.io/hackathon_book/sitemap.xml
```

---

### Step 6: Docker Deployment

**File**: `backend/Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**File**: `docker-compose.yml`

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    env_file:
      - ./backend/.env
    restart: unless-stopped
```

---

## Testing Strategy

### Unit Tests

**File**: `backend/tests/unit/test_ingestion.py`
- Test `get_all_urls()`: Mock sitemap.xml response
- Test `extract_text_from_url()`: Mock HTML response
- Test `chunk_text_generator()`: Verify chunk size, overlap, metadata

**File**: `backend/tests/unit/test_retrieval.py`
- Test `get_embedding()`: Mock Cohere API response
- Test Qdrant search: Mock Qdrant client

**File**: `backend/tests/unit/test_agent.py`
- Test `retrieve()` tool: Mock Qdrant results
- Test `query_agent()`: Mock agent response

---


## Deployment Plan

### Free-Tier Hosting Options

**Option 1: Render**
- Deploy backend as Web Service (Free Tier: 750 hours/month)
- Connected to github already
- Auto-deploy on push

**Recommendation**: Render (most generous free tier for this use case)

---


## Success Criteria Checklist

- [ ] **SC-P2-001**: Chatbot answers traceable to book sections
- [ ] **SC-P2-002**: No login required
- [ ] **SC-P2-003**: Text selection flow works
- [ ] **SC-P2-004**: Infrastructure costs <$5/month
- [ ] **SC-P2-005**: No API keys exposed client-side
- [ ] **SC-P2-006**: Rate limiting functional
- [ ] **SC-P2-007**: Deployable from GitHub + docker-compose
- [ ] **SC-P2-008**: No PII stored
- [ ] **SC-P2-009**: Functional under free-tier constraints
- [ ] **SC-P2-010**: Backend handles retrieval + context + model calls

---


## Next Steps

1. Run `/sp.tasks` to generate detailed tasks.md from this plan
2. Begin implementation with Step 1 (RAG Ingestion)
3. Test ingestion pipeline with small subset of pages
4. Implement agent (Step 2) and test locally
5. Build FastAPI backend (Step 3) and test endpoints
6. Deploy and verify end-to-end flow