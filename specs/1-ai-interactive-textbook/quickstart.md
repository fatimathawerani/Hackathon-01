# Quickstart: AI-Native Interactive Textbook

This guide will help you get started with the AI-Native Interactive Textbook.

## Prerequisites

-   Python 3.11
-   Node.js 18.x
-   Access to Qdrant Cloud, Neon Postgres, and OpenAI API.

## Backend Setup

1.  Clone the repository.
2.  Create a virtual environment: `python -m venv venv`
3.  Activate the virtual environment: `source venv/bin/activate`
4.  Install the dependencies: `pip install -r requirements.txt`
5.  Set up the environment variables in a `.env` file:
    ```
    QDRANT_API_KEY=...
    NEON_DATABASE_URL=...
    OPENAI_API_KEY=...
    BETTER_AUTH_SECRET=...
    ```
6.  Run the database migrations: `alembic upgrade head`
7.  Start the backend server: `uvicorn main:app --reload`

## Frontend Setup

1.  Navigate to the `frontend` directory.
2.  Install the dependencies: `npm install`
3.  Start the development server: `npm start`
4.  The frontend will be available at `http://localhost:3000`.

## Running the textbook

1.  Make sure both the backend and frontend servers are running.
2.  Open your browser and navigate to `http://localhost:3000`.
3.  You should now be able to read the textbook, interact with the chatbot, and use the personalization features.
