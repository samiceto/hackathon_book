---
id: 3
stage: spec
title: Create Physical AI & Humanoid Robotics Capstone Course Specification
date: 2025-12-11
model: Claude Sonnet 4.5
surface: agent
feature: physical-ai-course
branch: 002-physical-ai-course
user: user
command: /sp.specify Complete Specification for the "Physical AI & Humanoid Robotics" Capstone Course...
labels: ["specification", "course-development", "physical-ai", "robotics"]
links:
  spec: "specs/002-physical-ai-course/spec.md"
  ticket: null
  adr: null
  pr: null
files:
  - "specs/002-physical-ai-course/spec.md"
  - "specs/002-physical-ai-course/checklists/requirements.md"
tests: []
---

# Create Physical AI & Humanoid Robotics Capstone Course Specification

## Original Prompt
Complete Specification for the "Physical AI & Humanoid Robotics" Capstone Course, for phase 1 of constitution only, dont create specs for phase 2

Target audience:
- University department heads, lab directors, and bootcamp founders who want to launch a cutting-edge, industry-aligned Physical AI / Humanoid Robotics course in 2026
- Instructors and TAs who will actually teach and support the course

Focus:
- Deliver a fully executable 13-week capstone course that takes students from zero robotics experience to deploying a voice-controlled autonomous humanoid (simulated + optional real hardware)
- Heavy emphasis on the modern 2025–2026 embodied-AI stack: ROS 2 Humble/Iron, NVIDIA Isaac Sim + Isaac ROS, Nav2, Vision-Language-Action models, Jetson Orin edge deployment


Constraints:
- Total course length: maximum 13 weeks
- Weekly student time budget: 12–15 hours (including lectures, labs, and project work)
- Prerequisite knowledge: Python, basic deep learning; no prior ROS or robotics required
- Primary OS: Ubuntu 22.04 LTS (all setup instructions must assume Linux)
- GPU requirement for simulation: RTX 4070 Ti / 4080 / 4090 class or equivalent cloud instance
- All assignments must be doable on student-owned hardware or provided lab kits
- Capstone must run at ≥15 Hz real-time inference on Jetson Orin Nano/Orin NX 8–16 GB

Not building:
- A beginner-level robotics or ROS introduction course
- A purely theoretical AI embodiment course with no hardware deployment
- A course focused on non-humanoid platforms (drones, self-driving cars, fixed-base arms as primary target)
- Vendor-specific product marketing (no mandatory use of a particular commercial humanoid)
- Full research survey of all humanoid robots ever built
- Custom LLM training from scratch (use of existing open-source VLA models is allowed)

Deliver the complete, ready-to-launch course specification package in Markdown with embedded file structure.

## Response Summary
Successfully created a comprehensive specification for the Physical AI & Humanoid Robotics Capstone Course in branch `002-physical-ai-course`. The specification includes:

- Complete 13-week curriculum structure
- Technology stack requirements (ROS 2, NVIDIA Isaac Sim, Vision-Language-Action models)
- Hardware specifications (Ubuntu 22.04, RTX GPUs for simulation, Jetson for deployment)
- Performance requirements (≥15 Hz real-time inference)
- Student prerequisites and time budget considerations
- User scenarios with acceptance criteria
- Functional requirements and success metrics
- Quality validation checklist

The specification is ready for the planning phase and meets all stated requirements for the 2026 course launch.

## Outcome
Specification successfully created and validated, ready for planning phase. Course structure is comprehensive and aligned with modern Physical AI and humanoid robotics technologies.