#### Glossary

- **request** — something a person asks the pipeline to build or change.
- **backlog item** — one row in the queue that tracks a single request through the pipeline.
- **entry route** — the point in the document stack where a request enters the pipeline.
- **delivery** — the close of a backlog item: the suite is green, guardrails pass, the commit lands, and acceptance is met.
- **intake classifier** — the step that reads a new request and states its size, priority, entry route, and work type.

---

### Requirement 1: Batched decision page

**User Story:** As a person using the pipeline, I want open questions gathered onto one decision page, so that I answer them in one place while my other work keeps moving.

#### Acceptance Criteria
1. WHEN several questions are open at once, the system SHALL present them together on one decision page. [E-22]
2. WHEN the decision page opens, the system SHALL open it in its own window. [INV-4]
3. WHILE the decision page waits for an answer, the system SHALL continue the rest of the work. [INV-4]
4. WHILE a question waits on the person, the system SHALL keep it in its backlog item and keep the queue moving. [INV-4]
5. WHEN the system presents a question, the system SHALL mark the recommended answer and leave room for a different one. [E-22]
6. WHEN the decision page returns answered, the system SHALL file the answers in `docs/decisions/` and fold each answer into its backlog item in the same session. [E-22]
7. IF an answer is left unread, THEN the system SHALL count the decision as lost. [E-22]
8. Before asking any question, the system SHALL search the recorded answers first — the decision archive, the journal, and the profile. [INV-59]
9. IF a question has already been answered, THEN the system SHALL treat asking it again as a defect. [INV-59]
10. WHEN a question is answered and stands, the system SHALL close it permanently and harvest the answer into its backlog item in the same session. [INV-59]
11. WHEN a person clicks an option, the system SHALL record the click as a first pick only. [INV-9]
12. The system SHALL change trust and proactivity levels only on the person's word, and SHALL never raise its own latitude. [INV-9]
13. IF a person takes back a picked option in plain speech, THEN the system SHALL withdraw the option and log it as answered-then-withdrawn. [INV-9]
14. WHEN an option is withdrawn, the system SHALL ask the question again later in plainer terms. [INV-9]
15. WHEN the same decision is withdrawn a second time, the system SHALL take the recommended option and surface it as a `[default]` in the delivery report. [INV-130]
16. WHILE a decision has converged on its recommended option, the system SHALL treat silence as consent and SHALL never re-ask it. [INV-31]
17. IF the person later changes their mind, THEN the system SHALL handle it as a new request rather than reopening the closed decision. [INV-130]
18. The system SHALL keep the decision page mechanism — the filename, the ordering, the round-trip — documented in exactly one place, the communicator skill's rule 10. [INV-13]
19. IF a shared rule is fully restated inside a working skill, THEN the system SHALL treat the copy as drift and fold it back to its one home. [INV-13]

---

### Requirement 2: Consequence-first decision cards

**User Story:** As a person answering a decision, I want each card written in terms of what the options change for me, so that I can choose without first learning the machinery.

#### Acceptance Criteria
1. WHEN the system opens a decision card, the system SHALL state what each option changes for the person, in the product's own words. [INV-32]
2. WHEN the system labels an option, the system SHALL label it by its consequence. [INV-32]
3. IF the mechanism aids the choice, THEN the system SHALL add the mechanism after the consequence. [INV-32]
4. IF a card cannot be answered without understanding the mechanism, THEN the system SHALL count the card as a defect. [INV-28]
5. The system SHALL lead every human-facing line with what changed for the reader in plain words, with codes, row numbers, session numbers, and coined names only trailing. [INV-28]
6. IF a bookkeeping number — a test count, a suite size, a version string — would stand as the message itself, THEN the system SHALL keep it out of the message content. [INV-28]

---

### Requirement 3: Classifying a request

**User Story:** As a person throwing a request, I want it classified by size, priority, and work type at intake, so that the pipeline spends effort in proportion and I know where it entered.

#### Acceptance Criteria
1. WHEN a request arrives, the system SHALL classify it by size, priority, and work type.
2. The system SHALL name a request's size with one four-word vocabulary: bug, small, surface, or large.
3. The system SHALL use those same four words in the queue's class column, and SHALL use no second size scale.
4. The system SHALL treat the entry route as a separate axis from size.
5. The system SHALL set a request's priority to normal unless its backlog item states otherwise.
6. WHEN the shipped product is broken for its user — an unusable surface, lost data, or a violated safety gate — the system SHALL mark the request critical.
7. WHEN a request is low effort, of immediate value, and carries no design decision inside, the system SHALL mark it a quick win.
8. WHEN a request arrives, the system SHALL tag it with exactly one work type from the curated vocabulary: product, infra, skill, or prose. [T-16]
9. The system SHALL keep the project's default work type in its profile. [T-16]
10. IF the intake classifier cannot call a request's size, priority, or work type, THEN the system SHALL ask the person at intake and SHALL NOT guess. [INV-12]
11. WHILE the person has not answered, the system SHALL carry the request at normal priority. [INV-12]
12. WHILE the work type is unnamed, the system SHALL use the project's recorded default, or none. [INV-22]
13. IF a work type is not yet named, THEN the system SHALL scale nothing down. [INV-22]
14. WHILE a classification question is open, the system SHALL keep it in the backlog item and keep the queue moving. [INV-4]
15. WHILE a pipeline step runs, the system SHALL scale its effort by the request's work type and report whether it applied or stood down, naming the step. [INV-22]
16. The system SHALL run the mandatory safety checks whatever the work type. [INV-22]

