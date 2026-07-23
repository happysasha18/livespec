# Throwing a wish: intake, naming, and the human exchange

This section states the first half of the build loop: how a wish is captured and shaped, how the work is named and reported back, and how work is shown to the person and decisions are asked of them. The build loop is the everyday path a piece of work travels — a wish comes in, is specified, is tested, and ships. This section is written for a reader who has never seen the pipeline before.

Bracket codes like `[INV-27]` and `[E-2]` point to the rule's home in the project spec; a reader can ignore them, a maintainer follows them. The letter before the number names the kind: `INV-` an invariant (a numbered rule that must always hold), `E-` an entity (a numbered part of the product), `T-` a transition (a numbered change of state), `M-` a rhythm rule (a numbered recurring routine), and `F-` a feature. A range such as `[T-1..T-7]` cites its whole run of codes. The keywords *when*, *while*, *if*, *then*, and *shall* are set in italics and carry their standard requirements meaning: *shall* states a duty, *when* and *while* open a situation, *if* and *then* open a condition and its result.

Terms already defined in the carried glossaries — request, inbox, pipeline, spec, architecture, invariant, guardrail, suite, host, pack, session, journal, attic, queue, movement, delivery, delivery report, resume file, profile, personal profile, migration chapter, capture echo, and seat — carry their meanings unchanged. The rhythm nouns milestone and breakpoint are owned by the rhythm stretch of this build loop and defined there, and the noun lane — one parallel work track building one queue row in its own isolated tree — is owned by the parallel-lanes stretch and defined there. The nouns routing rule and tier are owned by the rules-and-who-applies section and defined there. The block below adds only the new nouns this section needs.

## Glossary additions

- **loop** — an autonomous recurring run the session performs with no person present, working in iterations and sleeping between them.
- **walk** — the pipeline's own handling of one wish, its path from capture to landing; a rule that binds the walk binds the process itself rather than any one actor.
- **beat** — one narration line marking one unit of the work's progress; a stretch with no beat is beatless, and the heartbeat line covers it.
- **checkpoint** — the saved point a piece of work reaches and can resume from, written under `.live-spec/`.
- **spec-delta** — the drafted change one wish makes to the spec, validated against the whole spec before any test or code is written.
- **wish** — one request a person voices in plain words, of any size and at any moment, captured as a queue row and carried to a recorded terminal state.
- **intake** — the pipeline's first station, where a wish already captured as a queue row is classified: the classifier reads its size, priority, door, and work-kind and states them back in one line.
- **door** — the axis naming where a wish enters the pipeline, its values the bug door, the feature door, and the refactor door, kept separate from the wish's size.
- **size** — the wish's extent, named by one word from a four-word vocabulary: bug, small, surface, or large. A surface-sized wish is a new surface or a multi-file behaviour change. A bug-sized wish is the bug door itself, one call stated once for both axes. The size word is what the row's class column carries, the priority mark standing on the row beside it. The word surface elsewhere stays the common noun for a screen a person sees, and the word bug elsewhere stays the common noun for a defect.
- **priority** — the wish's urgency, normal unless its row carries one of two marks, critical or quick win.
- **work-kind** — the kind of work a wish is, named at intake by one word from a curated vocabulary: product, infra, skill, or prose.
- **decision page** — one surface that carries several open questions to the person together, opening in its own window while the rest of the work continues.
- **decision card** — one question on a decision page, opening with what each option changes for the person and carrying the recommended answer.
- **decision archive** — the directory `docs/decisions/` where an answered decision page is filed.
- **feature map** — the product's map of features, constituted by the spec's scenario sections and the architecture's nodes together, with no separate map document.
- **user story** — one distinct thing a person does and sees; a wish carries one, and a wish carrying more is split at intake into a row apiece.
- **leg** — one of the separately-accepted parts a multi-part row still carries, each with its own Done-when acceptance.
- **regression fence** — one sentence in a spec-delta naming a neighbouring promise that must stay true, citing the clause it guards.
- **non-goal** — one sentence in a spec-delta naming what the change deliberately leaves out, so a deliberate absence reads as a decision.
- **facet** — one aspect of a feature's design, ending as a written spec sentence that is decided or tagged as a default.
- **success measure** — one written way to notice a feature worked for its person, with a number where one exists.
- **status report** — the short current-state account kept in the chat, naming the work in hand and what the queue holds next.
- **narration** — the running account of work as it happens, said in the roadmap's terms between the capture echo and the delivery report.
- **heartbeat** — a narration line on a long beatless stretch, naming what is grinding and why the stretch runs long.
- **offline window** — a narration line before a stretch that needs nothing from the person, naming that the person may step away, an honest range for how long, and what the person is needed for at its end.
- **register lint** — the pre-show check `scripts/preshow-register-lint.py` that reads a surface's text for machine dialect and blocks the showing on a red result.
- **removal list** — the dated record of the literal phrasings a person cut from a taste-reviewed artifact, appended when a cut happens and never removed.

---

## Requirement 1: A wish is captured as a queue row that is never lost  [feature: F-wish]

**Context:** A wish is one request a person voices in plain words, of any size, at any moment. The moment a person voices one it becomes a row in the queue (ROADMAP.md), the persistent ordered home of every wish. The row holds the person's words, the wish's class, its status, and its acceptance criterion.

**User Story:** As a person who voices a request in passing, I want it captured as a durable queue row the instant I speak it, so that a thought thrown mid-sentence is never lost between intake and its resolution.

### Acceptance Criteria

**Case: a wish becomes a row at once**

1. *when* a person voices a wish, the system *shall* record it as one row in the queue that same moment, holding the person's words, its size in the class column with the priority mark beside it, its status, and its acceptance criterion. [E-2, E-3]
2. *when* a wish is recorded, the system *shall* keep its row existing even *if* the session ends immediately after, since the row is written before anything else proceeds. [E-3]

