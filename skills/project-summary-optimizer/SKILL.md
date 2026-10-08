---
name: project-summary-optimizer
description: Full lifecycle manager for PROJECT_SUMMARY.md (case-insensitive e.g. project_summary.md, Project_Summary.md) across software projects. Automatically scaffolds and initializes fresh baseline summaries from codebase analysis (detecting stack, entry points, database, and recent git history), and intelligently compacts/archives bloated summaries (>150-200 lines) into structured archives (docs/archive/PROJECT_SUMMARY_ARCHIVE.md) to eliminate LLM token bloat while guaranteeing 100% historical continuity. Trigger on /setup-summary, /init-summary, /scaffold-summary, /optimize-summary, /project-summary-optimizer, "สร้างไฟล์สรุปโปรเจกต์", "setup project summary", "สร้าง project_summary.md", "เริ่มต้น project summary", "clean up summary", or "shrink devlog".
---

# Project Summary Lifecycle Manager (Setup & Optimizer)

An autonomous lifecycle skill for **scaffolding, initializing, maintaining, and optimizing** living `PROJECT_SUMMARY.md` files across software projects. It ensures AI assistants and engineering teams always have instant, high-density project context without bloating LLM context windows.

---

## 🎯 Purpose & The Dual Challenge

1. **The Blank Canvas Problem (Starting a Project)**:
   - When onboarding an AI agent onto a new or existing repository without a summary file, the agent wastes tokens repeatedly rediscovering the stack, entry points, and recent work.
   - **Solution (Mode 1 - Setup)**: Autonomously scan project files, configuration, and git history to generate a complete, standardized baseline summary in under 30 seconds.

2. **The Context Bloat Problem (Project Growth)**:
   - As projects evolve over weeks, `PROJECT_SUMMARY.md` expands into thousands of lines of obsolete debugging logs, diluting AI attention and burning tokens.
   - **Solution (Mode 2 - Optimize)**: Move historical logs to `docs/archive/PROJECT_SUMMARY_ARCHIVE.md` with zero data loss, keeping the main summary lean (80–150 lines).

---

## 🔄 Dual Operational Modes

The skill automatically selects or switches modes based on user intent and repository state:

```
                                [Check Repository State]
                                           │
                    ┌──────────────────────┴──────────────────────┐
                    ▼                                             ▼
        [File Missing or /init requested]             [File Exists & Bloated]
                    │                                             │
             ▼ MODE 1: SETUP                               ▼ MODE 2: OPTIMIZE
       1. Auto-Scan Codebase                         1. Evaluate Line Count
       2. Extract Stack & Entry points               2. Extract Historical Logs
       3. Analyze Recent Git History                 3. Write to Archive File
       4. Scaffold Clean Baseline                    4. Condense Main Summary
```

---

## 🛠️ Mode 1: Automated Discovery & Setup (Init Mode)

Triggered when:
- User calls `/setup-summary`, `/init-summary`, `/scaffold-summary`, or asks *"สร้างไฟล์สรุปโปรเจกต์"*, *"setup project summary"*
- OR when `PROJECT_SUMMARY.md` (any casing) does not exist in the repository.

### Step 1: Codebase Deep Discovery
Run non-destructive read operations to extract foundational context:
1. **Tech Stack & Dependencies**:
   - Inspect package manifests: `package.json`, `composer.json`, `requirements.txt`, `pyproject.toml`, `go.mod`, `pom.xml`, `Cargo.toml`.
   - Identify language version, web framework, runtime, and key libraries.
2. **Database & Persistence**:
   - Look for ORM schemas, database migrations, or SQL files (`migrations/`, `prisma/`, `schema.sql`, `models/`, `.env.example`).
3. **Application Entry Points & Module Map**:
   - Locate main entry files (e.g. `index.html`, `src/App.tsx`, `src/index.ts`, `server.js`, `api/`, `routes/`, `app.py`).
4. **Active Development Focus & Git History**:
   - Run `git log -n 5 --oneline` and `git status` to see what was recently committed or is currently in progress.
5. **Test Framework & Verification Commands**:
   - Detect test suites (`npm test`, `pytest`, `phpunit`, `go test`, etc.).

### Step 2: Scaffold Standard Baseline
Generate `PROJECT_SUMMARY.md` adhering strictly to Rule 1 and the high-density standard:

```markdown
# Project Summary: [Project Name]

## 1. Overview & Objective
- **Project Goal**: [Concise 1–2 sentence description of the system]
- **Tech Stack & Environment**: [Runtime, Framework, Database, Styling/Tooling]
- **Target Architecture**: [Monolith / Client-Server / Microservices / CLI]

## 2. System Architecture & Module Map
| Module | Core Files / Directories | Responsibility | Status |
| :--- | :--- | :--- | :--- |
| **Auth / Core** | `src/auth/` | Session management & authentication | ✅ Ready |
| **API Engine** | `src/api/` | REST / GraphQL endpoints | 🔄 In Progress |

## 3. Current State & Progress
- [x] Initialized architecture and core modules
- [/] Active feature in progress
- [ ] Upcoming priority milestone

## 4. Key Technical Decisions
- **[Technology/Architecture]**: [Decision made] — *Rationale:* [Brief reason why]

## 5. Automated Test Suites & Verification
| Test Suite | Purpose | Command | Status |
| :--- | :--- | :--- | :--- |
| Unit / Integration | Core logic verification | `npm test` | ✅ Passing |

## 6. Known Issues & Constraints
- [Active blockers or architectural constraints, or "None"]

## 7. Next Steps
1. [Immediate next actionable item]
2. [Subsequent milestone task]
```

---

## ⚡ Mode 2: Archival & Token Optimization (Optimizer Mode)

Triggered when:
- User calls `/optimize-summary`, `/project-summary-optimizer`, or asks *"clean up summary"*, *"shrink devlog"*, *"บีบอัด summary"*
- OR when the file exceeds **180–200 lines** or contains **>3 historical sessions**.

### Step 1: Evaluate Size & Partition Content
Analyze the file into 4 functional buckets:
1. **Core Identity & Architecture (KEEP & DENSE-IFY)**: Tech stack, modules table, database definitions.
2. **Active Sprint / Recent Work (KEEP)**: Only the last 1–2 active sessions and current WIP tasks.
3. **Older Historical Logs (MOVE TO ARCHIVE)**: Previous sprint logs, fixed bugs from past weeks/months.
4. **Test Commands & Roadmap (KEEP & TABULATE)**: Keep test table and active backlog.

### Step 2: Write / Append to Historical Archive
- **Destination**: `docs/archive/PROJECT_SUMMARY_ARCHIVE.md` (or `PROJECT_SUMMARY_ARCHIVE.md` in root if no `docs/` folder exists).
- **Format**: Chronological Markdown log with dates, session titles, and full detail.
- **Zero Data Loss Rule**: Never discard architectural rationale or historical context; store 100% of historical detail in the archive file.

### Step 3: Rewrite High-Density Main Summary
Rewrite `PROJECT_SUMMARY.md` keeping it strictly under **80–150 lines**:
- Add top reference link to archive: `> **Historical Archive**: See [PROJECT_SUMMARY_ARCHIVE.md](file:///path/to/archive)`
- Use Markdown tables rather than verbose paragraphs.
- Keep only immediate next steps and recent architectural changes.

---

## ✅ Quality Checklist

Before completing either mode:
- [ ] Primary summary is concise (<150 lines) and readable in under 60 seconds.
- [ ] File links use valid Markdown file URIs (`file:///...`).
- [ ] If archival was performed, archive file is created, linked, and verified.
- [ ] Tech stack and verification commands accurately reflect the current repo.
