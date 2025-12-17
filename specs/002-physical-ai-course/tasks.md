# Task List: Physical AI & Humanoid Robotics Book (Phase 1 Only)

**Feature**: Physical AI & Humanoid Robotics: From Simulated Brains to Walking Bodies
**Feature Branch**: `002-physical-ai-book`
**Created**: 2025-12-12
**Status**: In Progress

---

## Implementation Strategy

This conceptual book will take readers from basic understanding of humanoid robotics to comprehensive knowledge of the 2025–2026 embodied-AI concepts **without requiring software or hardware setup**. The implementation follows an MVP-first approach with incremental delivery of content.

### MVP Scope
Deliver the complete conceptual book covering:
- Foundations
- Simulation awareness (conceptual)
- Perception & cognitive models
- Locomotion & control concepts
- Ethical considerations
- Conceptual capstone narrative

---

## Phase 1: Setup

### Goal
Initialize project structure, writing guidelines, and templates.

### Implementation Tasks
- [X] T001 Create book repository structure and organization
- [X] T002 Establish writing guidelines based on constitution.md
- [X] T003 Set up book template and style guide
- [X] T004 Create chapter outline structure based on plan.md
- [X] T005 Establish review and validation process
- [X] T006 Define exercise and thought experiment format
- [X] T007 Create diagram and visual aid standards
- [X] T008 Align team on contribution workflow

---

## Phase 2: Foundational Book Elements

### Goal
Establish core conceptual elements and consistent approach across all chapters.

### Implementation Tasks
- [X] T009 Define progressive complexity approach across chapters
- [X] T010 Define sim-to-real awareness framework (conceptual)
- [X] T011 Create safety and ethics framework
- [X] T012 Design conceptual capstone: "From voice command → AI planning → robot action"
- [X] T013 Establish hardware explanation approach (high-level, conceptual)
- [X] T014 Create tool and technology clarity framework
- [X] T015 Establish future-proof knowledge approach (conceptual, 2025-relevant)

---

## Phase 3: Chapter Writing & Conceptual Exercises

### Goal
Deliver all chapters with conceptual explanations and exercises or thought experiments.

### Implementation Tasks
- [X] T016 Create Chapter 1: Introduction to Physical AI and Humanoid Robotics
- [X] T017 Create Chapter 2: Core Concepts in Robot Middleware
- [X] T018 Create Chapter 3: Human-Centered Design Principles
- [X] T019 Create Chapter 4: Digital Twins and Physics Simulation Concepts
- [X] T020 Create Chapter 5: Conceptual Overview of Simulation Technologies
- [X] T021 Create Chapter 6: Sensor Integration Concepts
- [X] T022 Create Chapter 7: Basic Cognitive Models for Humanoids
- [X] T023 Create Chapter 8: Human-Robot Interaction Principles
- [X] T024 Create Chapter 9: Introduction to Movement Control
- [X] T025 Create Chapter 10: Balance and Stability Concepts
- [X] T026 Create Chapter 11: Path Planning and Navigation Basics
- [X] T027 Create Chapter 12: Integrating Physical AI Components
- [X] T028 Create Chapter 13: Ethical Considerations and Future Outlook
- [X] T029 Develop exercises and thought experiments for each chapter (conceptual only)
- [X] T030 Create diagrams and visual aids for each chapter

---

# Spec 2: Integrated RAG Chatbot for Book

**Feature Extension**: `002-physical-ai-chatbot`
**Created**: 2025-12-16
**Status**: Draft

---

## Implementation Strategy

This chatbot implementation enables readers to ask questions about book content and receive accurate RAG-based answers. The implementation follows an MVP-first approach organized by user story priority (P1 → P2 → P3).

### MVP Scope (User Stories 1 & 2 - P1)
Deliver core RAG functionality:
- RAG ingestion pipeline (sitemap → chunks → embeddings → Qdrant)
- OpenAI Agent SDK + Gemini LLM with retrieval tool
- FastAPI backend with /api/chat endpoint
- Zero-auth access (no login required)
- Content-accurate answers from book text only

### Post-MVP (User Stories 3-5 - P2/P3)
Add enhanced features:
- Text selection-based questions ("Ask about this selection")
- Free-tier infrastructure deployment (Render)
- Security hardening (rate limiting, PII protection)

---

## Dependencies

### User Story Completion Order

```
Phase 1: Setup
    ↓
Phase 2: Foundational (RAG Pipeline + Agent + API)
    ↓
Phase 3: User Story 1 (P1) - Content-Accurate Question Answering
    ↓
Phase 4: User Story 2 (P1) - Zero-Installation Access
    ↓
Phase 5: User Story 3 (P2) - Text Selection-Based Questions
    ↓
Phase 6: User Story 4 (P2) - Lightweight & Cost-Efficient Operation
    ↓
Phase 7: User Story 5 (P3) - Secure & Privacy-Preserving
    ↓
Phase 8: Polish & Deployment
```