---

### Requirement 4: Negotiating the scope of a large request

**User Story:** As a person throwing a large request, I want the pipeline to negotiate its scope rather than its schedule, so that oversized work is cut or staged without any hidden choices.

#### Acceptance Criteria
1. The system SHALL NOT ask how long a request will take, and SHALL NOT accept an estimate in hours or days as an input. [T-15]
2. WHEN a request is larger than its worth, the system SHALL answer in scope terms and propose either cutting the scope or splitting into stages. [T-15]
3. WHEN the system cuts the scope, the system SHALL take fewer surfaces in and set plainer defaults on what stays. [T-15]
4. WHEN the system splits a request into stages, the system SHALL send each stage through the full pipeline on its own. [INV-12]
5. WHEN the system proposes a scope move, the system SHALL proceed on the recommended option and SHALL NOT park the queue on it. [INV-4]
6. WHEN the system makes a scope cut, the system SHALL report it in the same batched report as every taken default. [INV-18]
7. The system SHALL surface every scope cut and SHALL make none silently. [INV-5]
8. WHEN the session makes a taste choice without asking, the system SHALL tell it in the delivery report with plain words, an example, and a `[default]` mark. [INV-31]
9. WHILE a taste default stands unchanged, the system SHALL take it as accepted. [INV-31]
10. WHEN a request is marked priority, the system SHALL bubble it to the queue head while the queue keeps running. [T-11]
11. IF a scope cut or a file's own date would change the running order, THEN the system SHALL leave the order unchanged. [T-11]
12. IF a cut surface is asked for again later, THEN the system SHALL handle it as a new request.
13. WHEN a request touches a surface that already works, the system SHALL open its spec-delta with regression checks, one sentence per neighbouring promise, each citing the clause it guards. [T-14]
14. WHEN the system cuts scope, the system SHALL NOT touch the regression checks. [T-14]
15. WHEN the system cuts scope, the system SHALL NOT touch a kept surface's aspects. [INV-18]
16. The system SHALL end every aspect of a feature as a written spec sentence — a decided value, or one tagged as a default and reported. [INV-18]
17. The system SHALL always write the non-goals sentence, and stating that nothing was deliberately left out SHALL be valid. [INV-20]
18. WHEN a scope cut narrows the non-goals, the system SHALL report the exclusion in the batched report. [INV-20]
19. The system SHALL have every feature state one success measure, decided or tagged as a default. [INV-21]
20. WHEN the system cuts scope, the system SHALL adjust richness only and SHALL leave the delta's mandatory sentences intact. [T-15]

---

### Requirement 5: Deriving a settled answer from a proven artifact

**User Story:** As a person, I want the pipeline to derive answers the documents already settle, so that I am asked only about genuinely open choices.

#### Acceptance Criteria
1. WHEN a design choice is about to surface, the system SHALL check whether a proven artifact — the architecture, the spec, or the invariants — already determines the answer. [INV-121]
2. IF a proven artifact determines the answer, THEN the system SHALL derive the requirement, say it back with the section cited, and offer no fork. [INV-121]
3. WHEN the artifacts leave a choice genuinely open — a taste call, or a real trade-off with no artifact-grounded winner — the system SHALL bring the fork to the person. [INV-121]
4. WHEN the agent is about to ask a question, the system SHALL first run the outside-reader read and the can-I-decide-or-verify-it-myself gate. [INV-81]
5. IF the agent can decide or verify the answer itself, THEN the system SHALL do the work instead of asking. [INV-81]
6. WHEN a question survives the gate, the system SHALL attach its recommendation. [INV-81]

---

### Requirement 6: One request is one story, and an item closes only whole

**User Story:** As a person, I want each request to become one story per backlog item and to close only when every part is done, so that nothing is fused, dropped, or half-delivered.

#### Acceptance Criteria
1. WHEN a request carries several user stories, the system SHALL split it at intake into one backlog item per story. [T-17]
2. WHEN a story has sub-behaviours — a hover face, a phone face, a backpointer — the system SHALL fold them into that story's backlog item as its acceptance. [T-17]
3. IF the number of stories in a request is unclear, THEN the system SHALL ask the person at intake and SHALL NOT guess. [INV-12]
4. The system SHALL treat a stage split as slicing one story's depth. [T-15]
5. The system SHALL never fuse separate stories into one backlog item. [T-17]
6. WHEN the system splits a request, the system SHALL have every resulting backlog item cite the one request it came from. [INV-1]
7. The system SHALL bring every request to a recorded terminal state, so none is dropped between intake and resolution. [INV-1]
8. WHEN a backlog item carries several legs, the system SHALL enumerate per-leg acceptance in its Done-when. [INV-26]
9. IF a leg is unmet, THEN the system SHALL NOT close the backlog item. [INV-26]
10. WHILE a leg is still open at compaction, the system SHALL restate it in full and SHALL NOT compress it out of the resume file. [M-2]
11. WHEN a movement ends, the system SHALL replace the resume state, add a dated journal entry, commit the work, compact its own context, and say so. [M-2]
