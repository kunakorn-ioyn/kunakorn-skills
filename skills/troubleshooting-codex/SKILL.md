---
name: troubleshooting-codex
description: Systematic capture, lookup, and documentation of technical bugs, root causes, architectural pitfalls, and verified fixes across the codebase. Use whenever the user says "record this as a lesson", "บันทึกเป็นบทเรียน", "/troubleshooting-codex", "/troubleshoot-log", "/learn", after resolving tricky bugs, or when encountering a recurring issue that needs fast root cause diagnosis from past incidents.
---

# Troubleshooting Codex & Lessons Learned Scribe

A specialized engineering skill for recording, indexing, and consulting the project's living knowledge base of solved bugs, design pitfalls, and architectural lessons learned.

---

## 🎯 Purpose & Philosophy

1. **Zero Repetition (Never Fail Twice)**: Once an architectural flaw or subtle bug is fixed, capture the root cause and golden prevention rule so future AI and human sessions never repeat it.
2. **Instant MTTR Reduction**: When encountering an issue, check `docs/troubleshooting/` first to see if a similar symptom was already diagnosed and resolved.
3. **Institutional Memory**: Document not just *what* was changed, but the exact mechanism of failure and the rule to prevent regression.

---

## 🚀 Workflows

### 1. Recording a New Incident / Lesson Learned (`/record-lesson` or after fixing a bug)

When an issue is diagnosed and fixed:
1. Determine the category:
   - `css-ui` (Layout, design tokens, responsive bugs, font/widget unstyling)
   - `api-db` (SQL queries, locking, transactions, concurrency, schema)
   - `auth-roles` (Session guards, role switching, permissions)
   - `storage-files` (Google Drive, uploads, IndexedDB, MIME types)
   - `wizard-workflow` (Stepper, draft caching, state persistence, validation)
2. Create or update the incident markdown in `docs/troubleshooting/YYYY-MM-DD-[slug].md` following `references/TEMPLATE_INCIDENT.md`.
3. Update `docs/troubleshooting/README.md` index table.
4. Record any high-level architectural rule in `PROJECT_SUMMARY.md`.

---

### 2. Consulting the Codex during Debugging

When investigating an unexpected behavior, error, or UI anomaly:
1. Scan `docs/troubleshooting/` for matching keywords, error messages, or symptoms.
2. If a matching incident is found, apply the verified solution and verify against the golden prevention rule.
3. If new nuances exist, update the existing incident file.

---

## 📝 Incident Schema

Every record in `docs/troubleshooting/` must contain:

- **Incident ID & Title**: Short descriptive title.
- **Date & Category**: When it occurred and affected area.
- **Symptoms & Visual Cues**: What the user saw (screenshots, broken layout, console errors).
- **Root Cause Mechanism**: The underlying reason why it failed.
- **Verified Fix (Code Diff)**: The exact change that solved it.
- **Golden Prevention Rule**: Clear directive on how to write code going forward to prevent regression.
- **Affected Files**: Clickable links to relevant files.
