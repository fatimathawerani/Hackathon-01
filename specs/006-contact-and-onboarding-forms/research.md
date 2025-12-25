# Research

**Date**: 2025-12-24
**Feature**: Contact & Onboarding Forms

## Decisions

### Frontend Components
- **Decision**: Create a reusable `ContactForm` component in `book/ai-interactive-textbook/src/components`.
- **Rationale**: Needs to be used in two distinct contexts: the public contact page and the post-signup onboarding flow. Reusability ensures UI consistency.
- **Alternatives Considered**: Separate forms for each. Rejected due to code duplication and inconsistent UX.

### Authentication & Metadata
- **Decision**: Use Better Auth's user metadata feature to store "Software Experience", "Hardware Access", and "Learning Depth".
- **Rationale**: Better Auth is already integrated. Storing this in metadata avoids creating a separate database table and keeps user profile data unified.

### Backend Contact Handling
- **Decision**: Implement a `/contact` POST endpoint in FastAPI.
- **Rationale**: Decouples the frontend from the message delivery mechanism.
- **Implementation**: For this MVP, the endpoint will log the message and return success. In the future, this can be swapped for an SMTP or SendGrid integration without changing the frontend.

### Accessibility
- **Decision**: Ensure the form uses semantic HTML (`<label>`, `<input>`, `<textarea>`) and handles keyboard navigation.
- **Rationale**: Compliance with Principle VI (Accessibility).
