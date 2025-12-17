# Feature Specification: Physical AI & Humanoid Robotics Book (Spec 1 Only)

**Feature Branch**: `002-physical-ai-book`
**Created**: 2025-12-12
**Status**: Draft
**Input**: User description: "Complete specification for writing the *Physical AI & Humanoid Robotics* book. Target audience: University department heads, lab directors, and bootcamp founders who want a book that explains and teaches humanoid robotics concepts in 2025–2026. Focus: Conceptual understanding, simulation-awareness, and practical exercises. Constraints: Book must be self-contained without requiring software or hardware setup."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Complete Book with Conceptual Understanding (Priority: P1)

University department heads, lab directors, and bootcamp founders need a comprehensive book that delivers conceptual understanding of humanoid robotics, including simulation and optional hardware discussion. The book must use the modern 2025–2026 embodied-AI stack concepts: ROS 2, NVIDIA Isaac Sim, Nav2, Vision-Language-Action models, and Jetson edge deployment (conceptually).

**Why this priority**: This is the core deliverable that defines the entire book. Without this, there is no book to offer.

**Independent Test**: Book can be read end-to-end with readers achieving the stated learning outcomes using the specified technology stack concepts.

**Acceptance Scenarios**:

1. **Given** a university department head or lab director, **When** they read the book, **Then** they will understand the concepts required to teach humanoid robotics using modern 2025-2026 technology stack
2. **Given** readers with Python and basic ML knowledge, **When** they complete the book, **Then** they will understand and have conceptual knowledge of the modern embodied-AI stack

---

### User Story 2 - Self-Contained Learning Resource (Priority: P2)

Readers with Python and basic ML knowledge but no prior robotics experience need a learning resource that guides them through humanoid robotics concepts without requiring installation of any software or hardware. The book must be readable without requiring purchase or setup of any tools.

**Why this priority**: This ensures the book is accessible to the target reader population without technical barriers.

**Independent Test**: Readers can complete all exercises and understand all concepts within the book without installing any software or purchasing any hardware.

**Acceptance Scenarios**:

1. **Given** a reader with Python and basic ML knowledge, **When** they read the book, **Then** they can complete all exercises without installing software or hardware
2. **Given** readers using the book, **When** they encounter hardware discussions, **Then** they can understand concepts at a high level without purchasing equipment

---

### User Story 3 - Practical Exercises and Thought Experiments (Priority: P3)

Readers must be able to engage with at least one exercise or thought experiment per chapter that enables them to reason through robotics problems conceptually. This ensures the book delivers practical, conceptual understanding without requiring physical implementation.

**Why this priority**: This validates that readers can apply concepts conceptually rather than just reading theory.

**Independent Test**: Readers can complete exercises and thought experiments that help them understand humanoid robotics pipelines from simulation → edge device → real robot.

**Acceptance Scenarios**:

1. **Given** completed chapters, **When** readers attempt exercises, **Then** they can reason through robotics problems conceptually
2. **Given** readers completing the book, **When** they encounter robotics challenges, **Then** they can explain the pipeline from simulation to real robot deployment

---

### Edge Cases

- What happens when readers want to implement concepts in practice after reading?
- How does the book handle readers with different levels of Python/ML background?
- What if readers want to see actual code examples beyond conceptual explanations?
- How does the book address different humanoid platforms beyond the focus areas?
- What happens when readers need more depth on specific topics covered briefly?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Book MUST deliver conceptual understanding of humanoid robotics, including simulation and optional hardware discussion.
- **FR-002**: Book MUST introduce modern 2025–2026 embodied-AI stack concepts: ROS 2, NVIDIA Isaac Sim, Nav2, Vision-Language-Action models, and Jetson edge deployment (conceptually).
- **FR-003**: Book MUST include at least one exercise or thought experiment per chapter.
- **FR-004**: Book MUST be readable without requiring installation of any software or hardware.
- **FR-005**: Book MUST explain hardware options at a high level, without requiring purchase or setup.
- **FR-006**: Book MUST include safety and ethics considerations in humanoid robotics.
- **FR-007**: Book MUST focus specifically on humanoid robotics, not drones, fixed-base arms, or other platforms.

### Key Entities