**Case: a row is never deleted**

3. The system *shall* never delete a row, and *shall* close a row only with a named exit. [INV-1]
4. The system *shall* carry every wish to a recorded terminal state, so a request captured in passing is never dropped. [INV-1]

---

## Requirement 2: A row rests in the home its exit names

**Context:** A row's exit decides where it lives next. A row closed with a terminal exit — landed, declined, or superseded — moves at a milestone to a dated queue archive and stays there unedited. A deferred row stays in the active queue carrying its revisit trigger. A far row stays too, but carries no revisit trigger and no plan to run.

**User Story:** As a person whose queue holds live work beside parked thoughts, I want each row to rest in the home its exit names, so that a closed wish is archived, a deferred one returns on its trigger, and a far one is kept out of that same what's-left answer.

### Acceptance Criteria

**Case: a terminal exit is archived**

1. *when* a milestone is reached, the system *shall* move a row closed with a terminal exit — landed, declined, or superseded — to a dated queue archive, and *shall* keep it there unedited. [INV-1]
2. The system *shall* keep in the archive only wishes no longer due back. [INV-1]

**Case: a deferred row waits on its trigger**

3. The system *shall* keep a deferred row in the active queue, carrying its revisit trigger, until the trigger fires or the row resolves to a terminal exit. [INV-222]

**Case: a far row is kept and stood down**

4. The system *shall* keep a far row in the active queue with no revisit trigger and no plan to run, so a thought worth keeping is not discarded. [INV-222]
5. *when* the runnable report — the what's-left answer naming the rows a session could take next, spoken at queue-take or on the person's ask — is produced, the system *shall* stand the far tier down by name and *shall* show it only on the person's request. [INV-222, INV-223]

---

## Requirement 3: From its row, a wish follows one fixed path

**Context:** From its row, a wish follows one path through the pipeline. The classifier reads and states its attributes, a spec-delta is drafted and validated, the wish is queued and worked, and it lands when its proofs pass. Each step is one transition in a fixed sequence.

**User Story:** As a person tracking a wish from capture to landing, I want it to travel one fixed path of stated steps, so that at any point I can see which step it sits at and what remains.

### Acceptance Criteria

**Case: the wish travels a fixed path**

1. *when* a wish is recorded as a row, the system *shall* read its size, priority, door, and work-kind and state them back to the person in one intake line. [T-1..T-7]
2. The system *shall* draft a spec-delta and *shall* validate it against the whole spec, sending only genuinely human questions to the person in a batch while everything else proceeds on the recommended option marked in the row. [T-1..T-7]
3. The system *shall* move the wish's status to queued and then to in-work. [T-1..T-7]
4. The system *shall* land the wish *when* the suite is green, the guardrails pass, the commit goes in, and the row closes with its acceptance met. [T-1..T-7]
5. *when* the wish lands, the system *shall* report to the person in one plain-language line naming the position on the feature map, what landed, and what remains. [T-1..T-7]

---

## Requirement 4: Open questions arrive together on one decision page

**Context:** Several open questions reach the person together on one decision page rather than one at a time in chat. The page opens in its own window while the rest of the work carries on. Each question is a card with its recommended answer marked and room to write another. Once answered, the page is filed and every answer folded into its queue row the same session.

**User Story:** As a person who owes the pipeline several decisions, I want them gathered on one page I answer on my own clock, so that questions never dribble out one at a time and no answer I give is lost.

### Acceptance Criteria

**Case: questions arrive together and are folded back**

1. *when* more than one open question stands, the system *shall* carry them to the person on one decision page that opens in its own window while the rest of the work carries on. [E-22, INV-4]
2. The system *shall* present each question as a card with its recommended answer marked and room to write a different one. [E-22]
3. *when* the decision page comes back answered, the system *shall* file it in the decision archive `docs/decisions/` and fold every answer into its queue row the same session, since an answer left unread is a decision lost. [E-22]

**Case: the person's word settles it**

4. The system *shall* treat the person's word as what settles a decision and *shall* read a click as recording only a first pick, so a pick taken back in plain speech is withdrawn, logged as answered-then-withdrawn, and asked again later in plainer terms. [INV-9]
5. The system *shall* settle nothing that needs the person's considered word on a pick made without understanding. [INV-9]
   [GAP: the at-pick signal for a without-understanding pick is unstated in the source; the stated mechanisms are the plain-speech withdrawal and the card-defect rule (a card unanswerable without its mechanism is a defect).]

**Case: a withdrawn decision converges**

6. *when* the same decision is withdrawn a second time, the system *shall* take the recommended option, surface it as a `[default]` in the delivery report, and never re-ask it, silence staying consent from there. [INV-130, INV-31]
7. The system *shall* close an answered question for good and *shall* route a later change of mind as a new wish, the closed decision staying closed. [INV-59, INV-130]

**Case: the page mechanics have one home**

8. The system *shall* keep how the page works — its filename, its ordering, its round-trip — written once in the communicator skill's rule 10. [INV-13]

---

## Requirement 5: A decision card asks in consequences

**Context:** A decision card opens with what each option changes for the person — what it gives them or what problem it removes — in the product's own words. The mechanism follows only where it aids the choice. Each option is labelled by its consequence, never by its implementation.

**User Story:** As a person answering a decision card, I want each option framed by what it changes for me, so that I can decide without first learning how the machinery works.

### Acceptance Criteria

**Case: the card asks in consequences**

1. *when* a decision card is shown, the system *shall* open it with what each option changes for the person and *shall* label every option by its consequence, bringing in the mechanism only where it aids the choice. [INV-32]
2. The system *shall* read a card that cannot be answered without understanding the mechanism as a defect of the card. [INV-32, INV-28]

---

## Requirement 6: A wish is classified by size, priority, and work-kind

