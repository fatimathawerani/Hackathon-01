# Implementation Plan: Contact & Onboarding Forms

**Branch**: `006-contact-and-onboarding-forms` | **Date**: 2025-12-24 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/006-contact-and-onboarding-forms/spec.md`

## Summary

This feature implements a reusable Contact Form component within the Docusaurus frontend. This component will be used for a public "Contact Us" page and integrated into the signup flow as an onboarding step. The backend (FastAPI) will expose a new endpoint to handle contact form submissions. User onboarding data (Software Experience, Hardware Access, etc.) will be stored using Better Auth's user metadata capabilities.

## Technical Context

**Language/Version**: Python 3.11, TypeScript (Docusaurus)
**Primary Dependencies**: FastAPI, Docusaurus, Better Auth client/server
**Storage**: Better Auth User Metadata (for profile info), File/Log based or Email service (for contact messages - TBD in research)
**Testing**: pytest (backend), Jest/React Testing Library (frontend)
**Target Platform**: Web
**Project Type**: Web application (Docusaurus Frontend + FastAPI Backend)
**Performance Goals**: Contact form submission < 500ms.
**Constraints**: Must not block content access. Must utilize existing Better Auth session.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [X] **I. Code Quality**: All code, including frontend, backend, and agent code, must adhere to the highest quality standards.
- [X] **II. Content Consistency**: All written content must maintain a consistent style, formatting, and terminology.
- [X] **III. Rigorous Testing**: A comprehensive testing strategy is mandatory for all critical components.
- [X] **IV. Chatbot Reliability and Accuracy**: The chatbot must provide reliable and accurate responses.
- [X] **V. Performance Optimization**: All components must be optimized for performance.
- [X] **VI. Accessibility**: The application must be accessible to all users.
- [X] **VII. User Experience Consistency**: A consistent and intuitive user experience must be maintained across all user-facing components.
- [X] **VIII. Comprehensive Documentation**: All components must be thoroughly documented.

## Project Structure

### Documentation (this feature)

```text
specs/006-contact-and-onboarding-forms/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── main.py           # New /contact endpoint
│   ├── models/           # Contact submission model
│   └── services/         # Contact handling logic
└── tests/

book/ai-interactive-textbook/src/
├── components/
│   ├── ContactForm/      # Reusable form component
│   └── Onboarding/       # Onboarding wrapper using ContactForm structure
├── pages/
│   ├── contact.tsx       # Public contact page
│   └── signup/           # Enhanced signup flow
└── services/
    └── auth.ts           # Better Auth metadata updates
```

**Structure Decision**: Extending existing backend and Docusaurus structure. Reusing `src/components` for the new form.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | N/A | N/A |