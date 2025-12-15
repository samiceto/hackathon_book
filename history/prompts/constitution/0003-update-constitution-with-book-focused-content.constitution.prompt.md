---
id: 0003
title: Update constitution with book-focused content
stage: constitution
date: 2025-12-12
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 002-physical-ai-course
user: user
command: /sp.constitution
labels: [constitution,book,physical-ai,humanoid-robotics]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

the constitution you currently have contains extra matarial that i dont
  want, udate it with, """# Physical AI & Humanoid Robotics – Book Constitution (Phase 1 Only)

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

## Governance
This constitution governs book writing only.
Any amendments require:
1. A clear change note
2. Justification
3. Updating templates if needed

---


# Phase 2 – Integrated RAG Chatbot Constitution (Clean Edition)

## Phase 2 Purpose
Develop and embed a Retrieval-Augmented Generation (RAG) chatbot directly inside the published book.
The chatbot must answer reader questions using the book's content, including questions based on user-selected text fragments.

---

## Core Principles (Phase 2)

### I. Book-native integration
The chatbot must function directly inside the book without redirecting users elsewhere.

### II. Zero-install access
Readers must use the chatbot instantly in-browser without creating an account or installing software.

### III. Content-accurate answers
All responses must rely strictly on:
- the book's text, and
- optionally user-highlighted selections.

### IV. Lightweight, cost-efficient design
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
- Use **ChatKit js**
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


### IV. No Authentication
The chatbot must be usable without login, account creation, or OAuth.

---

## Governance
Any modification to Phase 2 standards must include:
1. A clear change description
 """ update the version and create phr

## Response snapshot

I'll help you update the constitution file with the new content you provided. Let me first check the current constitution file to understand what needs to be replaced.

[Response continued with the steps taken to update the constitution file]

## Outcome

- ✅ Impact: Updated constitution to focus on book writing rather than course structure, with clear phases for book content and RAG chatbot integration
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md updated from v1.1.0 to v1.2.0
- 🔁 Next prompts: Could update related templates to align with new constitution
- 🧠 Reflection: Constitution now properly focused on book writing rather than course structure

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Update templates to align with new constitution