# 🌊 LinguoFlow Skills Hub

Centralne repozytorium skilli i skryptów automatyzacji dla ekosystemu LinguoFlow.

## 📂 Struktura Repozytorium

- **`/skills`**: Gotowe definicje skilli (pliki `SKILL.md` + dedykowane skrypty).
  - `exam-management`: Zarządzanie egzaminami, synchronizacja z API, walidacja.
- **`/shared`**: Współdzielona logika, narzędzia i schematy JSON.
- **`/templates`**: Szablony ułatwiające tworzenie nowych narzędzi.

## 🛠️ Jak korzystać ze skilli?

Aby użyć skilla w konkretnym projekcie, zaleca się utworzenie symlinka:

```bash
mkdir -p .gemini/skills
ln -s ~/projects/LinguoFlow-skills/skills/exam-management .gemini/skills/exam-management
```

## 📜 Lista Skilli

| Skill | Opis | Status |
| :--- | :--- | :--- |
| **exam-management** | Pełna obsługa cyklu życia egzaminu (v0.4) | Gotowy |
| **content-generator** | AI Prompty do generowania zadań | Planowany |

---
*Created and managed by Gemini CLI.*
