---

description: "Task list for AI-Native Interactive Textbook implementation"
---

# Tasks: AI-Native Interactive Textbook

**Input**: Design documents from `/specs/2-ai-native-textbook/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, quickstart.md

**Tests**: This project uses manual verification for testing in this phase, as per the plan.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure for Spec-Kit Plus and Docusaurus integration.

- [x] T001 Verify `ai-interactive-textbook/` directory exists and contains a Docusaurus project.
- [x] T002 Create `book.yaml` for Spec-Kit Plus configuration at `book.yaml`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Configure `book.yaml` with chapter details and output settings. This MUST be complete before generating any chapter files.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T003 Define chapter list in `book.yaml` with titles and slugs for all 11 chapters:
    - Overview
    - Introduction to Physical AI
    - ROS 2 Fundamentals
    - Gazebo Simulation
    - NVIDIA Isaac Platform
    - Humanoid Robotics
    - Conversational Robotics
    - Hardware Requirements
    - Lab Architecture
    - Edge Kits and Digital Twin
    - Capstone Autonomous Humanoid
- [x] T004 Configure `book.yaml` to output generated files into `ai-interactive-textbook/docs/`.
- [x] T005 [P] Ensure `ai-interactive-textbook/docs/` directory exists or is creatable (per FR-005).

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Student Accesses Course Material (Priority: P1) 🎯 MVP

**Goal**: Students can access the textbook and navigate between chapters on the Docusaurus site.

**Independent Test**: Successfully build and serve the Docusaurus site, then navigate through the generated chapters via the sidebar.

### Implementation for User Story 1

- [ ] T006 [P] [US1] Generate all chapter markdown files (FR-001) in `ai-interactive-textbook/docs/` (FR-002).
    - Ensure naming convention (FR-003: `NN-slugified-title.md`)
    - Ensure frontmatter with title (FR-004)
    - Ensure H1 heading and TODO comment (FR-006)
- [ ] T007 [US1] Run Docusaurus build command (`npm run build` or `yarn build`) from `ai-interactive-textbook/`.
- [ ] T008 [US1] Serve Docusaurus site locally (`npm run start` or `yarn start`) from `ai-interactive-textbook/`.
- [ ] T009 [US1] Manually verify site loads and chapters are navigable via sidebar.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Instructor References Curriculum (Priority: P2)

**Goal**: Instructors can easily verify the textbook's chapter structure aligns with the official course curriculum.

**Independent Test**: Review the Docusaurus site's navigation sidebar to confirm all official course chapters are listed in the correct order and with accurate names.

### Implementation for User Story 2

- [ ] T010 [US2] Manually verify chapter names and their order in the Docusaurus sidebar match the official course structure.

**Checkpoint**: All user stories should now be independently functional

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and ensuring a production-ready structure.

- [ ] T011 Run `quickstart.md` validation steps from `specs/2-ai-native-textbook/quickstart.md`.
- [ ] T012 Confirm all functional requirements from `specs/2-ai-native-textbook/spec.md` have been met.
- [ ] T013 Final review of generated Markdown files for formatting and content placeholders.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Depends on US1 for generated content to verify.

### Within Each User Story

- Tasks are generally sequential, follow T-ID order.
- `T006` (Generate files) is critical for US1.

### Parallel Opportunities

- `T005` can be done in parallel with `T003` and `T004` if implemented within Spec-Kit Plus generation logic. For manual implementation, it's a prerequisite to `T006`.
- `T006` includes several sub-requirements (naming, frontmatter, H1, TODO comment) which could be parallelized if handled by distinct functions in a generation script.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing (N/A for manual verification here)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