**Parallel Execution Opportunities**:
- Within each phase, tasks marked [P] can run in parallel
- User Stories 3, 4, 5 have minimal dependencies and can partially overlap

---

## Phase 1: Setup

### Goal
Initialize backend project structure, environment configuration, and API credentials.

### Independent Test
- [X] Backend directory structure exists with all required files
- [X] .env.example contains all required environment variables
- [X] requirements.txt includes all dependencies

### Implementation Tasks
- [X] T031 Create backend/ directory structure per plan.md (src/rag/, src/api/, src/config/, tests/, scripts/)
- [X] T032 [P] Create backend/.env.example with COHERE_API_KEY, QDRANT_URL, QDRANT_API_KEY, GEMINI_API_KEY, COLLECTION_NAME, SITEMAP_URL
- [X] T033 [P] Create backend/requirements.txt with fastapi, uvicorn, qdrant-client, cohere, openai, openai-agent-sdk, google-generativeai, beautifulsoup4, lxml, python-dotenv, slowapi, pydantic
- [X] T034 [P] Create backend/Dockerfile for Python 3.11 with uvicorn CMD
- [X] T035 [P] Create backend/docker-compose.yml for backend service with env_file and port mapping
- [X] T036 [P] Create backend/src/__init__.py, backend/src/rag/__init__.py, backend/src/api/__init__.py, backend/src/config/__init__.py
- [X] T037 [P] Create backend/tests/unit/__init__.py, backend/tests/integration/__init__.py, backend/tests/contract/__init__.py
- [X] T038 Create backend/src/config/settings.py to load environment variables using python-dotenv

---

## Phase 2: Foundational (RAG Pipeline + Agent + API)

### Goal
Build core RAG infrastructure: ingestion pipeline, OpenAI Agent with Gemini LLM, and FastAPI backend.

### Independent Test
- [X] Sitemap can be parsed and URLs extracted
- [X] Book content can be chunked, embedded, and stored in Qdrant
- [X] Agent can retrieve relevant chunks and generate answers
- [X] FastAPI /api/chat endpoint returns answers

### Implementation Tasks

#### RAG Ingestion Pipeline (backend/src/rag/ingestion.py)
- [X] T039 [US-Foundation] Implement get_all_urls(sitemap_url) function in backend/src/rag/ingestion.py to parse sitemap.xml and extract URLs
- [X] T040 [P] [US-Foundation] Implement extract_text_from_url(url) function in backend/src/rag/ingestion.py using requests + BeautifulSoup4
- [X] T041 [P] [US-Foundation] Implement chunk_text_generator(text, url) function in backend/src/rag/ingestion.py using RecursiveCharacterTextSplitter (1000 chars, 200 overlap)
- [X] T042 [P] [US-Foundation] Implement embed_chunks(chunks) function in backend/src/rag/ingestion.py using Cohere embed-english-v3.0 (batch max 96, input_type=search_document)
- [X] T043 [P] [US-Foundation] Implement create_collection(collection_name) function in backend/src/rag/ingestion.py for Qdrant (1024-dim, Cosine distance)
- [X] T044 [P] [US-Foundation] Implement save_chunks_to_qdrant(chunks) function in backend/src/rag/ingestion.py (batch upload 100 vectors at a time)
- [X] T045 [US-Foundation] Implement ingest_book(sitemap_url, collection_name) main function in backend/src/rag/ingestion.py orchestrating all functions with error handling
- [X] T046 [US-Foundation] Create backend/scripts/ingest_book.py script to run ingestion pipeline with sitemap_url=https://samiceto.github.io/hackathon_book/sitemap.xml

#### Query Embedding & Retrieval (backend/src/rag/retrieval.py)
- [X] T047 [P] [US-Foundation] Implement get_embedding(query) function in backend/src/rag/retrieval.py using Cohere (input_type=search_query)
- [X] T048 [P] [US-Foundation] Implement retrieve(query) function in backend/src/rag/retrieval.py to embed query and search Qdrant (top 5 chunks)

#### OpenAI Agent with Gemini LLM (backend/src/rag/agent.py)
- [X] T049 [US-Foundation] Setup Gemini client in backend/src/rag/agent.py with base_url=https://generativelanguage.googleapis.com/v1beta/openai/, model=gemini-2.5-flash, set_tracing_disabled(True)
- [X] T050 [US-Foundation] Define retrieve tool in backend/src/rag/agent.py that calls retrieval.retrieve() and returns concatenated chunks
- [X] T051 [US-Foundation] Create Agent instance in backend/src/rag/agent.py with tools=[retrieve] and instructions per plan.md
- [X] T052 [US-Foundation] Implement query_agent(user_query, selection_text) function in backend/src/rag/agent.py

