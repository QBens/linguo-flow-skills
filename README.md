# 🌊 LinguoFlow Skills Hub

Central repository for skills and automation scripts for the LinguoFlow ecosystem.

## 📂 Repository Structure

- **`/skills`**: Ready-to-use skill definitions (`SKILL.md` files + dedicated scripts).
  - `exam-management`: Exam management, API synchronization, validation.
- **`/shared`**: Shared logic, tools, and JSON schemas.
- **`/templates`**: Templates to facilitate the creation of new tools.

## 🛠️ How to use skills?

To use a skill in a specific project, it is recommended to create a symbolic link:

```bash
mkdir -p .gemini/skills
ln -s ~/projects/LinguoFlow-skills/skills/exam-management .gemini/skills/exam-management
```

## 📜 Skill List

| Skill | Description | Status |
| :--- | :--- | :--- |
| **exam-management** | Full lifecycle support for exams (v0.4) | Ready |
| **content-generator** | AI Prompts for task generation | Planned |

---
*Created and managed by Gemini CLI.*
