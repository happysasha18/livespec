# The build loop — doors, specifying a feature, and parallel lanes

This section states the second half of throwing a wish inside the build loop: how a wish is sorted at intake into one door and one work-kind and read for its footprint, how a feature-doored wish is specified and proven, and how one session rolls several build lanes at once under one pen. It is written for a reader who has never seen the pipeline before.

Bracket codes like `[INV-133]` and `[T-12]` point to the rule's home in the project spec. The letter before the number names the kind: `INV-` an invariant, `E-` an entity, `T-` a transition, `M-` a rhythm rule, `A-` an adoption step, `ACT-` an actor, and `C-` a composition-axis rule. A reader can ignore the anchors; a maintainer follows them. The keywords *when*, *while*, *if*, *then*, and *shall* are set in lowercase italics and carry their standard requirements meaning: *shall* states a duty, *when* and *while* open a situation, *if* and *then* open a condition and its result.

Terms already defined in the intake glossary and the earlier sections carry their meanings unchanged and are not redefined here: request, inbox, pipeline, spec, architecture, invariant, guardrail, suite, host, pack, harness, session, journal, attic, backlog item, queue, movement, delivery, delivery report, footprint, project layers, settings ladder, personal profile, profile, resume file, migration chapter, ratchet manifest, pen, far tier, capture echo, net, seat, earned message, test matrix. The block below adds only the new nouns this section needs. The nouns prototype, the labelled sketch it names, and its one-way fence are owned by the prototype stretch of this build loop and defined there; the regression fence defined below and the concurrent-edit fence — the check that blocks a shared write when the repository has moved under the session since its last read, defined in the rules section of this document — are two further mechanisms carrying the same word fence. The batched report — the periodic decision page that carries the person's open questions and the pending recommendations together, at most a few per pass — and the surface list — the host-authored file naming every user-facing surface the product carries — are defined in their own sections and carried here. The noun wish — one request a person voices, of any size, captured as a queue row and carried to a recorded terminal state — is owned by the intake stretch of this build loop and defined there.

## Glossary additions

- **door** — the intake classification that places a queued wish at one entry point of the pipeline, one of feature, bug, refactor, docs-only, or skip, decided before any code is written. A request that never becomes a queued wish — an ask merely to see or try a thing — takes a separate entry lane, the labelled-sketch door, held outside this five-way set.
- **tripwire** — one fixed mechanical rule in the door step that lifts a wish to a door whatever its casual label.
- **work-kind** — the intake axis naming what a wish produces, one of product, infra, skill, or prose, which scales how much machinery each pipeline step spends.
- **map note** — the row field, written `map:`, that records the intake verdict of how a wish maps onto the product: changes feature X, new feature, or restructure.
- **spec-delta** — the set of spec sentences one feature's specification adds or changes.
- **standard facet** — one dimension every visible feature has whether or not anyone names it, such as a viewport band, touch, or an empty state, swept when a feature is specified.
- **regression fence** — one sentence stating that a neighbouring promise stays true through a change, citing the existing clause it guards.
- **fit walk** — the intake interrogation of how a feature sits in the person's path, scaled to the wish's kind.
- **prover** — the review pass that reads a spec for holes, reasoning in entities, states, transitions, and invariants.
- **design review** — the pass that reads a proven spec and judges its design, grouping the elements a person acts on and checking each group for behaviour parity.
- **lens** — one standing question the prover or the design review runs by construction over a spec.
- **defect** — a prover finding where a stated invariant is violated, a spec claim is false, or a required invariant is missing; it blocks the design until it is folded.
- **recommendation** — a prover finding where nothing stated is broken and nothing required is missing; it queues for a taste call and does not block.
- **confidence read** — a design review finding's label of one of two values, confident or likely, saying whether the deciding fact lives in the spec text or in the person's intent.
- **declared-laws home** — the one place the spec lists its cross-cutting laws, each carrying its per-surface clause or dated exemption and the net that enforces it.
- **watch-level** — a law's status when the design review is its named net: the law is watched and recommended rather than blocked, until the author's own declaration moves it to a blocking net.
- **milestone gate** — the whole-spec pass that re-proves the spec and the architecture, runs the design review, and completes the full gate list.
- **catch-up walk** — the adoption procedure that brings an already-adopted project's documents and records up to the pack's current state.
- **cross-link mode** — the prover's focused pass at a surface add, scoped to the new surface's seams, carrying one mandatory whole-document step: it sweeps the document for enumerations and universal quantifiers and re-verifies each against the surface set including the newcomer.
- **lane** — one build train a session rolls through the pipeline.
- **lane branch** — a lane's isolated copy, a git worktree holding a branch named for its queue row.
- **pen-stage** — one span in which a lane holds the pen for one indivisible piece of shared-truth work, from taking the pen to its landing, never cut mid-edit.
- **seat** — the one acting orchestrator that judges lane independence; the source also calls this actor the senior, the senior agent, and the orchestrator, and this section keeps the one name seat throughout.
- **departures board** — the status-report view, read live off the queue's open rows at report time, that names every rolling train's station and the row a waiting lane sits behind; no separate file is kept for it.
- **non-goal** — the sentence a feature's spec-delta writes for what it deliberately leaves out.
- **success measure** — the sentence a feature's spec-delta writes for how the feature's working would be noticed for its person.

---

## Requirement 1: A critical bug heads the queue, and priority is recorded

**Context:** Priority changes the queue order, and the change is written into the row. A critical bug lands before everything, heading even the waiting-bug line. Preemption of an in-work lane belongs to the bug door alone.

**User Story:** As a person with an urgent defect, I want a critical bug to head the queue and the reordering recorded, so that the most urgent work runs first and the reason is answerable from the row.

### Acceptance Criteria

**Case: critical priority heads the queue**

1. *when* a bug is marked critical, the system *shall* place it at the head of the queue ahead of the waiting-bug line, and *shall* let only the bug door preempt the in-work lane. [T-9]
2. *when* a critical mark raises a wish's priority, the system *shall* record the change in the wish's row, so the reordering is answerable from the record. [T-9]

---

## Requirement 2: A critical mark on a non-bug heads the queue but never stops the rolling lane

**Context:** Critical priority on a non-bug door sends the wish to the head of the queue while the rolling lane keeps running. A live break that must stop the work now is a bug, which takes the pen at the end of the current pen-stage. The two are different promises, so the bound is echoed back at intake and the human can re-door the wish a bug.

**User Story:** As a person who marks a non-bug critical, I want the wish to head the queue while the lane keeps running and the bound spoken back at intake, so that I hear the difference and can re-door it a bug if I meant a live break.

### Acceptance Criteria

**Case: the bound the non-bug critical buys**

1. *when* a wish is marked critical on a non-bug door, the system *shall* head the queue with it and *shall* admit it at the pen-holder's next pen-stage boundary without interrupting the rolling lane, since preemption belongs to the bug door alone. [INV-133]
2. *when* a wish is marked critical on a non-bug door, the system *shall* say in the capture echo that it heads the queue, does not stop the lane, and that only the bug door preempts, so the person can re-door it a bug. [INV-133]
3. The system *shall* keep priority the human's own to set, stating what critical buys on each door and never refusing the mark. [INV-133]

---

## Requirement 3: A small wish may be promoted, and arrivals order by registration

**Context:** Priority is the one thing that reorders the lane, and it does so visibly. A small queued wish may be taken ahead of larger ones when the lane frees, with the promotion marked in its row. A wish is registered at the moment it arrives, and that registration order settles ties.

**User Story:** As a person throwing wishes of many sizes, I want a small wish promotable with the promotion recorded and arrivals ordered by registration, so that quick work can jump ahead visibly while a stream of small wishes cannot starve a big one.

### Acceptance Criteria

**Case: the recorded promotion**

1. *when* the lane frees, the system *shall* let the agent take a small queued wish ahead of a larger queued wish, marking the promotion in the row rather than making it in silence. [T-11]
   [GAP: the source lets a small wish be promoted ahead of larger queued wishes but names no size boundary or measure separating a promotable wish from a larger one; the agent judges with no stated threshold.]
2. *when* one promoted wish lands, the system *shall* run the queue head next, so a stream of small wishes cannot starve a big wish. [T-11]

**Case: registration order settles arrivals**

3. *when* an inbox wish arrives, the system *shall* register it at the moment of arrival and *shall* let no file's own date compete with a spoken timestamp. [T-11]
4. *when* two arrivals tie, the system *shall* resolve the tie by queue row order top to bottom, and *shall* register an inbox batch swept in one pass in filename-sorted order. [T-11]

---

## Requirement 4: Every wish is classified into one door before any code

**Context:** The door says where a wish enters the pipeline: feature, bug, refactor, docs-only, or skip. Classification is an explicit step with fixed rules, decided before any code is written, and personal judgment does not settle it. A row carries three axes stated together in one intake line: size, priority, and door. A wish too big for its worth is renegotiated in scope, never in time.

**User Story:** As a person throwing a wish however casually, I want it sorted into one door by a fixed ordered procedure, so that what counts as a feature is decided by the rule, whatever words the request used.

### Acceptance Criteria

**Case: the intake line and the door set**

