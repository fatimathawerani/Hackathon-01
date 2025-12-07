<!--
Sync Impact Report:

- Version change: N/A → 1.0.0
- Modified Principles:
  - [PRINCIPLE_1_NAME] → I. Code Quality
  - [PRINCIPLE_2_NAME] → II. Content Consistency
  - [PRINCIPLE_3_NAME] → III. Rigorous Testing
  - [PRINCIPLE_4_NAME] → IV. Chatbot Reliability and Accuracy
  - [PRINCIPLE_5_NAME] → V. Performance Optimization
  - [PRINCIPLE_6_NAME] → VI. Accessibility
- Added Sections:
  - VII. User Experience Consistency
  - VIII. Comprehensive Documentation
  - Development Workflow
  - Quality Gates
- Removed Sections: None
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/tasks-template.md
  - ✅ .gemini/commands/sp.constitution.toml
- Follow-up TODOs: None
-->
# Claude Project Constitution

## Core Principles

### I. Code Quality
All code, including frontend, backend, and agent code, must adhere to the highest quality standards. This includes following established coding conventions, writing clean, maintainable, and well-documented code.

### II. Content Consistency
All written content must maintain a consistent style, formatting, and terminology throughout all chapters and documentation. A project-wide style guide will be maintained and enforced.

### III. Rigorous Testing
A comprehensive testing strategy is mandatory. This includes unit, integration, and end-to-end tests for all critical components, including the RAG pipeline, API endpoints, authentication, and chatbot functionalities.

### IV. Chatbot Reliability and Accuracy
The chatbot must provide reliable and accurate responses. The Retrieval-Augmented Generation (RAG) pipeline must be continuously evaluated and improved to ensure the quality of retrieved information.

### V. Performance Optimization
All components must be optimized for performance. This includes fast page loads for Docusaurus, efficient backend inference, and optimized vector search to ensure a smooth user experience.

### VI. Accessibility
The application must be accessible to all users. This includes adhering to WCAG guidelines, ensuring readable typography, proper color contrast, and clear, intuitive navigation.

### VII. User Experience Consistency
A consistent and intuitive user experience must be maintained across all user-facing components, including the main book content, chatbot, authentication screens, and personalization features.

### VIII. Comprehensive Documentation
All components must be thoroughly documented to facilitate understanding, maintenance, and extension by future contributors and instructors. This includes code comments, API documentation, and architectural diagrams.

## Development Workflow

- All changes must be submitted through pull requests.
- All pull requests must be reviewed by at least one other contributor.
- All pull requests must pass all automated checks before being merged.

## Quality Gates

- Code coverage must not decrease.
- All new features must be accompanied by tests.
- All reported bugs must have a corresponding regression test.

## Governance

- This constitution is the single source of truth for all development principles.
- Amendments to this constitution must be proposed via a pull request and approved by the project maintainers.
- All contributors are expected to adhere to the principles outlined in this document.

**Version**: 1.0.0 | **Ratified**: 2025-12-07 | **Last Amended**: 2025-12-07