# 🌊 LinguoFlow: Exam Repository & Management

This project serves as a centralized hub for **generating, validating, and managing exams** within the LinguoFlow ecosystem. It provides the structured data and procedural intelligence required to maintain a high-quality library of language assessments.

## 🎯 Project Goals

1.  **Exam Lifecycle Management**: Automate the creation, testing, and deployment of exams using the LinguoFlow API.
2.  **Format Standardization**: Ensure all tests strictly adhere to the **LinguoFlow Universal Test Format Specification**.
3.  **Data Integrity**: Maintain a consistent repository of exam templates that are validated against the live assessment engine.
4.  **AI-Ready Infrastructure**: Optimize exam content (including media descriptions and rubrics) for AI-driven evaluation and generation.

## 🛠️ Mandatory Skill

All interactions within this repository **MUST** utilize the following skill:

- **`linguoflow-exam-management`**: This skill contains the procedural logic, API integration details, and validation checks necessary to work with LinguoFlow exams safely. 

## 📏 Core Requirements

- **API Integration**: All modifications to exams should be synced with the local or production API (default: `http://localhost:3000`).
- **Authentication**: A valid `LINGUOFLOW_API_KEY` must be present in the environment for all API-based operations.
- **Sync & Validate**: Always fetch the latest specification (`/api/exams/spec`) before performing structural changes to ensure forward compatibility.