1. *when* a wish is captured, the system *shall* state its size, priority, and door together in one intake line, and *shall* renegotiate a wish too big for its worth in scope rather than in time. [T-12, T-15]
   [GAP: the judge and measure of a wish's effort against its worth are unstated in the source.]
2. The system *shall* draw the door from the closed set of five — feature, bug, refactor, docs-only, and skip — naming it before any code is written. [T-12]

**Case: the ordered procedure**

3. *when* the door step runs, the system *shall* call a wish a feature *if* any tripwire holds — a new user-visible surface appears, new persistent state appears, a new interaction lands on an existing surface, the touched surface is marked a later surface in the spec — it carries the `[target]` planned-feature mark on its own line, its building row still open, or the change adds behaviour no spec clause backs. [T-12, INV-16]
4. *if* no tripwire fired but shipped behaviour is wrong against what the spec or product already promises, *then* the system *shall* call the wish a bug. [T-12]
5. *if* behaviour stays identical while structure moves, *then* the system *shall* call the wish a refactor, and *if* only prose outside the normative spec changes, *then* the system *shall* call it docs-only, routing a reworded spec rule as feature or bug instead. [T-12]
6. *if* a single file changes with no new state, element, or visible behaviour and an existing test level already covers the touched fact, *then* the system *shall* call the wish a skip. [T-12]
7. *when* a casual label conflicts with a fired tripwire, the system *shall* let the tripwire verdict outrank the label, re-door the wish, and record the re-door in the intake line. [INV-16, INV-5]

---

## Requirement 5: A re-doored wish gets no preemption, and the door is re-checked mid-work

**Context:** Queue-cutting belongs only to the bug door, so a wish re-doored to feature gets no preemption. The door is also re-checked mid-work: the moment running work is about to create a surface or state its current door does not grant, the work stops and the door step fires again. A mid-work re-door that creates a surface or state re-runs the independence edges between the parallel lanes.

**User Story:** As a person whose wish turns out to be a feature mid-work, I want it re-doored in place without preemption and the lane independence re-checked, so that a change that grows a surface is caught and the departures board never asserts a stale independence.

### Acceptance Criteria

**Case: no preemption, re-entry in place**

1. The system *shall* give a re-doored wish no queue-cutting, letting the human raise its priority while no word lets a feature skip the spec step. [INV-16]
2. *when* running work is about to create a user-visible surface or persistent state its current door does not grant, the system *shall* stop the work, fire the door step again, keep the lane, and re-enter the pipeline in place with no re-queue and no parking. [INV-16]

**Case: the re-door rebuilds the independence graph**

3. *when* a mid-work re-door creates a surface or state that did not exist when the lanes were opened, the system *shall* re-run the independence edges against every rolling lane. [INV-131]
4. *when* a new edge appears, the system *shall* pull the re-doored lane back to serial behind the lane it now shares a surface with and *shall* say so on the departures board, so the board never asserts a stale independence after the ground moved. [INV-131]

---

## Requirement 6: A fix touching a spec-backed literal owes its docs and test the same session

**Context:** The bug door and the skip door carry one added tripwire, fired by the door step before any code: does this edit touch a spec-backed literal or clause — a version string, a pinned count, a named vocabulary, a promised wording? The tripwire reads the edit's content, so a one-word change to a spec-cited literal owes the same duty as a full feature.

**User Story:** As a person making a one-line fix to a spec-backed literal, I want its docs and test to land in the same session, so that the size of the diff grants no exemption from the duty a full feature owes.

### Acceptance Criteria

**Case: the literal tripwire binds the same-session duty**

1. *when* the door step reads that an edit touches a spec-backed literal or clause, the system *shall* land the documentation update and the red-first test in the same session as the fix. [INV-104]
2. The system *shall* read the edit's content for the tripwire, so a one-word change to a spec-cited literal owes the same duty as a full feature whatever the size of the diff. [INV-104]

---

## Requirement 7: Every request enters through a three-source impact read, and the footprint decides the route

**Context:** Beside the door and the work-kind, a third dimension is read at the same intake moment: the footprint, read from three sources at once. The spec says what behaviour changes, the architecture says which module owns it, and the code says what actually gets touched. The read produces one named footprint that sizes how far each step reaches, and it re-classifies mid-work when an edit reaches past its named layer.

**User Story:** As a person handing over a request, I want its footprint read from spec, architecture, and code and written in the row, so that a wrong route is catchable after the fact and the change spends effort matched to its reach.

### Acceptance Criteria

**Case: the read names one footprint**

1. *when* a request is captured, the system *shall* read its footprint from the spec, the architecture, and the code at one intake moment and *shall* name one footprint — presentation-only, single-module, or cross-cutting. [INV-128]
2. *when* the footprint is named, the system *shall* speak it in the capture echo and write it in the row's footprint note beside the door, kind, and map notes. [INV-128, INV-43, INV-108]

**Case: the footprint composes with the door**

3. The system *shall* let the door decide which steps run and the footprint decide how far each step reaches, and *shall* never let the footprint promote a feature past the spec step nor demote the door's verdict. [INV-128, INV-16]
4. *when* the footprint is cross-cutting, the system *shall* open the full pipeline from the spec step across every layer the change moves; *when* it is single-module, the system *shall* scope the steps the door grants to the one owned module; *when* it is presentation-only, the system *shall* take the lightest road the door already grants. [INV-128]

**Case: disagreement is routed to its owning home**

5. *when* the three sources disagree, the system *shall* name the disagreement and route it to the home that owns it — a bug row for code past spec, a spec fix for a moved pin, a restructure row for a missing node — rather than pick a winner in silence. [INV-128, INV-37]
6. The system *shall* let the three-source read tell whether a proven artifact already settles a question, so the only fork the human hears is what the three sources leave open. [INV-128, INV-121]

**Case: the footprint re-classifies mid-work**

7. *when* an edit reaches past its named layer, the system *shall* stop the work, read the footprint again, and record in the delivery report the footprint held or re-classified to a named footprint at a named step. [INV-128]
8. The system *shall* read repeated cross-cuts on the same module pair as the signal to move a boundary, moving it only through the architecture step and its re-prove on the recorded-footprint evidence. [INV-128, INV-37]

---

## Requirement 8: A landed feature-or-refactor row carries its footprint note, held by a suite check

**Context:** The footprint the intake read named is written in the landing row's footprint note. A suite check reads the queue and reddens a landed feature-or-refactor row that carries no footprint note, the mechanical floor under the footprint read.

**User Story:** As a person trusting the routing record, I want a landed feature-or-refactor row's footprint note held by a suite check, so that a landed row never silently drops the note.

### Acceptance Criteria

**Case: the note and its check**

1. The system *shall* write the intake read's footprint — presentation-only, single-module, or cross-cutting — in the landing row's footprint note beside the door, kind, and map notes. [INV-134, INV-128]
2. *when* the suite check reads the queue, the system *shall* red a landed feature-or-refactor row that carries no footprint note, the same shape the delegation-accounting check gives the routing rule. [INV-134, INV-103]

**Case: the duty binds forward**

3. The system *shall* require the footprint note only on a feature-or-refactor row landed once the impact-analysis station was law, leaving rows that landed before it as they landed. [INV-134, INV-159]

---

## Requirement 9: A request enters at the highest document it reaches, and the door set is closed

**Context:** A request enters the pipeline at the highest document in the derivation chain — spec, then architecture, then test matrix, then code, then docs — whose sentences must change for the request to be satisfied. The set of entry points is closed on purpose, so a request that matches no kind becomes one plain question, its route named by the human.

**User Story:** As a person handing over a request of any shape, I want it entered at the highest document its change reaches with the door set closed, so that no gap opens between the layers and an unmatched request becomes a plain question.

### Acceptance Criteria

**Case: the entry test**

1. *when* a request is captured, the system *shall* enter it at the highest document whose sentences must change to satisfy it, testing each document from the top by whether any sentence would read differently once the request is done. [INV-151]
2. *when* a technically-phrased request trips a surface, state, or unbacked-behaviour tripwire, the system *shall* lift it to the spec at the door rather than after the architecture work is built on an unlifted premise. [INV-151, INV-16]

**Case: the closed set of entry points**

3. The system *shall* route each request-kind to its own entry — a product-behaviour request to the spec, a defect to the test matrix with a red-on-bug test, a docs-only change to its light path, a tiny reversible edit to the skip shortcut still owing the spec-backed-literal tripwire, a settings value to the settings ladder, an outside request through the inbox as one wish, an ask to see or try a thing through the labelled-sketch door, and a thing handed back through feedback-intake. [INV-151, INV-104, INV-17, T-20]
4. *if* a request matches no kind in the closed set, *then* the system *shall* make it one plain question to the human, its route settled by the answer, and *shall* treat a held backlog item that cannot say why it belongs to the human as the same shape of finding. [INV-151, INV-4, INV-152]

---

## Requirement 10: When the product and the spec diverge, the spec is the definition of correct

**Context:** A divergence between the product and the spec defaults to a possible error in the product, checked against the spec. The divergence is first named and routed to the home that owns it. Changing a spec that is confirmed the error is a decision the human's word settles, and the spec is never silently rewritten to match the product.

**User Story:** As a person whose product and spec have drifted apart, I want the spec held as the definition of correct and any change to it made a decision, so that a wrong product is fixed while the spec is never quietly rewritten.

### Acceptance Criteria

**Case: the divergence is named and routed**

1. *when* the product and the spec diverge, the system *shall* first name what the spec states, what the product does, and why they differ, and route the divergence to the home that owns it. [INV-144, INV-37]
2. *when* the product is wrong against the spec, the system *shall* fix the product to the spec. [INV-144, INV-124]

**Case: completing a silent spec, changing a confirmed-wrong spec**

3. *when* the spec is silent where the product is correct, the system *shall* complete the spec to state the guarantee, pin it with a test, and report the completion as a default on the ordinary spec-delta road, and *when* what counts as correct is itself genuinely open, the question goes to the person, whose word alone settles it. [INV-144, INV-18, INV-31]
4. *when* the spec conflicts with a correct product, the system *shall* change the spec only *when* the spec is confirmed the error and the human has understood the divergence and confirmed the change, and *shall* never silently rewrite the spec to match the product. [INV-144, INV-9, INV-4]

---

## Requirement 11: The intake line names the work-kind

**Context:** The intake line also names what is being built. The work-kind says what kind of thing the work produces and which pipeline machinery is warranted, drawn from four kinds: product, infra, skill, and prose. The classifier calls the kind from what the wish produces, one kind per wish.

**User Story:** As a person throwing a wish, I want its work-kind named at intake, so that each pipeline step spends machinery matched to what the work produces.

### Acceptance Criteria

**Case: one kind per wish**

1. *when* a wish is captured, the system *shall* name its work-kind — product, infra, skill, or prose — from what the wish produces, one kind per wish. [T-16]
2. *when* a wish genuinely produces two kinds, the system *shall* split it into two wishes at intake, and *when* the classifier cannot call the kind, *shall* ask the human the same as an uncallable size. [T-16, INV-12]

**Case: the host default and the curated vocabulary**

3. *when* a host has one usual kind, the system *shall* let the host record it as a host-profile default the intake line starts from, and *when* a host's wishes span kinds, *shall* record no default and call each wish on its own. [T-16, E-8, E-13]
4. The system *shall* curate the kind vocabulary by real routed work, admitting a fifth kind only with a named wish the four failed to serve and re-justifying the set at milestones. [T-16]
5. The system *shall* require no retroactive kind on a row queued before the kind axis existed, letting it name its kind the moment it next moves. [T-16, INV-159]

---

## Requirement 12: A duty binds forward from the first landing after its clause exists

**Context:** A rule this project adopts governs from the first landing that touches its surface once the rule is law, and what already landed stays as it landed. A backlog item queued before the clause carries the rule the moment it next moves, and a project that predates the clause brings the rule up as an owned landing. This is the one statement of the forward-binding convention every such duty cites.

**User Story:** As a person adopting a new rule, I want it to bind forward from the first landing that touches its surface and never reach back over what already landed, so that existing work is not retroactively judged and every binds-forward citation has one home.

### Acceptance Criteria

**Case: the forward-binding convention**

1. *when* a rule becomes law, the system *shall* govern from the first landing that touches its surface and *shall* leave what already landed as it landed. [INV-159]
2. *when* a backlog item was queued before the clause, the system *shall* owe no retroactive backfill, letting the item carry the rule the moment it next moves, and *shall* bring the rule up as an owned landing on a project that predates the clause. [INV-159]

**Case: the citation net**

3. The system *shall* have each duty that binds forward — the work-kind axis, the success-measure and lens-sweep duties, the spec-and-architecture pair and its quality budgets, the runtime and placement views, and each self-enforcing landing rule — cite this one law rather than restate it. [INV-159, T-16, INV-15, INV-41, INV-74, INV-75]
4. *when* a clause states that a duty binds forward and cites no root, the system *shall* make the bare citation the finding a standing net catches, the same enforced membership the suite-honesty class carries. [INV-159, INV-160, INV-163, A-3]

---

## Requirement 13: A skill-kind wish's verify walks the skill-creator review

**Context:** When the classifier names the work-kind skill — a pack skill created or edited — the verify step additionally runs the installed skill-creator's review of the touched skill: its craft and its evals where applicable. The classifier is the trigger, and the walk fires on every skill-kind landing.

**User Story:** As a person shipping a skill change, I want its verify to walk the skill-creator review, so that a regression in a skill every session reads is caught before it lands.

### Acceptance Criteria

**Case: the walk fires on every skill-kind landing**

1. *when* the classifier names the work-kind skill, the system *shall* run the installed skill-creator's review of the touched skill at the verify step, folding or rejecting each finding by name in the landing record. [INV-99]
2. The system *shall* fire the walk on every skill-kind landing from the classifier alone, and *shall* leave skills that landed before this law to the milestone gate's whole-pack walk. [INV-99, M-1]

---

## Requirement 14: The kind scales the steps and never silently skips one

**Context:** The door picks which steps run; the kind picks the form each running step takes, never whether the pipeline runs at all. At landing, every pipeline step has either applied in the form the kind's table states or stood down by name in the delivery report, so a skipped step is a written fact.

**User Story:** As a person shipping a change of any kind, I want the kind to scale each step's form while every step applies or stands down by name, so that a small change spends proportionate effort and no mandatory check is silently dropped.

### Acceptance Criteria

**Case: the kind adjusts form, never presence**

1. The system *shall* let the door pick which steps run and the kind pick the form each running step takes, never letting the kind decide whether the pipeline runs. [INV-22, T-12]
2. *when* a wish lands, the system *shall* have every pipeline step either applied in the form the kind's table states or stood down by name in the delivery report. [INV-22, E-12]
3. *while* the kind question stays open on a row, the system *shall* apply every step in full, since standing a step down requires a named kind to account for it. [INV-22, INV-12]

**Case: the checks no kind may change**

4. The system *shall* let no kind change the door law and its tripwires, the delta's mandatory sentences the scope-cut law names (the law, stated in the intake stretch of this build loop, that a scope cut spares the regression fences, a kept surface's facets, the non-goals, and the success measure), or ask-at-intake. [INV-22, T-12, INV-16]