**Context:** A wish is classified by size, priority, and work-kind, three separate axes. Size uses one four-word vocabulary everywhere. The door — where the wish enters the pipeline — is a separate axis, and size is a separate question. Priority is normal unless a row carries a mark.

**User Story:** As a person whose wish enters a disciplined pipeline, I want its size, priority, and work-kind pinned at intake by the person when unclear, so that each attribute is set by a considered, explicit call.

### Acceptance Criteria

**Case: the three axes and their vocabularies**

1. The system *shall* classify each wish by one size word from the four-word measure — bug, small, surface, or large — and *shall* carry the same four words in the queue row's class column with no second size scale. [INV-12, T-16]
   [GAP: the boundary separating a small wish from a large one is unstated in the source; only the surface and bug sizes carry stated readings.]
2. The system *shall* keep the door a separate axis from size, naming where the wish enters the pipeline. [T-16]
3. The system *shall* name one work-kind per wish from the curated vocabulary — product, infra, skill, or prose — taking the host's recorded default where the person names none. [T-16]

**Case: priority and its two marks**

4. The system *shall* carry a wish at normal priority unless its row states otherwise, marking it critical *when* the shipped product is broken for its user — an unusable surface, lost data, or a violated safety gate — and quick win *when* the work is low in effort, of immediate value, and holds no design decision. [INV-12]
   [GAP: the source gives critical three concrete conditions but gives quick win only the qualitative phrases "low effort" and "immediate value", naming no measure or threshold separating a quick win from a normal wish; the classifier and the person judge it at intake with nothing pinned.]

**Case: an unclear attribute is asked, never guessed**

5. *when* the classifier cannot call a size, a priority, or a work-kind, the system *shall* ask the person at intake and *shall* not guess. [INV-12, T-16]
6. *while* an unclear attribute stays open, the system *shall* carry the wish at normal priority with the host's default work-kind or none, scale nothing down for a work-kind not yet named — a named work-kind scales how much machinery each pipeline step spends — and keep the open question in the row *while* the lane keeps moving. [INV-22, INV-12, INV-4, T-16]

---

## Requirement 7: A large wish negotiates scope, never time

**Context:** The walk never asks how long a wish will take and never accepts an estimate in hours or days as an input. When a wish is worth less than the work it demands, the walk answers in scope terms and proposes cutting the scope or splitting into stages. Every cut is reported.

**User Story:** As a person whose wish may cost more than it returns, I want the walk to renegotiate its scope while holding its schedule, so that an oversized wish is trimmed or staged and every trim reaches me in the report.

### Acceptance Criteria

**Case: scope is the axis, never time**

