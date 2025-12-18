# Data Model

**Date**: 2025-12-17
**Feature**: User Personalization and Translation

## Entities

### UserProfile
- **Description**: Stores the user's background information.
- **Fields**:
  - `software_experience`: string (Beginner, Intermediate, Advanced)
  - `hardware_access`: string (Laptop, GPU, Robotics kit)
  - `learning_depth`: string (Conceptual, Practical, Research)
- **Relationships**: Associated with a user account in Better Auth.