---

## Requirement 15: Each step is worked with its craft's standards

**Context:** A single generalist working the whole pipeline produces generalist artifacts. Each step therefore names the profession the agent works it as, and each artifact is judged by that craft's standards. The craft, like the step's form, follows the kind.

**User Story:** As a person relying on each artifact, I want each step worked with its own craft's standards, so that a spec reads like a product manager's and a test matrix like a quality-assurance engineer's rather than one generalist's notes.

### Acceptance Criteria

**Case: each step names its craft**

1. The system *shall* work the spec as a strong product manager, the architecture as a software architect, the test matrix and tests as a quality-assurance automation engineer, the code as a senior developer, the two prove steps as the prover's formal-reviewer role, commit-and-show as a careful release engineer, and the verify walk as the visitor's own outside eyes. [INV-33, E-12]
2. The system *shall* judge each artifact by its craft's standards and speak the delivery report's step accounting in them. [INV-33]

**Case: the craft follows the kind**

3. The system *shall* let the wish's kind say what each craft's standards look like in its medium, working the code step as a strong writer on a prose product and as a tool builder on infra. [INV-33, INV-22, INV-30]

---

## Requirement 16: A feature is specified past what the human knows to ask

**Context:** The human says add a room where photos hang; the human does not say and decide what happens on a phone, because the human cannot know that is a question. So a feature-doored wish's spec-delta walks a fixed sweep of the standard facets — the dimensions every visible feature has whether or not anyone names them. The facet list has one home in the spec-author skill, and the inline list is its reader's echo.

**User Story:** As a person asking for a feature in plain words, I want its spec-delta to sweep the standard facets, so that the questions I did not know to ask — the phone layout, touch, the empty state — are each decided before the feature ships.

### Acceptance Criteria

**Case: the sweep runs the facet set**

1. *when* a wish's door says feature, the system *shall* walk its spec-delta through the standard facets — the viewport width and height bands, touch where the design assumed a mouse, the empty and error and loading states of each new surface, keyboard reach and readable contrast, the performance envelope, visual hierarchy, two windows at once, and a missing source. [T-13, INV-138]
2. The system *shall* end a layout-bearing feature's sweep with a decided or defaulted sentence per viewport band its layout law names or excludes, letting a law scoped to one band answer for the others. [T-13, INV-138]

**Case: the sweep's scope and the curated list**

3. The system *shall* scope the sweep to the feature's visible surfaces, satisfying a feature with none by one explicit sentence that no visible surface exists and the facets do not apply, never a silent skip. [T-13]
4. *when* a wish is re-doored to feature mid-work, the system *shall* walk the sweep before work resumes, and *shall* not sweep a fenced prototype, firing the sweep only when promotion makes it a feature. [T-13, INV-16, E-17]
5. The system *shall* keep the facet list in the spec-author skill as one closed enumerable set that grows a member only with a named real incident it would have caught, re-justified at milestones, naming every facet on its own line rather than letting any facet ride unnamed inside another's. [T-13, INV-226]

---

## Requirement 17: Every facet ends as a spec sentence

**Context:** A facet sentence is written one of two ways: decided, when the human or the walk's batched questions called it, or defaulted, when the recommended option is taken so the lane keeps moving. A defaulted sentence carries the literal tag `[default]` at its line end, and a facet with no sentence at all is a spec defect the prover flags.

**User Story:** As a person whose feature has many facets, I want each one written decided or defaulted rather than left silent, so that a later prover can tell a taken default from a hole and no facet ships as an unasked question.

### Acceptance Criteria

**Case: decided or defaulted, never silent**

1. The system *shall* write each facet as a decided sentence or a defaulted sentence tagged `[default]` at its line end, deriving the facet's test row either way. [INV-18, E-15]
2. The system *shall* never ask the human to confirm a default and never ping once per facet, since silence is consent and the human's veto becomes a new wish. [INV-18, INV-31]
3. *when* a facet has neither a decided nor a defaulted sentence, the system *shall* have the prover flag it a spec defect. [INV-18]

**Case: defaults on a live surface, and the split by time**

4. *when* a surface already lives, the system *shall* read a default from the shipped truth and reconcile it like any re-engineered claim, never inventing it against live behaviour. [INV-18, A-10, A-3]
5. The system *shall* let the facet sweep author the facet sentences when the feature is first specified and let the axis rule compose and test them across views once the surface exists. [INV-18, C-1]

---

## Requirement 18: The spec names its cross-cutting laws in one place, and every section answers them

**Context:** A product declares laws that cut across every surface — measurement, accessibility, error handling, a register of speech. The spec keeps that list in one declared-laws home, and each new surface's section states its line against each declared law before the prover reads it. Each declared law also names the net that enforces it.

**User Story:** As a person guarding a product-wide law, I want the laws listed in one home with each surface answering each and each law naming its net, so that a missing clause or a missing net ranks as a broken invariant.

### Acceptance Criteria

**Case: the declared-laws home and the per-surface answer**

1. The system *shall* keep the cross-cutting laws in one declared-laws home and *shall* have each new surface's section state its clause or a dated exemption against each declared law before the prover reads it. [INV-101]
2. The system *shall* have the prover's station enumerate every surface and transition per declared law and demand the clause or the dated exemption per item, ranking a missing clause a broken invariant. [INV-101]

**Case: this pack's declared laws and their nets**

3. The system *shall* declare this pack's three laws — the plain-language register on every human-facing surface, clock-honest stamps on every dated line, and no self-certification on any claim of done — each naming its mechanical gate. [INV-101, INV-28, INV-34, INV-83, INV-24, INV-94]
4. *when* a declared law names no net, the system *shall* rank the missing net a broken invariant, the same rank as a missing per-surface clause. [INV-101]

---

## Requirement 19: Every declared law names its enforcing net, and declaration moves a property to a blocking net

**Context:** A law that cuts across surfaces is enforced by one of three nets, and the law names which: a mechanical gate where a deterministic check can decide the violation, the prover's judgment station where the violation pins to a stated sentence, or the design review's recommendation where the deciding fact lives only in the person's intent. Declaration is the lever that moves a property between the nets.

**User Story:** As a person deciding how a law is enforced, I want each law to name one of three nets by where its violation can be decided, so that declaring a property promotes it from a soft recommendation to a blocking net with no property owned by two nets at once.

### Acceptance Criteria

**Case: the three nets and where each law belongs**

1. The system *shall* assign a law to a mechanical gate *when* a deterministic check can decide the violation, to the prover *when* the violation pins to a stated sentence, and to the design review *when* the deciding fact lives only in the person's intent. [INV-150, INV-125]
2. The system *shall* record each law's net beside it in the declared-laws home and *shall* rank a law with no named net a broken invariant. [INV-150, INV-101]
3. *when* a law is held at watch-level, the system *shall* name the design review as its net with a dated reason, so a watch-level choice reads as a deliberate decision. [INV-150]

**Case: declaration promotes and blocks**

4. *when* the author declares a grouping, a facet, or a law in the declared-laws home, the system *shall* move the property from the design review to the prover or a mechanical gate and start blocking on it, keeping the architecture's one-owner check as the backstop. [INV-150, INV-141]

---

## Requirement 20: Every incoming thing routes to the home whose declared sentence governs it

**Context:** The request classifier, the property net, the deferral test, and the earned message are one principle stated four times: every incoming thing routes to the home whose declared sentence governs it, and a thing that pins to no home is itself the finding. The four stay separate controls under the one principle because they run at different moments under different verifiers.

**User Story:** As a person handing the pack many kinds of thing, I want each routed to the home whose declared sentence governs it and a homeless thing made the finding, so that nothing is homeless by silence and declaration is the one lever across all four controls.

### Acceptance Criteria

**Case: each thing routes to its governing home**

1. The system *shall* route a request to the highest document whose sentences it changes, a property to the net that can pin its violation to a stated sentence, a backlog item to the seat unless it names a fact only the human holds, and a question to the sender's own blocked work. [INV-153, INV-151, INV-150, INV-152, INV-189]
2. *when* a thing pins to no home, the system *shall* make the thing itself the finding — an unmatched request a plain question, a netless declared law a broken invariant, a held backlog item defaulting to the seat, and a groundless question dropped with the holding named. [INV-153, INV-4, INV-101, INV-143, INV-191]

**Case: declaration is the lever, verified adjacent to each thing**

3. The system *shall* let declaration promote a property to a blockable check, a door or tripwire to a mechanical route, and named blocked work to a gate-readable message. [INV-153, INV-150]
4. The system *shall* verify each control adjacent to the thing it audits — the classifier by the landing's applied-or-stood-down contract, the property net by the declared-laws station, the deferral test by the seat's derive-before-defer posture, and the earned message by the receiving sweep's gate. [INV-153, INV-22, INV-101]

