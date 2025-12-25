---
id: 20
title: Plan Contact and Onboarding Forms
stage: plan
date: 2025-12-24
surface: agent
model: gemini-cli
feature: 006-contact-and-onboarding-forms
branch: 006-contact-and-onboarding-forms
user: unspecified
command: /sp.plan
labels: [implementation-plan]
links:
  spec: specs/006-contact-and-onboarding-forms/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/006-contact-and-onboarding-forms/plan.md
  - specs/006-contact-and-onboarding-forms/research.md
  - specs/006-contact-and-onboarding-forms/data-model.md
  - specs/006-contact-and-onboarding-forms/contracts/openapi.yaml
  - specs/006-contact-and-onboarding-forms/quickstart.md
tests:
  - none
---

## Prompt

Frontend (Docusaurus):
+ Create reusable ContactForm component
+ Reuse form for:
+  - Public Contact page
+  - Signup onboarding step
+ Auto-fill user data when authenticated
+ Client-side validation only

Auth (Better Auth):
+ Extend signup flow with onboarding form
+ Store contact & profile data in user metadata
+ Do not require contact form for signin

Backend (FastAPI):
+ Add /contact endpoint
+ Accept anonymous or authenticated submissions
+ Persist or email messages (implementation-agnostic)

Safety:
+ No changes to /ask behavior
+ No auth enforcement on reading or translation

## Response snapshot

Created implementation plan, research, data model, and API contracts for Contact & Onboarding Forms.

## Outcome

- ✅ Impact: The implementation plan and design artifacts have been created, providing a clear roadmap for developing the contact form and onboarding flow.
- 🧪 Tests: No tests were run.
- 📁 Files: 
  - `specs/006-contact-and-onboarding-forms/plan.md`
  - `specs/006-contact-and-onboarding-forms/research.md`
  - `specs/006-contact-and-onboarding-forms/data-model.md`
  - `specs/006-contact-and-onboarding-forms/contracts/openapi.yaml`
  - `specs/006-contact-and-onboarding-forms/quickstart.md`
- 🔁 Next prompts: /sp.tasks
- 🧠 Reflection: The planning phase went smoothly. The architecture is straightforward, leveraging existing components and infrastructure.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
