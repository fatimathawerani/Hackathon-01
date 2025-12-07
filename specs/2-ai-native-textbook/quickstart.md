# Quickstart Guide: AI-Native Interactive Textbook Structure

This guide provides instructions to quickly set up and view the generated AI-Native Interactive Textbook structure using Docusaurus.

## Prerequisites

- Node.js (LTS version recommended)
- npm or Yarn (npm is used in these instructions)

## Steps

### 1. Navigate to the Docusaurus Project

Ensure you are in the root directory of your Docusaurus project, which is assumed to be `ai-interactive-textbook/`:

```bash
cd ai-interactive-textbook
```

### 2. Install Dependencies

If you haven't already, install the necessary Node.js dependencies for Docusaurus:

```bash
npm install
# or
yarn install
```

### 3. Build the Docusaurus Site

Generate the static build of your Docusaurus site. This will process the Markdown files (including the newly generated chapter files) and create a production-ready output in the `build/` directory:

```bash
npm run build
# or
yarn build
```

### 4. Start the Docusaurus Development Server

To view the textbook locally in your browser, start the Docusaurus development server:

```bash
npm run start
# or
yarn start
```

This command will usually open your browser to `http://localhost:3000/` (or another available port). You should see the textbook's home page and be able to navigate through the generated chapters using the sidebar.

## Important Notes

- **Chapter Content**: The generated chapter Markdown files currently contain only a title and a "TODO" placeholder. You will need to add the actual content for each chapter.
- **Sidebars**: Docusaurus automatically detects Markdown files in the `docs/` directory. The chapter numbering (e.g., `01-`, `02-`) will ensure the correct order in the sidebar navigation.