---

## Requirement 21: A feature is interrogated for how it fits the product

**Context:** The device facets ask what every visible feature owes; nobody has yet asked how this feature sits in the person's path. Path holes ship green because no clause ever promised the way out. So a feature-doored wish's spec-delta also walks the fit walk, scaled to the wish's kind, and the prover gains the matching focused mode, feature-fit.

**User Story:** As a person adding a feature, I want its spec-delta walked for how the person arrives, acts, and moves on, so that a path hole with no way out is caught at intake, before it ever ships green.

### Acceptance Criteria

**Case: the fit walk, scaled to the kind**

1. *when* a wish enters the feature door, the system *shall* walk its spec-delta through the fit walk scaled to its kind — a product wish through the visitor's journey, an infra wish through its flows, a skill wish through trigger, correction, and when not to fire. [INV-29]
2. The system *shall* interrogate the feature and not the person, deriving each answer from the existing spec and the shipped truth first. [INV-29]

**Case: holes closed, defaulted, or asked**

3. *when* a hole is trivially closable — its answer pins to an existing artifact: a base rule, a spec sentence, the architecture, or an already-answered decision — the system *shall* close it and write the closing down, writing the rest decided or `[default]`-tagged and sending only genuine taste calls out in a batch. [INV-29, INV-4, INV-18]
4. The system *shall* give the prover the feature-fit mode that walks the journey seams against the whole spec, and *shall* owe a landed feature its walk at the first landing that touches it rather than retroactively. [INV-29, INV-159]

---

## Requirement 22: A face that can be entered once owes a way back or a written one-way

**Context:** A surface's faces get entered under conditions — a first-visit door, an empty state, an onboarding screen, a one-time banner. A face whose condition can never re-arise is a dead end the state lenses miss. Trigger wording is the tell: only on first visit, only on first run, until dismissed.

**User Story:** As a person who can leave and re-enter a surface, I want every conditionally-entered face to state its re-entry path or name its one-way, so that a face reachable again always says how it is reached.

### Acceptance Criteria

**Case: the return sentence or the written one-way**

1. The system *shall* have every conditionally-entered face state its deliberate re-entry path or state the one-way as a decision by name. [INV-50]
2. *when* a face carries trigger wording such as only on first visit or until dismissed, the system *shall* owe that clause its return sentence and have the prover read for it through the entry-symmetry lens. [INV-50, INV-29]

---

## Requirement 23: Verify-by-deed walks the visit and judges the feel

**Context:** For the product kind, the verify step includes a named visitor walk: the whole journey as the person will live it. The agent walks the first visit, the return visit, entry through another door, where am I and how do I move on from any point, and the exits. The agent also runs a feel pass against the approved prototype as the bar, in the form the medium actually has.

**User Story:** As a person shipping a product feature, I want verify to walk the visit and judge the feel against the prototype, so that shipped work is checked the way a person actually lives it and findings become rows or red rather than a mental note.

### Acceptance Criteria

**Case: the visitor walk and the feel pass**

1. *when* the verify step runs on a product-kind wish, the system *shall* walk the first visit, the return visit, entry through another door, where the person is and how they move on from any point, and the exits. [INV-30]
2. *when* the feel pass runs, the system *shall* judge motion quality and each affordance's craft against the approved prototype as the bar, turning findings into rows or red. [INV-30, E-17]

**Case: the walk runs in the medium's own form**

3. The system *shall* run the walk in the form the medium has — motion and affordance for a browser, reading path and chapter flow for a book, the command round-trip for a command-line tool — reading its checklist from the build-pipeline product cell. [INV-30, E-12, INV-22]

---

## Requirement 24: The prover labels each finding a defect or a recommendation

**Context:** Every prover finding carries its kind, so the human knows at a glance what the finding asks of them. A defect blocks and the design becomes buildable only once it is folded; a recommendation does not block and queues for a taste call. The kind is derivable from the finding's own ground.

**User Story:** As a person reading prover findings, I want each labelled a defect or a recommendation, so that I sort what blocks from what queues at the point of report rather than by hand.

### Acceptance Criteria

**Case: the two kinds and their verdicts**

1. The system *shall* label a finding a defect *when* it names a violated invariant, a false spec claim, or a missing required invariant, blocking until it is folded. [INV-140]
2. The system *shall* label a finding a recommendation *when* nothing stated is broken and nothing required is missing, queuing it for a taste call with an optional now-or-later grade. [INV-140]

**Case: the gate folds and queues**

3. The system *shall* have the push gate fold every defect and queue every recommendation, deriving the kind from the finding's own ground. [INV-140, M-6]
4. *when* a delta-scoped gate meets a pre-existing defect outside the delta, the system *shall* queue it by that law rather than block the merge it did not create. [INV-140, INV-114]

---

## Requirement 25: A design review reads a proven spec and judges the design behind it

**Context:** After the prover has checked a spec, a separate pass called the design review reads the same spec and judges its design. It builds its own transient inventory of every element a person acts on, writes one plain sentence of what the person does with each, and proposes elements whose sentences match as a same-kind group. Its findings are recommendations or questions and never block a landing.

**User Story:** As a person guarding design consistency, I want a design review to group the elements a person acts on and check each group for behaviour parity, so that same-kind things behave alike and a divergence is brought to me with two concrete objects in hand.

### Acceptance Criteria

**Case: the inventory and the same-kind groups**

1. *when* the prover has checked a spec, the system *shall* have the design review read the same spec, build its own transient inventory of every element a person acts on that a spec sentence names, and write one plain sentence of what the person does with each in the person's own action words, never writing that inventory into the surface list the host authors. [INV-141, E-10]
2. The system *shall* propose elements whose sentences match as a same-kind group, check each group for the same gestures, transitions, and affordances, and stay silent where the grouping or the difference is not plain. [INV-141]

**Case: findings recommend or ask, never block**

3. The system *shall* name two concrete objects with the spec sentence each comes from on every finding, produce no blocking defects, and write a dated record with a per-finding outcome column. [INV-141, INV-140]
4. *when* the human confirms two elements are the same kind, the system *shall* have the spec author write a class sentence the existing checks then hold, and *when* the human says they differ by intent, *shall* write a decided sentence that closes the question. [INV-141, INV-125, INV-59]

**Case: the review runs in the kind's own form**

5. *when* a kind has no element a person acts on, the system *shall* stand the design review down by name in the record rather than run it vacuously, running it in the project kind's own form the way the verify walk and the design principles do and keeping the spec's own declared-class check governing where a class is already declared. [INV-141, INV-22, INV-125, INV-30, INV-136, INV-139]

---

## Requirement 26: A gesture or overlay spec triggers the design review's motion-parity lens

**Context:** The bottom-up similarity lens builds its groups from matching role sentences, so it can miss a same-kind grouping the medium makes obvious. A spec that ships a gesture, a motion, or a layer that opens and closes over another carries a standing lens the design review runs by construction, naming three same-kind groups the text need not have declared.

**User Story:** As a person shipping a gesture or overlay, I want the design review's motion-parity lens run by construction, so that the way out mirrors the way in, every object type behaves alike, and every slot behaves alike before a device ever shows a divergence.

### Acceptance Criteria

**Case: the three same-kind groups**

1. *when* a spec ships a gesture, a motion, or a layer that opens and closes over another, the system *shall* run the motion-parity lens by construction, naming entry-mirrors-exit as the first group so a layer closes by the reverse of the motion that opened it. [INV-165, INV-141]
2. The system *shall* name every object type the gesture acts on as the second group, each kind opening and closing the same way and landing back on its own on-screen rectangle, and every position as the third group, the same gesture on the same type in a different slot behaving the same. [INV-165]

**Case: each finding recommends or asks**

3. The system *shall* make each motion-parity finding a recommendation or a question and never a blocker, holding it by the prover's uniformity check once the human declares the parity a class sentence. [INV-165, INV-125]

---

## Requirement 27: A feature delta adding a second member of a kind draws the scoped design review at intake

**Context:** The moment an undeclared same-kind grouping comes into existence is the intake of its second member: the first member ships alone with no class to belong to, so when a delta adds a sibling the uniformity check has no class clause to hold and the full design review is not due until the next milestone. Feature intake therefore carries one standing question the feature-fit walk asks by construction.

**User Story:** As a person adding a sibling to an existing kind, I want the scoped design review drawn at intake, so that the window where a second sibling ships and diverges before the next full pass is closed.

### Acceptance Criteria

**Case: the second-sibling question**

1. *when* a feature delta adds a second member of a kind an existing surface already has — the same gesture, overlay shape, or one-sentence role — the system *shall* draw the scoped design review over the delta's elements against the existing inventory. [INV-169, INV-141]
2. *when* a delta adds no such sibling, the system *shall* hold the intake stand-down and record the no as a lens verdict in the feature-fit record. [INV-169, INV-29]

**Case: the closed window**

3. The system *shall* close the window a second sibling entered by drawing this pass at intake, the same channel the uniformity lens and the motion-parity lens were born from. [INV-169, INV-125, INV-165]

---

## Requirement 28: A re-enterable surface triggers the prover's entry-state lens

**Context:** The prover reasons in states, transitions, and initialization, so a surface a visitor can leave and re-enter carries a standing lens the prover runs by construction. The entry-symmetry lens tests that a re-entry path exists; this lens tests the state that re-entry opens in.

**User Story:** As a person shipping a re-enterable surface, I want the prover's entry-state lens run by construction, so that a spec pinning the open, exit, and guards while leaving the entry position and reset-or-resume blank raises an open question before code.

### Acceptance Criteria

**Case: the entry state the lens demands**

1. *when* a surface can be left and re-entered, the system *shall* have the prover demand the spec declare where the surface opens focused or positioned and whether entering resets its internal state or resumes the state a prior visit left. [INV-167, INV-1]
2. *when* the spec pins the open ceremony, exit, variants, and guards while the entry position and reset-or-resume semantics stay blank, the system *shall* raise the unstated transition end-state as an open question before any code is written. [INV-167, INV-50]

**Case: the lens hands off once declared**

3. *when* the human declares the entry state a spec sentence, the system *shall* let the prover's ordinary state-coverage hold it. [INV-167, INV-125]

---

## Requirement 29: Every stated transition carries a payload lens

**Context:** The prover verifies the state graph's topology — that a way in, a way out, and a way back exist. Beside topology it reads each transition's payload: the parameters a person perceives across it. A parameter the spec leaves blank is answered by the platform's own default alone, so the payload a transition carries is the hole the topology lenses miss.

**User Story:** As a person specifying a transition, I want each one's perceived payload enumerated and demanded, so that a parameter left to the platform default becomes a finding, surfaced before it can silently become the behaviour.

### Acceptance Criteria

**Case: enumerate and demand each payload parameter**

