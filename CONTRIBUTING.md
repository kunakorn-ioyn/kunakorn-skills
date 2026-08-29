# Contributing to Antigravity AI Skills

Thank you for your interest in contributing to this collection of AI Agent Skills! By contributing new skills or refining existing ones, you help developers build more reliable, context-aware AI workflows.

---

## 📐 Skill Design Standards

Every skill in this repository must adhere to the following standards:

### 1. Directory Structure

Each skill must reside in its own self-contained directory under the `skills/` folder, named in `kebab-case`:

```text
skills/my-new-skill/
├── SKILL.md             # Required: Skill instructions and YAML frontmatter
├── scripts/             # Optional: Helper scripts (e.g. bash, node, python)
└── references/          # Optional: Reference templates or examples
```

### 2. YAML Frontmatter Specification

The `SKILL.md` file **must** begin with standard YAML frontmatter:

```yaml
---
name: my-new-skill
description: Clear, high-density description of what the skill does and exact semantic trigger cues (e.g. "Trigger on /my-command, when user mentions X, or when resolving Y.").
---
```

- **`name`**: Must match the directory name exactly in `kebab-case`.
- **`description`**: Must explain both **what** the skill accomplishes and **when** the AI should dynamically trigger it (including trigger keywords or slash commands).

### 3. Body Content Guidelines

- **No Ambiguity**: Provide exact step-by-step procedures, decision trees, or scripts.
- **Fail-Safe & Edge Cases**: Include troubleshooting sections for common pitfalls and edge cases.
- **Token Efficiency**: Use clear, concise Markdown without fluff to keep token usage optimal.

---

## 🚀 How to Submit a Contribution

1. **Fork the Repository** on GitHub.
2. **Create a Feature Branch**:
   ```bash
   git checkout -b feat/add-new-skill
   ```
3. **Add Your Skill**: Create `skills/my-new-skill/SKILL.md` following the directory structure and formatting specifications above.
4. **Update the Catalog**: Add your skill to the table in [README.md](README.md).
5. **Commit Your Changes** using Conventional Commits:
   ```bash
   git commit -m "feat: add my-new-skill for automated XYZ"
   ```
6. **Push to Your Fork**:
   ```bash
   git push origin feat/add-new-skill
   ```
7. **Open a Pull Request** against the `main` branch.

---

## 📜 Code of Conduct

Please maintain a collaborative, respectful, and constructive environment for all contributors and users.
