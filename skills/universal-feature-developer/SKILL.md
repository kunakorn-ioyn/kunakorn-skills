---
name: universal-feature-developer
description: Universal skill for building features, refactoring, and fixing bugs on ANY active project regardless of tech stack (PHP, Node.js, Python, React, Go, etc.). Handles dynamic context discovery, safe execution, automated stack-specific testing, and auto-syncs progress to the project's Obsidian Codex.
---

# Universal Feature Developer & Execution Skill

A project-agnostic master skill designed to guide AI Agents through building features, debugging, and maintaining any codebase while keeping quality high and the Obsidian Knowledge Base (Codex) up to date.

## Core Mandate

1. **Context Discovery First**: Inspect existing code, project rules, and stack before writing new features.
2. **Stack-Agnostic Quality Gate**: Detect and run the project's native syntax/linting/test commands after every code modification.
3. **Obsidian Codex Auto-Sync**: Automatically record task completions, technical decisions, and bug fixes into the project's Obsidian Vault.

---

## Standard Execution Workflow

### Phase 1: Dynamic Discovery & Pre-Check

Before writing or modifying code, inspect and identify:

- **Tech Stack & Architecture**: Inspect existing codebase and read `01_Context/` files in Obsidian (if available) to understand patterns and domain logic.
- **Verification Commands**: Detect available project check scripts (e.g., `php -l`, `npm run lint`, `npx tsc`, `pytest`, `go vet`).
- **Target Files**: Identify exact files needing changes to minimize unnecessary edits.

### Phase 2: Implementation Guidelines

1. **Respect Existing Conventions**: Mirror the style, naming conventions, and design patterns already present in the repository.
2. **Targeted Edits**: Perform surgical, incremental edits rather than full-file rewrites.
3. **Security & Quality**: Enforce input validation, parameter isolation, and proper error handling relevant to the active tech stack.

### Phase 3: Automated Quality Gate

Execute the stack's native check command immediately after editing. Do not consider a task complete until syntax/tests pass cleanly.

_Common stack verification triggers:_

- **PHP**: `php -l <filename>`
- **Node / TS**: `npx tsc --noEmit` or `npm run lint`
- **Python**: `python -m py_compile <filename>` or `pytest`
- **Go**: `go vet ./...` / `go test ./...`
- **Rust**: `cargo check`

### Phase 4: Obsidian Codex Auto-Sync

Upon successful verification, update the project's Obsidian Vault:

1. **Update Roadmap**: Move completed tasks from _In-Progress/Backlog_ to _Completed_ in `02_Execution/Status_and_Roadmap.md`.
2. **Append DevLog Entry** (at the bottom of execution/status notes):

```markdown
### [YYYY-MM-DD] Task: [Feature / Fix Name]

- **Scope**: Summary of changes made.
- **Files Modified**: `path/to/file1`, `path/to/file2`
- **Verification**: [Passed command, e.g., `php -l` / `npm test`]
```