1. *when* the prover reads a stated transition, the system *shall* enumerate the parameters a person perceives across it — where focus and selection land, what scroll or playback position holds, whether sound continues, whether a timer keeps running, whether a shown value is fresh or stale — and demand the spec name each. [INV-168, INV-72, INV-127]
2. The system *shall* raise each unstated payload parameter as an open question, the author writing it as a spec sentence or the human deciding it where the choice is theirs alone. [INV-168, INV-30]

**Case: the lens generalizes its instances**

3. The system *shall* read the motion-parity lens as this lens on the exit's animation and the entry-state lens as this lens on a re-entry's internal state, both instances this parent generalizes. [INV-168, INV-165, INV-167]

---

## Requirement 30: A surface add re-verifies the document's quantified claims

**Context:** A new surface falsifies existing document-level sentences without touching them: a class clause's member enumeration excludes the newcomer, a sentence quantified over every, only, all, or exactly one ranges over a set that just grew, and a previously terminal scenario's decided edge may no longer be terminal. A seam-scoped pass misses these, so the cross-link mode carries one mandatory whole-document step.

**User Story:** As a person adding a surface or a member, I want the document's quantified claims re-verified against the grown set, so that a sentence the newcomer falsifies is a finding at the add itself, ahead of the next full pass.

### Acceptance Criteria

**Case: the quantifier re-verify**

1. *when* a surface is added, the system *shall* have the cross-link mode sweep the document for enumerations and universal quantifiers — every, only, all, exactly, an explicit member list — and re-verify each such sentence against the surface set including the newcomer. [INV-170, INV-125, INV-127]
2. The system *shall* fire the step on every member add, not only a surface add — a new invariant joining a family, a new skill joining the pack, a second sibling the intake question catches — re-verifying the same way in the full pass's own sweep. [INV-170, INV-169, INV-171]

---

## Requirement 31: A full prover pass owes a coverage record

**Context:** Phase-level prose proves nothing about which lenses actually ran, and on a kind where the classic coverage tables all go not-applicable a skipped lens is indistinguishable from a lens that found nothing. The prover's stress lenses therefore split into two tiers, and each mandatory sweep owes one verdict line.

**User Story:** As a person trusting a full prover pass, I want each mandatory sweep to owe one verdict line rendered as a surface-by-sweep table, so that a missing verdict reads as a skipped sweep, its absence never passing for a clean one.

### Acceptance Criteria

**Case: the mandatory sweeps owe verdicts**

1. The system *shall* have each mandatory sweep — the declared-laws walk, edge-condition completeness, cross-surface uniformity, the lifecycle sweep under the transition-payload parent, and the unwritten-seams derivation — owe one verdict line in the persisted record: hit, clean, or not-applicable with its reason. [INV-171, INV-101, INV-138, INV-125, INV-168, INV-50, INV-167, INV-126, INV-127, INV-72]
2. The system *shall* render the verdicts as a surface-by-sweep table, the replacement for the coverage tables on a kind where those go not-applicable, and leave the imaginative probes — the checks the prover invents for the particular document beyond the mandatory sweeps — discretionary owing no verdict. [INV-171, INV-135, INV-156]
3. *when* a verdict line is missing, the system *shall* read it as a skipped sweep and never as a clean one. [INV-171]

---

## Requirement 32: Every review pass writes its record of one class

**Context:** A review pass — the prover's spec re-check, the design review, the periodic adversarial audit (the fresh-checker read run over a high-stakes delivery, set on refuting its claims and finding its holes; its cadence and rules live in the rules section of this document), and the verify-by-deed audit — records its outcome so a later session reads every pass the same way. Three of them write a dated file of one shared shape under the pass's own home, and the verify-by-deed audit is the one deliberate difference.

**User Story:** As a later session reading past passes, I want each review pass to write its record of one class with a per-finding disposition column, so that the prover, the design review, and the audit read the same way and the verify audit's difference is named.

### Acceptance Criteria

**Case: the shared record shape**

1. The system *shall* have the prover, the design review, and the periodic audit each write a dated file of one shared shape under its own home, naming the skill and version that ran the pass, carrying a per-finding disposition column, and taking a same-day suffix so two passes never overwrite. [INV-156, INV-140, INV-141, INV-145]
2. The system *shall* land a feature-fit record in the prover's own home in this shape, and give the design review alone a held-ask home since it alone carries a question across passes. [INV-156, INV-29, INV-169, INV-142]

**Case: the verify audit's difference, and forward binding**

3. The system *shall* land the verify-by-deed audit's verdict and its per-landing skill-creator review in the landing record, since verify is a per-landing gate and keeps no dated file of this class. [INV-156, INV-46, INV-99]
4. The system *shall* have a new review pass state its record against this class and *shall* leave records written before the class was declared unreshaped. [INV-156, INV-159]

---

## Requirement 33: Every design review finding carries a confidence read, and a strong likely one becomes one question

**Context:** Each design review finding carries a confidence read of confident or likely. A confident finding is written as a recommendation that queues and never blocks; a likely finding is written as one question to the human with both objects in hand, raised only when the signal is strong. At most three such questions ride per pass, strongest first, and an unanswered question is held quietly for the person.

**User Story:** As a person the design review would ask, I want a confident finding queued and a strong likely one raised as one batched question, so that the strongest genuine questions reach me without the lane ever waiting on them.

### Acceptance Criteria

**Case: confident queues, likely asks**

1. The system *shall* write a confident finding as a recommendation that queues and never blocks, a finding being confident *when* the reviewer would defend the grouping and the divergence on the spec text alone. [INV-142, INV-140]
2. The system *shall* write a likely finding as one question to the human with both objects and each object's spec sentence, raised only *when* the shared role fits one plain sentence, the difference is a whole behaviour one member lacks, and no spec sentence already decides it. [INV-142, INV-141]

**Case: the batched channel and the held question**

3. The system *shall* ride these questions on the batched report, at most three per pass strongest first, holding a signal below that bar silent. [INV-142, E-22, INV-4]
4. The system *shall* not apply the recommended default to the spec the pack's usual proceed-on-recommended way, landing the class sentence only on the human's word while the lane never blocks. [INV-142, INV-4, INV-141]
5. *while* a question stands unanswered, the system *shall* hold it on the dated record and not raise it again on its own until the human answers, each pass first reading the open questions and dropping a freshly-derived divergence already carried there. [INV-142, INV-130]

---

## Requirement 34: The prover and the design review iterate to a bounded fixed point

**Context:** The prover and the design review form a loop over repeated rounds. A round is one prover re-read of the changed part of the spec followed by one design-review re-read over the current spec. Only a human-accepted declaration advances the loop, and it is capped at three progressing rounds by default. On reaching the cap the loop surfaces the unsettled groupings without holding the landing.

**User Story:** As a person watching the design settle, I want the prover and design review to iterate to a bounded fixed point and surface non-convergence without holding the landing, so that a design converges in the ordinary case and a live cap keeps the loop from running away.

### Acceptance Criteria

**Case: what advances the loop**

1. The system *shall* advance the loop only on a human-accepted declaration — a class sentence over a grouping or a decided sentence over a difference — re-reading the changed part and the re-partitioned elements in the next round. [INV-154, INV-125, INV-59]
2. The system *shall* not advance the loop on a confident finding queued as a recommendation or a likely finding riding as a question, since neither re-reads the spec on its own. [INV-154, INV-142]

**Case: the loop rests with a named reason**

3. *when* a round produces no new class sentence and no new decided sentence, the system *shall* rest the loop and name why in the record — it converges when the design review left no open question and no new grouping, it waits when a question stands unanswered, and it stands down when no element a person acts on exists. [INV-154, INV-141, INV-142]

**Case: the cap and the surfacing**

4. The system *shall* cap the loop at three progressing rounds by default, let a host set its own cap, and count progressing rounds on the design-review pass alone, resetting when a fresh pass opens. [INV-154]
5. *when* the loop reaches the cap without convergence, the system *shall* surface the unsettled groupings on the dated record with its best reading of the cause, and *shall* let the landing proceed with the unsettled groupings recorded. [INV-154, INV-141]

---

## Requirement 35: A taste choice made without asking is told, never confirmed

**Context:** While building a feature, the walk makes small taste calls itself so the lane keeps moving — an animation's speed, a button's shape, a caption's wording. The agent writes each into the spec with its `[default]` tag, names it in the delivery report, and re-asks nothing later.

**User Story:** As a person whose feature carries small taste calls, I want each one told in plain words with an example and marked tweakable rather than confirmed, so that the lane keeps moving and every such choice stays findable.

### Acceptance Criteria

**Case: told with an example, marked tweakable**

1. *when* the walk makes a taste call without asking, the system *shall* write it into the spec with its `[default]` tag and name it in the delivery report in plain words with an example, marked tweakable. [INV-31, INV-18]
2. The system *shall* request no confirmation and re-ask nothing later, since silence is consent, and *shall* keep every such choice findable by its `[default]` tag so the person can ask when they want it changed. [INV-31]

---

## Requirement 36: A tunable parameter is set to a default and told, never asked

**Context:** Some choices are a mechanical knob with a range — an image's resolution, a batch size, a timeout, a sampling rate. The walk sets each knob itself and keeps the lane moving, writing it with its `[default]` tag and naming what it trades in the delivery report.

**User Story:** As a person whose feature carries tunable knobs, I want each set to a default and reported with what it trades rather than asked, so that the agent never stalls on a knob it can set and I tune it afterward only if I want a different point.

### Acceptance Criteria

**Case: set, tagged, and told**

1. *when* the walk meets a tunable knob, the system *shall* set it to a default value, choosing the cheaper or faster point wherever quality allows, write it with its `[default]` tag, and name in the delivery report what it trades. [INV-70, INV-31, INV-18]
   [GAP: the quality bar that permits the cheaper point is unstated in the source.]
2. The system *shall* owe no re-ask, letting the human tune the knob afterward and updating it together at most, the same idea the economy ladder applies to cost. [INV-70, T-19]

**Case: the agent moves every task it can**

3. The system *shall* move every task it can and reserve a question for what it genuinely cannot decide. [INV-70, INV-4]
4. *where* the human has granted it, the system *shall* ship to production on its own certification once the work is sound, keeping the grant the human's to give or withdraw. [INV-70, M-6, INV-9]

---

## Requirement 37: The smallest sample is judged before the full artifact

**Context:** For a taste-heavy deliverable — voice, copy, visual style, spec prose — the build stops at the cheapest judgeable sample: one paragraph, one card, two sections. The human's word on that sample sets the bar before the full build spends anything. This is the agent's own discipline, distinct from a declared show-me-first entry condition.

**User Story:** As a person whose deliverable is taste-heavy, I want the smallest judgeable sample put before me before the full build, so that my word sets the bar before the full build spends anything.

### Acceptance Criteria

**Case: the cheapest judgeable sample first**

1. *when* a deliverable is taste-heavy, the system *shall* stop the build at the cheapest judgeable sample — one paragraph, one card, two sections — and take the human's word on that sample before the full build spends. [INV-62]
   [GAP: the boundary classifying a deliverable as taste-heavy is unstated in the source; the source names examples (voice, copy, visual style, spec prose) and no closed test.]
