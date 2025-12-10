# Quickstart Guide: Building the Docusaurus Book

This guide provides the essential steps to set up, build, and view the Docusaurus-based textbook.

## Prerequisites

- Node.js (LTS version recommended)
- An npm-compatible package manager (e.g., npm, yarn, pnpm)

## 1. Project Setup

If you are starting from scratch, initialize a new Docusaurus project.

```bash
# This will create a new Docusaurus site in a directory named 'ai-interactive-textbook'
npm init docusaurus@latest ai-interactive-textbook --typescript
```

Navigate into your newly created project directory:
```bash
cd ai-interactive-textbook
```

Install the dependencies:
```bash
npm install
```

## 2. Content Scaffolding

Follow the file structure outlined in the `plan.md` to create the chapter and lesson files. For example:

```
docs
├── 01-getting-started/
│   ├── _category_.json
│   └── 01-introduction.md
└── intro.md
```

**`_category_.json` Example:**
```json
{
  "label": "1. Getting Started",
  "position": 1
}
```

**`01-introduction.md` Example:**
```markdown
---
title: Introduction to the Course
---

# Introduction to the Course

<!-- TODO: Add lesson content here -->
```

## 3. Running the Development Server

To preview your site as you make changes, run the development server:

```bash
npm start
```

This will open a browser window to `http://localhost:3000` where you can see your book, with live reloading as you edit files.

## 4. Building the Static Site

When you are ready to deploy, create a production-ready static build of your site:

```bash
npm run build
```

The output will be generated in the `build/` directory. You can then serve these static files from any web server.