1. The system *shall* refuse to ask how long a wish will take and *shall* refuse an estimate in hours or days as an input. [T-15]
2. *when* the work a wish demands is larger than the wish is worth, the system *shall* answer in scope terms and *shall* propose one of two moves — cut the scope to fewer surfaces with plainer defaults, or split into stages that each land through the full pipeline. [T-15, INV-12]
   [GAP: the source triggers the scope negotiation on a wish being "larger than its worth" but names no measure of a wish's worth and no judge of the comparison, so when the negotiation opens is unpinned.]

**Case: the proposal proceeds and every cut is reported**

3. The system *shall* proceed on the recommended option and *shall* not park the lane on the proposal. [T-15, INV-4]
4. The system *shall* report every cut in the batched delivery report alongside every taken default, and *shall* not cut silently. [INV-18, INV-5]

---

## Requirement 8: A proven artifact settles a fork before the person hears it

**Context:** Before surfacing a design choice, a session checks whether an existing proven artifact — the architecture, the spec, the invariants — already determines the answer. When it does, the session derives the requirement and states it back with the section cited, offering no fork. A fork reaches the person only for what the artifacts leave genuinely open.

**User Story:** As a person asked only about real choices, I want a session to derive from a proven artifact whatever the artifact already settles, so that I hear a fork only for a taste call or a trade-off no document has decided.

### Acceptance Criteria

**Case: a settled fork is derived**

1. Before surfacing a design choice, the system *shall* check whether a proven artifact already determines the answer, and *when* one does *shall* derive the requirement and state it back with the section cited as its ground, offering no fork. [INV-121, INV-4]
2. The system *shall* raise a fork to the person only for what the artifacts leave genuinely open — a taste call, or a trade-off with no artifact-grounded winner. [INV-121]
3. The system *shall* apply this check as the design-fork sharpening of the pre-ask decide-or-verify gate. [INV-4, INV-81]

---

## Requirement 9: A scope cut moves scope alone and spares the mandatory sentences

**Context:** A scope cut changes scope only, never order. A cut surface returned later is a new wish. No cut touches the delta's mandatory sentences — the regression fences, a kept surface's facets, the non-goals, and the success measure. Scope adjusts richness.

**User Story:** As a person whose wish was trimmed, I want the cut to move scope alone and to leave the mandatory sentences intact, so that trimming never reorders the lane and never drops a fence, a facet, a non-goal, or the success measure.

### Acceptance Criteria

**Case: a cut moves scope alone**

1. The system *shall* treat a cut surface returned later as a new wish. [T-11]
2. The system *shall* let a scope cut change scope only, reading it as no quick-win mark, since only priority moves the lane order. [T-11]

**Case: the mandatory sentences are uncuttable**

3. The system *shall* keep every cut clear of the delta's mandatory sentences — the regression fences, a kept surface's facets, the non-goals, and the success measure. [T-14, INV-18, INV-20, INV-21]
4. The system *shall* adjust richness through a cut and *shall* leave the mandatory sentences standing whole. [T-15]

---

## Requirement 10: One wish is one user story, and a row closes only whole

**Context:** One wish is one user story — one distinct thing a person will do and see. A wish carrying more than one story is split at intake, each story its own row through the full pipeline. Sub-behaviours of one story — its hover face, its phone face, a backpointer — are that story's acceptance, folded into that same row.

**User Story:** As a person who voices a wish that hides two stories, I want it split at intake into a row per story, so that each row traces to one clear thing I wanted and no two behaviours are fused into one close.

### Acceptance Criteria

**Case: a multi-story wish is split**

1. The system *shall* split a wish carrying more than one user story at intake, giving each story its own row through the full pipeline. [T-17]
2. The system *shall* fold the sub-behaviours of one story — its hover face, its phone face, a backpointer — into that story's own row as its acceptance. [T-17]
3. The system *shall* keep separate stories in separate rows and *shall* not fuse them, distinct from a stage split that slices one story's depth. [T-17, T-15]

**Case: the split is asked and loses nothing**

4. *when* the story count is unclear, the system *shall* ask the person at intake and *shall* not guess. [INV-12]
5. The system *shall* have every row a split produces cite the one spoken wish it came from. [T-17, INV-1]

---

## Requirement 11: A multi-leg row enumerates per-leg acceptance

**Context:** Some rows still carry more than one leg — a legacy fusion or a harvested batch. Such a row states acceptance for each leg in its Done-when and closes only when every leg is met. Half-done is a status, never a landing.

**User Story:** As a person whose row carries several legs, I want per-leg acceptance enumerated and the row held open until every leg is met, so that a half-finished row stays visibly open rather than closing on an unmet leg.

### Acceptance Criteria

**Case: per-leg acceptance and no partial close**

1. *where* a row carries more than one leg, the system *shall* enumerate per-leg acceptance in its Done-when and *shall* not close the row with an unmet leg. [INV-26]
2. The system *shall* read half-done as a status and never as a landing. [INV-26]

**Case: compaction preserves an open leg**

3. The system *shall* keep the resume file's live-state supersession (the newest live-state block replacing the older one whole) from compressing an unfinished leg out of existence, restating in full a leg still open at compaction (the announced pass where a session prunes its own working context, carrying live lines forward). [INV-26, M-2]

---

## Requirement 12: The system echoes every wish back and reports each feature's stage

**Context:** The system speaks every captured wish back to the person in one immediate sentence. The echo opens with what was heard, which door the wish entered, the name the work goes by, and its row number; further law in this section adds the wish's feature-map position, and a long-running direct command adds an honest time range. Every status report then names each in-flight feature and the pipeline stage it sits at.

**User Story:** As a person who threw a wish and leads several windows, I want an immediate one-sentence echo and a status report that names each feature's stage, so that I always see a request was captured and exactly where it stands.

### Acceptance Criteria

**Case: the immediate echo**

1. *when* a wish is captured, the system *shall* echo it back in one plain sentence stating what was heard, which door it entered, the name the work goes by, and its row number. [INV-27]
2. *when* a wish arrives silently — dropped into an inbox as a file, or pulled from a batch — the system *shall* carry its echo in the next status report rather than as an interruption. [INV-27]
3. *when* a wish is bridged in from a stranger's Issue, the system *shall* also post its echo on that Issue, since the stranger reads no status report of the host's. [INV-146, INV-147]

**Case: the status report names each stage**

4. The system *shall* have every status report name each in-flight feature and the one pipeline stage it sits at, drawn from the nine steps in fixed order — spec, prove, architecture, prove architecture, matrix, test, code, verify, and commit-and-show. [INV-27]
5. The system *shall* report a paused feature under its stage's name and *shall* read landed as a terminal state that is not itself a pipeline step. [INV-27]
6. The system *shall* have the echo also state where the wish sits on the product's feature map. [INV-27, INV-37]

---

## Requirement 13: Every wish is placed on the feature map by one of three verdicts

**Context:** Every wish is placed on the product's feature map, and the placement is stated by default. The feature map is the spec's scenario sections and the architecture's nodes together, so no separate map document exists. Each placement is one of three verdicts: it changes an existing feature, it is a new feature, or it is a restructure.

**User Story:** As a person tracking where a wish lands in the product, I want its placement stated and recorded as one of three verdicts, so that the map stays the spec plus the architecture and a restructure opens its own row rather than re-dividing on the spot.

### Acceptance Criteria

**Case: the three placement verdicts**

1. *when* a wish is captured, the system *shall* place it on the feature map — the spec's scenario sections and the architecture's nodes together — as one of three verdicts: it changes an existing feature and names that scenario, it is a new feature with its own scenario section and architecture node, or it is a restructure. [INV-37, E-14]
2. *when* the verdict is restructure, the system *shall* open its own row — the refactor door where only structure moves, the feature door where behaviour moves with it — and *shall* carry the re-division through the architecture stage and its re-proof rather than re-dividing on the spot. [INV-37, E-14]

**Case: placement reports, records, and defers the structure change**

3. The system *shall* let a placement report that the structure no longer fits, yet *shall* alter the structure only through a completed change. [INV-37]
4. The system *shall* place a bug on the feature it repairs, and *when* the classifier cannot determine a wish's feature *shall* ask the person. [INV-37, INV-12]
5. The system *shall* record the verdict in the wish's row as a note — a named changed feature, new, or restructure — so the placement stays searchable after the report scrolls away. [INV-37, T-14]

---

## Requirement 14: The outcome does the talking, and every handle trails

**Context:** The outcome does the talking: names are plain and every handle trails. A feature's echo-name is a short descriptive phrase in the product's own words that a reader who missed its birth can parse cold. A human-facing report or board line opens with what changed for the reader, and every internal handle trails in parentheses. Bookkeeping numbers are handles too.

**User Story:** As a reader who did not watch the work, I want every line to lead with what changed for me while codes and counts only trail, so that I get the outcome in plain words without decoding an internal handle.

### Acceptance Criteria

**Case: names are plain**

1. The system *shall* give a feature a short descriptive echo-name in the product's own words that a reader who missed its birth can parse cold, and *shall* not use a private metaphor. [INV-28]
2. The system *shall* read a name that needs its story told first as a bare handle. [INV-28]

**Case: the line leads with the outcome**

3. The system *shall* open a human-facing report or board line — a chat report, a narration line, a report page, a decision page, or the capture echo — with what the reader can now do, see, or stop fearing, and *shall* keep every internal handle, a spec code, a row or session number, or a coined name, trailing in parentheses. [INV-28, INV-35]
4. The system *shall* give one fact one standalone sentence and *shall* read a compression that needs the writer's own context to parse as a defect of the line. [INV-28]

**Case: bookkeeping numbers are handles**

5. The system *shall* keep a bookkeeping number — a test count, a suite size, a version string, or a check tally — out of the message content, stating what the number means for the reader while the number only trails or stays in the records. [INV-28]
6. *when* the number is the asked substance — a direct question about it, or the done-claim evidence walk that pins its artifact and method version — the system *shall* let the number itself be the content. [INV-28, INV-25]

**Case: the laws have a mechanical voice**

7. The system *shall* inject through the prompt hook `hooks/chat-law-hook.sh` a reminder of the chat laws into every prompt — plain words with codes trailing, the narration beats, the say-what-it-is line (naming a thing by its own positive sentence), the banned contrast frame (naming a thing by denying its neighbour, the `"X, not Y"` shape), and the routing line by which the orchestrator seat routes work to the cheapest tier the routing rule names while a worker finds for itself the files and lines its task needs, so the orchestrator's context stays lean — the skills and the profile staying the laws' homes. [INV-28, INV-69, INV-137]
8. Before a human-facing artifact is shown, the system *shall* have `scripts/preshow-lint.py` flag any line opening with an internal handle so the agent rewrites it to lead with the outcome, a warning to clear that reads only the shown surface. [INV-28]

---

## Requirement 15: Anything shown to a person passes a register lint first

**Context:** Anything shown to a person passes a register lint before it is shown. The check reads the text for machine dialect — a coined internal metaphor shown raw, an English pack term calqued into another language, or a transliterated pack term. A red result blocks the showing until the text reads in the reader's own plain words.

**User Story:** As a person about to read a shown surface, I want its machine dialect caught and blocked before it reaches me, so that a coined metaphor or a calque never reaches my eyes as nonsense.

### Acceptance Criteria

**Case: the lint blocks the showing**

1. Before a human-facing surface is shown, the system *shall* have `scripts/preshow-register-lint.py` read its text and block the showing on a red result until the flagged text is rewritten into the reader's plain words. [INV-83]
2. The system *shall* treat this as a hard block, and *shall* scope its reach to the shown artifact — a rendered page, a mockup, a decision page, or a report page. [INV-83, INV-34]

**Case: the class the list cannot hold**

3. The system *shall* keep the literal pattern set as the free first pass and *shall* grow it by nobody's duty, since a growing list stays one escape behind the next word. [INV-83]
4. The system *shall* hand the residual machine-dialect class to the register judge, the model that reads meaning at the cheapest tier the routing rule names, standing as the ceiling the literal list cannot reach. [INV-83, INV-203, INV-69]
5. The system *shall* hold the chat line by the register judge's chat arm, the mechanical gate for the chat surface. [INV-203]

---

## Requirement 16: No line certifies its own sincerity

**Context:** No line certifies its own sincerity. A sentence that praises its author's honesty, directness, or diligence carries no information, since naming a quality informs only where its absence stood as a live alternative. The content carries the honesty; the label comes off.

**User Story:** As a person reading the pack's reports, I want a self-praising sincerity label stripped from every line, so that the honesty stays in the content rather than in a phrase that distinguishes nothing.

### Acceptance Criteria

**Case: the label comes off every surface**

1. The system *shall* strip a sentence that praises its author's honesty, directness, or diligence, since a report whose every line is meant to be true distinguishes nothing by saying so. [INV-94]
2. The system *shall* bind this across every surface — a shown artifact through the register lint, and the chat through the session's own read and the hook's reminder. [INV-94, INV-83]

**Case: the register judge holds the class**

3. The system *shall* have the register judge hold this class, a caught phrase informing the judge and the literal first pass while the pattern list grows by nobody's duty. [INV-94, INV-203]

---

## Requirement 17: The report law is walked as a live step

**Context:** The report law is walked as a live step each time, since chat has no suite to enforce it. Before any movement-end or milestone report reaches the person, the agent re-reads the communicator rules and passes the draft phrase by phrase through one question: does this sentence stand for a reader who does not live inside the pack?

**User Story:** As a reader outside the pack, I want every report walked phrase by phrase before it reaches me, so that a report I read lands understood rather than making me ask what a named surface is.

### Acceptance Criteria

**Case: the walk before every report**

1. Before any movement-end or milestone report reaches the person, the system *shall* re-read the communicator rules and pass the draft phrase by phrase through the outside-reader question. [INV-34]
2. The system *shall* explain any pack surface the draft names in the reader's own words or drop it, while quiet trailing anchors stay legal. [INV-34]
3. The system *shall* read a report that makes the reader ask what a thing is as the walk not walked, its acceptance belonging to the reader. [INV-34]

---

## Requirement 18: A question walks the same scan and one gate more

**Context:** A question to the person walks the same phrase-by-phrase scan a report walks, and one gate more, asked first: can I decide or verify this myself? A question that fails that gate is work, done instead of asked. A question that survives it arrives with its recommendation attached.

**User Story:** As a person asked only what I alone can settle, I want every question gated by can-the-agent-decide-this-first, so that a question the agent could answer itself becomes work done and a surviving question arrives with a recommendation.

### Acceptance Criteria

**Case: the scan and the extra gate**

1. Before any question is asked — in a report's batched tail, on a decision page, or as a lone ask in chat — the system *shall* pass it through the same phrase-by-phrase read, every term grounded in the reader's own words. [INV-81, INV-34]
2. The system *shall* ask first whether it can decide or verify the answer itself, and *shall* turn a question that fails that gate into work done rather than asked. [INV-81, INV-4, INV-5]
3. The system *shall* have a question that survives the gate arrive with its recommendation attached. [INV-81, INV-60]

---

## Requirement 19: Work is narrated while it runs

**Context:** Work is narrated while it runs, the third voice between the capture echo and the delivery report. The person leads many windows at once, so otherwise silence is all they get. While work runs, the agent says each beat worth a sentence — a stage passed, a load-bearing find, a change of direction — in the roadmap's terms and the reports' voice.

**User Story:** As a person leading many windows, I want each beat of running work narrated in plain roadmap terms, so that a silent stretch never reads to me as lost work.

### Acceptance Criteria

**Case: beats are narrated as they happen**

1. *while* work runs, the system *shall* say each beat worth a sentence in one or two plain sentences in the roadmap's terms, and *shall* keep the mechanical grind quiet. [INV-35]
2. The system *shall* name in every beat the work it belongs to — which wish is in hand and which pipeline stage it stands at, and whether it mends something broken or builds something new. [INV-35]
3. *when* a station completes, the system *shall* make its line a beat carrying a short digest of what the station produced in the work's own words. [INV-35]

**Case: the heartbeat and the detached run**

4. *when* a stretch runs long with no beat, the system *shall* say what is grinding and why the stretch runs long, owing this heartbeat past a beatless stretch of about 10 minutes as a default. [INV-35]
5. *when* an operation runs detached past about 2 minutes, the system *shall* open with a start line naming what runs, where its log lives, and an honest range, keep a beat landing about every 2 minutes or at each stage, and close with a done digest. [INV-35, INV-93]

**Case: the offline window**

6. *when* the coming stretch needs nothing from the person, the system *shall* say so before it starts — that the person may step away, an honest range for how long, and what the person is needed for at its end — stating an unknown duration as unknown. [INV-35]
7. *when* the person is needed again, the system *shall* say so plainly as a beat naming the gate or decision that waits, batching questions born inside the window to its end. [INV-35, INV-4]

**Case: narration is chat-register**

8. The system *shall* keep a narration line an informal chat message that walks no pre-report walk, asks nothing, and replaces no report, while every human-facing-line law still binds. [INV-35, INV-27, INV-28]

**Case: the delegated beat and the time accounting**

9. *when* a delegated worker closes a station, the system *shall* fold it into the trail, a station a delegated worker closed becomes the senior's beat the moment it lands, the trail the session's time accounting where token and test counts stay bookkeeping. [INV-35, INV-28]

**Case: the offline window's honest edges**

10. *when* the offline window runs, the system *shall* keep its edges honest, never a guess dressed as a promise, a window off its spoken range saying so, overrun, done sooner, or blocked on the human's word alone, the needed-again beat a chat line awaiting his return, never a summons, and no offline sentence fires when the very next beat needs the human. [INV-35, INV-4]

---

## Requirement 20: Every ask hears its price in time, and the landing settles it

**Context:** Every ask hears its price in time, and the landing settles it. The capture echo carries an honest time range read from the work's known shape or observed runs, an unknown stated as unknown. Work expected to run an hour or more is explained up front in plain steps. The delivery report states the estimate beside the actual.

**User Story:** As a person who owes time to a task, I want an honest range at capture and the estimate settled against the actual at landing, so that I know what a task costs before it starts and how the guess held afterward.

### Acceptance Criteria

**Case: the range at capture and the settling at landing**

1. The system *shall* carry in the capture echo an honest time range read from the work's known shape or observed runs, stating an unknown as unknown. [INV-93, INV-27, INV-35]
2. *when* work is expected to run an hour or more, the system *shall* explain it up front in plain steps — what has to happen and why it takes that long — and *shall* say on the heartbeat how much time remains as the stretch runs. [INV-93, INV-35]
3. *when* a wish lands, the system *shall* state the estimate beside the actual in the delivery report, saying an overrun or an under plainly. [INV-93]
4. *when* a direct command holds the session for more than a beat, the system *shall* have it hear its range even though it registers no row. [INV-93]
   [GAP: the beat's duration for a direct command's range announcement is unstated in the source.]

---

## Requirement 21: A rewrite that removes substance accounts for it

**Context:** A rewrite that removes substance accounts for it in the delivery report. A restyle or a restructure drops content as it tightens, and some of what it drops carries weight — a section, an argument, a rationale, a worked example. The rule scopes to substance and leaves line-level wording free.

**User Story:** As a person whose document a rewrite tightened, I want every removed piece of substance accounted for in the report, so that deleted content is kept and cited, killed by my own word, or raised as a question rather than cut silently.

### Acceptance Criteria

**Case: every removal is accounted for**

1. *when* a rewrite or restyle removes substance — a section, an argument, a rationale, or a worked example — the system *shall* list every removal in the delivery report with one line of judgment each: the fact was kept and where, the person killed it by name, or the rewriter proposes dropping it and asks. [INV-109]
2. The system *shall* turn a removal the rewriter cannot justify into a question before the report closes, and *shall* not cut substance silently. [INV-109]

**Case: line-level wording stays free**

3. The system *shall* scope this accounting to substance and *shall* leave a tightened sentence or a reordered clause needing no account. [INV-109]

---

## Requirement 22: One spoken leave-word winds the session down to a safe stop

**Context:** One spoken leave-word winds the session down to a shutdown-safe stop. When the person says they are leaving, the session stops taking new work and walks what is open to a safe point: background workers halt or run to their landing, every open lane reaches its checkpoint, green work is committed under its gates, and the resume file says what resumes where.

**User Story:** As a person about to close or sleep the machine, I want one leave-word to bring the session to a shutdown-safe stop, so that no worker dies mid-write, no red work is committed, and I am told plainly when it is safe to power off.

### Acceptance Criteria

**Case: the wind-down to a safe point**

1. *when* the person says they are leaving, the system *shall* stop taking new work and *shall* halt background workers or run them to their landing, recording any worker that cannot halt in time by the handoff discipline — a note carrying the worker's id, the exact files its brief lets it write, and the liveness checks a resuming session runs before touching them. [INV-95, INV-76]
2. The system *shall* bring every open lane to its checkpoint, committing green work under its standing gates and committing no red work, with the failing test name and hypothesis topping the resume file. [INV-95]
3. The system *shall* have the resume file say what resumes where. [INV-95]

**Case: the closing line and its timing**

4. The system *shall* answer in the first beat roughly how many minutes remain to the safe point, and *shall* give as its last a single closing line — safe to power off, plus what resumes where on return — said only *when* every point above holds. [INV-95, INV-93]
5. The system *shall* ride the remaining-minutes habit on long work even before any leave-word, and *shall* never guess from silence that the person is leaving. [INV-95, INV-35]

---

## Requirement 23: Anything handed to the person opens with a one-line identifier

**Context:** Anything handed to the person opens with a one-line identifier. A page that opens in the browser states two things: which project it belongs to, and whether it needs the person's attention. A page that states neither reads as noise.

**User Story:** As a person who finds a page open in my browser, I want it to name its project and say what it needs of me, so that I always know what I am looking at and what it asks.

### Acceptance Criteria

**Case: the identifier states project and need**

1. The system *shall* show the project's name in a handed page's visible content, not only in its URL. [INV-51]
2. The system *shall* state what the page needs from the person — a word, with what and by when, or that it is only an update with no action. [INV-51]
3. The system *shall* lead every handed or opened artifact — a report page, a decision page, or a rendered doc — with that identifier, and *shall* carry the same two facts in the chat line that announces it. [INV-51]

---

## Requirement 24: During an away-stretch, artifacts accumulate on one page

**Context:** During an away-stretch, artifacts accumulate and one window opens at the end. When the person has stepped away for an overnight loop or an offline window, the agent does not open a browser window mid-stretch. Artifacts accumulate on one page.

**User Story:** As a person who stepped away, I want artifacts gathered on one page that opens once at the end, so that an overnight stretch never scatters windows across my screen.

### Acceptance Criteria

**Case: one page for the away-stretch**

1. *while* the person is away for an overnight loop or an offline window, the system *shall* not open a browser window mid-stretch and *shall* accumulate the stretch's decisions and report on one page. [INV-52, INV-35]
2. The system *shall* allow a mid-stretch re-open only as that same page refreshed in place. [INV-52]

---

## Requirement 25: The showing channel matches where the session runs

**Context:** The showing channel matches where the session runs. A session on the person's own machine shows a rendered artifact as a local page in a browser window. A remote session runs in the cloud, is read through a browser, and cannot open a local page, so it shows the same content through its own channel.

**User Story:** As a person reading a session that may run locally or in the cloud, I want it to show through the channel its seat can reach, so that a remote session never hands me a local file path that opens into nowhere.

### Acceptance Criteria

**Case: the seat picks the channel**

1. The system *shall* read where the session runs from what it can reach — the platform, the display, and whose filesystem it sees — and *shall* name the channel it picked. [INV-67]
2. The system *shall* show a local session's artifact as a local page in a browser window, and *shall* show a remote session's artifact through its own channel — an artifact page the host renders, or the chat itself — carrying the same identifier and the same round-trip. [INV-67, INV-51]
3. The system *shall* re-read the seat after any move between machines, and *shall* read handing a local file path to a remote reader as a defect of the exchange. [INV-67]

---

## Requirement 26: The current state of the work is answerable in any setting

**Context:** The current state of the work is answerable at any moment, in any setting. The harness's own task panel and activity line are a convenience of the local terminal, absent in a browser and stalling on a long run of tool calls. So the live status lives in the chat, the one surface present in every setting.

**User Story:** As a person who looks in at any moment, I want the work's state kept current in the chat, so that a glance answers what we are working on and what comes next whatever setting I read from.

### Acceptance Criteria

**Case: the status lives in the chat**

1. The system *shall* keep a short status current in the chat — a Now line naming the work in hand and its pipeline stage, and a Next line naming what the queue holds next. [INV-71, INV-67]
2. The system *shall* refresh the status at every stage change and *shall* carry a heartbeat on a long stretch. [INV-71, INV-35]

**Case: the harness panel is a courtesy view**

3. The system *shall* keep the harness task panel, where a setting shows it, in plain product words as a courtesy, and *shall* not make it the home of the status. [INV-71, INV-28]
4. The system *shall* offer a rendered status page as an optional richer view of the same Now and Next on a local session, and *shall* apply this to every project the pack runs. [INV-71, INV-67]

---

## Requirement 27: The end of a stretch is delivered so the person cannot miss it

**Context:** The end of a stretch is delivered so the person cannot miss it. A report that exists but sits above tool noise counts as undelivered. When a stretch ends, the last rendered thing is one short final line.

**User Story:** As a person who might miss a report buried above tool output, I want one short final line as the very last thing rendered, so that I can never miss where the run ended.

### Acceptance Criteria

**Case: the final line comes last**

1. *when* a stretch ends — a loop iteration going to sleep, an away-stretch closing, or a session ending — the system *shall* render as the last thing one short final line carrying what closed, what is next, what is needed from the person, and when the agent wakes. [INV-57]
2. The system *shall* place the long report above that line and *shall* render the final line last, after every tool call. [INV-57]
3. The system *shall* repeat a page deliverable's identifier in that final line. [INV-57, INV-51]

---

## Requirement 28: A review surface shows its sources and accepts the person's edits

**Context:** A review surface shows its sources and accepts the person's edits. Anything shown for review carries per-claim provenance, marking each claim by where it came from — read from the artifact, the person's own recorded word, or the agent's inference. Inferences are flagged most prominently.

**User Story:** As a person reviewing a surface the agent shows, I want each claim marked by its source and the surface open to my edits, so that no work reaches me as a read-only wall or an unmarked guess.

### Acceptance Criteria

**Case: per-claim provenance**

1. The system *shall* mark each claim on a review surface by where it came from — read from the artifact, the person's own recorded word, or the agent's inference — and *shall* flag an inference most prominently. [INV-64]

**Case: the surface is commentable**

2. The system *shall* keep the surface commentable and open, giving line-by-line room for the person's word and capturing the answers. [INV-64]
3. The system *shall* extend the decision page's saved-answers rule to a review surface as one round-trip back to the project. [INV-64, INV-32]

---

## Requirement 29: The person's word is read as meant, and the person's cuts hold

**Context:** The person's word on a shown artifact is read as meant, and the person's cuts hold. A phrasing the person removed in a review round stays removed in every later draft of that artifact. A vivid phrase from the person is adopted only as meant, since a person sometimes writes mockery of a bad draft rather than guidance.

**User Story:** As a person who cut a phrasing and wrote a colorful remark, I want the cut to hold across every later draft and the remark read for its intent, so that a cut word never reappears and a parody is never baked in as if prescribed.

### Acceptance Criteria

**Case: a cut holds across drafts**

1. The system *shall* keep a phrasing the person removed in a review round removed in every later draft of that artifact, holding the removal list where the artifact's project keeps its records rather than in session memory alone. [INV-42]
2. The system *shall* read a cut word reappearing a later round as a defect, however fresh it looks, since a memory wipe restores no cut phrasing. [INV-42]

**Case: a vivid phrase is read for intent**

3. Before a colorful phrase from the person shapes the work, the system *shall* read its intent from context or ask, rather than assuming a mockery of a bad draft is prescriptive. [INV-42, INV-4]
4. The system *shall* cross-link the two standing bans this rests on — no self-praising drama, and no approval-begging under silence-is-consent — rather than restate them. [INV-42, INV-31]

---

## Requirement 30: Approved text is frozen, and a revision applies only the named correction

**Context:** Approved text is frozen, and a revision applies only the named correction. Once the person approves a text it is settled material. A later revision applies exactly the correction the person named and does not rewrite the surrounding text.

**User Story:** As a person who approved a text, I want a later revision to apply only the correction I named, so that approved material never churns under a rewrite I did not ask for.

### Acceptance Criteria

**Case: only the named correction lands**

1. *when* the person approves a text, the system *shall* treat it as settled material. [INV-58]
2. *when* a revision is applied, the system *shall* make exactly the correction the person named — trim what they said to trim, swap what they said to swap — and *shall* leave the surrounding text untouched. [INV-58]
3. The system *shall* read churn of approved material as a defect, kin of a reappearing cut. [INV-58, INV-42]

---

## Requirement 31: No question is asked twice, and dialogues converge

**Context:** No question is asked twice, and dialogues converge. Before any ask, the agent searches the recorded word — the decision archives, the review records, the journal, and the profile. An answered question closes permanently and is recorded into its row the same session.

**User Story:** As a person whose answers are on record, I want the agent to search them before asking and to close an answered question for good, so that I am never asked a question a record already answers and a solved problem returns with evidence rather than re-described.

### Acceptance Criteria

**Case: the search before every ask**

1. Before any ask, the system *shall* search the recorded word — the decision archives, the review records, the journal, and the profile — and *shall* read asking a question a record already answers as a defect. [INV-59]

**Case: dialogues converge**

2. The system *shall* close an answered question permanently and record it into its row the same session. [INV-59]
3. The system *shall* return a problem the person named solved with evidence rather than re-described, so a later round carries only new material. [INV-59]

---

## Requirement 32: A taste ask arrives carrying the agent's own researched proposal

**Context:** A taste ask arrives carrying the agent's own researched proposal. A genuine taste question arrives with work already done — mined exemplars, precedents, and real options with citations — and a chosen recommendation with its evidence.

**User Story:** As a person asked a taste question, I want it to arrive with the agent's own research and a recommendation, so that I am never asked to supply what the agent should have mined first.

### Acceptance Criteria

**Case: research precedes the ask**

1. The system *shall* mine the material first — exemplars, precedents, and real options with citations — and *shall* then ask with a chosen recommendation and its evidence. [INV-60]
2. The system *shall* read asking the person to supply what the agent should have mined as a defect, this sharpening the recommended-option rule for a taste call. [INV-60, INV-4]

---

## Requirement 33: The removal list has a mechanical form

**Context:** The removal list has a mechanical form. For a host with taste-reviewed artifacts, the pack ships a removal-list template that holds the person's cuts as dated literals, appended the moment a cut happens and never removed. The pack also ships guardrails guidance for a scanner.

**User Story:** As a person whose cuts must hold, I want the removal list backed by a shipped template and a scanner, so that a literal I once cut turns the suite red if it reappears in the artifact's surfaces.

### Acceptance Criteria

**Case: the template and the scanner**

1. The system *shall* ship a removal-list template holding the person's cuts as dated literals, appended the moment a cut happens and never removed. [E-26]
2. The system *shall* ship guardrails guidance for a scanner that reads the table and greps the artifact's surfaces, turning the suite red *when* a removed literal reappears. [E-26, INV-42]

**Case: the scanner stays per-project**

3. The system *shall* keep the scanner per-project, the pack shipping the shape — the template and the guidance — while each host owns the greps that read its own surfaces and holds its own dated cuts. [E-26, INV-163]
4. *when* a host's scanner grows a genuinely generic seam, the system *shall* lift that seam to the pack and *shall* keep the host-specific greps at home. [E-26, INV-163]
