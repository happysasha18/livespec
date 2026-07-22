# Intake: taking in a request and shaping it

This document states what the pipeline does when a person hands it a request. It is written for a reader who has never seen the pipeline before.

Bracket codes like `[INV-4]` and `[T-15]` point to the rule's home in the project spec. They are reference anchors for the author. A reader can ignore them. The letter before the number names the rule's kind: `INV-` an invariant (a numbered rule of behaviour that must always hold), `T-` a transition (a numbered change of state the pipeline performs), `E-` an entity (a numbered part of the product), and `M-` a rhythm rule (a numbered recurring routine, such as the routine at the end of a movement).

The keywords *when*, *while*, *if*, *then*, and *shall* are set in italics and carry their standard requirements meaning. *Shall* states a duty. *When* and *while* open a situation. *If* and *then* open a condition and its result.

Within each requirement, the criteria are grouped into named cases. A case names one situation; its criteria state what the system does in it.

---

## Glossary

Every domain noun used below is defined here. A word of ordinary English has no entry.

- **request** — one thing a person asks the pipeline to build, change, or fix.
- **inbox** — a folder in the project where a request can arrive as a dropped file.
- **intake** — the first step, where the pipeline reads a new request and records what it is before any work starts.
- **intake classifier** — the part of intake that reads a new request and states its size, its priority, its entry route, and its work type.
- **backlog item** — one row that tracks a single request from intake to its close.
- **queue** — the ordered list of backlog items waiting for work. The pipeline runs the item at the head first.
- **pipeline** — the fixed sequence of steps a request passes through, from intake to delivery: spec, architecture, test matrix, tests, code, and a final check.
- **spec** — the document that states what the product does for its user.
- **architecture** — the document that states which module owns which behaviour.
- **invariant** — one numbered rule of behaviour that tests enforce; the `INV-` codes in brackets name them.
- **proven document** — a document the reviewer role has reviewed until no findings remain; the spec, the architecture, and the invariants can each be proven.
- **skill** — one role's instruction file; the pipeline's roles — analyst, reviewer, tester, reporter — each have one.
- **document chain** — the ordered set of project documents where each is derived from the one above it: spec, then architecture, then test matrix, then code, then docs.
- **entry route** — the route a request takes into the pipeline, named at intake from a closed set of five: feature, bug, refactor, docs-only, and skip. The route decides which pipeline steps run, and each route enters the document chain at the highest document whose sentences must change for the request to be satisfied.
- **work type** — the kind of thing a request builds, named with one of four words: product, infra, skill, or prose.
- **session** — one conversation with the system, from its start to the moment the conversation closes or its working memory is wiped. Work promised in the same session lands before that boundary.
- **decision** — one open choice the pipeline needs the person to settle before or during the work.
- **decision page** — one page that gathers the open decisions together, so the person answers them in one place while other work keeps running.
- **decision card** — one block on the decision page. It states a single decision, lists the options, and marks the recommended one.
- **decision archive** — the folder `docs/decisions/`, where answered decision pages are kept.
- **journal** — the project's dated work log, the file `JOURNAL.md`. It holds history and the reasons behind past choices; the spec holds only today's behaviour.
- **footprint** — the reach of a request across the code, named with one of three words: presentation-only, single-module, or cross-cutting.
- **scope** — the set of surfaces and behaviours a request covers.
- **stage** — one slice of a large request that passes through the full pipeline on its own.
- **regression check** — one written sentence in a spec change that guards a neighbouring promise the change could break.
- **delivery** — the close of a backlog item. The suite is green, the guardrails pass, the commit lands, and the acceptance is met.
- **delivery report** — the summary the pipeline gives the person when a backlog item is delivered. Its batched section lists together every taken default, scope cut, and deliberate narrowing, so none is reported alone or in silence.
- **default mark** — the tag `[default]` on a choice the pipeline made on its own and is reporting for review.
- **guardrail** — an automatic check that runs on every save or push and blocks a change that breaks a stated rule.
- **suite** — the full set of automated tests for the project. Green means every test passes.
- **compaction** — a scheduled pass that removes duplicated content so each fact lives in one place. It never removes content whose loss would change meaning.
- **movement** — one block of work, from taking a backlog item to its delivery report.
- **resume file** — the short file the pipeline reads at a cold start to learn what to resume. It holds at most 100 lines.
- **profile** — the file `.live-spec/profile.md` in the project. It holds the project's own settings — its default work type, its language, and its reporting preferences.

