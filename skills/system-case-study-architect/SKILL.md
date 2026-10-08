---
name: system-case-study-architect
description: Autonomous engineering case study extractor and portfolio architect. Conducts an interactive, multi-phase Socratic interview (Grill Flow) to analyze, extract, and document real-world software systems into high-value "System Portfolio & Engineering Case Studies" (with Mermaid diagrams, ADRs, business impact metrics, and NDA sanitization). Trigger on /case-study, /system-portfolio, /extract-case-study, "บันทึกผลงานระบบ", "ทำ case study", "เก็บพอร์ตระบบ", or whenever the user wants to document past systems, architectures, and engineering achievements.
---

# System Case Study Architect

Turn real-world software engineering achievements and system architectures into high-value, standardized **System Portfolio & Engineering Case Studies**.

This skill guides you through an interactive Socratic interview to probe system context, architectural decisions, technical trade-offs, measurable business impacts, and production retrospectives—while ensuring strict NDA/PII sanitization and auto-updating a Master Portfolio Hub.

---

## Workflow Overview

When invoked, execute the following phased process:

```
[Phase 0: Intake & NDA Setup]
        ↓
[Phase 1: Problem & Business Context]
        ↓
[Phase 2: Architecture & Data Flow (+ Dynamic Mermaid)]
        ↓
[Phase 3: Key Architectural Decisions & Trade-Offs (ADR)]
        ↓
[Phase 4: Impact, Metrics & Production Retrospective]
        ↓
[Phase 5: Markdown Generation & Portfolio Hub Indexing]
```

---

## Phase 0: Intake & NDA Sanitization Setup

Ask the initial triage questions:
1. **System Name / Working Title**
2. **Confidentiality / NDA Level**:
   - `Public`: Real company & system name allowed.
   - `Confidential / NDA-Protected`: AI must immediately formulate a sanitized industry descriptor (e.g. *"Top 3 Logistics Provider in SEA"*, *"Tier-1 Enterprise Fintech Platform"*).
3. **Role & Timeline**: e.g., *Lead Architect / Senior Full-Stack Engineer (2024 - 2025)*.
4. **Primary Domain**: e.g., FinTech, E-Commerce, Logistics, HealthTech, Internal Ops.

> [!IMPORTANT]
> **Sanitization Rules**:
> - Never store real client names, database connection strings, internal IP addresses, secrets, or real customer PII.
> - Use abstracted service names (e.g., `payment-webhook-receiver` instead of `internal-corp-pay-prod-01`).

---

## Phase 1: Problem & Business Context (The "Why")

Probe the starting conditions and business/technical blockers before the system existed:
- **Core Bottleneck**: What was broken or failing? (e.g., legacy monolith crashes, manual batch processing taking 6 hours, database locks).
- **Constraints**: Time, budget, team size, legacy compliance, SLA requirements.
- **Goal**: What was the north star metric or target when starting?

*Formulate 2-3 specific probing questions and wait for the user's response.*

---

## Phase 2: Architecture & Solution Deep-Dive (The "How")

Deep-dive into the technical design:
- **Tech Stack**: Languages, frameworks, databases, message brokers, caching, infrastructure/cloud.
- **Topology & Separation of Concerns**: Monolith, Modular Monolith, Microservices, Event-Driven, or Serverless.
- **Dynamic Mermaid Diagram Selection**:
  - For microservices / multi-tier: Render a **Component Topology Graph** (`graph TD` / `graph LR`).
  - For transactional / API pipelines: Render a **Flow Sequence Diagram** (`sequenceDiagram`).
  - For complex workflow lifecycles (e.g. Order states, Payment escrow): Render a **State Diagram** (`stateDiagram-v2`).

*Review the user's stack, synthesize the data flow, and preview the proposed Mermaid diagram to get confirmation.*

---

## Phase 3: Key Decisions & Trade-Offs (ADR)

Probe the non-obvious engineering decisions:
- What alternative approaches or technologies were considered?
- Why was **Technology X** chosen over **Alternative Y**? (e.g., PostgreSQL JSONB vs MongoDB, Redis Pub/Sub vs Kafka, REST vs gRPC).
- What were the accepted trade-offs or compromises?

*Extract at least 1-2 concrete Architectural Decision Records (ADRs) with Context, Decision, and Trade-offs.*

---

## Phase 4: Impact, Metrics & Retrospective (The "Results")

