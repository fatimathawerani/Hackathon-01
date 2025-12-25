# Actionable Tasks for: Contact & Onboarding Forms

**Branch**: `006-contact-and-onboarding-forms` | **Date**: 2025-12-24 | **Spec**: [spec.md](spec.md)

## Phase 1: Setup
- [X] T001 Create component directory for ContactForm in `book/ai-interactive-textbook/src/components/ContactForm/`.

## Phase 2: Foundational
- [X] T002 Create Pydantic model for ContactSubmission in `backend/src/models/contact.py`.
- [X] T003 Implement basic ContactService (logging only) in `backend/src/services/contact_service.py`.
- [X] T004 Implement `/contact` endpoint in `backend/src/main.py`.

## Phase 3: User Story 1 - General Contact Form (P1)
- **Goal**: Enable users to contact administrators via a form.
- **Independent Test**: Submit a form on `/contact` and verify backend log.

- [X] T005 [US1] Implement reusable `ContactForm` UI component in `book/ai-interactive-textbook/src/components/ContactForm/index.tsx`.
- [X] T006 [US1] Create public Contact page in `book/ai-interactive-textbook/src/pages/contact.tsx`.
- [X] T007 [US1] Integrate `ContactForm` into the Contact page.
- [X] T008 [US1] Connect `ContactForm` submission logic to the `/contact` backend endpoint.
- [X] T009 [US1] Implement auto-fill logic for logged-in users in `ContactForm` using `auth.ts` (or auth hook).

## Phase 4: User Story 2 - Enhanced Signup Onboarding (P2)
- **Goal**: Collect user metadata during signup.
- **Independent Test**: Signup a new user and verify metadata (Experience, Hardware, etc.) is stored.

- [X] T010 [US2] Update `auth.ts` service to include method for updating user metadata in `book/ai-interactive-textbook/src/services/auth.ts`.
- [X] T011 [US2] Create `Onboarding` component that wraps/reuses form elements or extends `ContactForm` in `book/ai-interactive-textbook/src/components/Onboarding/index.tsx`.
- [X] T012 [US2] Integrate `Onboarding` component into the signup flow (create/update `book/ai-interactive-textbook/src/pages/signup/index.tsx` or equivalent).

## Phase 5: Polish & Cross-Cutting Concerns
- [X] T013 Ensure form is accessible (aria-labels, keyboard nav) in `book/ai-interactive-textbook/src/components/ContactForm/index.tsx`.
- [X] T014 Update project documentation with new features.

## Dependencies

- **US1** depends on **Foundational** backend tasks.
- **US2** depends on **US1** (reusing form components) and **Foundational** (auth service updates).

## Implementation Strategy

1.  **Backend First**: Establish the API contract and endpoint.
2.  **Frontend Component**: Build the isolated form component.
3.  **Pages**: Assemble the pages using the component.
4.  **Integration**: Connect frontend to backend and auth services.
