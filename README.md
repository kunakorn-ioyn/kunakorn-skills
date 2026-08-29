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
  <a href="#-how-it-works">How It Works</a> •
  <a href="#-contributing">Contributing</a> •
  <a href="#-license">License</a>
</p>

---

</div>

## 🌟 Overview

This repository contains a curated collection of dynamic **Agent Skills** designed to supercharge autonomous AI engineering. Each skill acts as a specialized instruction module that equips AI agents (such as Google Antigravity, Gemini, and Claude/Cursor) with domain-specific workflows, zero-repetition error handling, continuous deployment automation, and Obsidian knowledge synchronization.

---

## 🗂️ Skills Catalog

| Skill Name | Category | Purpose & Workflow | Key Triggers & Keywords |
| :--- | :--- | :--- | :--- |
| [**`aapanel-git-autodeploy`**](./skills/aapanel-git-autodeploy/SKILL.md) | `DevOps & CI/CD` | Automates CI/CD auto-deployment from GitHub to aaPanel servers using Webhooks with root-level script isolation & permission fixing. | `aaPanel deploy`, `webhook setup`, `$HOME not set`, `dubious ownership` |
| [**`existing-project-onboarding`**](./skills/existing-project-onboarding/SKILL.md) | `Workflow & Context` | Rapidly audits active codebases, retroactively establishes context & execution baselines, and plans next steps without re-doing finished work. | `onboard project`, `audit codebase`, `project catchup`, `context baseline` |
| [**`project-summary-optimizer`**](./skills/project-summary-optimizer/SKILL.md) | `Efficiency & Token` | Archives verbose session logs and compacts `PROJECT_SUMMARY.md` into high-density reference docs to prevent LLM context window bloating. | `/optimize-summary`, `/project-summary-optimizer`, `clean up summary`, `shrink devlog` |
| [**`troubleshooting-codex`**](./skills/troubleshooting-codex/SKILL.md) | `Engineering Memory` | Systematic capture and indexing of bugs, root causes, and golden prevention rules into a living lessons-learned codex. | `/record-lesson`, `/troubleshooting-codex`, `บันทึกเป็นบทเรียน`, `never repeat` |
| [**`universal-feature-developer`**](./skills/universal-feature-developer/SKILL.md) | `Feature Engineering` | Stack-agnostic feature builder and refactoring workflow with dynamic pre-checks, native linting gates, and Obsidian auto-sync. | `/build-feature`, `add new feature`, `refactor module`, `stack-specific test` |
| [**`universal-project-manager`**](./skills/universal-project-manager/SKILL.md) | `Project Management` | Master orchestrator for step-by-step project planning, tracking active sprint state, and formatting structured notes for Obsidian. | `/project-manager`, `plan milestone`, `track sprint`, `Obsidian project sync` |

---

## 🚀 Quick Installation

### 1-Click Automated Installation (Recommended)

Clone the repository and run the installer script:

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

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
├── .github/                      # GitHub issue & PR templates
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── pull_request_template.md
├── scripts/                      # ⚡ 1-Click installation scripts
│   ├── install.ps1               # Windows PowerShell installer
│   └── install.sh                # macOS & Linux Bash installer
├── skills/                       # 📦 Curated collection of AI skills
│   ├── aapanel-git-autodeploy/   # aaPanel CI/CD WebHook deployment skill
│   ├── existing-project-onboarding/ # Ongoing codebase audit & onboarding skill
│   ├── project-summary-optimizer/   # Token-efficient summary optimizer & archiver
│   ├── troubleshooting-codex/    # Bug diagnosis & institutional memory scribe
│   ├── universal-feature-developer/ # Dynamic feature development & lint-gate runner
│   └── universal-project-manager/   # Master project orchestrator & Obsidian tracker
├── .gitignore                    # Standard ignore rules
├── CONTRIBUTING.md               # Guide for contributing new skills
├── LICENSE                       # MIT License
├── PROJECT_SUMMARY.md            # Living state & continuity record
└── README.md                     # Repository documentation
```

---

## 🤝 Contributing

Contributions, new skills, and enhancements are warmly welcomed! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on formatting `SKILL.md` files and submitting pull requests.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
