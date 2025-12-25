# Quickstart: Contact & Onboarding Forms

**Date**: 2025-12-24
**Feature**: Contact & Onboarding Forms

## Frontend
1.  **Navigate to Contact Page**: Go to `/contact`.
2.  **Submit Form**: Fill in Name, Email, Message and submit.
3.  **Signup Flow**: Go to `/signup`, create an account, and proceed to the onboarding step.

## Backend
1.  **Run Backend**: Ensure FastAPI is running (`uvicorn main:app --reload`).
2.  **Test Endpoint**: Send a POST request to `/contact` with valid JSON payload.
    ```bash
    curl -X POST http://localhost:8000/contact \
      -H "Content-Type: application/json" \
      -d '{"name": "Test User", "email": "test@example.com", "message": "Hello"}'
    ```

