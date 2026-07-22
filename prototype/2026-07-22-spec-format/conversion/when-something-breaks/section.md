# When something breaks

This section states what happens when the normal flow is interrupted: a live bug in the shipped product, and the workshop itself misbehaving. It is written for a reader who has never seen the pipeline before.

Bracket codes like `[T-9]` and `[INV-23]` point to the rule's home in the project spec; a reader can ignore them, a maintainer follows them. The letter before the number names the kind: `INV-` an invariant (a numbered rule that must always hold), `E-` an entity (a numbered part of the product), `T-` a transition (a numbered change of state), `M-` a rhythm rule (a numbered recurring routine), `ACT-` an actor, `B-` a bootstrap step, and `F-` a feature the section realizes. The keywords *when*, *while*, *if*, *then*, and *shall* are set in italics and carry their standard requirements meaning: *shall* states a duty, *when* and *while* open a situation, *if* and *then* open a condition and its result.

Terms already defined in the intake glossary and the founding, agents-together, and bounds sections — request, inbox, pipeline, spec, architecture, invariant, guardrail, suite, host, pack, session, journal, attic, queue, movement, delivery, milestone, project kind, and their siblings — carry their meanings unchanged. A handful of build-loop nouns this section leans on — bug, feature, wish, lane, checkpoint, station, node, feature door, kill-list, the fence, the prover, worker, the batched report, compaction — are owned by their home sections and defined there. The block below adds only the new nouns this section introduces.

## Glossary additions

- **problem ledger** — the host's list of the workshop's own operational noise, one git-tracked file `.live-spec/PROBLEMS.md`, born on its first entry.
- **signature** — one entry in the problem ledger: a short greppable plain phrase that names a recurring operational problem, carrying its dated occurrences and one status.
- **workshop noise** — a problem that comes from the workshop rather than the product: a test harness or tool that flakes, a missing dependency, a shell command that fails outside the product, a tool that times out.
- **class hunt** — the search a confirmed bug drives before it closes: name the defect abstractly, find every sibling of that kind, and fix them in one change.
- **priority bubble** — the one way priority reorders the lane: a marked wish jumps ahead of the fresh queued wishes, visibly, straight to the queue head. The intake classification writes the mark — critical or quick win — on the wish's row; an unmarked row carries normal priority.
- **delta** — the drafted change a wish or feature makes to the spec, proven against the whole spec before it lands.
- **crafts** — the professions a project's own work already draws on, such as a product manager, an architect, a test engineer, or a senior developer, matched against the project's kind when the fit list is proposed.

---

## Requirement 1: A bug preempts the lane, and rolling features park  [feature: F-bug]

**Context:** Mid-feature, the human reports a bug in the shipped product — the card is broken on the phone. The feature in work is set aside at a checkpoint, the bug takes the lane, and once no bug waits the feature returns as the next thing to finish. When nothing is in work, the bug takes the lane directly.

**User Story:** As the product owner, I want a reported bug fixed before anything else while the mid-build feature comes back on its own afterward, so that an urgent defect is handled at once and no in-flight work is lost.

### Acceptance Criteria

**Case: the bug takes the lane, the feature parks**