2. The system *shall* build smallest first as the agent's own discipline even unasked, distinct from the human's declared show-me-first entry condition. [INV-62, INV-43]

---

## Requirement 38: A rejected artifact reopens its source

**Context:** When the human rejects an artifact, the fix starts at the artifact's source — the spec clause, the card, or the brief that produced it. Patching the rejected output line-by-line against an unchanged source is the five-round trap by name, and it is banned.

**User Story:** As a person rejecting an artifact, I want the fix to reopen its source and rebuild from it, so that the correction lands at the root rather than looping the same rejection against an unchanged source.

### Acceptance Criteria

**Case: correct the source, rebuild from it**

1. *when* the human rejects an artifact, the system *shall* correct its source — the spec clause, the card, or the brief — first and rebuild the artifact from it. [INV-63]
2. The system *shall* ban patching the rejected output line-by-line against an unchanged source, the five-round trap by name. [INV-63]

---

## Requirement 39: What already works is fenced before it is touched

**Context:** When a feature-doored wish touches a surface that already lives, its spec-delta opens with regression fences before the facet sweep authors anything new. A fence is one sentence for a neighbouring promise that must stay true through the change, citing the existing clause it guards. The delta splits everything it touches in two: promises that stay are fenced and untouched, behaviour being changed is re-authored as new law.

**User Story:** As a person changing a live surface, I want its neighbouring promises fenced and cited before anything new is authored, so that fixed one thing and quietly broke the neighbour turns red before it ships.

### Acceptance Criteria

**Case: the fence and what it guards**

1. *when* a feature-doored wish touches a surface that already lives, the system *shall* open its spec-delta with regression fences before the facet sweep authors anything new, each fence one sentence for a neighbouring promise that must stay true and citing the existing spec clause it guards. [T-14]
2. The system *shall* earn no new test-matrix row for a fence, discharging it through the cited clause's own never-side and proving the fence held by the landing's full-suite run. [T-14, INV-19, INV-6]

**Case: an unwritten promise, and where fencing belongs**

3. *when* a fence finds no clause behind it, the system *shall* reconcile the discovered promise from the shipped truth like an adopted claim, write it as its own spec fact with its own row, and surface it rather than silently assume it. [T-14, A-3, INV-5]
4. The system *shall* name the wish's fences by the anchors they cite in the queue row, keep fence-authoring to the feature door, let the bug and refactor doors inherit only the catching, and fence nothing on a prototype since it promises nothing. [T-14, T-7, E-17]

---

## Requirement 40: A feature says its non-goals and its success measure

**Context:** Every feature's spec-delta closes with two short sentences, both always written: the non-goals, what is deliberately left out, and the success measure, how the feature's working would be noticed for its person. A non-goal that narrows what the wish asked for is a scope decision, and a success measure derives no test-matrix row.

**User Story:** As a person closing a feature's spec, I want its non-goals and its success measure both written rather than left silent, so that what the feature excludes is on the record and how we would notice it worked is a written promise.

### Acceptance Criteria

**Case: the two sentences, always written**

1. The system *shall* close every feature's spec-delta with a non-goal sentence and a success-measure sentence, both always written, taking nothing deliberately left out this time as a valid non-goal and reading only a missing sentence as a hole. [INV-20, INV-21]
2. *when* a non-goal narrows what the wish asked for, the system *shall* ride it on the batched report as a stated scope decision. [INV-20, INV-4, INV-5]

**Case: the success measure carries no row**

3. The system *shall* write the success measure decided or `[default]`-tagged with a number where one exists, derive no test-matrix row from it, and keep it a written promise the human checks by eye until the reading machinery ships. [INV-21, INV-18]
4. The system *shall* bind both sentences forward from features specified after this rule, owe an adopted feature its pair at the first landing that touches it, and write neither on a prototype. [INV-20, INV-21, A-3, E-17, INV-159]

**Case: the reading machinery is promised**

5. The system *shall* keep the success-measure reading machinery promised under its own queue row. [INV-21]
   [target]

---

## Requirement 41: Intake is parallel, integration is serial — one landing under one pen

**Context:** While the session walks, intake is parallel and integration is serial: one landing at a time, per repo, under one pen. The pen is the right to write the shared truth — the spec, the architecture doc, the test matrix, the queue, the integration of a delta, the closing of a row. One lane holds it at a time, and claiming a lane is an atomic committed act.

**User Story:** As a person whose repo two sessions might share, I want one landing at a time under one pen with claims resolved by a total order, so that two lanes never scramble the shared tree and exactly one claimant backs off.

### Acceptance Criteria

**Case: the pen and the atomic claim**

1. The system *shall* hold the right to write the shared truth — the spec, the architecture doc, the test matrix, the queue, the integration of a delta, and the closing of a row — under one pen one lane holds at a time. [INV-2]
2. *when* a lane is claimed, the system *shall* commit the row-to-in-work flip first, then re-check under the concurrent-edit fence right before its first shared-truth write, and *shall* have the later claimant back off and re-queue *when* the re-check finds a foreign session's committed in-work row. [INV-2, INV-11]

**Case: the total order picks the winner**

3. The system *shall* read later by a total order that git ancestry defines: the claim whose commit is the ancestor in git history holds, and *when* two concurrent claims share no ancestry the claim whose session identity sorts lower holds; a wall-clock timestamp never enters the ordering. [INV-2, INV-117]
4. The system *shall* record the claiming session's identity in the flip so a peer computes the same order from either side, backing off exactly one session and never both. [INV-2, INV-117]

**Case: workers overlap, foreign hands never share the pen**

5. The system *shall* let bounded delegated workers overlap on disjoint brief-named files or an isolated tree with the concurrent-edit fence armed, and *shall* have a new wish wait its turn unless a bug preempts. [INV-2, ACT-3, T-10]

---

## Requirement 42: A pending question never stops the work, and no decision is silent

**Context:** Three more things hold while the session walks: a pending question never stops the work, no micro-decision is made silently, and every landing cites its wish row. The batched report carries the no-silent-decisions rule as its own postcondition.

**User Story:** As a person waiting on a decision, I want the lane to proceed on the recommended option while every choice not in my wish is asked or recorded and surfaced, so that a pending question never stalls the work and nothing is decided and buried.

### Acceptance Criteria

**Case: the pending question and the silent-decision ban**

1. *when* a question for the human is open, the system *shall* proceed on the recommended option and keep the question open in the row, revisitable any time. [INV-4]
2. The system *shall* make every choice not in the human's wish either asked or recorded in the spec and surfaced in the same batched report, reading a decision absent from the report as silent by definition. [INV-5]

**Case: every landing cites its wish**

3. The system *shall* have every landing name its wish row in the commit message or journal entry, so why a change exists is always answerable. [INV-3]

---

## Requirement 43: Each session carries a stable identity minted at its start

**Context:** Before its first act — before the inbox sweep — a session mints one identity and records it in its session checkpoint under `.live-spec/`, unchanged for the session's life. This identity is what the pen tie-break orders on, and it exists for every session.

**User Story:** As a person whose repo carries several sessions, I want each to mint a stable identity at its start, so that two sessions racing one claim compute the same tie-break order and the inbox source-mark reuses that one identity.

### Acceptance Criteria

**Case: the identity every session mints**

1. *when* a session starts, the system *shall* mint one identity before its first act and record it in the session checkpoint under `.live-spec/`, unchanged for the session's life. [INV-117]
2. The system *shall* use the harness session identity where the context carries one and otherwise mint the identity from the session's start moment joined with its worktree path and a nonce, carrying enough entropy to be unique. [INV-117]

**Case: one identity, reused by the source-mark**

3. The system *shall* order the pen tie-break on this identity and *shall* make the inbox source-mark's short session token a projection of that same one identity. [INV-117, T-10]

---

## Requirement 44: Trains may roll — one pen writes

**Context:** Parallelism already runs below the lane; this law lifts it to feature level where it is safe. One assigned session may hold up to the profile-declared lane cap of build lanes in-work at once, with a package default of three. The seat's independence read runs as the dependency graph over the runnable rows, and a lane opens only when that graph shows the lanes pairwise independent, the verdict narrated aloud as the lane opens. Everything that does not write the shared truth may overlap; everything that writes it takes the pen one lane at a time.

**User Story:** As a person whose session has independent work waiting, I want several lanes rolled at once up to the cap while every shared-document write and every landing passes through one pen, so that independent work proceeds together without the lanes corrupting each other's tree.

### Acceptance Criteria

**Case: the cap and the independence condition**

1. The system *shall* hold up to the profile-declared lane cap of build lanes in-work at once, a settings-ladder value with a package default of three, opening a lane only *when* the independence graph shows the lanes pairwise independent, narrating that read aloud as the lane opens. [T-18, E-13, INV-49]
2. *when* work waits past the cap, the system *shall* raise the cap only on the human's asked word, a session-scope settings-ladder value that outranks the profile's declared cap, and *shall* then open one more lane under the raised value, and *shall* never count read-only background analysis against the cap. [T-18, E-13]

**Case: what overlaps and what takes the pen**

3. The system *shall* let a later train's code and tests in its own isolated tree, read-only analysis and research, and a prover run reading committed law overlap. [T-18]
4. The system *shall* take the pen one lane at a time for edits to every shared document, the integration of a lane's delta, and the closing of a row, so two lanes' document stages never interleave mid-edit. [T-18]

**Case: the board, the bug, and the milestone**

5. The system *shall* show every rolling train on the board with its own station line, have a waiting lane name the row it waits behind, and ride the rolling trains' questions on one batched decision page. [T-18, INV-27, INV-4]
6. *when* a bug arrives, the system *shall* take the pen for it at the end of the current pen-stage, never cutting a pen-stage mid-edit and letting no lane take the pen back until the bug lands. [T-18, T-9]
7. *when* a milestone runs, the system *shall* run its whole-spec operations with one train only, holding the other lanes at a clean checkpoint and resuming them in landing order once the milestone lands. [T-18, M-1]

**Case: the held-for-milestone state**

8. *when* a milestone holds the other lanes, the system *shall* quiesce each in a distinct held-for-milestone state, named apart from bug-parked because nothing failed. [T-18, M-1]

---

## Requirement 45: A landing commit carries exactly one row's delta

**Context:** A milestone gate is one indivisible pen-stage: a bug arriving mid-gate waits for the gate to finish rather than preempting a half-run audit. While several trains roll, the landing stays pure — a landing commit carries exactly one row's delta and its gate runs on a tree holding nothing of any other lane's unfinished work.

**User Story:** As a person trusting a landing, I want each landing commit to carry exactly one row's delta gated on a clean tree, so that half of another train never rides a landing and the lane that landed first wins.

### Acceptance Criteria

**Case: the milestone gate is one pen-stage**

1. *when* a bug arrives mid-gate, the system *shall* have it wait for the milestone gate to finish and take the pen the moment the milestone lands ahead of the held lanes' resume, the one exception to a bug cutting the line at the end of the current pen-stage. [T-18, T-9]

