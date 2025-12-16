<!-- Sync Impact Report:
Version change: 1.1.0 -> 1.2.0
List of modified principles:
  - Removed old principles related to course structure
  - Added "Real-world readiness" (Phase 1)
  - Added "Hands-on over theory" (Phase 1)
  - Added "Sim-to-Real awareness" (Phase 1)
  - Added "Future-proof knowledge" (Phase 1)
  - Added "Progressive complexity" (Phase 1)
  - Added "Book-native integration" (Phase 2)
  - Added "Zero-install access" (Phase 2)
  - Added "Content-accurate answers" (Phase 2)
  - Added "Lightweight, cost-efficient design" (Phase 2)
Added sections:
  - Core Purpose (Phase 1)
  - Key Standards (Phase 1)
  - Constraints (Phase 1)
  - Phase 2 Purpose
  - Core Principles (Phase 2)
  - Technical Standards
  - Frontend Integration Requirements
  - Security Requirements
  - Reproducibility requirement
  - Constraints (Phase 2)
Removed sections:
  - Old course-focused principles and constraints
Templates requiring updates:
  - .specify/templates/plan-template.md: ⚠ pending
  - .specify/templates/spec-template.md: ⚠ pending
  - .specify/templates/tasks-template.md: ⚠ pending
  - .specify/templates/commands/sp.constitution.md: ⚠ pending
Follow-up TODOs: None
-->
# Physical AI & Humanoid Robotics – Book Constitution (Phase 1 Only)

## Core Purpose
This constitution defines the rules for writing the *Physical AI & Humanoid Robotics* book.
It ensures clarity, consistency, accuracy, and student-readiness while avoiding unnecessary technical or infrastructural constraints.

---

## Core Principles

### I. Real-world readiness
Book content must connect concepts to real humanoid/embodied systems.

### II. Hands-on over theory
Chapters must emphasize practical, applicable knowledge with examples, diagrams, and exercises.

### III. Sim-to-Real awareness
Explain the conceptual pipeline from simulation → real robot deployment at a high level.

### IV. Future-proof knowledge
Use tools, frameworks, and terminology that are industry-relevant as of 2025 (without locking to specific versions).

### V. Progressive complexity
Start from fundamentals → full humanoid autonomy concepts by the end of the book.

---

## Key Standards (Phase 1 – Book Writing)

### I. Tool and Technology Clarity
Tools should be introduced clearly, but without deep installation or setup instructions.

### II. Chapter-Level Practical Exercises
Each chapter must include at least one exercise or thought experiment.

### III. Capstone Narrative
The book must gradually build toward a conceptual capstone:
**"From voice command → AI planning → robot action."**

### IV. Hardware Explained, Not Required
Explain hardware options (e.g., Jetson, sensors, servos) at a high level; readers should not need to purchase or run hardware.

### V. Safety & Ethics
The book must address safety principles (collision avoidance, emergency stop logic, responsible AI behavior).

---

## Constraints (Phase 1 Only)

### I. Audience
Target audience: advanced undergraduate or early graduate students with Python & basic ML background.

### II. Primary OS (Examples Only)
Ubuntu 22.04 may be referenced for examples, but no installation is required.

### III. No Deployment Requirements
The book must not assume:
- servers or cloud accounts
- vector databases
- LLM usage limits
- ROS, Qdrant, Postgres, or backend setup

These belong to the course or Phase 2, not the book.

### IV. Timelessness
Avoid version-specific instructions unless absolutely essential for explanation.

### V. Reproducibility (Conceptual)
Diagrams, pseudocode, frameworks, and explanations must be complete within the book itself.

---

# Phase 2 – Integrated RAG Chatbot Constitution (Clean Edition)

## Phase 2 Purpose
Develop and embed a Retrieval-Augmented Generation (RAG) chatbot directly inside the published book.
The chatbot must answer reader questions using the book's content, including questions based on user-selected text fragments.

---

## Core Principles (Phase 2)

### I. Content-accurate answers
All responses must rely strictly on:
- the book's text, and
- optionally user-highlighted selections.

### II. Lightweight, cost-efficient design
The solution must operate entirely within free-tier or near-zero-cost infrastructure.

---

## Technical Standards

### I. RAG Pipeline Requirements
The chatbot must use:
- Text chunking
- Embeddings
- Qdrant Cloud Free Tier vector store
- Retrieval → LLM generation

### II. Backend Requirements
Backend must use:
- **FastAPI**
- Hosted on a free-tier service
- Handles retrieval, context construction, and model calls


### III. Frontend Integration Requirements
Frontend must:
- Use **ChatKit js** (already integrated)
- Embed the chatbot widget or iframe inside the book
- Support highlight → "Ask about this selection" flow

### IV. Security Requirements
- API keys must never be exposed client-side
- Queries rate-limited per IP or session
- No storage of reader PII

### V. Reproducibility
A complete working implementation must be reproducible from:
- a single public GitHub repository
- including a `docker-compose.yml` for backend setup

---

## Constraints (Phase 2 Only)

### I. Hosting Constraints
Must run on fully free-tier or near-zero-cost hosting.
(Any free-tier platform is acceptable.)

### II. Technical Constraints
Backend must be implemented with FastAPI and hosted on free-tier services only.

### III. Security Constraints
No user PII should be stored, and API keys must never be exposed client-side.

### IV. No Authentication
The chatbot must be usable without login, account creation, or OAuth.

---

## Governance
This constitution governs book writing only.
Any amendments require:
1. A clear change note
2. Justification
3. Updating templates if needed

**Version**: 1.2.0 | **Ratified**: 2025-12-11 | **Last Amended**: 2025-12-12