1. *when* a bug report arrives mid-feature, the system *shall* move the feature to parked with a checkpoint written first — the failing test names when any are red, the current hypothesis, and the touched files — and *shall* commit no work while a test is red. [T-9]
2. *when* the bug holds the lane, the system *shall* run it to completion, and *shall* have an arriving bug join the waiting line and interrupt nothing. [T-9]
3. The system *shall* order waiting bugs critical-first and bugs of equal priority by arrival. [T-9]
   [GAP: the source orders waiting bugs critical-first but names no judge or measure for a bug's priority, so which bug counts as critical is undecidable at the line.]

**Case: resume order and the parking bound**

4. *when* no bug waits, the system *shall* resume parked features ahead of the whole queue. A wish marked critical or quick win may bubble. It jumps only fresh queued wishes. It never jumps a resume. [T-11]
5. The system *shall* park at most one feature per lane, and *when* more than one lane was rolling *shall* park them all, each at its own checkpoint, resuming in their landing order. [T-18]

**Case: a resumed feature re-proves on the new tree**

6. *when* a parked feature resumes, the system *shall* re-fence and re-prove its delta against the now-committed truth before it integrates, since the bug's fix may have moved the law the delta was built against. [T-9, INV-39]
7. The system *shall* integrate no delta proven only against the pre-bug truth without re-verifying it on the new tree, and *shall* leave every parked feature back in work or landed in its original order once the fix has landed, with no red work committed anywhere. [T-9, INV-39]

---

## Requirement 2: A confirmed bug drives a class hunt before it closes  [feature: F-bug]

**Context:** A confirmed bug is one sample of its class. Before the fix is called done, the method drives four moves rather than one, so a point fix that leaves the rest of the class standing is a status, never a landing.

**User Story:** As the product owner, I want a confirmed bug treated as one instance of a class and its siblings hunted before the fix closes, so that the same kind of defect is cleared everywhere it lives rather than patched where it happened to show.

### Acceptance Criteria

**Case: name the class and hunt its siblings**

1. *when* a bug is confirmed, the system *shall* name the defect abstractly — the kind of mistake, a scope too narrow, a missing guard, an assumption that holds in one place and fails in its neighbour — then search every surface where that kind could live and fix every sibling found in the same change. [INV-124, INV-56]

**Case: check the architecture and the spec**

2. *when* the bug has a structural cause — a boundary the architecture drew wrong or left silent, a node owning what it should not — the system *shall* update the architecture in the same change. [INV-124]
3. *if* the spec is silent on the broken behaviour or under-describes its composition, *then* the system *shall* fix the spec first so the prover can flag it, and *shall* land the code fix under it. [INV-124, INV-15]

**Case: escalate a boundary call, and the close condition**

4. *when* the class boundary needs the human's read — which behaviours are one class, the intended design, whether a whole area wants a rethink — the system *shall* stop and ask rather than guess the boundary. [INV-124, INV-4]
5. The system *shall* treat the four moves as the bug's close condition, and *shall* read a point fix that leaves the siblings standing as a status rather than a landing. [INV-124, INV-26]
6. The system *shall* have the prover carry a class lens on a found defect — whether the same kind lives elsewhere, whether the architecture accounts for it, and whether the spec describes it. [INV-124]

---

## Requirement 3: The problem ledger holds the workshop's own noise  [feature: F-problem-ledger]

**Context:** Some noise comes from the workshop itself: a test harness or tool flakes at random, a dependency goes missing, a shell command fails for a reason outside the product, a tool times out. A session retries and moves on, and then the same noise eats the same minutes session after session. A flaky test the project itself owns is a different thing, a defect fixed at its root and never workshop noise.

**User Story:** As a person losing minutes to recurring operational noise, I want each workshop problem recorded in one ledger with a status, so that noise seen twice gets a tracked owner instead of being rediscovered and retried each session.

### Acceptance Criteria

**Case: the ledger and its home**

1. The system *shall* keep the workshop's operational noise in the problem ledger, one git-tracked file `.live-spec/PROBLEMS.md`, born on its first entry, and, within `.live-spec/`, *shall* keep only the checkpoints git-ignored. [E-24, E-8]
2. *when* a test the project itself owns flakes, the system *shall* read it as a defect fixed at its root, never workshop noise and never a retry. [INV-155]

**Case: the signature and its status**

3. The system *shall* record each entry as a signature — a short greppable plain phrase — carrying its dated occurrences and one status. [E-24]
4. The system *shall* hold the four statuses: `watched` when seen once, `owned` when a named queue row will solve it, an `agreed non-problem` dated on the human's word, and `solved` when its row landed with the date kept. [E-24]

---

## Requirement 4: The ledger walk and its two-strikes ladder  [feature: F-problem-ledger]

**Context:** The moment noise fires mid-work, the session greps the ledger for the signature, and what the grep returns decides the next move. The walk climbs a fixed ladder from a first sighting to a method defect.

**User Story:** As a person meeting operational noise mid-work, I want the ledger walk to record a first sighting, buy an owner on the second, and escalate a third unowned recurrence to the pack, so that a problem seen twice is never silently retried and a method defect reaches the pack's own queue.

### Acceptance Criteria

**Case: a first sighting**

1. *when* noise fires and its signature is not listed, the system *shall* write one `watched` line — signature, date, one line of context — and keep working, replacing the silent retry and never taking the lane. [INV-23]
2. *if* the noise is a defect of the product, *then* the system *shall* send it to the bug lane instead. [T-9]

**Case: the second occurrence buys an owner**

3. *when* a listed signature fires a second time, the system *shall* pick the branch its own read of the signature supports: a problem that needs solving gets a queue row the system opens itself, closing the duty at once; a signature that reads as noise gets a written no-problem recommendation, and that no-problem verdict stays the human's alone. [INV-23, INV-9]
   [GAP: the measure separating a problem that needs solving from noise at the second occurrence is unstated in the source; the seat's own read picks the branch and the human's dated word settles a no-problem close.]
4. *when* the branch is the no-problem recommendation, the system *shall* write it right away and let the ask ride the batched report; the recommendation is a pending owner only, so the signature stands without an owner of record until the human's dated word lands, and the lane never stalls on it. [INV-4, E-22]

**Case: a third unowned recurrence is a method defect**

5. *when* a signature recurs a third time with no queue row open on it and no human word closing it, the state a pending no-problem recommendation still riding the batched report leaves it in, the system *shall* file it as a defect of the method that reaches past a single day, leaving the host as one inbox file to the pack's own queue and citing the signature and its dates. [INV-23, E-11, INV-10]

---

## Requirement 5: A resolved entry collects dates and archives at the milestone  [feature: F-problem-ledger]

**Context:** Once an entry has its owner, it only collects dates. A recurrence appends a date and changes nothing else, and a landing that closes the owning row flips the entry closed in the same session rather than waiting for an audit.

**User Story:** As a person tracking an owned problem, I want a recurrence to only append its date and a landing to close the entry at once, so that the ledger stays current without a recurrence reopening a settled verdict or an audit lagging the truth.

### Acceptance Criteria

**Case: an owned entry only collects dates**

1. *when* an `owned` or `agreed non-problem` entry recurs, the system *shall* append its date and change nothing else. [E-24]
2. The system *shall* leave the re-raising of an agreed non-problem to the human, who re-raises it from the growing date list. [INV-9]

**Case: a landing closes the entry in its own session**

3. *when* a landing closes an `owned` entry's queue row, the system *shall* flip that entry to `solved` the same session, the entry never waiting for an audit to learn its row landed. [E-24]

**Case: archival at the milestone**

4. *when* the milestone compaction runs, the system *shall* move `solved` and agreed entries to a dated archived tail of the same file, keeping one file as the one home so the ledger never grows without bound. [M-1]

---

## Requirement 6: A known owned problem stays parked while unrelated work rolls  [feature: F-problem-ledger]

**Context:** A known, owned problem never blocks unrelated work; it stays parked while every unrelated lane keeps rolling. It is either a recurring defect with a named mechanical owner or a check held red for an understood, recorded reason, held in place by its ledger line, its owning row, or an expected-red note.

**User Story:** As a person with one known problem parked, I want every unrelated lane to keep rolling and the problem's instances serviced in batch, so that one thing not quite working never blocks the rest and never interrupts the work with a per-instance ceremony.

### Acceptance Criteria

**Case: the parked problem lets unrelated work move**

1. The system *shall* keep a known, owned problem parked while every unrelated lane keeps rolling, held in place by its ledger line, its owning row, or an expected-red note. [INV-56]

**Case: two rules keep it parked**

2. The system *shall* cap hand-fixing loops at the two-strikes law, the second occurrence buying an owner rather than another hand-pass. [INV-56]
3. *when* a defect has a named mechanical owner, the system *shall* service its instances in batch — the fence fixing them silently wherever it catches them, then appending one ledger line at the session's end — with no per-instance ceremony interrupting the work or the human reading it. [INV-56]

**Case: a real bug still preempts**

4. *when* a real new bug arrives, the system *shall* let it preempt, this parking law governing only the known, owned problem. [T-9, INV-56]

---

## Requirement 7: The ledger's seams and the scope of this landing  [feature: F-problem-ledger]

**Context:** The ledger's seams state who writes it, how two sessions share it, when two entries are one problem, and where the workshop's law ends and the product's begins. The landing opens the pack's own ledger and leaves the mechanical guard for later.

**User Story:** As a person maintaining the ledger across sessions and workers, I want its write-ownership, concurrency, and merge rules stated and this landing's scope named, so that a worker's noise reaches the ledger safely, two sessions never clobber it, and one problem under two wordings becomes one entry.

### Acceptance Criteria

**Case: who writes the ledger**

1. The system *shall* have sessions write the ledger, a worker reporting noise in its checkpoint for the session to carry over, and a worker whose brief names the ledger among its files writing it directly, the brief stating the write-ownership law. [ACT-3]
2. The system *shall* have two sessions on one host share the file under the concurrent-edit fence, like any document. [INV-11]

**Case: one problem, one entry**

3. *when* two entries are judged one problem by grep and eyes, the system *shall* merge them into a single entry at the milestone compaction, signatures staying short so the grep stays honest. [M-1]

**Case: the workshop's law ends at the product**

4. The system *shall* keep this the workshop's law while the product keeps its own, and *when* a product bug recurs *shall* re-door it to a feature under the pipeline's rule, distinct by what broke. [T-9]
5. The system *shall* carry no visible surface for the ledger, so the standard feature checks — phone behavior, touch, empty, error, and loading states, accessibility, and performance — do not apply. [E-24]

**Case: what this landing does not add**

6. The system *shall* add no mechanical guard yet, the named candidate — a pre-push check that no entry crosses a milestone unowned — earning its row after real usage. [E-24]
7. The system *shall* add no automated signature matching, and *shall* open the pack's own ledger this landing while a foreign host opens its ledger from its own window. [E-24, INV-10]

**Case: the success measure**

8. The system *shall* land the next operational hiccup in a session as a ledger line rather than a silent retry, checked at the milestone audit. [INV-23, M-1]

---

## Requirement 8: Search for an existing skill before reinventing a fix  [feature: F-problem-ledger]

**Context:** Before reinventing a fix, the pack searches for an existing skill. Two moments trigger the search: a project's setup, and a struggle that keeps returning. A found skill is adopted or rejected by name, and borrowing keeps to one practice.

**User Story:** As a person about to reinvent a fix, I want the pack to search for an existing skill at setup and at every struggle, so that a returning failure class is met by something that already owns it rather than built again from scratch.

### Acceptance Criteria

**Case: the two moments that trigger a search**

1. *when* a project is set up — at founding, or adoption's orient, beside the founding questions — the system *shall* scan the installed skills and the catalogs it can reach, propose a fit list matched to the project's kind and crafts with a recommendation, and leave the pick to the human's word. [INV-65, B-2, B-3]
2. *when* a struggle keeps returning — a ledger entry reaching its second occurrence, a taste artifact rejected twice (voice, copy, visual style, or spec prose the human has sent back twice), or any failure family that recurs — the system *shall* wait for one search before the next attempt, and *shall* adopt or reject a found skill by name, recording the verdict where the struggle lives. [INV-65, INV-23, INV-62]

**Case: how a borrowed skill travels**

3. The system *shall* invoke a found skill as it ships, paraphrase a borrowed lesson into the project's own documents with the source credited by name, and carry verbatim text only under its license with the notice kept. [INV-65]
4. The system *shall* never republish unlicensed text. [INV-65]