**Case: the pure landing**

2. The system *shall* have a landing commit carry exactly one row's delta and run its gate — the full suite plus the guardrails — on a tree holding nothing of any other lane's unfinished work. [INV-39]
3. *when* a lane lands, the system *shall* have every still-rolling lane re-check under the fence and re-run its gate against the tree as it now stands, landed-first winning and the later lanes re-verifying. [INV-39, INV-11]

---

## Requirement 46: Lanes are picked by a graph, never by mood

**Context:** At queue-take the session reads the runnable head and builds a dependency graph. It draws an edge between two runnable movements only on a true dependency or a same-section collision. Mere co-location in a shared living document draws no edge, since the shared living documents are a convergence point reconciled at integration, never a serializing surface.

**User Story:** As a person with independent work waiting, I want lanes picked from a dependency graph rather than by mood, so that movements that merely share a living document still parallelize and only genuinely dependent or same-section rows serialize.

### Acceptance Criteria

**Case: the edge and the non-edge**

1. *when* the session takes the queue, the system *shall* build a dependency graph over the runnable head, drawing an edge only on a true dependency — one movement needs another's landed output — or a same-section collision where two movements rewrite the same clause or behaviour rule. [INV-49]
2. The system *shall* draw no edge on co-location in a shared living document, treating the spec, the architecture, and the test matrix as a convergence point reconciled at integration. [INV-49, INV-198]

**Case: the lane set and when not to parallelize**

3. The system *shall* open lanes on a pairwise-independent set up to the cap, serialize rows joined by an edge inside one lane, and pre-roll integration-only collisions with the landing order declared at claim time, the later lane re-fencing on the new truth. [INV-49, T-18, INV-39]
4. The system *shall* ride tiny rows serial since parallel pays only *when* build stages dominate the pen work, narrate the chosen set and order at opening, and hold false-serialization to the seat's read rather than a gate. [INV-49, INV-214]
   [GAP: the source rides tiny rows serial when build stages do not dominate the pen work but states no measure of a tiny row or of when build stages dominate; the seat judges with no stated threshold.]

---

## Requirement 47: A lane's isolated copy is a branch in its own worktree

**Context:** The isolated copy where a later train writes its code and tests is a git worktree holding a branch of its own. A lane delegated to a worker takes one through the Agent tool's worktree isolation option, which carries no gate, and the worker's brief names the branch its work rides.

**User Story:** As a person rolling a worker lane, I want its isolated copy to be a git worktree holding its own branch, so that the lane builds in real isolation and its open lanes read off the machine itself.

### Acceptance Criteria

**Case: the worktree branch a worker lane takes**

1. The system *shall* make a lane's isolated copy a git worktree holding a branch of its own, carrying that lane's code and tests. [E-34]
2. *when* a lane is delegated to a worker, the system *shall* take a worktree through the Agent tool's worktree isolation option with no permission gate and name the branch in the worker's brief. [E-34, INV-201]

**Case: overlapping lanes default to isolation**

3. *when* two concurrent lanes' write-sets overlap, the system *shall* default the later lane to worktree isolation, its copy reaching the shared tree only through integration under the pen. [E-34, INV-105]

---

## Requirement 48: A lane branch is born from the claim commit, on main

**Context:** The claim's row-to-in-work flip is committed to main under the pen, and the branch is cut from that commit. The claim lands on main because two claims are ordered by git ancestry and a peer reads that ancestry from the refs the worktrees share, so a claim on a lane's own branch would sit outside the ordering.

**User Story:** As a person opening a lane, I want its branch cut from a claim commit on main, so that two sessions' claims stay ordered by git ancestry and the open lanes read off the branch names.

### Acceptance Criteria

**Case: the branch cut from the claim commit**

1. *when* a lane is claimed, the system *shall* commit the row-to-in-work flip to main under the pen and cut the branch from that commit, naming it for its row as `lane/<row>-<slug>`. [T-23]
2. The system *shall* land the claim on main so two claims order by git ancestry, since a claim committed on a lane's own branch would leave two sessions each reading itself as first. [T-23, INV-2, INV-117]

---

## Requirement 49: The pen moves main, and a lane's branch is penless

**Context:** Under branches the shared tree is main, so holding the pen is the sole right to move main. A lane commits to its own branch as often as it likes, and that traffic is penless. Git holds the same bound on its own, refusing every other worktree's attempt to check out, force, or push to a branch a tree holds checked out, though three named roads walk past even that refusal.

**User Story:** As a person integrating a lane, I want holding the pen to be the sole right to move main while a lane commits freely to its branch, so that git turns back the roads a lane walks by habit ahead of any gate the pack writes.

### Acceptance Criteria

**Case: the pen owns main, the branch is free**

1. The system *shall* make holding the pen the sole right to move main and *shall* let a lane commit to its own branch freely as penless traffic, since nothing another lane reads has moved. [INV-198, T-18]
2. The system *shall* rely on git refusing every other worktree's attempt to check out, force, or push to a branch a tree holds checked out as a strong first net, naming its three known edges — `git update-ref`, the `--ignore-other-worktrees` flag, and a changed `receive.denyCurrentBranch` — rather than a guarantee. [INV-198]

**Case: the pen still keeps the shared documents**

3. The system *shall* keep every document on the pen's list under the pen even under branches, since two lanes drafting deltas on two branches would each prove against a spec the other is about to move and no suite reads a proof. [INV-198, E-34, INV-101]
4. The system *shall* keep the shared tree clean of every lane's unfinished work, turning the one-row landing commit's precondition from a discipline into a structure. [INV-198, INV-39]

**Case: the config-health net is promised**

5. The system *shall* keep the config-health check on the primary tree holding main promised, git's refusal the net until it ships. [INV-198]
   [target]

---

## Requirement 50: A lane lands by fast-forward from a rebased branch

**Context:** At integration the lane takes the pen, rebases its branch onto main's tip, runs the landing gate on the rebased tree, and fast-forwards main onto it. Rebase and fast-forward are what the existing law already demands, since a merge commit's second parent would break the one-row landing commit and a linear main keeps the claim ordering total. A landed lane's branch and worktree are removed at the landing.

**User Story:** As a person landing a lane, I want it to rebase onto main's tip and fast-forward with the branch torn down, so that main stays a linear one-commit-per-row history and the gate never reads a stale tree.

### Acceptance Criteria

**Case: rebase, gate, fast-forward**

1. *when* a lane integrates, the system *shall* take the pen, rebase its branch onto main's tip, run the landing gate on the rebased tree, and advance main onto it with no merge commit. [INV-199, INV-39, INV-2]
2. The system *shall* stand one check ahead of the gate — the branch's merge-base with main equals main's tip — redding a lane that has not rebased so the gate never reads a stale tree. [INV-199, T-23]

**Case: teardown at the landing**

3. *when* a lane lands, the system *shall* remove its branch and worktree, and *shall* keep both on a parked lane with the board saying which. [INV-199, T-9, INV-27]
4. The system *shall* refuse teardown on a worktree holding uncommitted work and read that refusal as a finding, and *shall* red a lane worktree or a lane branch with no open row in the config-health gate. [INV-199, INV-150]

**Case: the pre-gate checks are promised**

5. The system *shall* keep the merge-base check ahead of the gate and the stale-lane check promised, the prover's station their net until then. [INV-199]
   [target]

---

## Requirement 51: A textual conflict is the lane's own work, and a semantic one meets the nets that exist

**Context:** Git halts the rebase on a textual conflict and the landing cannot proceed, so the tool is that net; the lane resolves it in its own worktree and re-runs its gate from the top. A semantic conflict is the one that survives a clean textual merge, and the road holds two nets for it.

**User Story:** As a person rebasing a lane, I want a textual conflict resolved as my own work and a semantic one met by the nets that exist, so that the road claims no net it does not hold and a residual is named honestly.

### Acceptance Criteria

**Case: the textual conflict**

1. *when* git halts the rebase on a textual conflict, the system *shall* have the lane resolve it in its own worktree and re-run its gate from the top on the resolved tree. [INV-200]

**Case: the semantic conflict and its residual**

2. The system *shall* meet a semantic conflict with the two nets that exist — the pen keeping every document delta together so two lanes' documents never diverge, and the full suite on the rebased tree reading two lanes' diverging code. [INV-200, INV-198]
3. *when* a semantic conflict survives a green suite on the rebased tree, the system *shall* name it a test-matrix gap and route it to the test matrix's own home rather than invent a net here. [INV-200, INV-73, E-15]

---

## Requirement 52: The isolation default and the worktree tool agree through one vendored line

**Context:** The isolation law fires on a machine-readable condition — two lanes' write-sets overlap — while the worktree tool fires only on a human's word or a project instruction and lists feature work among the cases it declines. So today neither fires and the fallback is the shared tree the law forbids. The tool accepts a project instruction as authorization equal to a human's word, so adoption vendors one line into the host's project instructions.

**User Story:** As a person adopting the pack, I want one vendored line to make the isolation law and the worktree tool agree, so that the two fire on one condition without a second home for it and the line is scoped to the host that adopted.

### Acceptance Criteria

**Case: the vendored line cites the law's condition**

1. The system *shall* vendor one line into the host's project instructions that cites the isolation law's write-set condition rather than restating it, keeping the condition's one home. [INV-201, INV-105, INV-101]
2. The system *shall* scope the line to the host it governs and version it in that host's own tree, carrying it to an already-adopted host through the catch-up walk. [INV-201, A-11, INV-159]

**Case: the line records the host owner's word**

3. *when* the host owner's word for the host's tree is spoken, the system *shall* write the vendored line recording that word, and *shall* leave the session lane shut until the pack's own owner gives the word for the pack's line. [INV-201, INV-152, INV-4]
4. The system *shall* red a host whose project instructions carry no worktree line at the adoption gate, a mechanical gate the prover's station stands as until the build lands. [INV-201, INV-150]
5. The system *shall* require no vendored line for a worker lane, since the subagent's isolation option carries no gate. [INV-201, E-34]

**Case: the adoption gate is promised**

6. The system *shall* keep the adoption gate for the host's worktree line promised, the prover's station its net until then. [INV-201]
   [target]

---

## Requirement 53: The cap holds at three, and across sessions the pen's arbitration fires

**Context:** The lane cap is the profile-declared value with a package default of three. The branch road removes the tree's cost — a lane writes no tree another lane reads — but the three costs that bound the cap survive untouched, so the tree was never what bound it. The lanes law does not fire across sessions, and that sentence scopes the cap, the board, and the independence judgment; the pen's arbitration fires across sessions and always did.

**User Story:** As a person running lanes, I want the cap held at its declared value and the pen's cross-session arbitration recognized, so that removing the tree's cost is no reason to raise the number and two sessions on one repo need no new law.

### Acceptance Criteria

**Case: the three surviving costs hold the cap**

