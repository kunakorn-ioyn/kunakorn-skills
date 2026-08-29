---
name: project-summary-optimizer
description: Optimize, compact, and archive long PROJECT_SUMMARY.md files (case-insensitive e.g. project_summary.md, Project_Summary.md) across software projects to prevent LLM context window bloating. Extracts historical session logs into a structured archive file (docs/archive/PROJECT_SUMMARY_ARCHIVE.md or PROJECT_SUMMARY_ARCHIVE.md) while consolidating core architecture, active sprint context, recent sessions, test suites, and roadmap into a high-density, context-efficient main summary. Trigger on /optimize-summary, /project-summary-optimizer, or whenever the user asks to clean up, compact, split, shrink, or archive long project summaries or devlogs.
---

# Project Summary Optimizer

A specialized skill for archiving historical logs and synthesizing long `PROJECT_SUMMARY.md` files into ultra-lean, high-density reference documents that maximize LLM context efficiency without losing critical engineering continuity.

---

## 🎯 Purpose & Why This Matters

As software projects evolve over days and weeks, `PROJECT_SUMMARY.md` files naturally grow from concise overviews into multi-thousand-line session logs. When an AI assistant (or human developer) loads this file into the context window on every prompt or task compaction, it:
1. Consumes tens of thousands of tokens unnecessarily (Context Bloat).
2. Dilutes attention across outdated debug histories from past months.
3. Increases latency and costs without adding actionable value.

**The Solution:**
Preserve **100% of historical detail** in a dedicated archive file, while maintaining a **lean, structured, high-density main summary** (under 100–150 lines) focused strictly on what is needed to build, verify, and continue active work.

---

## 🔄 Execution Workflow

Follow these 5 steps in sequence when optimizing a project summary:

```
[1. Discover File] ──> [2. Evaluate Size] ──> [3. Archive History] ──> [4. Synthesize Main] ──> [5. Verify Integrity]
```

---

### Step 1: Case-Insensitive File Discovery

Locate the project summary file regardless of casing or directory location:
- Primary locations: `./PROJECT_SUMMARY.md`, `./project_summary.md`, `./Project_Summary.md`, `./docs/PROJECT_SUMMARY.md`
- If no summary file exists, notify the user and offer to create a new baseline summary using the template in `references/template.md`.

---

### Step 2: Inspection & Archival Threshold Evaluation

Analyze the current line count and content structure:
- **Optimal Target**: 80–150 lines in the primary summary.
- **Threshold for Archival**: If the file exceeds **180–200 lines** or contains more than **3–4 historical sessions**, trigger the optimization & archival process.

Identify content blocks:
1. **System Identity & Architecture**: Tech stack, core modules, database tables, auth/storage models (KEEP & DENSE-IFY).
2. **Current Sprint / Active Work**: Last 1–3 active sessions, recent architectural decisions (KEEP).
3. **Older Historical Sessions**: Past debug logs, outdated sprint notes from weeks/months ago (MOVE TO ARCHIVE).
4. **Automated Test Matrix**: Test commands and pass/fail status (KEEP & TABULATE).
5. **Future Roadmap / Backlog**: Upcoming planned tasks (KEEP).

---

### Step 3: Archive Historical Logs

Create or append to the archive file:
- **Default Archive Path**: `docs/archive/PROJECT_SUMMARY_ARCHIVE.md` (or `PROJECT_SUMMARY_ARCHIVE.md` in the root if no `docs/` folder exists).
- **Format**: Chronological Markdown log with session dates, titles, and detailed bullet points.
- **Zero Data Loss Rule**: Never delete or summarize away historical decisions in the archive file; preserve the full original fidelity so it can be referenced whenever deep archaeology is required.

---

### Step 4: Synthesize the High-Density Main Summary

Rewrite the primary `PROJECT_SUMMARY.md` using the standard 5-part architecture:

#### 1. Header & Quick Meta
```markdown
# Project Summary: [Project Name]

> **Repository Status**: [Active Development / Staging / Production]  
> **Target Architecture**: [Tech Stack, Framework, Database, Storage Layer]  
> **Historical Archive**: See [docs/archive/PROJECT_SUMMARY_ARCHIVE.md](file:///path/to/archive) for past session logs.
```

#### 2. System Architecture & Module Map (Table)
Summarize all core modules, file entry points, and readiness states in a clear Markdown table:
```markdown
## 🏛️ System Architecture & Module Map

| Module | Core Files | Responsibility | Status |
| :--- | :--- | :--- | :--- |
| **Auth** | `login.php`, `auth/` | Session management, RBAC | ✅ Production Ready |
| **Core Feature** | `feature/index.php` | Main workflow engine | ✅ Active |
```

#### 3. Active Phase / Recent Engineering Work
Highlight only the last 1–3 relevant sessions with concrete technical decisions and file links:
```markdown
## 🚀 Active Phase: [Current Feature / Sprint Focus]

### 1. [Recent Major Feature] ([path/to/file](file:///...))
- Summary of architecture change, key parameters, and design patterns.
```

#### 4. Automated Test Matrix & Verification Commands
A single tabular matrix of verification tests and their latest execution status:
```markdown
## 🧪 Automated Test Suites & Verification

| Test Suite | Purpose | Status |
| :--- | :--- | :--- |
| `tests/test_feature.php` | Unit & integration validation | ✅ 100% PASS |
```

#### 5. Future Roadmap & Architectural Backlog
Clear list of upcoming features, technical debt to refactor, or security hardening items.

---

### Step 5: Verification & Integrity Checklist

Before finalizing, verify:
- [ ] Primary summary is concise (<150 lines) and readable in under 60 seconds.
- [ ] All file paths in Markdown links are valid and clickable (`file:///...`).
- [ ] No active roadmap items or test commands were accidentally omitted.
- [ ] Archive file exists, is linked from the main summary, and contains all historical sessions.
- [ ] Automated tests continue to pass without error.

---

## 📌 Summary of Operating Rules

1. **Case-Insensitive Agnostic**: Handle `PROJECT_SUMMARY.md`, `project_summary.md`, or any case variation seamlessly.
2. **High Information Density**: Prefer structured Markdown tables and bulleted key-value pairs over conversational paragraphs.
3. **Continuous Maintainability**: Every time this skill runs on a project, it keeps the main file permanently within the optimal 100–150 line zone.
