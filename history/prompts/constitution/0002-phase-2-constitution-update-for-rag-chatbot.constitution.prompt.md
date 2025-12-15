---
id: 0002
title: Phase 2 Constitution Update for RAG Chatbot
stage: constitution
date: 2025-12-11
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: Unknown
command: /sp.constitution start phase 2
labels: [constitution, documentation]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- path: .specify/memory/constitution.md
  status: modified
tests:

---

## Prompt

```text
Phase 2 – Integrated RAG Chatbot Embedded in the "Physical AI & Humanoid Robotics" Book

Core principles:
- Book-native experience: the chatbot must feel like a seamless part of the published digital book (PDF + web version)
- Zero-install for readers: users must be able to talk to the book instantly in-browser with no account creation
- Context-perfect answers: must answer accurately using only the book content + optionally only the user-highlighted text selection
- Production-grade reliability and speed (<1.5 s first token, 99.9% uptime)
- Full cost control: must stay within completely free tiers or <$15/month total operating cost

Key standards:
- RAG pipeline: chunking → embeddings → Qdrant vector store → retrieval → OpenAI gpt-4o-mini or gpt-4.1-mini reasoning
- Backend: FastAPI + Neon Serverless Postgres (for session memory & metadata) + Qdrant Cloud Free Tier (50k vectors)
- Frontend integration: use OpenAI ChatKit / Agents SDK + embedded iframe/widget directly inside the published book (Leanpub, GitBook, and static PDF web viewer)
- User-selected context mode: when user highlights text in the book → “Ask about this selection” button → answer uses only that fragment + relevant retrieved chunks
- All code and infrastructure: 100% reproducible from a single public GitHub repository with docker-compose.yml
- Security: no PII stored, rate-limited per IP, OpenAI API key never exposed client-side

Constraints:
- Vector database: Qdrant Cloud Free Tier only (no paid upgrade)
- Database: Neon Serverless Postgres free tier only
- LLM usage: stay under 2 million tokens/month total (all users combined)
- Deployment platform: Render.com, Fly.io, or Railway free/hobby tier only
- No external authentication required
- Must work on the final published book formats: Leanpub Markdown-rendered web version + static HTML book + PDF
```

## Response snapshot

```text
I have completed Phase 2 of the constitution for the "Physical AI & Humanoid Robotics" course. I have updated the constitution document to version 1.1.0, incorporating the principles and standards for Phase 2, including the RAG Chatbot integration.

I've also updated `plan-template.md` to include the new "Constitution Check" items. The `spec-template.md` and `tasks-template.md` are still marked for follow-up and will be addressed in subsequent steps.

My suggested commit message for this change is: `docs: amend constitution to v1.1.0 (add phase 2 RAG chatbot principles + constraints)`.

I have also created a PHR for this action.
```

## Outcome

- ✅ Impact: Constitution for Phase 2 updated and written to file.
- 🧪 Tests: N/A
- 📁 Files: .specify/memory/constitution.md modified.
- 🔁 Next prompts: Update spec-template.md, tasks-template.md.
- 🧠 Reflection: Successfully updated the constitution for Phase 2 and created the corresponding PHR.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
