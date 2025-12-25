---
id: 19
title: Specify Contact and Onboarding Forms
stage: spec
date: 2025-12-24
surface: agent
model: gemini-cli
feature: 006-contact-and-onboarding-forms
branch: 006-contact-and-onboarding-forms
user: unspecified
command: /sp.specify
labels: [feature-specification]
links:
  spec: specs/006-contact-and-onboarding-forms/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/006-contact-and-onboarding-forms/spec.md
  - specs/006-contact-and-onboarding-forms/checklists/requirements.md
tests:
  - none
---

## Prompt

Feature set to add: 6. Contact & Onboarding Forms Contact Form: - Reusable contact form component - Fields: - Name - Email - Message - Accessible to: - Anonymous users - Logged-in users - Logged-in users auto-fill name & email - Submits to backend endpoint - No impact on RAG or embeddings Auth-aware Signup Extension: - Contact-style form used during Signup - Collects: - Software experience - Hardware access - Learning depth - Optional message / goal - Stored via Better Auth user metadata Constraints: - No blocking of reading content - No modification of existing auth flows - No duplication of profile schema

## Response snapshot

Created feature specification and quality checklist for Contact & Onboarding Forms.

## Outcome

- ✅ Impact: The feature specification for "Contact & Onboarding Forms" has been created, defining the requirements for the contact form and enhanced signup onboarding.
- 🧪 Tests: No tests were run.
- 📁 Files: 
  - `specs/006-contact-and-onboarding-forms/spec.md`
  - `specs/006-contact-and-onboarding-forms/checklists/requirements.md`
- 🔁 Next prompts: /sp.plan
- 🧠 Reflection: The process was straightforward. The user provided clear requirements which mapped directly to user stories and functional requirements.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