1. The system *shall* hold the cap at its declared value, three by the package default and by the profile line, since the branch road touches none of the three costs that bound it — pen-wait, the rebase-and-re-gate work every landing forces on every rolling lane, and the orchestrator's dividing review attention. [T-18, E-13]
2. The system *shall* proceed on this recommendation while the owner's word on raising the cap stays owed, naming the measurement the pack has not taken — pen-wait time per lane and re-fences per landing. [T-18, INV-4]

**Case: the pen arbitrates across sessions**

3. The system *shall* scope the cap, the board, and the independence judgment to one session and *shall* fire the pen's arbitration across sessions, a foreign session's claim commit on main being readable with no fetch. [T-18, INV-198, INV-2]
4. *when* a second session takes a lane on one repo, the system *shall* give it its own worktree and branch under the stated road with no new law, since two worktrees share one object store and one set of refs. [T-18, INV-11, INV-117]

---

## Requirement 54: The branch road's machines, and what each one owes

**Context:** The branch road stands on machines. Two are git's own and run today, each guarding a road a session walks by habit; four are the road's build half and stand until the build lands, with the prover's station as their net meanwhile. The road states each machine's boundary rather than hiding it, so it claims no net it does not hold.

**User Story:** As a person relying on the branch road, I want each of its machines named with what it owes, so that git's known-edged refusals and the pack's own gates together cover the roads a lane walks.

### Acceptance Criteria

**Case: git's own machines**

1. The system *shall* rely on git refusing every other worktree's checkout, branch-force, and push against a branch a tree holds checked out, and on git halting a rebase on a textual conflict, as strong nets whose edges are known. [T-23, INV-198]
2. The system *shall* carry the roads git leaves open — a moved checked-out branch, a documented override flag, a changed refusal default — in the pack's own gates below. [T-23, INV-198]

**Case: the pack's four build-half machines**

3. The system *shall* red a branch whose merge-base sits behind main's tip in the merge-base check, red a lane worktree or a lane branch carrying no open queue row and a primary tree that does not hold main in the config-health check, red a host whose project instructions carry no worktree line in the adoption gate, and red a lane opened past the cap in the board's lane-count check. [T-23, INV-150]
4. The system *shall* make all four mechanical gates under the net-routing law, since a deterministic check decides every one of these violations. [T-23, INV-150, INV-101]

**Case: what the road fences and leaves out**

5. The system *shall* leave the pen's document list unchanged, keep the one-row landing commit and its clean-tree gate, keep the claim ordering and its tie-break, keep the isolation condition's one home, keep write-ownership untouched, and open no cross-session cap, no cross-session board, no automatic conflict resolution, no long-lived or pushed branch, and no merge commit on main. [T-23, INV-39, INV-2, INV-117, INV-105, INV-101, INV-11, INV-10]

---

## Requirement 55: Opening a lane is a performed act, and single-file work while lanes stand free is a recorded choice

**Context:** A grant with no performed step leaves the session on the single-file road every time. So opening a lane is a named act with a performable procedure, run when the independence graph shows two or more independent runnable rows and lanes stand free under the cap. Going single-file while lanes stand free is a recorded choice said aloud on the board.

**User Story:** As a person asking one window for parallel work, I want opening a lane to be a performed act and going single-file a recorded choice, so that the law's grant of parallel lanes actually gets used instead of items rolling one after another.

### Acceptance Criteria

**Case: the performed lane-open act**

1. *when* the independence graph shows two or more independent runnable rows and lanes stand free under the cap, the system *shall* read that graph verdict as the seat's own independence judgment and *shall* perform the lane-open act — commit the row-to-in-work flip on main under the pen, cut the branch into its own worktree, and delegate the lane to a worker whose brief names the branch. [INV-214, INV-49, INV-198, T-23, E-34, T-18]
2. The system *shall* offer the act as `scripts/open-lane.sh`, which reads the settings-ladder-resolved cap — raised for the session only by the human's asked word — and refuses to open a lane past that value, runs the fence before it commits, and carries the claim commit alone so the landing keeps its one-row delta. [INV-214, E-13, INV-11, INV-39]

**Case: single-file is a recorded, ungated choice**

3. *when* the session goes single-file while the graph shows free independent lanes, the system *shall* say so on the board as the serial-by-the-graph line, naming which standing reason holds — a shared-section collision, a full cap, tiny rows, or a dependency. [INV-214, INV-49]
4. The system *shall* keep the recorded-reason duty a matter of discipline, since judging two rows independent is the independence graph itself and the lane branches that would evidence a parallel run are torn down at each landing, leaving the cap refusal as the one mechanical guard the act carries. [INV-214, T-23]

---

## Requirement 56: Deferred rows are revisited at every queue-take

**Context:** A deferred row carries a revisit trigger, and a time-bound one can come true and lapse in the gap between two milestone gates. So the milestone re-scan is not the trigger's only reader: at every queue-take the session also re-scans each deferred row's revisit trigger against the current moment, and a fired trigger returns its row to the runnable head right then.

**User Story:** As a person with a time-bound deferral, I want its revisit trigger read at every queue-take and not only at milestones, so that a window that opens and closes between gates is caught by whichever cadence comes first.

### Acceptance Criteria

**Case: the two cadences read the same triggers**

1. *when* the session takes the queue, the system *shall* re-scan each deferred row's revisit trigger against the current moment and *shall* return a fired trigger's row to the runnable head. [INV-129, T-8, INV-49]
2. The system *shall* read the same triggers by the same rule at queue-take and at the milestone gate, so a deferred wish never waits on a trigger nobody reads, and *shall* keep the trigger vocabulary free-form since a reader now runs at queue cadence. [INV-129, M-1, INV-1]

---

## Requirement 57: A deferred item's own state is re-derived from the code before its work resumes

**Context:** A resume file and a queue row record a past moment, and the technical problem statement one item carries can go stale as the code it touches moves on. So a session resuming a deferred or queued item, before it designs anything, reads the code the item touches, confirms the problem still holds, and re-derives the item's real current state.

**User Story:** As a session resuming a deferred item, I want its own state re-derived from the shipped code before I design anything, so that I never build a fix from a stale model of code that has since moved and catch an item already handled.

### Acceptance Criteria

**Case: the resume-side re-read**

1. *when* a session resumes a deferred or queued item, the system *shall* read the code the item touches, confirm the problem the row describes still holds, and re-derive the item's real current state before it designs anything on the item. [INV-247, INV-129]
2. The system *shall* fire this read at the same resume moment as the deferral re-test that re-asks whether the item is still the seat's or the human's, owing both reads. [INV-247, INV-152]

**Case: no push gate holds it**

3. The system *shall* keep this a discipline the seat holds, since a resume is an in-session act at chat cadence with no committed artifact for a gate to scan, carried by the base rulebook's resume habit. [INV-247, INV-83]

---

## Requirement 58: The queue has a far tier the runnable report stands down by name

**Context:** A wish can be worth keeping while carrying no plan to run and no event that would bring it back. Such a row takes the far status, and a far row is not a deferred one: a deferred row carries a revisit trigger the queue-take re-scans, while a far row carries no trigger and returns only when the person asks or the rare self-surfacing line offers it.

**User Story:** As a person keeping a far backlog, I want far rows told apart from deferred ones and left out of the runnable report, so that the what's-left report notes the far tier in one line rather than naming its rows among runnable work.

### Acceptance Criteria

**Case: far and deferred told apart**

1. The system *shall* give a row worth keeping with no plan to run and no event that would bring it back the far status, distinct from a deferred row whose revisit trigger the queue-take re-scans. [INV-222, INV-129]
2. The system *shall* read the boundary both ways — a far row carrying a revisit trigger is a deferred row wearing the wrong token, and a deferred row carrying no trigger leaves the re-scan nothing to read. [INV-222]

**Case: the runnable report stands the tier down**

3. *when* the what's-left report or the feature-map answer reads the runnable queue, the system *shall* stand the far tier down by name — one line that a far backlog exists, its count, and that the whole tier prints on request — rather than name its rows among runnable work. [INV-222, INV-223, INV-206, E-3]
4. *when* a report names a far-tier row among the runnable what's-left, the system *shall* red the report-shape check, which rides the suite and not the push chain since the status report is a chat surface with no committed file to gate. [INV-222, INV-83]

---

## Requirement 59: A deferred row can carry a mechanical revisit trigger

**Context:** A deferred row's revisit trigger is usually prose a reader judges at the queue-take. Where the awaited event is mechanically observable, the trigger is a check the queue-take runs. The worked instance is the day the harness gains a listener, a component that lets one session push a message directly to another running session in place of the inbox's file drop. The row deferred on that day carries a mechanical trigger the queue-take reads.

**User Story:** As a person deferring work on a mechanically observable event, I want its revisit trigger to become a one-shot check the queue-take runs, so that the row returns the moment the event fires and stays silent until a real record carries the field.

### Acceptance Criteria

**Case: the mechanical trigger and its check**

1. *when* a deferred row's awaited event is mechanically observable, the system *shall* make its revisit trigger a check the queue-take runs rather than prose a reader judges. [INV-231, T-8, INV-129]
2. The system *shall* fire the listener-tripwire check only on a session record carrying a non-empty socket field — the record's field naming the address a listener would serve — and stay silent on an empty or absent one, so a listenerless harness leaves it quiet. [INV-231, INV-183]

**Case: it rides the queue-take scan**

3. *when* the check fires, the system *shall* return the row to the runnable head, and *shall* ride the queue-take scan and the suite with no push-gate letter, the way the far-tier check takes none, since a queue-cadence read is no committed file for a push gate to scan. [INV-231, INV-129, INV-222, INV-83]

---

## Requirement 60: A wish can end without landing in one of three end-states

**Context:** A wish can end without landing, and its row stays in the table in one of three end-states: declined when the human said no, deferred when parked with a named revisit trigger, or superseded when absorbed by another wish so the row points to the absorbing one. A superseded wish never dies by pointer.

**User Story:** As a person whose wish ends without landing, I want it settled into one recorded end-state with what it absorbed preserved, so that a declined or superseded wish still reaches a named terminal state and nothing it held is lost.

### Acceptance Criteria

**Case: the three end-states**

1. *when* a wish ends without landing, the system *shall* keep its row in the table as declined, deferred, or superseded, a superseded row pointing to the absorbing wish. [T-8]
2. *when* a wish that other rows were superseded into is declined, the system *shall* list those rows at its decline, preserving what the declined wish had absorbed. [T-8, INV-1]

**Case: each absorbed row is settled by name**

3. *when* a wish is declined, the system *shall* either decline each listed row by name where the human's no covered it or return it to the queue as its own row where the no was about the absorber's shape, never letting a superseded wish die by pointer. [T-8, INV-1]

---

## Requirement 61: What the wishes grow is the spec

**Context:** What the wishes grow is the spec, the living statement of what the product is, where one surface carries one name everywhere.

**User Story:** As a person reading what the wishes built, I want them to grow one living spec with one name per surface, so that the whole team reads one current truth rather than scattered descriptions.

### Acceptance Criteria

**Case: one living statement, one name per surface**

1. The system *shall* grow the spec as the living statement of what the product is, naming each surface one way everywhere. [E-4]

---
