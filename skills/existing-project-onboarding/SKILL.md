---
name: existing-project-onboarding
description: Skill for onboarding an AI Agent onto an ongoing/in-progress project. Use when the user brings an active codebase or existing project context, needs to audit the current state, retroactively generate Obsidian context notes, and plan immediate next steps without re-doing finished work.
---

# Existing Project Onboarding & Catch-Up Skill

A specialized skill to rapidly audit, structure, and onboard an active project into an Obsidian Knowledge Base and prepare the AI Agent for immediate execution.

## Core Mandate

1. **Audit & Reconstruct**: Extract requirements, architecture, and completed progress from existing materials (code, logs, scattered notes).
2. **Create Baseline Notes**: Generate initial Obsidian notes for `01_Context` and `02_Execution` based on historical work.
3. **Determine Ground Zero**: Identify exact current status, blockers, and immediate next tasks.

---

## Workflow Steps

### Step 1: Project Discovery & Context Dump

Ask the user or inspect provided files for 4 core elements:

- **Current State**: What parts are working/finished?
- **Current Architecture/Tech Stack**: Languages, frameworks, tools, or APIs currently in use.
- **Existing Files/Docs**: Source code, config files, or old notes available for reference.
- **Immediate Goal**: What is the immediate feature to build or bug to fix _today_?

### Step 2: Generate Obsidian Baseline (Retro-Fit)

Synthesize the provided information into 2 master baseline notes ready for Obsidian:

1. **`01_Context/Project_Overview.md`**
   - Background & Goals
   - Current Architecture & Tech Stack
   - Key Decisions Made So Far

2. **`02_Execution/Status_and_Roadmap.md`**
   - ✅ **Completed Features** (Historified)
   - 🚧 **In-Progress Work**
   - 📋 **Backlog / Next Steps**

### Step 3: Transition to Active Execution

Once the baseline context is established:

- Confirm understanding of the current state with the user.
- Switch to active development mode (using the `universal-project-manager` workflow) to assist with the next task.
