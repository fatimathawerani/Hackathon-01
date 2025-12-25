# Feature Specification: Contact & Onboarding Forms

**Feature Branch**: `006-contact-and-onboarding-forms`  
**Created**: 2025-12-24  
**Status**: Draft  
**Input**: User description: "Feature set to add: 6. Contact & Onboarding Forms Contact Form: - Reusable contact form component - Fields: - Name - Email - Message - Accessible to: - Anonymous users - Logged-in users - Logged-in users auto-fill name & email - Submits to backend endpoint - No impact on RAG or embeddings Auth-aware Signup Extension: - Contact-style form used during Signup - Collects: - Software experience - Hardware access - Learning depth - Optional message / goal - Stored via Better Auth user metadata Constraints: - No blocking of reading content - No modification of existing auth flows - No duplication of profile schema"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - General Contact Form (Priority: P1)

Any user (anonymous or logged-in) wants to send a message to the administrators so they can ask questions or provide feedback.

**Why this priority**: Basic communication channel is essential for user engagement and support.

**Independent Test**: A user can navigate to the contact page, fill out the form, and successfully submit it.

**Acceptance Scenarios**:

1. **Given** an anonymous user is on the contact page, **When** they fill in Name, Email, and Message and click Submit, **Then** the form is submitted to the backend and a success message is shown.
2. **Given** a logged-in user is on the contact page, **When** they load the form, **Then** their Name and Email fields are auto-filled.
3. **Given** a user submits an invalid email, **When** they try to submit, **Then** an error message is displayed and submission is blocked.

---

### User Story 2 - Enhanced Signup Onboarding (Priority: P2)

A new user signing up wants to provide their background information (software experience, hardware access, etc.) immediately so their profile is personalized from the start.

**Why this priority**: capturing user context at signup improves the immediate value of the platform (personalization).

**Independent Test**: A new user goes through the signup process and sees the additional onboarding fields, and after completion, this data is persisted in their profile.

**Acceptance Scenarios**:

1. **Given** a user is on the signup page, **When** they are prompted for details, **Then** they see fields for Software Experience, Hardware Access, Learning Depth, and an optional Message/Goal.
2. **Given** a user fills out the onboarding form during signup, **When** they complete the process, **Then** the data is stored in the Better Auth user metadata.
3. **Given** a user skips the optional message, **When** they submit the form, **Then** the profile is still created successfully with the other required fields.

### Edge Cases

- What happens if the backend endpoint for contact form submission is down?
- What happens if the user metadata storage limit is reached?
- How does the system handle special characters in the message field?
- What if a logged-in user changes their auto-filled email in the contact form to one that doesn't match their account? (Should be allowed as it's just a contact email).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a reusable contact form component with fields: Name, Email, Message.
- **FR-002**: System MUST allow both anonymous and logged-in users to submit the contact form.
- **FR-003**: System MUST auto-fill Name and Email fields for logged-in users in the contact form.
- **FR-004**: System MUST submit contact form data to a dedicated backend endpoint.
- **FR-005**: System MUST NOT impact existing RAG or embeddings functionality with contact form submissions.
- **FR-006**: System MUST extend the signup flow to collect: Software Experience, Hardware Access, Learning Depth, and Optional Message/Goal.
- **FR-007**: System MUST store the extended signup data in Better Auth user metadata.
- **FR-008**: System MUST NOT block reading of content for users who have not completed the enhanced onboarding (unless it's a hard gate for signup itself, but spec says "No blocking of reading content").
- **FR-009**: System MUST NOT duplicate the user profile schema; it should reuse existing definitions where applicable.

### Key Entities *(include if feature involves data)*

- **ContactSubmission**: Represents a message sent via the contact form (Name, Email, Message, Timestamp).
- **UserProfileMetadata**: The extended user data structure stored within Better Auth (Experience, Hardware, Learning Depth, Goal).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of valid contact form submissions are received by the backend.
- **SC-002**: 95% of new signups successfully complete the extended onboarding questions.
- **SC-003**: Contact form loads in under 1 second for both anonymous and logged-in users.
- **SC-004**: Zero regression in RAG pipeline performance due to form handling.