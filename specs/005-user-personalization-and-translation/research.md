# Research

**Date**: 2025-12-17
**Feature**: User Personalization and Translation

## Decisions

### Frontend
- **Component**: A reusable `ChapterActions` component will be created in Docusaurus.
- **Injection**: The component will be injected into MDX pages using a wrapper.
- **Authentication**: An authentication modal will be implemented using Better Auth.
- **State Management**: User profile information will be stored in the client session.

### Backend
- **Endpoint**: The existing `/ask` endpoint in the FastAPI backend will be extended.
- **Payload**: The `/ask` endpoint will accept an optional `user_profile` payload.
- **Personalization**: Personalization will be achieved by injecting the user profile into the RAG prompt.
- **Translation**: A new `/translate` endpoint will be created to translate content from English to Urdu.

### Data
- **User Profile**: User profile data will be managed by Better Auth.
- **Storage**: No new database is required.

### Safety
- **API**: Existing APIs will be preserved.
- **Compatibility**: All changes will be backward compatible.
