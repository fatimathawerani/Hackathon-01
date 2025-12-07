# Data Model: AI-Native Interactive Textbook

## Entities

### Textbook

**Description**: Represents the entire interactive textbook. It is a logical collection of chapters that together form the course material.

**Attributes**:
- **id**: A unique identifier for the textbook (implicit, not explicitly generated but represents the overall book).
- **title**: The title of the textbook ("Physical AI & Humanoid Robotics Course Textbook").

**Relationships**:
- **Has Many**: Chapters (a Textbook is composed of multiple Chapters).

### Chapter

**Description**: Represents a single section or unit within the Textbook. Each chapter corresponds to a distinct Markdown file and has a defined order within the textbook.

**Attributes**:
- **id**: A unique identifier for the chapter (implicit, often derived from its order and title).
- **title**: The full, human-readable title of the chapter (e.g., "Overview of Physical AI & Humanoid Robotics").
- **slug**: A URL-friendly and file-system-safe version of the title, used for file naming (e.g., "overview-of-physical-ai-humanoid-robotics").
- **order**: A numerical value indicating the sequence of the chapter within the textbook (e.g., `01`, `02`).
- **file_name**: The complete file name for the Markdown file (e.g., `01-overview-of-physical-ai-humanoid-robotics.md`).
- **file_path**: The absolute or relative path where the Markdown file is stored (e.g., `ai-interactive-textbook/docs/01-overview-of-physical-ai-humanoid-robotics.md`).
- **content**: The Markdown content of the chapter, including frontmatter, H1 title, and a TODO placeholder.

**Relationships**:
- **Belongs To**: Textbook (each Chapter is part of a Textbook).