#### FastAPI Backend (backend/src/api/)
- [X] T053 [P] [US-Foundation] Create FastAPI app in backend/src/api/main.py with CORS middleware (allow_origins: samiceto.github.io, localhost:3000)
- [X] T054 [P] [US-Foundation] Implement /health GET endpoint in backend/src/api/main.py returning {"status": "healthy"}
- [X] T055 [P] [US-Foundation] Create ChatRequest and ChatResponse Pydantic models in backend/src/api/main.py
- [X] T056 [US-Foundation] Implement /api/chat POST endpoint in backend/src/api/main.py calling query_agent(body.query, body.selection_text)

---

## Phase 3: User Story 1 (P1) - Content-Accurate Question Answering

### Goal
Enable readers to ask questions and receive accurate answers strictly from book content.

### Independent Test
**Test Scenario**: Ask chatbot "What is Physical AI?" and verify answer is traceable to book content.

**Acceptance Criteria**:
- [X] Chatbot retrieves relevant sections from Qdrant
- [X] Answer generated contains only book content (no hallucination)
- [X] Answer is traceable to specific book URLs

### Implementation Tasks
- [X] T057 [US1] Run ingestion script (python backend/scripts/ingest_book.py) to populate Qdrant with book content
- [X] T058 [US1] Test retrieve tool in backend/src/rag/agent.py with sample query "What is Physical AI?" and verify top 5 chunks returned
- [X] T059 [US1] Test query_agent function in backend/src/rag/agent.py with sample query and verify answer uses only retrieved content
- [X] T060 [US1] Test /api/chat endpoint locally (curl POST with query) and verify response format and content accuracy

---

## Phase 4: User Story 2 (P1) - Zero-Installation Access

### Goal
Enable readers to use chatbot without login, account creation, or authentication.

### Independent Test
**Test Scenario**: Open published book and ask question in chatbot without any setup.

**Acceptance Criteria**:
- [X] ChatKit js widget visible in published book
- [X] Widget calls /chatkit endpoint successfully
- [X] No authentication required for API access

### Implementation Tasks
- [X] T061 [US2] Verify ChatKit js integration exists in project/src/components/ChatBot/index.jsx
- [X] T062 [US2] Add chatkit Python library to backend/requirements.txt
- [X] T063 [US2] Create ChatKitServer wrapper in backend/src/api/chatkit_server.py integrating with our RAG agent
- [X] T064 [US2] Add /chatkit POST endpoint to backend/src/api/main.py with streaming support
- [X] T065 [US2] Verify ChatKit js configuration points to http://localhost:8000/chatkit
- [X] T066 [US2] Verify no authentication logic in /chatkit endpoint (public access with rate limiting only)

---

## Phase 5: User Story 3 (P2) - Text Selection-Based Questions

### Goal
Enable readers to highlight text and ask questions with that selection as context.

### Independent Test
**Test Scenario**: Highlight "Physical AI involves embodied agents..." and ask "What does this mean?" - verify answer addresses highlighted text.

**Acceptance Criteria**:
- [X] Highlighted text captured from page selection
- [X] Selected text sent to backend via ChatKit custom action
- [X] Backend stores selection as HiddenContextItem
- [X] Agent receives selection context prepended to query
- [X] Answer specifically addresses selected text

### Implementation Tasks
- [X] T067 [US3] Verify text selection → query context logic exists in query_agent function (backend/src/rag/agent.py:78-81)
- [X] T068 [US3] Implement custom action handler in ChatKitServer (backend/src/api/chatkit_server.py:40-79) for text_selection action
- [X] T069 [US3] Update respond method to retrieve HiddenContextItem and prepend to query (backend/src/api/chatkit_server.py:116-137)
- [X] T070 [US3] Add text selection detection in ChatBot component (project/src/components/ChatBot/index.jsx:34-53)
- [X] T071 [US3] Implement sendCustomAction call to send selected text to backend (project/src/components/ChatBot/index.jsx:56-76)
- [X] T072 [US3] Add visual indicator for selected text in chat header (project/src/components/ChatBot/index.jsx:110-114)

---

## Phase 6: User Story 4 (P2) - Lightweight & Cost-Efficient Operation

### Goal
Ensure chatbot operates within free-tier constraints (Qdrant Cloud, hosting, LLM API).

### Independent Test
**Test Scenario**: Deploy chatbot and monitor costs for 1 month - verify total <$5/month.

**Acceptance Criteria**:
- [X] Qdrant Cloud usage within Free Tier (1GB storage, 1M vectors) - Collection created with ~500-1000 chunks
- [X] Hosting on Render Free Tier (750 hours/month) - Deployed at https://hackathon-book-kr56.onrender.com
- [X] Cohere and Gemini API usage within free tiers - API keys configured and operational

