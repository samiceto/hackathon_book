---
id: 0008
title: Spec 2 RAG Chatbot Planning
stage: plan
date: 2025-12-16
surface: agent
model: claude-sonnet-4-5-20250929
feature: 002-physical-ai-course
branch: 002-physical-ai-course
user: user
command: /sp.plan
labels: ["rag", "chatbot", "planning", "spec2", "fastapi", "gemini", "qdrant", "cohere"]
links:
  spec: specs/002-physical-ai-course/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/002-physical-ai-course/spec.md
  - specs/002-physical-ai-course/plan.md
tests:
  - None (planning phase)
---

## Prompt

/sp.plan use only the spec 2 from spec.md file for creating the plan.md and create a heading in plan.md "spec 2" and append the content you create under this heading, keep existing plan.md content unchanged, use the system for plan.

step 1. rag:
  sitemap_url =https://samiceto.github.io/hackathon_book/sitemap.xml
  collection_name="hackathon_book"
  COHERE_API_KEY=(in te file .env)
  embed_model="embed-english-v3.0"
  QDRANT_URL=(in .env) QDRANT_API_KEY=(in .env)
  system_design:
    get_all_urls
    extract_text_from_url
    chunk_text_generator(also handle memory error if the content is too big)
    embed
    create_collection
    save_chunk_to_qdrant
    ingest_book(the main function that invokes all).

step 2 agent:
  setup openai agent you can acess the openai-agent-sdk docs in context7,
  setup the agent with gemini llm
  GEMINI_API_KEY=(in .env)
  set_tracing_disabled(disabled=True)
  gemini base url base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
  model="gemini-2.5-flash",
  create agent with one tool that accept a quiry embed it with the help of function 'get_embedding'
  retrive the data from quadrant and return the text,
  the agent instructions="""
You are an AI tutor for the Physical AI & Humanoid Robotics textbook.
To answer the user question, first call the tool `retrieve` with the user query.
Use ONLY the returned content from `retrieve` to answer.
If the answer is not in the retrieved content, say "I don't know".
"""

step 3: use the chatkit python and fasapi to link this backend with chatbot(chatkit js) that already exist

## Response snapshot

Successfully created comprehensive implementation plan for Spec 2 (Integrated RAG Chatbot for Book). The plan includes:

**Summary**: RAG chatbot embedded in Physical AI & Humanoid Robotics book using Cohere embeddings, Qdrant Cloud Free Tier, Gemini LLM via OpenAI Agent SDK, and FastAPI backend.

**Technical Context**: Python 3.11+, FastAPI, Qdrant Client, Cohere (embed-english-v3.0), OpenAI Agent SDK, Gemini (gemini-2.5-flash), ChatKit Python, BeautifulSoup4, pytest.

**Constitution Check**: All Phase 2 principles and constraints verified (✅ all checks pass).

**Project Structure**: Web application structure with backend/ (RAG pipeline, agent, API) and frontend/ (ChatKit js integration).

**Phase 0 - Research & Clarifications**: 7 research tasks documented with decisions, rationale, and alternatives:
1. Sitemap crawling & content extraction (requests + BeautifulSoup4)
2. Text chunking strategy (1000-char chunks, 200-char overlap)
3. Cohere embeddings configuration (embed-english-v3.0, search_document)
4. Qdrant Cloud configuration (Free Tier, Cosine similarity)
5. OpenAI Agent SDK with Gemini LLM (gemini-2.5-flash)
6. Rate limiting strategy (SlowAPI, 10 req/min/IP)
7. ChatKit integration (ChatKit Python + FastAPI)

**Phase 1 - Architecture & Design**:
- Data Model: BookChunk, QueryRequest, QueryResponse, Source entities
- System Architecture: Detailed diagrams for query flow and ingestion pipeline
- API Contracts: OpenAPI spec (rag-api.yaml) for /api/chat and /health endpoints
- Quickstart Guide: Environment setup, ingestion, running backend, testing, deployment

**Phase 2 - Implementation Plan**: 6 detailed steps:
1. RAG Ingestion Pipeline (ingestion.py): 7 functions with specifications
2. OpenAI Agent Setup with Gemini LLM (agent.py): Client setup, retrieval tool, agent creation, query function
3. FastAPI Backend + ChatKit Integration (main.py): App setup, chat endpoint, health check, rate limiting
4. Frontend Integration: Verification of existing ChatKit js
5. Environment Configuration: .env.example with all required API keys
6. Docker Deployment: Dockerfile + docker-compose.yml

**Testing Strategy**: Unit tests (ingestion, retrieval, agent), integration tests (RAG pipeline, API endpoints), contract tests (OpenAPI validation)

**Deployment Plan**: Free-tier hosting options (Render, Railway, Fly.io) with detailed deployment steps

**Success Criteria**: 10 measurable outcomes checklist (SC-P2-001 through SC-P2-010)

**Risks & Mitigation**: 6 risks identified with impact levels and mitigation strategies

**Next Steps**: Run /sp.tasks, begin implementation with RAG ingestion, test incrementally, deploy and verify

## Outcome

- ✅ Impact: Comprehensive implementation plan for Spec 2 RAG chatbot created and appended to plan.md. Plan covers architecture, research decisions, implementation steps, testing, and deployment. Fully aligned with Phase 2 constitution principles and user's technical guidance.
- 🧪 Tests: None (planning phase - test strategy defined in plan)
- 📁 Files: Modified specs/002-physical-ai-course/plan.md (appended ~1000 lines for Spec 2), referenced specs/002-physical-ai-course/spec.md
- 🔁 Next prompts: Run /sp.tasks to generate detailed tasks.md from plan.md; Create research.md, data-model.md, contracts/rag-api.yaml as specified in plan
- 🧠 Reflection: Plan successfully integrates user's 3-step technical guidance (RAG ingestion, OpenAI Agent SDK + Gemini, ChatKit integration) with comprehensive architecture decisions. All Phase 2 constitution constraints verified. Free-tier infrastructure strategy ensures cost-efficiency. Clear path from planning → implementation → deployment.

## Evaluation notes (flywheel)

- Failure modes observed: None. Plan created successfully following /sp.plan workflow. Initial template replacement by setup-plan.ps1 was reversed via git checkout to preserve Spec 1 content before appending Spec 2.
- Graders run and results (PASS/FAIL): Manual validation PASS - all placeholders filled, constitution checks complete, technical decisions documented with rationale.
- Prompt variant (if applicable): N/A (standard /sp.plan workflow)
- Next experiment (smallest change to try): Execute /sp.tasks to validate plan completeness and generate actionable tasks. Test RAG ingestion with small subset of pages before full implementation.
