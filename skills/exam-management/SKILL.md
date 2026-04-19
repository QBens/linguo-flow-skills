---
name: linguoflow-exam-management
description: Procedures for creating, validating, and managing LinguoFlow exams via the API.
---

# 🌊 LinguoFlow: Exam Management

This skill guides you through the process of creating and managing exams within the LinguoFlow ecosystem.

## 📋 Core Principles

1.  **Always Check the Latest Specification**: The LinguoFlow API is evolving. Before generating any exam JSON, fetch the latest instructions via `GET /api/exam-spec.md`.
2.  **Immutability vs. Working Drafts**: 
    *   **Development Phase (Draft)**: During the initial creation and testing phase (before any students have taken the exam), you have two options for modifications:
        *   **PATCH**: For partial updates (fixing typos, updating a single block, or changing `media_description`).
        *   **PUT**: For a full replacement (Full Replace) of the exam structure under the existing ID. Use this when making significant structural changes to a draft.
        Do NOT use POST to update a draft, as it creates redundant exam IDs.
    *   **POST (Create)**: Use ONLY for the very first upload of a new exam template or when creating a completely separate version.
    *   **Versioning (Live)**: If an exam version has already been taken by students, it is considered "Live". Any subsequent changes must be treated as a new version and created using **POST** with a new ID to preserve historical integrity.
3.  **Correction vs. Creation**: 
    *   If you are fixing, refining, or completing an existing ID: **PATCH** or **PUT**.
    *   If you are starting a fresh project or branching a published test: **POST**.
4.  **Standardization**: Always use ISO 639-1 for languages (e.g., `en`, `pl`, `es`) and CEFR levels for `target_level` (e.g., `A2`, `B1`, `C1`).
5.  **Safety First (Backups)**: Before performing any operation that overwrites or modifies an existing exam state on the server (`PUT` or `PATCH`), **always** ensure a local backup of the current JSON file exists. The `sync-exam.py` script handles this automatically by creating a copy in the `backups/` directory.

## 🤖 Automation Scripts

The following scripts are available within the skill directory to automate common tasks:

-   **`fetch-spec.sh`**: Fetches the latest exam specification from the API.
    -   *Usage*: `./.gemini/skills/linguoflow-exam-management/scripts/fetch-spec.sh [output_file]`
-   **`list-exams.py`**: Lists all exams from the API with optional filtering by name.
    -   *Usage*: `./.gemini/skills/linguoflow-exam-management/scripts/list-exams.py [search_pattern]`
-   **`sync-exam.py`**: Synchronizes an exam JSON file with the API using POST, PUT, or PATCH.
    -   *Automatic Backup*: Creates a timestamped copy in `backups/` before any `PUT` or `PATCH` operation.
    -   *Usage*: `./.gemini/skills/linguoflow-exam-management/scripts/sync-exam.py [file.json] [METHOD] [ID]`

## 🧪 Quality Assurance & Validation Protocol

Every exam must pass through a three-stage verification process before synchronization:

### 1. Substantive and Educational Verification
- **CEFR Compliance**: Do the vocabulary and grammatical structures match the declared level (e.g., A2)?
- **Distractor Quality**: Incorrect answers must not be "absurd." They should be based on typical student errors (e.g., L1 interference, incorrect regular spelling for irregular verbs).
- **Difficulty Level**: Avoid overly obvious answers. Distractors should force analysis of context or subtle grammatical differences.

### 2. Logical and Linguistic Verification
- **Unambiguity**: Is there only one correct answer? Eliminate situations where two different words fit the same gap equally well.
- **Naturalness (Flow)**: Do the texts/dialogues sound natural? Avoid "artificial" textbook sentences in favor of authentic communicative contexts.
- **Formatting**: Text in gap-fill tasks must be readable (use `\n` for dialogues).

### 3. Technical Validation (Pre-flight)
- **ID Sync**: Full consistency between `interactions`, `text` (gap markers `{{id}}`), and `expected_answers`.
- **Interaction Types**: Strict compliance with the latest specification version (v0.4).

## 🛠️ Working Procedure

### Step 1: Search and Fetch
Before creating or updating, check if the exam already exists or find related templates.
- **Script**: `./.gemini/skills/linguoflow-exam-management/scripts/list-exams.py "pattern"`
- **Fetch Detail**: `curl -H "x-api-key: $LINGUOFLOW_API_KEY" http://localhost:3000/api/exams/{id} > local-file.json`

### Step 2: Educational Design & Draft
Create the JSON based on the blueprint and previous exams. Ensure:
- [ ] Task variety (MCQ, Gap-fill, Matching).
- [ ] Contextual embedding (tasks tell a story or share a theme).

### Step 3: Multi-Stage Quality Check (CRITICAL)
Perform a manual and automated review:
1. **Linguistic Audit**: Check for typos, natural phrasing, and L1 interference.
2. **Ambiguity Test**: Try to find an alternative valid answer for each gap. If found, rephrase the sentence to be more specific.
3. **Distractor Audit**: Replace weak distractors (e.g., obviously wrong parts of speech) with strong ones (e.g., common spelling mistakes like *stoped* vs *stopped*).

### Step 4: Technical Validation & Sync Spec
Fetch the latest technical documentation to ensure compatibility with the current engine.
- **Script**: `./.gemini/skills/linguoflow-exam-management/scripts/fetch-spec.sh latest-spec.md`
- **Endpoint**: `GET http://localhost:3000/api/exam-spec.md`

### Step 5: Execution
Choose the correct method based on the intent (Creation vs. Correction).
- **Script**: `./.gemini/skills/linguoflow-exam-management/scripts/sync-exam.py [file.json] [METHOD] [ID]`
- **Methods**:
    - **POST**: `http://localhost:3000/api/exams` (New exam)
    - **PUT**: `http://localhost:3000/api/exams/{id}` (Full draft replacement)
    - **PATCH**: `http://localhost:3000/api/exams/{id}` (Partial draft update)
- **Auth**: Always include the `x-api-key` header using the `LINGUOFLOW_API_KEY` environment variable.

### Step 6: Verification & Error Handling
After execution, verify the result. If the API returns a validation error:
1. Re-read the `spec` to identify the structural mismatch.
2. Fix the JSON autonomously.
3. Only ask the user for help if the error implies a missing business requirement (e.g., a missing asset or ambiguous instruction).
