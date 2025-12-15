---
id: 0001
title: Initial Constitution for Physical AI Course
stage: constitution
date: 2025-12-11
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: Unknown
command: /sp.constitution phase 1 Project: Constitution for the "Physical AI & Humanoid Robotics" course
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
phase 1 Project: Constitution for the "Physical AI & Humanoid Robotics" course

Core principles:
- Real-world readiness: every learning objective must map to deployable skills on actual humanoid/embodied platforms
- Hands-on over theory: students must build, simulate, and (when possible) deploy on physical hardware
- Sim-to-Real pipeline: every module must explicitly teach the bridge from simulation (Isaac Sim/Gazebo) → edge device (Jetson) → real robot
- Future-proof stack: prioritize currently industry-dominant tools (ROS 2 Humble/Iron, NVIDIA Isaac Sim/ROS, Nav2, modern VLA approaches)
- Progressive complexity: start simple (single node → full autonomous humanoid with voice commands)

Key standards:
- All tools and versions must be explicitly stated and currently supported (as of 2025)
- Every module must contain at least one graded hands-on assignment that runs on student hardware/cloud
- Capstone project must demonstrate end-to-end autonomy: voice command → LLM planning → ROS 2 action sequence → navigation + manipulation in simulation and (optional) real robot)
- Hardware recommendations must include exact model numbers, minimum specs, and realistic cost tiers
- Safety and ethical deployment of physical robots must be addressed (emergency stops, teleoperation fallback, responsible AI guidelines)

Constraints:
- Course duration: 13 weeks maximum
- Target audience: advanced undergrad or master’s students with prior Python + basic ML experience (no prior robotics required)
- Primary OS: Ubuntu 22.04 LTS (dual-boot or native Linux mandator-only” modules)
- Course syllabus, weekly schedule, hardware guide, and grading rubric are complete and immediately usable by any university or bootcamp instructor in 2026+
- All recommended hardware kits are purchasable today and supported by manufacturers until at least 2028
```

## Response snapshot

```text
I have read the constitution template. I will now create the constitution for "Phase 1 Project: Constitution for the 'Physical AI & Humanoid Robotics' course".

I will fill in the project name, the five core principles, the five key standards, and the five constraints. I will also set the initial version to `1.0.0` and the ratification/amendment dates to today, 2025-12-11.

Then, I will proceed with the consistency propagation checklist by reading the other templates.

Here's the draft for the updated constitution content:
```

## Outcome

- ✅ Impact: Constitution for Phase 1 created and written to file.
- 🧪 Tests: N/A
- 📁 Files: .specify/memory/constitution.md modified.
- 🔁 Next prompts: Update plan-template.md, spec-template.md, tasks-template.md; Create PHR for Phase 1.
- 🧠 Reflection: Successfully created and wrote the Phase 1 constitution. Need to ensure PHRs are created for all significant actions.

## Evaluation notes (flywheel)

- Failure modes observed: Bash script for PHR creation failed.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Use agent-native file writing for PHR creation if shell script fails.
