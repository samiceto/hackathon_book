---
id: 4
stage: plan
title: Create Book Plan for Physical AI & Humanoid Robotics Textbook
date: 2025-12-11
model: Claude Sonnet 4.5
surface: agent
feature: physical-ai-book
branch: 002-physical-ai-course
user: user
command: /sp.plan Create: Complete book plan for the title "Physical AI & Humanoid Robotics: From Simulated Brains to Walking Bodies"
labels: ["planning", "book-development", "physical-ai", "robotics", "textbook"]
links:
  plan: "specs/002-physical-ai-course/plan.md"
  ticket: null
  adr: null
  pr: null
files: []
tests: []
---

# Create Book Plan for Physical AI & Humanoid Robotics Textbook

## Original Prompt
Create: Complete book plan for the title
"Physical AI & Humanoid Robotics: From Simulated Brains to Walking Bodies" (a definitive 2026 practitioner textbook + lab manual)

Target reader:
- Advanced undergraduate / Master's students in robotics, AI, and embodied intelligence
- Industry engineers transitioning into humanoid robotics
- University instructors who will adopt the book as primary course text

Core deliverables from this plan:
- Full architecture sketch (part/chapter breakdown with exact chapter titles and short abstracts)
- Precise section structure for every chapter (H1 → H2 → H3 hierarchy)
- Research approach and source strategy
- Quality validation pipeline
- Decisions needing documentation (complete list of major choices with options + tradeoffs)
- Estimated word count per chapter and total
- Timeline with milestones (12–14 months to first draft)

Technical details & methodology:
- Writing approach: research-concurrent + code-concurrent (all code snippets and tutorials must be tested weekly on real hardware during writing)
- Primary software stack locked to 2025–2027 supported versions: ROS 2 Iron Irwini / Jazzy Jalisco, NVIDIA Isaac Sim 2024.2+, Isaac ROS 3.0+, Nav2, Ubuntu 22.04/24.04
- All hardware recommendations must include exact model numbers, current (2025) prices, and purchase links from at least two vendors
- Every major algorithm or pipeline must include at least one fully reproducible GitHub repository (public, MIT license)
- Citation style: APA 7th edition
- Code style: Black + ROS 2 Python style guide (PEP8 + flake8)
- Book format: Markdown source → converted to LaTeX → PDF (with separate Leanpub/Kindle builds)
- Total length target: 550–650 pages (~160,000–190,000 words including code)

Phased writing structure:
Phase 1 → Foundations & Nervous System (ROS 2)
Phase 2 → Digital Twins & Simulation Mastery (Gazebo, Isaac Sim, Unity)
Phase 3 → Perception & Edge Brain (Isaac ROS, Jetson deployment)
Phase 4 → Embodied Cognition & VLA Models
Phase 5 → Bipedal Locomotion & Whole-Body Control
Phase 6 → Capstone Integration & Sim-

## Response Summary
Successfully created a comprehensive book plan for "Physical AI & Humanoid Robotics: From Simulated Brains to Walking Bodies". The plan includes:

- 18 chapters organized into 6 phases covering the complete humanoid robotics development lifecycle
- Detailed H1 → H2 → H3 section structure for every chapter
- Research-concurrent + code-concurrent methodology with hardware validation
- Multi-stage quality validation pipeline ensuring technical accuracy
- Documentation of 6 major architectural decisions with tradeoffs
- 175,000-word target across 18 chapters (within 160,000-190,000 range)
- 14-month timeline with quarterly milestones and risk mitigation

The plan addresses all requirements for a 2026 practitioner textbook targeting advanced students, engineers, and instructors in humanoid robotics.

## Outcome
Comprehensive book plan completed with detailed architecture, timeline, and validation approach. Ready for implementation phase with all major decisions documented and resources allocated.