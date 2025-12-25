# Data Model

**Date**: 2025-12-24
**Feature**: Contact & Onboarding Forms

## Entities

### ContactSubmission
- **Description**: A message submitted via the contact form.
- **Fields**:
  - `name`: string (Required)
  - `email`: string (Required, Email format)
  - `message`: string (Required)
  - `user_id`: string (Optional, if logged in)
  - `timestamp`: datetime

### UserProfileMetadata (Better Auth Extension)
- **Description**: Additional user context stored in Better Auth metadata.
- **Fields**:
  - `software_experience`: enum ["Beginner", "Intermediate", "Advanced"]
  - `hardware_access`: enum ["Sim Only", "Edge Kit", "Full Robot"]
  - `learning_depth`: enum ["Conceptual", "Practical", "Research"]
  - `learning_goal`: string (Optional)