Extract verifiable results and lessons learned:
- **Quantifiable Metrics**:
  - Speed / Latency (e.g., *p95 response time dropped from 1.8s to 120ms*)
  - Throughput / Scalability (e.g., *scaled from 500 RPS to 10,000 RPS without downtime*)
  - Operational / Cost (e.g., *cut AWS monthly bill by 42%, reduced daily manual tasks from 4 hours to 0*)
- **Production Retrospective**:
  - What unexpected surprises or edge cases appeared post-launch?
  - If you had to redesign this system today from scratch, what would you do differently?

---

## Phase 5: Artifact Generation & Indexing

Once all phases are completed:

### 1. Write the Case Study Document
Create `case-studies/<slug-project-name>/README.md` (or `case-studies/<slug-project-name>.md`) using this structure:

```markdown
---
title: "[Project Title]"
slug: "[slug-project-name]"
domain: "[Domain]"
role: "[Role]"
timeline: "[Year/Duration]"
tech_stack: ["Tech1", "Tech2", "Tech3"]
architecture_patterns: ["Event-Driven", "Microservices", ...]
impact_summary: "[1-sentence impact]"
nda_sanitized: true
date_documented: "YYYY-MM-DD"
---

# [System Title / Sanitized Title]

> **Executive Summary**: [2-3 concise lines describing system purpose, role, stack, and primary business impact]

## 1. Problem & Context
- **Business Challenge**: ...
- **Legacy Limitations & Bottlenecks**: ...
- **Target Goals & Constraints**: ...

## 2. Architecture & Technical Solution
- **High-Level Overview**: ...
- **Core Tech Stack**:
  - **Backend / Compute**: ...
  - **Storage & Caching**: ...
  - **Messaging / Async**: ...
  - **DevOps & Infra**: ...

### System Architecture Diagram
\`\`\`mermaid
[Dynamic Mermaid Diagram fitting system complexity]
\`\`\`

- **Key Data Flow**:
  1. ...
  2. ...

## 3. Key Architectural Decisions (ADR)
### ADR-01: [Decision Title]
- **Context & Problem**: ...
- **Considered Options**: ...
- **Chosen Decision**: ...
- **Trade-offs & Rationale**: ...

## 4. Measurable Impact & Metrics
| Metric | Before | After | Change / Benefit |
| :--- | :--- | :--- | :--- |
| **[Metric 1]** | ... | ... | **+X% / -Y%** |
| **[Metric 2]** | ... | ... | ... |

## 5. Lessons Learned & Retrospective
- **What Worked Well**: ...
- **Production Pitfalls & Roadblocks**: ...
- **What We Would Do Differently**: ...
```

---

### 2. Update Master Hub (`case-studies/PORTFOLIO_INDEX.md`)

Automatically create or update `case-studies/PORTFOLIO_INDEX.md` maintaining a structured index:

```markdown
# 🏛️ Systems Portfolio & Engineering Case Studies

Master catalog of engineered systems, architectures, and measurable technical achievements.

## 📊 Quick Statistics
- Total Documented Systems: `N`
- Domains Covered: `FinTech`, `E-Commerce`, `Logistics`, ...

---

## 🗂️ All Case Studies

| System / Project | Domain | Tech Stack | Key Pattern | Impact Highlight | Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **[Sanitized Title]** | FinTech | Go, Redis, PostgreSQL | Event-Driven | -40% AWS Cost, 10k RPS | [View Study](./[slug]/README.md) |

---

## 🏷️ Browse by Domain
- **FinTech**: ...
- **Logistics & Supply Chain**: ...

## ⚡ Browse by Architecture Pattern
- **Event-Driven / Async Queues**: ...
- **High-Throughput / Caching**: ...
```

---

## Best Practices & Conversational Rules

1. **One Question Phase at a Time**: Do not dump 15 questions in one message. Ask Phase 1, absorb the answer, probe deeper if vague, then proceed to Phase 2.
2. **Help User Articulate Trade-offs**: If the user says "we used Redis because it is fast", probe gently: *"Did you consider Memcached or in-memory LRU? What data eviction or persistence requirements drove that decision?"*
3. **Make Diagrams Crystal Clear**: Keep Mermaid diagrams semantic, clean, and legible.
4. **Sanitize by Default**: If there is any doubt about whether a metric or name is proprietary, anonymize it responsibly while keeping the engineering depth intact.
