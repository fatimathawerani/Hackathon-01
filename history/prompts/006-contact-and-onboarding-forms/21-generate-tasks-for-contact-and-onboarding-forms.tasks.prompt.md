---
id: 21
title: Generate Tasks for Contact and Onboarding Forms
stage: tasks
date: 2025-12-24
surface: agent
model: gemini-cli
feature: 006-contact-and-onboarding-forms
branch: 006-contact-and-onboarding-forms
user: unspecified
command: /sp.tasks
labels: [task-generation]
links:
  spec: specs/006-contact-and-onboarding-forms/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/006-contact-and-onboarding-forms/tasks.md
tests:
  - none
---

## Prompt

Tasks: [ ] Design reusable ContactForm component [ ] Add Contact page in Docusaurus [ ] Auto-fill form for authenticated users [ ] Integrate ContactForm into Better Auth signup [ ] Define contact payload schema [ ] Add FastAPI /contact endpoint [ ] Store or forward contact messages [ ] Validate anonymous + logged-in flows [ ] Ensure zero impact on RAG & embeddings [ ] Document form usage

## Response snapshot

Generated actionable tasks for Contact & Onboarding Forms.

## Outcome

- ✅ Impact: The tasks.md file has been generated with 14 tasks organized by user story and dependency.
- 🧪 Tests: No tests were run.
- 📁 Files: 
  - `specs/006-contact-and-onboarding-forms/tasks.md`
- 🔁 Next prompts: /sp.implement
- 🧠 Reflection: The task breakdown is logical. Backend tasks are prioritized to unblock frontend integration.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
