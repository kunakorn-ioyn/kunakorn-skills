---
name: universal-project-manager
description: Master skill for managing, executing, and documenting any software or workflow project. Use whenever the user starts a new project, works through features, debugs issues, or wants to format context/logs for saving into Obsidian. Trigger automatically on project setup, devlogs, error troubleshooting, or documentation requests.
---

# Universal Project Manager & Context Keeper

A master skill designed to guide AI Agents through structured execution while capturing all project context, architecture, troubleshooting, and lessons learned for Obsidian.

## Core Mandate

1. **Maintain Context**: Keep track of requirements, architecture decisions, and current state without losing history.
2. **Step-by-Step Execution**: Break complex requests into clear, testable steps.
3. **Obsidian-Ready Output**: Automatically format knowledge, logs, and solutions into clean Markdown ready to be pasted into Obsidian.

---

## Standard Operating Procedure

### Phase 1: Context Capture & Requirement Definition

When starting or resuming a project, establish the core parameters first:

- **Goal & Target**: What problem are we solving?
- **Tech Stack / Tools**: Languages, frameworks, APIs, or software involved.
- **Constraints**: Mandatory rules, forbidden practices, or performance limits.
- **Obsidian Structure**: Ensure outputs align with `01_Context`, `02_Execution`, `03_Troubleshooting`, `04_Knowledge`, and `05_Outputs`.

### Phase 2: Feature Development & DevLog

When building features or executing tasks:

1. Explain the logic and approach **before** generating long code blocks.
2. Execute work incrementally and verify each step.
3. Provide a **DevLog Summary** at the end of each completed task:

```markdown
### [YYYY-MM-DD] Task: [Feature Name]

- **Objective**: What was implemented.
- **Key Changes**: Files created/modified or steps taken.
- **Architecture/Design Decision**: Why this method was chosen.
```
