# Data Model: AI-Native Interactive Textbook

This data model reflects the hierarchical structure of the Docusaurus book as outlined in the implementation plan.

## Entities

### Book

**Description**: Represents the entire Docusaurus project and the collection of all content.

**Attributes**:
- **title**: The overall title of the book, configured in `docusaurus.config.ts`.
- **structure**: The collection of chapters that make up the book.

**Relationships**:
- **Has Many**: Chapters

### Chapter

**Description**: A logical grouping of related lessons, represented by a directory within the `docs` folder.

**Attributes**:
- **order**: A numerical prefix in the directory name (e.g., `01-`) that defines its sequence.
- **slug**: The human-readable part of the directory name (e.g., `chapter-one`).
- **label**: The display name for the chapter in the sidebar, defined in the `_category_.json` file.

**Relationships**:
- **Belongs To**: Book
- **Has Many**: Lessons

### Lesson

**Description**: An individual content page within a chapter, represented by a Markdown file.

**Attributes**:
- **order**: A numerical prefix in the filename (e.g., `01-`) that defines its sequence within the chapter.
- **slug**: The human-readable part of the filename (e.g., `lesson-one.md`).
- **title**: The display title of the lesson, defined in the frontmatter of the Markdown file.
- **content**: The Markdown body of the lesson.

**Relationships**:
- **Belongs To**: Chapter