- **Book Content**: Chapters covering concepts, pipelines, exercises, and ethical considerations.
- **Reader Profile**: Python and basic ML literate, no prior robotics experience.
- **Conceptual Capstone**: Voice-command → AI planning → humanoid action pipeline explained with diagrams and exercises.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Book clearly communicates all concepts required to understand a humanoid robotics 13-week learning path.
- **SC-002**: Exercises enable readers to reason through robotics problems conceptually.
- **SC-003**: Readers can explain pipelines from simulation → edge device → real robot conceptually.
- **SC-004**: Book is self-contained and does not require hardware or software setup.
- **SC-005**: Ethical and safety practices are clearly explained.

---

# Spec 2: Integrated RAG Chatbot for Book

**Feature Extension**: `002-physical-ai-chatbot`
**Phase Created**: 2025-12-16
**Status**: Draft
**Purpose**: Develop and embed a Retrieval-Augmented Generation (RAG) chatbot directly inside the published book. The chatbot must answer reader questions using the book's content, including questions based on user-selected text fragments.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Content-Accurate Question Answering (Priority: P1)

Readers need to ask questions about book content and receive accurate answers that are strictly based on the book's text. The chatbot must retrieve relevant sections from the book and generate responses without hallucination or external information.

**Why this priority**: This is the core value proposition of the RAG chatbot—enabling readers to get instant, accurate answers from the book's own content.

**Independent Test**: Chatbot responses can be verified against the book's text, with all answers traceable to specific book sections.

**Acceptance Scenarios**:

1. **Given** a reader has a question about a concept in the book, **When** they ask the chatbot, **Then** the chatbot retrieves relevant sections and generates an accurate answer based solely on book content
2. **Given** a reader highlights a text selection, **When** they click "Ask about this selection", **Then** the chatbot uses that selection as context to answer questions
3. **Given** multiple relevant sections exist, **When** the chatbot retrieves content, **Then** it presents information from the most relevant chunks with proper context

---

### User Story 2 - Zero-Installation Access (Priority: P1)

Readers must be able to use the chatbot immediately without any installation, account creation, login, or authentication. The chatbot must be embedded directly in the published book interface and work instantly.

**Why this priority**: Removes all barriers to accessing help, ensuring maximum reader engagement and satisfaction.

**Independent Test**: Readers can ask questions in the chatbot without any setup steps.

**Acceptance Scenarios**:

1. **Given** a reader opens the published book, **When** they see the chatbot interface, **Then** they can immediately ask questions without login or setup
2. **Given** a reader on any device, **When** they access the book, **Then** the chatbot is functional and responsive
3. **Given** a first-time visitor, **When** they interact with the chatbot, **Then** no account creation or authentication is required

---

### User Story 3 - Text Selection-Based Questions (Priority: P2)

Readers must be able to highlight any text in the book and ask questions specifically about that selection. The chatbot must use the highlighted text as additional context for more precise answers.

**Why this priority**: Enables contextual help exactly where readers need it, improving comprehension of difficult sections.

**Independent Test**: Highlighted text appears in the chatbot context and influences answer generation.

**Acceptance Scenarios**:

1. **Given** a reader highlights a paragraph, **When** they click "Ask about this selection", **Then** the chatbot includes that selection in the query context
2. **Given** a highlighted selection and a question, **When** the chatbot generates an answer, **Then** the answer specifically addresses the selected text
3. **Given** no text is highlighted, **When** a reader asks a question, **Then** the chatbot performs normal RAG retrieval without selection context

---

### User Story 4 - Lightweight and Cost-Efficient Operation (Priority: P2)

The chatbot infrastructure must operate entirely within free-tier or near-zero-cost services. This includes vector storage (Qdrant Cloud Free Tier), backend hosting (free-tier FastAPI service), and LLM API calls (within free/affordable limits).

**Why this priority**: Ensures long-term sustainability and accessibility without ongoing costs.

**Independent Test**: All infrastructure costs remain within free tiers or under $5/month.

**Acceptance Scenarios**:

1. **Given** the chatbot is deployed, **When** it operates for a month, **Then** total infrastructure costs remain within free tiers or near-zero
2. **Given** Qdrant Cloud Free Tier limits, **When** the book content is embedded, **Then** vector storage fits within free tier constraints
3. **Given** FastAPI backend deployment, **When** hosting is configured, **Then** it runs on a free-tier service successfully

---

### User Story 5 - Secure and Privacy-Preserving (Priority: P3)

The chatbot must protect reader privacy by not storing any personally identifiable information (PII). API keys must never be exposed client-side, and queries must be rate-limited to prevent abuse.

**Why this priority**: Ensures reader trust and compliance with privacy best practices.