---

## Requirement 1: One decision page for open decisions

**Context:** During the work, the pipeline reaches choices it cannot settle on its own. Rather than stopping to ask each one in chat, it gathers the open decisions onto one decision page. The person opens that page and answers the decisions together. The rest of the work keeps running while the page waits.

**User Story:** As a person whom the pipeline needs a decision from, I want the open decisions gathered onto one page, so that I answer them in one place while my other work keeps moving.

### Acceptance Criteria

**Case: the page opens**

1. *when* more than one decision is open at once, the system *shall* present them together on one decision page. [E-22]
2. *when* the decision page opens, the system *shall* open it in its own browser window. [INV-4]

**Case: work keeps moving while the page waits**

3. *while* the decision page waits for an answer, the system *shall* keep the rest of the work running. [INV-4]
4. *while* a decision waits on the person, the system *shall* keep it in its backlog item and keep the queue moving. [INV-4]

**Case: answering on the page**

5. *when* the system presents a decision, the system *shall* mark the recommended option and leave room for a different answer. [E-22]
6. *when* the decision page returns answered, the system *shall* file the answers in the decision archive and fold each answer into its backlog item in the same session. [E-22]
7. *if* an answer is left unread, *then* the system *shall* count the decision as lost. [E-22]

**Case: no decision is asked twice**

8. Before asking any decision, the system *shall* first search the recorded answers: the decision archive, the journal, and the profile. [INV-59]
9. *if* a decision has already been answered, *then* the system *shall* treat asking it again as a defect, and a defect of the product opens its own backlog item on the bug entry route. [INV-59, T-9]
10. *when* a decision is answered and the answer stands, the system *shall* close it for good and fold the answer into its backlog item in the same session. [INV-59]

**Case: a click against the person's word**

11. *when* a person clicks an option, the system *shall* record the click as a provisional choice; the person's words in chat can still change it before the decision closes. [INV-9]
12. The system *shall* change its trust and proactivity settings — the settings that widen or narrow what it may do on its own word — only when the person says so. The system may propose a level; it *shall* set none itself. [INV-9]

**Case: a withdrawn option**

13. *if* a person takes back a picked option in chat, in the person's own words, *then* the system *shall* withdraw the option and log it as answered-then-withdrawn. [INV-9]
14. *when* an option is withdrawn, the system *shall* ask the decision again later, in chat, in plainer words than the first ask used. [INV-9]
15. *when* the same decision is withdrawn a second time, the system *shall* take the recommended option and surface it as a default mark in the delivery report. [INV-130]

**Case: a settled decision**

16. *while* a decision has settled on its recommended option, the system *shall* treat silence as consent and *shall* leave it unasked. [INV-31]
17. *if* the person later says in chat that they have changed their mind, *then* the system *shall* handle the change as a new request through ordinary intake, and *shall* leave the closed decision closed. [INV-130]

**Case: one home for the mechanism**

18. The system *shall* keep the decision-page mechanism — the page's filename, its question order, and its round-trip from open to answered — documented in one place. That place is rule 10 of the reporter role's instruction file. [INV-13]
19. *if* a shared rule is fully restated inside one role's skill, *then* the system *shall* treat the copy as drift and fold it back to its one home. [INV-13]

---

## Requirement 2: A decision card states each option's effect

**Context:** Each decision on the decision page is shown as a decision card. The card names the decision, lists the options, and marks the recommended one. The person reads the card and picks one option. The card states each option's effect in product terms, so the person can choose without reading the pipeline's internal steps.

**User Story:** As a person answering a decision on the decision page, I want each decision card to state what each option changes for me, so that I can choose one option from the card without first learning how the pipeline works inside.

### Acceptance Criteria

**Case: the card speaks in effects**

1. *when* the system opens a decision card, the system *shall* state what each option changes for the person, in the product's own words. [INV-32]
2. The person chooses one option from the options listed on the decision card. The system *shall* state each option's effect on the card, so the person can choose without reading the pipeline's internal steps. [INV-32]
3. *when* the system labels an option, the system *shall* name the option by its effect on the person. [INV-32]

**Case: the mechanism trails**

4. *if* the pipeline's internal mechanism helps the choice, *then* the system *shall* add the mechanism after the effect. [INV-32]
5. *if* a decision card cannot be answered without understanding the pipeline's internal mechanism, *then* the system *shall* count the card as a defect, and a defect of the product opens its own backlog item on the bug entry route. [INV-28, T-9]

