# Tasks: Floating Chatbot UI

**Input**: Design documents from `/specs/004-chatbot-ui/`
**Prerequisites**: plan.md, spec.md

## Phase 1: Setup

**Purpose**: Create the basic structure for the ChatWidget component.

- [X] T001 Create a new directory at `book/src/components/ChatWidget`.
- [X] T002 [P] Create an empty `index.js` file in `book/src/components/ChatWidget`.
- [X] T003 [P] Create an empty `styles.css` file in `book/src/components/ChatWidget`.

---

## Phase 2: User Story 1 - View and Interact with Chatbot (Priority: P1) 🎯 MVP

**Goal**: Display a floating chatbot button on the site that opens a chat window.

**Independent Test**: The floating button appears, and clicking it opens and closes the chat window.

### Implementation for User Story 1

- [X] T004 [US1] Implement the basic `ChatWidget` component in `book/src/components/ChatWidget/index.js`.
- [X] T005 [US1] Add the floating button and a hidden chat window to the `ChatWidget` component.
- [X] T006 [US1] Implement the logic to toggle the chat window's visibility on button click.
- [X] T007 [US1] Modify `book/src/theme/Root.js` to import and render the `ChatWidget` component.
- [X] T008 [US1] Add basic styling for the floating button and chat window in `book/src/components/ChatWidget/styles.css`.

---

## Phase 3: User Story 2 - Send and Receive Messages (Priority: P2)

**Goal**: Enable users to send messages and receive replies from the chatbot.

**Independent Test**: Users can type a message, send it, and see a response from the bot.

### Implementation for User Story 2

- [ ] T009 [US2] Add a message list, text input, and "Send" button to the `ChatWidget` UI in `book/src/components/ChatWidget/index.js`.
- [ ] T010 [US2] Implement state management for the message list and input field.
- [ ] T011 [US2] Implement the `handleSend` function to send a POST request to `http://127.0.0.1:8000/chat` with the user's message.
- [ ] T012 [US2] Display the bot's response in the message list.
- [ ] T013 [US2] Implement a typing indicator that shows while waiting for the bot's response.
- [ ] T014 [US2] Ensure the message list automatically scrolls to the latest message.

---

## Phase 4: User Story 3 - Manage Chat Session (Priority: P3)

**Goal**: Allow users to clear the chat history.

**Independent Test**: Clicking the "Clear Chat" button removes all messages from the chat window.

### Implementation for User Story 3

- [ ] T015 [US3] Add a "Clear Chat" button to the `ChatWidget` UI in `book/src/components/ChatWidget/index.js`.
- [ ] T016 [US3] Implement the `handleClear` function to clear all messages from the state.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Ensure the chatbot is responsive and well-styled.

- [ ] T017 Add responsive styles to `book/src/components/ChatWidget/styles.css` to ensure the chat widget looks good on all screen sizes.