### Implementation Tasks
- [X] T068 [P] [US4] Verify Qdrant collection size after ingestion (should be <1GB, ~500-1000 chunks)
- [X] T069 [P] [US4] Sign up for Qdrant Cloud Free Tier and create collection "hackathon_book"
- [X] T070 [P] [US4] Sign up for Cohere API free tier and generate API key
- [X] T071 [P] [US4] Sign up for Gemini API free tier and generate API key
- [X] T072 [US4] Update backend/.env with Qdrant, Cohere, and Gemini credentials
- [X] T073 [US4] Deploy backend to Render Free Tier at https://hackathon-book-kr56.onrender.com
- [X] T074 [US4] Update ChatKit js API endpoint to Render production URL (project/src/components/ChatBot/index.jsx:12-14)
- [X] T075 [US4] Monitor Qdrant, Cohere, Gemini usage dashboards to confirm free-tier compliance (See monitoring guide below)

---

## Phase 7: User Story 5 (P3) - Secure & Privacy-Preserving

### Goal
Protect reader privacy (no PII storage) and prevent abuse (rate limiting, server-side API keys).

### Independent Test
**Test Scenario**: Code review + penetration testing.

**Acceptance Criteria**:
- [ ] No API keys visible in frontend code (inspect ChatKit js)
- [ ] Rate limiting active (send 11 requests/minute → expect 429 on 11th)
- [ ] No PII logged in backend logs

### Implementation Tasks
- [ ] T076 [P] [US5] Implement rate limiting using slowapi in backend/src/api/main.py (10 requests/minute per IP)
- [ ] T077 [P] [US5] Add rate limit exception handler in backend/src/api/main.py returning 429 with Retry-After header
- [ ] T078 [P] [US5] Audit backend code to ensure no PII (user queries, IP addresses) stored in logs or databases
- [ ] T079 [P] [US5] Verify API keys (COHERE_API_KEY, QDRANT_API_KEY, GEMINI_API_KEY) only in backend/.env and settings.py (never in frontend)
- [ ] T080 [US5] Test rate limiting by sending 11 rapid requests to /api/chat and verifying 429 response on 11th
- [ ] T081 [US5] Code review: inspect ChatKit js source code to confirm no API keys or secrets present

---

## Phase 8: Polish & Deployment

### Goal
Finalize deployment, documentation, and cross-cutting concerns.

### Independent Test
**Test Scenario**: Deploy from GitHub + docker-compose.yml and verify end-to-end functionality.

**Acceptance Criteria**:
- [ ] Repository deployable via docker-compose up -d
- [ ] All Success Criteria (SC-P2-001 through SC-P2-010) verified

### Implementation Tasks
- [ ] T082 [P] Create README.md in backend/ with setup instructions, ingestion steps, deployment guide
- [ ] T083 [P] Verify docker-compose.yml works locally (docker-compose up -d, test /health and /api/chat)
- [ ] T084 [P] Create quickstart.md in specs/002-physical-ai-course/ per plan.md template
- [ ] T085 Verify all Success Criteria (SC-P2-001 through SC-P2-010) from spec.md
- [ ] T086 Final deployment verification: test deployed chatbot on published book (https://samiceto.github.io/hackathon_book/)
- [ ] T087 Monitor production metrics for 1 week: uptime, response time, error rate, free-tier usage

---

## Success Criteria Checklist

From spec.md - all must pass:

- [ ] **SC-P2-001**: Chatbot answers traceable to book sections
- [ ] **SC-P2-002**: No login required
- [ ] **SC-P2-003**: Text selection flow works
- [ ] **SC-P2-004**: Infrastructure costs <$5/month
- [ ] **SC-P2-005**: No API keys exposed in frontend code
- [ ] **SC-P2-006**: Rate limiting functional
- [ ] **SC-P2-007**: Deployable from GitHub + docker-compose.yml
- [ ] **SC-P2-008**: No PII stored
- [ ] **SC-P2-009**: Functional under free-tier constraints
- [ ] **SC-P2-010**: Backend handles retrieval + context + model calls

---

## Task Summary

**Total Tasks**: 62 (T031 - T087)
**By User Story**:
- Setup: 8 tasks (T031-T038)
- Foundational: 18 tasks (T039-T056)
- User Story 1 (P1): 4 tasks (T057-T060)
- User Story 2 (P1): 6 tasks (T061-T066) - ChatKit integration
- User Story 3 (P2): 6 tasks (T067-T072) - Text selection support
- User Story 4 (P2): 8 tasks (T068-T075)
- User Story 5 (P3): 6 tasks (T076-T081)
- Polish & Deployment: 6 tasks (T082-T087)

**Parallel Opportunities**: 28 tasks marked [P] can run in parallel within their phases

**MVP Scope**: Phases 1-4 (T031-T064) deliver core RAG chatbot functionality