**Case: every line the person reads**

6. The system *shall* lead every line the person reads with what changed for them, in plain words. Codes, internal bookkeeping numbers — queue positions, work-session counters — and internal names *shall* trail the line. [INV-28]
7. *if* a bookkeeping number — a test count, a suite size, or a version string — would stand as the whole message, *then* the system *shall* keep it out of the message body. [INV-28]

---

## Requirement 3: The intake classifier states a request's size, priority, and work type

**Context:** A request arrives from the person. Before any work starts, the intake classifier reads the request and records what it is. It states the request's size, its priority, and its work type. The person sees these on the backlog item.

**User Story:** As a person handing in a request, I want the intake classifier to state its size, priority, and work type at intake, so that a small request gets a small process and a large one gets the full pipeline, and I can see how the request was read.

### Acceptance Criteria

**Case: size**

1. *when* a request arrives, the system *shall* classify it by size, priority, and work type.
2. The system *shall* name a request's size with one four-word vocabulary: bug, small, surface, or large.
3. The system *shall* use those same four words in the queue's class column, and *shall* keep to one size scale.
4. The system *shall* treat the entry route as a separate axis from size, with one stated tie: a request sized bug enters by the bug entry route, one call stated once, and the route axis adds the other four values. [T-12]

**Case: priority — critical**

5. The system *shall* set a request's priority to normal unless its backlog item states another value.
6. *when* the intake classifier judges the shipped product broken for its user, the system *shall* mark the request critical. The intake classifier judges the product broken by three tests: a surface the user cannot use, lost data, or a violated guardrail. [T-11]
7. *when* a request on a non-bug entry route is marked critical, the system *shall* move it to the head of the queue while the running work keeps going. [INV-133]
8. *when* a request on a non-bug entry route is marked critical, the system *shall* keep the running work running. [INV-133]
9. *when* a request is marked critical, the system *shall* state at intake that the mark heads the queue and keeps the running work running, so the person can reclassify it as a bug if the person meant a live break that must stop the work now. [INV-133]
10. The system *shall* set priority on the person's word, and the critical mark *shall* stand once the person gives it. [INV-133]

**Case: priority — quick win**

11. *when* the intake classifier judges a request low in effort, immediate in value, and free of any design decision, the system *shall* mark the request a quick win. [T-11]
    [GAP: the spec does not define how the intake classifier measures a request's effort or a request's value for the quick-win mark.]
12. *when* the queue frees and a quick win is waiting, the system *shall* be free to take the quick win ahead of larger queued items, and *shall* mark the promotion in the backlog item. [T-11]
13. *when* a promoted quick win is delivered, the system *shall* run the queue head next, so a run of quick wins does not starve a larger request. [T-11]

**Case: work type**

14. *when* a request arrives, the system *shall* tag it with one work type from the curated vocabulary: product, infra, skill, or prose. [T-16]
15. The system *shall* keep the project's default work type in its profile. [T-16]
16. *while* a pipeline step runs, the system *shall* scale its effort by the request's work type, and *shall* report whether it applied or stood down, naming the step. [INV-22]
17. The system *shall* run the guardrails whatever the work type. [INV-22]

**Case: the classifier is unsure**

18. *if* the intake classifier cannot call a request's size, priority, or work type, *then* the system *shall* ask the person at intake and *shall* refrain from guessing. [INV-12]
19. *while* the person has not answered, the system *shall* carry the request at normal priority. [INV-12]
20. *while* the work type is unnamed, the system *shall* use the project's recorded default, or none. [INV-22]
21. *if* a work type is not yet named, *then* the system *shall* scale nothing down. [INV-22]
22. *while* a classification decision is open, the system *shall* keep it in the backlog item and keep the queue moving. [INV-4]

**Case: the bug route**

23. *when* a request enters by the bug entry route, the system *shall* admit it at the test-matrix step and *shall* reproduce the break as a failing test before fixing it. [T-12]
24. The bug entry route is the one route allowed to interrupt running work: the running work parks at a stopping point from which it can resume with nothing lost, the bug is fixed, and the parked work resumes in its original order. [T-9]

---

## Requirement 4: The three-source impact read at intake

