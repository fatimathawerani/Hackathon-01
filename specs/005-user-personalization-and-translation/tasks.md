# Actionable Tasks for: User Personalization and Translation

**Branch**: `005-user-personalization-and-translation` | **Date**: 2025-12-17 | **Spec**: [spec.md](spec.md)

## Phase 1: Foundational Tasks
- [X] T001 Create a new reusable component `ChapterActions` in `book/ai-interactive-textbook/src/components/ChapterActions/index.tsx`.
- [X] T002 Create a service to handle Better Auth integration in `book/ai-interactive-textbook/src/services/auth.ts`.
- [X] T003 Create a translation service in `backend/src/services/translation.py`.

## Phase 2: User Story 1 - Chapter Translation (P1)
- **Goal**: A user can translate a chapter to Urdu and toggle back to English.
- **Independent Test**: Open a chapter, click "Translate to Urdu", see the content in Urdu. Click "Show English" to revert.

- [X] T004 [US1] Add a "Translate to Urdu" button to the `ChapterActions` component in `book/ai-interactive-textbook/src/components/ChapterActions/index.tsx`.
- [X] T005 [US1] Implement the translation logic in the `ChapterActions` component to call the `/translate` endpoint in `book/ai-interactive-textbook/src/components/ChapterActions/index.tsx`.
- [X] T006 [US1] Implement the `/translate` endpoint in `backend/src/main.py` to use the translation service.
- [X] T007 [US1] Inject the `ChapterActions` component into the chapter layout, likely by wrapping MDX content in `book/ai-interactive-textbook/src/theme/Root.js`.

## Phase 3: User Story 2 - User Authentication (P2)
- **Goal**: A user can sign up and sign in.
- **Independent Test**: A new user can sign up. An existing user can sign in.

- [X] T008 [US2] Add "Sign In" and "Sign Up" buttons to the UI, likely in the navbar.
- [X] T009 [US2] Implement the authentication flow using the Better Auth service in `book/ai-interactive-textbook/src/services/auth.ts`.

## Phase 4: User Story 3 - User Profiling (P2)
- **Goal**: A new user is prompted to create a profile after signup.
- **Independent Test**: A user who signs up is prompted to provide their profile information.

- [X] T010 [US3] Create a user profile form to collect user's software experience, hardware access, and learning depth.
- [X] T011 [US3] After a successful signup, redirect the user to the profile creation form.
- [X] T012 [US3] Store the user profile using Better Auth's mechanisms.

## Phase 5: User Story 4 - Personalized Content (P3)
- **Goal**: An authenticated user can get personalized explanations.
- **Independent Test**: An authenticated user can click a "Personalize" button and see adjusted content.

- [X] T013 [US4] Add a "Personalize" button to the `ChapterActions` component for authenticated users in `book/ai-interactive-textbook/src/components/ChapterActions/index.tsx`.
- [X] T014 [US4] Implement the personalization logic in the `ChapterActions` component to call the `/ask` endpoint with the user's profile in `book/ai-interactive-textbook/src/components/ChapterActions/index.tsx`.
- [X] T015 [US4] Extend the `/ask` endpoint in `backend/src/main.py` to accept the `user_profile` payload.

## Phase 6: User Story 5 - Reusable Intelligence Layer (P3)
- **Goal**: Centralize user profile and prompt generation logic.
- **Independent Test**: Changes to the prompt building logic are reflected in both the chatbot and chapter personalization.

- [X] T016 [US5] Create a reusable intelligence module in the backend that contains the shared prompt builder.
- [X] T017 [US5] Refactor the existing chatbot to use the new intelligence module.
- [X] T018 [US5] Ensure the `/ask` endpoint for personalization uses the same intelligence module.

## Phase 7: Polish & Cross-Cutting Concerns
- [X] T019 Ensure all new UI components are accessible and responsive.
- [ ] T020 Add error handling for API calls.
- [ ] T021 [P] Write unit tests for the new frontend components.
- [ ] T022 [P] Write unit tests for the new backend services.
- [ ] T023 Update documentation to reflect the new features.

## Dependencies

- **US1 (Translation)** is independent.
- **US2 (Authentication)** is a prerequisite for US3, US4, and US5.
- **US3 (Profiling)** is a prerequisite for US4 and US5.
- **US4 (Personalization)** depends on US2 and US3.
- **US5 (Intelligence Layer)** depends on US2 and US3.

## Implementation Strategy

The recommended approach is to implement the user stories in order of priority (P1, P2, P3). User Story 1 can be implemented independently. User Stories 2 and 3 should be implemented before User Stories 4 and 5.
