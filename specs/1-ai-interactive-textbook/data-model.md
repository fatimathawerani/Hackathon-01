# Data Model: AI-Native Interactive Textbook

## Entities

### User

Represents a person interacting with the system.

-   `id`: `UUID` (Primary Key)
-   `email`: `String` (Unique)
-   `password_hash`: `String`
-   `profile`: `JSONB`
    -   `skill_level`: `JSONB` (e.g., `{"software": "beginner", "hardware": "expert"}`)
    -   `language_preference`: `String` (e.g., "en" or "ur")
-   `created_at`: `Timestamp`
-   `updated_at`: `Timestamp`

### Chapter

A section of the textbook.

-   `id`: `UUID` (Primary Key)
-   `title`: `String`
-   `content_english`: `Text`
-   `content_urdu`: `Text`
-   `created_at`: `Timestamp`
-   `updated_at`: `Timestamp`

### Chatbot Session

Represents a conversation between a user and the chatbot.

-   `id`: `UUID` (Primary Key)
-   `user_id`: `UUID` (Foreign Key to User)
-   `history`: `JSONB` (e.g., `[{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]`)
-   `created_at`: `Timestamp`
-   `updated_at`: `Timestamp`

### Personalization Rule

A rule that defines how the content should be adapted for a user with a specific profile.

-   `id`: `UUID` (Primary Key)
-   `skill_level`: `JSONB`
-   `prompt`: `Text` (The prompt to use for personalization)
-   `created_at`: `Timestamp`
-   `updated_at`: `Timestamp`

## Relationships

-   A `User` can have multiple `Chatbot Sessions`.
-   A `Chatbot Session` belongs to one `User`.
