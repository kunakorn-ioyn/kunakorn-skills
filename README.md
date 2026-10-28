<div align="center">

# ⚡ Antigravity AI Skills Collection

**Production-grade, battle-tested Agent Skills for Google Antigravity, Gemini CLI, Cursor, and Modern AI Coding Workflows.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Antigravity%20%7C%20Gemini%20%7C%20Cursor-8A2BE2)](#-quick-installation)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](#)

<p align="center">
  <a href="#-skills-catalog">Skills Catalog</a> •
  <a href="#-quick-installation">Quick Installation</a> •
  <a href="#-syncing-skills">Syncing Skills</a> •
  <a href="#-how-it-works">How It Works</a> •
  <a href="#-contributing">Contributing</a> •
  <a href="#-license">License</a>
</p>

---

</div>

## 🌟 Overview

This repository contains a curated collection of dynamic **Agent Skills** designed to supercharge autonomous AI engineering. Each skill acts as a specialized instruction module that equips AI agents (such as Google Antigravity, Gemini, and Claude/Cursor) with domain-specific workflows, zero-repetition error handling, continuous deployment automation, UX/UI hardening, academic report generation, exam item analysis & grading automation, and Obsidian knowledge synchronization.

---

## 🗂️ Skills Catalog

The skills are categorized into 6 specialized domains:

### 1. 🎨 UX/UI & Usability Architecture
| Skill Name | Purpose & Workflow | Key Triggers & Keywords |
| :--- | :--- | :--- |
| [**`ux-feature-architect`**](./skills/ux-feature-architect/SKILL.md) | Senior UX/UI Architect & Product Usability Specialist. Conducts deep user journey audits, edge-case risk prevention, developer blindspots detection, friction reduction, and staging vs commit architectures. | `/ux-architect`, `/ux-advisor`, `/ux-audit`, `/feature-hardening`, `วิเคราะห์ UX`, `คิดมุมมอง UXUI`, `ออกแบบยังไงให้ใช้ง่าย`, `คิดความเสี่ยง` |
| [**`webapp-doc-architect`**](./skills/webapp-doc-architect/SKILL.md) | Automated software documentation engine that extracts project information, schemas, and routes to generate enterprise manuals, technical specs, Word (.docx), PowerPoint (.pptx), and PDF guides (Diataxis & IEEE 1063). | `/webapp-doc`, `/generate-manual`, `สร้างคู่มือระบบ`, `ทำเอกสารสถาปัตยกรรม` |

---

### 2. 🚀 Feature Engineering & Project Management
| Skill Name | Purpose & Workflow | Key Triggers & Keywords |
| :--- | :--- | :--- |
| [**`universal-feature-developer`**](./skills/universal-feature-developer/SKILL.md) | Stack-agnostic feature builder and refactoring workflow with dynamic pre-checks, native linting gates, and Obsidian auto-sync. | `/build-feature`, `add new feature`, `refactor module`, `stack-specific test` |
| [**`universal-project-manager`**](./skills/universal-project-manager/SKILL.md) | Master orchestrator for step-by-step project planning, tracking active sprint state, and formatting structured notes for Obsidian. | `/project-manager`, `plan milestone`, `track sprint`, `Obsidian project sync` |
| [**`existing-project-onboarding`**](./skills/existing-project-onboarding/SKILL.md) | Rapidly audits active codebases, retroactively establishes context & execution baselines, and plans next steps without re-doing finished work. | `onboard project`, `audit codebase`, `project catchup`, `context baseline` |

---

### 3. 🧠 Engineering Memory & Session Continuity
| Skill Name | Purpose & Workflow | Key Triggers & Keywords |
| :--- | :--- | :--- |
| [**`troubleshooting-codex`**](./skills/troubleshooting-codex/SKILL.md) | Systematic capture and indexing of bugs, root causes, and golden prevention rules into a living lessons-learned codex. | `/record-lesson`, `/troubleshooting-codex`, `บันทึกเป็นบทเรียน`, `never repeat`, `อย่าพลาดอีก` |
| [**`daily-devlog-recorder`**](./skills/daily-devlog-recorder/SKILL.md) | Multi-layer change detection engine (FS Timestamps, Git Diff/Log, Active Session Context) recording daily progress into Keep-a-Changelog standard devlogs. | `/daily-log`, `/changelog`, `/devlog`, `สรุปงานวันนี้`, `บันทึกสิ่งที่แก้ไขวันนี้`, `จบงานวันนี้` |
| [**`project-summary-optimizer`**](./skills/project-summary-optimizer/SKILL.md) | Full lifecycle manager for `PROJECT_SUMMARY.md`. Autonomously scans codebase to scaffold fresh baseline summaries, and intelligently compacts/archives bloated files to prevent token bloat. | `/setup-summary`, `/init-summary`, `/optimize-summary`, `สร้างไฟล์สรุปโปรเจกต์`, `setup project summary`, `clean up summary` |

---

### 4. 🎓 Academic, Thesis & Enterprise Reporting
| Skill Name | Purpose & Workflow | Key Triggers & Keywords |
| :--- | :--- | :--- |
| [**`capstone-thesis-generator`**](./skills/capstone-thesis-generator/SKILL.md) | Autonomous generator of complete 5-chapter Thai University Graduation Project / Capstone Theses in Word (.docx) format with Selenium live screenshots, full Data Dictionaries, and Black-box test matrices. | `/thesis`, `/capstone-thesis`, `/academic-report`, `/generate-thesis`, `ทำเล่มจบ`, `สร้างเล่มปริญญานิพนธ์`, `ทำรายงานโครงงาน 5 บท` |
| [**`km-system-report-generator`**](./skills/km-system-report-generator/SKILL.md) | Official Knowledge Management (KM) and Full System Engineering Report generator in Word (.docx) format aligned with official university KM standards. | `/km-report`, `/full-report`, `/generate-doc`, `สร้างรายงานฉบับเต็ม`, `ทำเอกสาร KM`, `สร้างรายงาน Word` |
| [**`doc-coauthoring`**](./skills/doc-coauthoring/SKILL.md) | Structured collaborative document creation across 3 stages: Context Gathering, Refinement & Structure, and Reader Testing. | `write a doc`, `draft a proposal`, `create a spec`, `co-author doc` |
| [**`vu-exam-exporter`**](./skills/vu-exam-exporter/SKILL.md) | ดึงข้อมูลคะแนนสอบ ผลสอบรายบุคคล คำตอบรายข้อ และวิเคราะห์คุณภาพข้อสอบ (Item Analysis: ค่าความยาก $p$, อำนาจจำแนก $r$) จากระบบ VU Exam Manage Summative ออกมาเป็นไฟล์ Excel 5 แผ่นงานแบบสมบูรณ์ รองรับโหมดถามทีละขั้น (Interactive Wizard) หรือระบุรหัสสอบทันที | `/vu-exam-exporter`, `ดึงคะแนนสอบ`, `VU Exam`, `วิเคราะห์ข้อสอบ`, `ทำรายงานผลสอบ`, `export exam`, `summative exam` |

---

### 5. ⚙️ DevOps & Cloud Deployment
| Skill Name | Purpose & Workflow | Key Triggers & Keywords |
| :--- | :--- | :--- |
| [**`aapanel-git-autodeploy`**](./skills/aapanel-git-autodeploy/SKILL.md) | Automates CI/CD auto-deployment from GitHub to aaPanel servers using Webhooks with root-level script isolation & permission fixing. | `aaPanel deploy`, `webhook setup`, `$HOME not set`, `dubious ownership` |

---

### 6. 🌌 World Building & Creative Systems
| Skill Name | Purpose & Workflow | Key Triggers & Keywords |
| :--- | :--- | :--- |
| [**`trpg-world-builder`**](./skills/trpg-world-builder/SKILL.md) | Turnkey TRPG & D&D 5e world builder and lore ingester into structured playable setting, dedicated classes, GM rules, and Obsidian codex. | `/build-world`, `/setup-campaign`, `/trpg-world-builder`, `/create-universe`, `สร้างโลก`, `เซ็ตอัพโลกใหม่` |
| [**`visual-entity-forge`**](./skills/visual-entity-forge/SKILL.md) | Lore-accurate entity and creature designer from user images, formulating complete D&D 5e stat blocks, combat tactics, and habitat lore. | `/forge-entity`, `/create-beast`, `/image-to-beast`, `ออกแบบจากรูป`, `สร้างมอนสเตอร์จากภาพ` |

---

## 🚀 Quick Installation

### 1-Click Automated Installation (Recommended)

Clone the repository and run the installer script:

```bash
# 1. Clone the repository
git clone https://github.com/kunakorn-ioyn/kunakorn-skills.git
cd kunakorn-skills

# 2. Run Installer
# For Windows (PowerShell)
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1

# For macOS / Linux (Bash)
chmod +x ./scripts/install.sh
./scripts/install.sh
```

> **Tip**: To install skills **locally** into your current project's `.agents/skills/` directory instead of global configuration:
> - Windows: `powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1 -TargetMode local`
> - Mac/Linux: `./scripts/install.sh local`

---

## 🔄 Syncing Skills

If you develop or tweak skills inside your global config (`~/.gemini/config/skills/`), you can pull them back into this repository with one command:

```powershell
# Sync all skills from global config to repository
powershell -ExecutionPolicy Bypass -File .\scripts\sync-from-global.ps1

# Or sync specific skills only
powershell -ExecutionPolicy Bypass -File .\scripts\sync-from-global.ps1 -SkillNames "ux-feature-architect", "daily-devlog-recorder"
```

---

### Manual Installation

You can also copy the `skills/` directory directly to your target destination:

- **Global Config (Antigravity & Gemini CLI)**:
  - Windows: `%USERPROFILE%\.gemini\config\skills\`
  - macOS/Linux: `~/.gemini/config/skills/`
- **Project-Level Config (Workspace Only)**:
  - Place skill folders into `<your-project-root>/.agents/skills/`

---

## ⚙️ How It Works

Each skill directory contains a self-contained `SKILL.md` file structured with YAML frontmatter and operational guidelines:

```markdown
---
name: skill-name
description: High-density description of what the skill accomplishes and exact semantic trigger cues.
---

# Skill Title
... detailed step-by-step guidance, decision matrices, and scripts ...
```

### Discovery & Execution Protocol
1. **Dynamic Scan**: The AI Agent scans the active skill roots (`~/.gemini/config/skills` or `.agents/skills`).
2. **Intent Matching**: When you issue a command or describe a task matching a skill's description, the agent automatically adopts the skill's persona, checklists, and safety constraints.
3. **Deterministic Output**: The agent follows the exact procedural pipeline defined in the skill documentation.

---

## 🛠️ Directory Structure

```text
.
├── .github/                         # GitHub issue & PR templates
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── pull_request_template.md
├── scripts/                         # ⚡ 1-Click deployment & sync scripts
│   ├── install.ps1                  # Windows PowerShell installer
│   ├── install.sh                   # macOS & Linux Bash installer
│   └── sync-from-global.ps1         # Sync skills from global config to repo
├── skills/                          # 📦 Curated collection of 16 AI skills
│   ├── aapanel-git-autodeploy/      # aaPanel CI/CD WebHook deployment
│   ├── capstone-thesis-generator/   # Thai university 5-chapter thesis generator (.docx)
│   ├── daily-devlog-recorder/       # 4-layer changelog & daily devlog recorder
│   ├── doc-coauthoring/             # Collaborative doc co-authoring workflow
│   ├── existing-project-onboarding/ # Ongoing codebase audit & onboarding
│   ├── km-system-report-generator/  # Official KM & full system engineering report (.docx)
│   ├── project-summary-optimizer/   # Token-efficient summary optimizer & archiver
│   ├── system-case-study-architect/ # Architecture case studies & portfolio extractor
│   ├── troubleshooting-codex/       # Bug diagnosis & institutional lessons codex
│   ├── trpg-world-builder/          # Autonomous TRPG & D&D 5e world builder
│   ├── universal-feature-developer/ # Dynamic feature development & lint-gate runner
│   ├── universal-project-manager/   # Master project orchestrator & Obsidian tracker
│   ├── ux-feature-architect/        # UX/UI usability & developer blindspots architect
│   ├── visual-entity-forge/         # Image-to-entity designer for beasts & items
│   ├── vu-exam-exporter/            # VU Exam Manage Summative extractor & item analysis (.xlsx)
│   └── webapp-doc-architect/        # Web app manuals & specs generator (.docx, .pptx, PDF)
├── .gitignore                       # Standard ignore rules
├── CONTRIBUTING.md                  # Guide for contributing new skills
├── LICENSE                          # MIT License
└── README.md                        # Repository documentation & skills catalog
```

---

## 🤝 Contributing

Contributions, new skills, and enhancements are warmly welcomed! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on formatting `SKILL.md` files and submitting pull requests.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