**Context:** At intake, the pipeline reads how far a request reaches into the code before it picks a route. It reads three sources: the spec, the architecture, and the code. The read produces one footprint. The footprint says how much of the pipeline the request needs.

**User Story:** As a person handing in a request, I want its reach read at intake from the spec, the architecture, and the code, so that the route it takes matches how far it actually reaches.

### Acceptance Criteria

**Case: the read**

1. *when* a request arrives, the system *shall* read its impact from three sources: the spec for what behaviour changes, the architecture for which module owns it, and the code for what the change touches. [INV-128]
2. *when* the impact read completes, the system *shall* name one footprint: presentation-only, single-module, or cross-cutting. [INV-128]

**Case: the footprint picks the route**

3. *when* the footprint is presentation-only, the system *shall* route the request through a shortened pipeline, one with fewer steps than the full pipeline runs. [INV-128]
4. *when* the footprint is single-module, the system *shall* route the request through the test-matrix step against that module's interface. [INV-128]
5. *when* the footprint is cross-cutting, the system *shall* route the request through the full pipeline. [INV-128]
6. The system *shall* match the route to the footprint, and *shall* let the footprint pick the route rather than the size. [INV-128]

**Case: the sources disagree**

7. *if* the three sources disagree, *then* the system *shall* name the disagreement as a finding and open it as its own backlog item with the document that owns the disputed fact: code past a spec promise opens a bug backlog item on the bug entry route; a spec pin that has moved opens a spec-fix backlog item; a module boundary with a missing owner opens a restructure backlog item, which changes the architecture only through the architecture step's re-check. [INV-128]
   [GAP: the spec does not name the entry routes for the spec-fix and restructure backlog items; of the three disagreement outcomes, only the bug item's route is stated.]
8. The system *shall* trust no single source in silence. [INV-128]

**Case: the footprint is recorded and can move**

9. *if* an edit reaches past its module while the work runs, *then* the system *shall* re-name the footprint and record the change in the delivery report. [INV-128]
10. The system *shall* record the named footprint in the backlog item. [INV-128]

---

## Requirement 5: Negotiating the scope of a large request

**Context:** A request can be larger than its worth. When the intake classifier judges it so, the pipeline negotiates its scope rather than its schedule. It proposes cutting the scope or splitting the request into stages. It reports every cut it makes.

**User Story:** As a person handing in a large request, I want the pipeline to negotiate its scope rather than its schedule, so that a request larger than its worth is cut or staged with no hidden choices.

### Acceptance Criteria

**Case: scope, never a schedule**

1. The system *shall* leave a request's duration unasked, and *shall* refuse an estimate in hours or days as an input. [T-15]
2. *when* the intake classifier judges a request larger than its worth, the system *shall* answer in scope terms and propose either cutting the scope or splitting the request into stages. [T-15]
   [GAP: the spec does not define who weighs a request's effort against its benefit, or by what measure, at scope negotiation.]

**Case: the two scope moves**

3. *when* the system cuts the scope, the system *shall* take in fewer surfaces than the request named, and *shall* set defaults on what stays plainer than the uncut request would have carried. [T-15]
4. *when* the system splits a request into stages, the system *shall* send each stage through the full pipeline on its own. [INV-12]
5. *when* the system proposes a scope move, the system *shall* proceed on the recommended option and *shall* keep the queue running. [INV-4]

**Case: every cut is reported**

6. *when* the system makes a scope cut, the system *shall* report it in the delivery report's batched section, beside every taken default. [INV-18]
7. The system *shall* surface every scope cut, and *shall* make each one openly. [INV-5]
8. *when* the session makes a taste choice without asking, the system *shall* tell it in the delivery report with plain words, an example, and a default mark. [INV-31]
9. *while* a taste default stands unchanged, the system *shall* take it as accepted. [INV-31]

**Case: the queue order stands**

10. *when* a request carrying the critical mark reaches the queue, the system *shall* move it to the queue head while the queue keeps running. [T-11]
11. *if* a scope cut would change the running order, *then* the system *shall* leave the order unchanged. A scope cut *shall* carry no quick-win mark. [T-11]
12. *when* a request arrives as a file in the inbox, the system *shall* place it in the queue by the moment it is registered as a backlog item, and *shall* leave the file's own modification date out of the ordering. [T-11]

**Case: a returned surface and the regression checks**

13. *if* a cut surface is asked for again later, *then* the system *shall* handle it as a new request.
14. *when* a request touches a surface that already works, the system *shall* open its spec change with regression checks: one sentence per neighbouring promise, each citing the clause it guards. [T-14]
15. *when* the system cuts scope, the system *shall* leave the regression checks unchanged. [T-14]

**Case: what a cut leaves intact**

16. *when* the system cuts scope, the system *shall* leave unchanged every dimension sentence a kept surface already carries. [INV-18]
17. The system *shall* end every dimension of a feature — its phone behaviour, touch, empty, error, and loading states, accessibility, and performance among them — as a written spec sentence: a decided value, or a value tagged as a default and reported. [INV-18]
18. The system *shall* always write the non-goals sentence. A sentence stating that nothing was deliberately left out *shall* be valid. [INV-20]
19. *when* a scope cut narrows the non-goals, the system *shall* report the exclusion in the delivery report's batched section. [INV-20]
20. The system *shall* have every feature state one success measure, decided or tagged as a default. [INV-21]
21. *when* the system cuts scope, the system *shall* adjust only how much ships — fewer surfaces than the request named, defaults plainer than the uncut request would have carried — and *shall* leave the spec change's mandatory sentences intact. [T-15]

---

## Requirement 6: Deriving a settled answer from a proven document

**Context:** Before the pipeline asks the person a design decision, it checks whether a proven document already settles it. A proven document is the architecture, the spec, or the invariants. If one settles the answer, the pipeline derives the answer and cites the section. The pipeline brings the person only the decisions the documents leave open.

**User Story:** As a person, I want the pipeline to derive the answers the documents already settle, so that I am asked only about the choices the documents leave open.

### Acceptance Criteria

**Case: derive before asking**

1. *when* a design choice is about to surface, the system *shall* check whether a proven document — the architecture, the spec, or the invariants — already settles the answer. [INV-121]
2. *if* a proven document settles the answer, *then* the system *shall* derive the requirement, say it back with the section cited, and offer no choice. [INV-121]
3. *when* the documents leave a choice open — a taste call, or a trade-off with no document-grounded winner — the system *shall* bring the choice to the person. [INV-121]

**Case: the pre-ask checks**

4. Before the system asks the person a question, the system *shall* check the question phrase by phrase as a reader without project context would read it, and *shall* treat any phrase that reader could not understand as the finding to fix before asking. [INV-81]
5. Before the system asks the person a question, the system *shall* test whether it can decide the answer itself or verify the answer against a document. *if* it can, *then* the system *shall* do the work and *shall* leave the question unasked. [INV-81]
6. *when* a question survives that test, the system *shall* attach its recommendation. [INV-81]

---

## Requirement 7: One request becomes one story, and a backlog item closes only whole

**Context:** A request can carry more than one user story. At intake, the pipeline splits it into one backlog item per story. A backlog item closes only when every part of its acceptance is met. An open part at compaction is restated in full in the resume file.

**User Story:** As a person, I want each request to become one story per backlog item, and each item to close only when every part is done, so that nothing is fused, dropped, or half-delivered.

### Acceptance Criteria

**Case: one story per backlog item**

1. *when* a request carries more than one user story, the system *shall* split it at intake into one backlog item per story. [T-17]
2. *when* a story has sub-behaviours — a hover view, a phone view, a link from the delivered result back to the request that caused it — the system *shall* fold them into that story's backlog item as its acceptance. [T-17]
3. *if* the number of stories in a request is unclear, *then* the system *shall* ask the person at intake and *shall* refrain from guessing. [INV-12]

**Case: a split loses nothing**

4. The system *shall* treat a stage split as slicing one story's depth. [T-15]
5. The system *shall* keep separate stories in separate backlog items. [T-17]
6. *when* the system splits a request, the system *shall* have every resulting backlog item cite the one request it came from. [INV-1]
7. The system *shall* bring every request to a recorded terminal state, so none is dropped between intake and resolution. [INV-1]

**Case: closing and the movement's end**

8. *when* a backlog item carries more than one part, the system *shall* enumerate per-part acceptance in its close condition. [INV-26]
9. *if* a part is unmet, *then* the system *shall* keep the backlog item open. [INV-26]
10. *while* a part is still open at compaction, the system *shall* restate it in full and *shall* keep it in the resume file. [M-2]
11. *when* a movement ends, the system *shall* replace the resume state, add a dated journal entry, commit the work, trim its own working notes so the session can be wiped or resumed with nothing lost, and say so. [M-2]
