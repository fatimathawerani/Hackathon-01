# Quickstart

**Date**: 2025-12-17
**Feature**: User Personalization and Translation

## Frontend
1.  **Install dependencies**: `npm install`
2.  **Run Docusaurus**: `npm start`
3.  **Authentication**: Use the "Sign In" / "Sign Up" buttons to authenticate with Better Auth.
4.  **Translation**: Open a chapter and click the "Translate to Urdu" button.
5.  **Personalization**: After signing in and completing your profile, open a chapter and click the "Personalize" button.

## Backend
1.  **Install dependencies**: `uv pip install -r requirements.txt`
2.  **Run FastAPI**: `uvicorn main:app --reload`
3.  **API**: The API will be available at `http://localhost:8000`.
4.  **Endpoints**:
    *   `POST /ask`: Get a personalized answer.
    *   `POST /translate`: Translate content to Urdu.