**Independent Test**: Code review confirms no PII storage, API keys are server-side only, and rate limiting is active.

**Acceptance Scenarios**:

1. **Given** a reader uses the chatbot, **When** they submit queries, **Then** no PII is stored in logs or databases
2. **Given** the frontend code, **When** inspected, **Then** no API keys or secrets are visible
3. **Given** multiple rapid queries from one IP, **When** rate limits are reached, **Then** the system throttles requests appropriately
4. **Given** the security review, **When** conducted, **Then** all API keys are confirmed to be server-side only

---

### Edge Cases

- What happens when a reader asks a question about content not in the book?
- How does the chatbot handle ambiguous questions with multiple valid answers?
- What if the reader highlights text from multiple different sections?
- How does the system handle rate limiting for legitimate heavy users?
- What happens when free-tier limits are approached or exceeded?
- How does the chatbot behave when the LLM API is temporarily unavailable?

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-P2-001**: Chatbot MUST retrieve answers strictly from the book's text using RAG (Retrieval-Augmented Generation).
- **FR-P2-002**: Chatbot MUST support text chunking, embeddings, vector storage (Qdrant Cloud Free Tier), and LLM generation.
- **FR-P2-003**: Chatbot MUST be accessible without login, account creation, or authentication.
- **FR-P2-004**: Chatbot MUST support "Ask about this selection" flow for highlighted text.
- **FR-P2-005**: Backend MUST be implemented with FastAPI and hosted on a free-tier service.
- **FR-P2-006**: Frontend MUST use ChatKit js (already integrated) and embed the chatbot widget/iframe inside the book.
- **FR-P2-007**: Chatbot MUST never expose API keys client-side.
- **FR-P2-008**: Chatbot MUST implement rate limiting per IP or session to prevent abuse.
- **FR-P2-009**: Chatbot MUST NOT store any reader PII (personally identifiable information).
- **FR-P2-010**: Complete implementation MUST be reproducible from a single GitHub repository including `docker-compose.yml`.

### Technical Requirements

- **TR-P2-001**: RAG pipeline MUST use text chunking, embeddings using cohere model, Qdrant Cloud Free Tier vector store, and retrieval → LLM generation.
- **TR-P2-002**: Backend MUST handle retrieval, context construction, and model API calls.
- **TR-P2-003**: Frontend MUST integrate ChatKit js widget with support for text selection → query flow.
- **TR-P2-004**: Infrastructure MUST operate within free-tier or near-zero-cost constraints.
- **TR-P2-005**: Deployment MUST include `docker-compose.yml` for reproducibility.

### Security Requirements

- **SR-P2-001**: API keys MUST be stored server-side only, never exposed in frontend code.
- **SR-P2-002**: Rate limiting MUST be implemented per IP or session.
- **SR-P2-003**: No PII MUST be stored in logs, databases, or any persistent storage.
- **SR-P2-004**: All external API calls MUST be proxied through the backend to protect credentials.

### Key Entities

- **Book Content Corpus**: The complete text of the Physical AI & Humanoid Robotics book, chunked and embedded for retrieval.
- **Vector Store**: Qdrant Cloud Free Tier instance storing book content embeddings.
- **FastAPI Backend**: Server handling RAG retrieval, context construction, and LLM API calls.
- **ChatKit Widget**: Frontend chatbot interface embedded in the published book.
- **Text Selection Context**: User-highlighted text passed to the chatbot for contextual questions.
- **Rate Limiter**: Component enforcing query limits per IP/session.

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-P2-001**: Chatbot answers can be traced back to specific sections of the book's content.
- **SC-P2-002**: Readers can use the chatbot without any login or account creation.
- **SC-P2-003**: Text selection → "Ask about this selection" flow works correctly.
- **SC-P2-004**: Total infrastructure costs remain within free tiers or under $5/month.
- **SC-P2-005**: No API keys are exposed in frontend code (verified by code review).
- **SC-P2-006**: Rate limiting prevents abuse without blocking legitimate usage.
- **SC-P2-007**: Complete implementation can be deployed from GitHub repository + `docker-compose.yml`.
- **SC-P2-008**: No PII is stored in any logs or databases (verified by audit).
- **SC-P2-009**: Chatbot remains functional under free-tier constraints (Qdrant Cloud, hosting, LLM API).
- **SC-P2-010**: Backend successfully handles retrieval, context construction, and model API calls.
