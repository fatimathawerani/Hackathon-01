# Tasks: AI-Native Interactive Textbook

**Input**: Design documents from `/specs/1-ai-interactive-textbook/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

- [X] T001 Initialize Spec-Kit Plus project structure.
- [X] T002 Create `book.yaml` with all chapters from the Physical AI course outline.
- [ ] T003 [P] Set up FastAPI project structure in `backend/`.
- [ ] T004 [P] Generate Docusaurus project using `spec-kit build` in `frontend/`.

## Phase 2: Foundational (Blocking Prerequisites)

- [ ] T005 [P] Configure Neon Postgres tables for `users`, `onboarding_questions`, and `personalization_preferences` in `backend/src/models/`.
- [ ] T006 [P] Set up Qdrant vector DB and create collection for book embeddings.
- [ ] T007 Build embedding and ingestion pipeline for all chapters in `backend/src/services/`.
- [ ] T008 [P] Integrate Better-Auth into Docusaurus for signup/signin flow in `frontend/src/`.
- [ ] T009 [P] Build signup flow with background questions.
- [ ] T010 Store user profile in Postgres.

## Phase 3: User Story 1 - Read the textbook (Priority: P1) 🎯 MVP

**Goal**: Users can read the textbook content.

**Independent Test**: The textbook can be browsed, and the content is readable.

### Implementation for User Story 1

- [ ] T011 [US1] Populate chapter markdown files with structured and well-written content in `docs/`.
- [ ] T012 [P] [US1] Add diagrams, tables, and visuals where needed in `docs/`.

## Phase 4: User Story 2 - Interact with the RAG chatbot (Priority: P1)

**Goal**: Users can ask questions and get answers from the chatbot.

**Independent Test**: The chatbot can answer questions based on the book's content.

### Implementation for User Story 2

- [ ] T013 [US2] Add RAG query endpoint in `backend/src/api/`.
- [ ] T014 [P] [US2] Add “selected text query” endpoint in `backend/src/api/`.
- [ ] T015 [P] [US2] Build ChatWidget React component in `frontend/src/components/`.
- [ ] T016 [US2] Connect widget to backend API.
- [ ] T017 [P] [US2] Add support for selecting text and sending it to the RAG endpoint.

## Phase 5: User Story 3 - Personalize my learning experience (Priority: P2)

**Goal**: Users can have a personalized learning experience.

**Independent Test**: Users can log in, and the content is personalized based on their profile.

### Implementation for User Story 3

- [ ] T018 [US3] Add OpenAI Agent integration using SDK in `backend/src/services/`.
- [ ] T019 [US3] Implement `personalize_content` agent skill.
- [ ] T020 [P] [US3] Add “Personalize Chapter” button to Docusaurus in `frontend/src/`.
- [ ] T021 [US3] Connect button to backend endpoint.

## Phase 6: User Story 4 - Read the textbook in Urdu (Priority: P2)

**Goal**: Users can read the textbook in Urdu.

**Independent Test**: The textbook content can be translated to Urdu.

### Implementation for User Story 4

- [ ] T022 [US4] Implement `translate_to_urdu` agent skill.
- [ ] T023 [P] [US4] Add “Translate to Urdu” button to Docusaurus in `frontend/src/`.
- [ ] T024 [US4] Connect to backend.

## Phase N: Polish & Cross-Cutting Concerns

- [ ] T025 [P] Deploy Docusaurus frontend to GitHub Pages or Vercel.
- [ ] T026 [P] Deploy FastAPI backend to Render or Fly.io.
- [ ] T027 Configure environment variables for all services.
- [ ] T028 Test RAG, chatbot, auth, personalization, and translation.
- [ ] T029 Record 90-second demo video.
- [ ] T030 Submit repo, live site, and video.

## Dependencies & Execution Order

- **Phase 1** must be completed before **Phase 2**.
- **Phase 2** must be completed before **Phases 3, 4, 5, and 6**.
- **Phases 3, 4, 5, and 6** can be worked on in parallel after **Phase 2** is complete.
- **Phase N** can be started after all other phases are complete.
