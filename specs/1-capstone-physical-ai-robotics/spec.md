# Feature Specification: Physical AI & Humanoid Robotics Capstone Course - Phase 1

**Feature Branch**: `1-capstone-physical-ai-robotics`
**Created**: 2025-12-11
**Status**: Draft
**Input**: User description: "Complete Specification for the "Physical AI & Humanoid Robotics" Capstone Course, for phase 1 of constitution only, dont create specs for phase 2

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

Deliver the complete, ready-to-launch course specification package in Markdown with embedded file structure."

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.

  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->

### User Story 1 - Deploy Voice-Controlled Autonomous Humanoid (P1)

A university department head, lab director, or bootcamp founder wants to launch a cutting-edge, industry-aligned Physical AI / Humanoid Robotics course in 2026 that delivers a fully executable 13-week capstone. This course should take students from zero robotics experience to deploying a voice-controlled autonomous humanoid in simulation and, optionally, on real hardware.

**Why this priority**: This is the core objective of the course and represents the primary value proposition for the target audience.

**Independent Test**: The capstone project's final deployment of a voice-controlled autonomous humanoid in simulation can be tested independently. This includes verifying voice command reception, LLM planning, ROS 2 action sequencing, and navigation/manipulation execution.

**Acceptance Scenarios**:

1. **Given** a student has completed all course modules and has a functional simulation environment, **When** they issue a voice command (e.g., "Navigate to the kitchen"), **Then** the simulated humanoid navigates to the specified location autonomously.
2. **Given** a student has access to compatible real hardware and has followed the Sim-to-Real deployment guide, **When** they issue a voice command, **Then** the real humanoid executes the command.

---

### User Story 2 - Emphasize Modern Embodied-AI Stack (P2)

Instructors and TAs need to ensure the course heavily emphasizes the modern 2025–2026 embodied-AI stack, including ROS 2 Humble/Iron, NVIDIA Isaac Sim + Isaac ROS, Nav2, Vision-Language-Action models, and Jetson Orin edge deployment.

**Why this priority**: This ensures the course's relevance and adherence to current industry standards, providing students with in-demand skills.

**Independent Test**: The course materials and lab assignments can be reviewed to confirm the explicit inclusion and practical application of ROS 2, Isaac Sim, Isaac ROS, Nav2, VLA models, and Jetson Orin deployment instructions.

**Acceptance Scenarios**:

1. **Given** an instructor is reviewing the course syllabus, **When** they examine the module breakdown, **Then** they see specific topics covering ROS 2, Isaac Sim, Nav2, VLA models, and Jetson Orin deployment.

---

### User Story 3 - Cater to Diverse Audiences and Constraints (P3)

University department heads, lab directors, and bootcamp founders need the course to be executable within specific constraints, catering to a target audience with no prior robotics experience but with Python and basic deep learning knowledge, using Ubuntu 22.04 LTS, and requiring specific GPU/edge hardware capabilities.

**Why this priority**: This ensures the course is practical, accessible, and aligned with the target audience's background and available resources.

**Independent Test**: The course prerequisites, setup instructions, hardware recommendations, and assignment requirements can be verified against the stated constraints and target audience profile.

**Acceptance Scenarios**:

1. **Given** a student with Python and basic deep learning knowledge, **When** they review the prerequisites, **Then** they confirm no prior ROS or robotics experience is needed.
2. **Given** a user is setting up the course environment, **When** they follow the setup instructions, **Then** they are guided to use Ubuntu 22.04 LTS.
3. **Given** a student is choosing hardware, **When** they consult the recommendations, **Then** they see specific guidance on GPU requirements (RTX 4070 Ti class) and Jetson Orin edge devices.

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST deliver a 13-week capstone course.
- **FR-002**: Course MUST guide students from zero robotics experience to deploying a voice-controlled autonomous humanoid.
- **FR-003**: Course MUST cover simulation and optionally real hardware deployment.
- **FR-004**: Course MUST heavily emphasize the 2025–2026 embodied-AI stack: ROS 2 Humble/Iron, NVIDIA Isaac Sim + Isaac ROS, Nav2, VLA models, Jetson Orin edge deployment.
- **FR-005**: All setup instructions MUST assume Ubuntu 22.04 LTS.
- **FR-006**: Assignments MUST be doable on student-owned hardware or provided lab kits.
- **FR-007**: Capstone MUST run at ≥15 Hz real-time inference on Jetson Orin Nano/Orin NX 8–16 GB.

### Key Entities *(include if feature involves data)*

- **Humanoid Robot**: Physical or simulated robotic platform with human-like form factor for locomotion and manipulation.
- **Autonomous System**: Software stack enabling robot operation without direct human control, including perception, planning, and actuation.
- **Embodied-AI Stack**: Combination of hardware and software components enabling AI to perceive, reason, and act in the physical world.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 90% of students successfully deploy a voice-controlled autonomous humanoid in simulation by the end of the 13-week course.
- **SC-002**: 75% of students who attempt real hardware deployment successfully achieve it.
- **SC-003**: Course feedback indicates a high level of student engagement and satisfaction with the emphasis on modern embodied-AI tools and techniques.
- **SC-004**: Students demonstrate proficiency in configuring and using ROS 2, Isaac Sim, Nav2, and VLA models relevant to humanoid robotics.
- **SC-005**: Course materials provide clear and actionable instructions for setting up the Ubuntu 22.04 LTS environment and deploying to Jetson Orin devices.
