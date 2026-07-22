# What holds the bounds

This section states the machinery that keeps the pack honest: the checks and gates that make "it works" mean something, and the write-access rules on the pack's own repository. It is written for a reader who has never seen the pipeline before.

Bracket codes like `[INV-202]` and `[E-11]` point to the rule's home in the project spec; a reader can ignore them, a maintainer follows them. The letter before the number names the kind: `INV-` an invariant (a numbered rule that must always hold), `E-` an entity (a numbered part of the product), `T-` a transition (a numbered change of state), `M-` a rhythm rule (a numbered recurring routine), `A-` an adoption step, `B-` a bootstrap step, `D-` a recorded decision, and `ACT-` an actor. The keywords *when*, *while*, *if*, *then*, and *shall* are set in italics and carry their standard requirements meaning: *shall* states a duty, *when* and *while* open a situation, *if* and *then* open a condition and its result.

Terms already defined in the intake glossary and the founding section's additions — request, inbox, pipeline, spec, architecture, invariant, guardrail, suite, host, pack, session, journal, attic, backlog item, queue, movement, delivery, delivery report, footprint, project layers, settings ladder, personal profile, profile, resume file, migration chapter, ratchet manifest — carry their meanings unchanged. The block below adds only the new nouns this section needs.

## Glossary additions

- **net** — one hook or guard that watches for a stated condition and fires when it holds. A guardrail is one kind of net.
- **push gate** — the ordered chain of nets that runs before a push to the pack's repository and blocks the push on any red. Each net in the chain carries a letter.
- **prover record** — one dated file under `docs/prover/` recording one review pass: what was reviewed, the findings, and the verdict. The push gate reads that a committed record dated the push's own day exists and is at least as new as the documents it covers.
- **net-liveness meter** — the shared instrument that records how often a net ran and how often it fired, and reads the two numbers back so a silent net is judged rather than trusted.
- **test matrix** — the document (`TEST_MATRIX.md`) whose rows pair one architecture node with one spec fact, each row pinning the test level that covers the fact.
- **feature-coverage trace** — a second traceability layer above the test matrix, keyed to the project's primary unit, that maps each unit to the node implementing it and a test exercising it.
- **register judge** — the model call that reads a stretch of outgoing text against the plain-language register law and returns the sentences that carry no information or leak register.
- **conduct judge** — the model call that reads a turn's action trace against the standing orchestration laws and reds a violation after the turn.
- **action trace** — the ordered record of which tools the seat called during one turn, read from the tool-use events in the transcript.
- **seat** — the running agent session, seen as the actor that reads, writes, and reports during a turn.
- **touchpoint** — one point of contact with the person, carrying a kind: synchronous when the person is present and the work waits on the person, asynchronous when the person reads on the person's own clock while the work keeps running.
- **far tier** — the queue's tier for a row kept with no revisit trigger and no plan to run, held so the thought is never lost; the rows it holds are the far backlog, and the report of runnable work names the tier in one line rather than listing its rows.
- **waiting board** — the file `WAITING.md` at the host root that holds every item parked for the person's eyes, so nothing waiting evaporates when chat scrolls.
- **decision-set record** — the file `DECISIONS.md` that shows the person the decisions the pack believes the person made, each naming the exchange it came from.
- **snapshot** — the saved artifact of the last accepted run of a surface — its rendered output, files, and numbers — that the next run diffs against as its baseline.
- **design-sync** — the optional machine that mirrors the components a delivery declared to the team's design project for human review.
- **skill eval** — one recorded scenario per working skill: a case where a bare session errs and the skill's text corrects it, proven red without the skill.
- **surface registry** — one host-authored list of every user-facing surface the product carries, read by a completeness net.
- **pen** — the single write-lock a repository holds, under which one delivery reaches the repository's shared truth at a time.
- **remote seat** — a session that shares no filesystem with the assigned session and reaches the repository only through git — a cloud session, a scheduled routine, or another machine.
- **grant** — one recorded permission a remote seat needs to act on a repository: a push grant to write, a read grant to clone and pull a private repository.
- **stranger** — a contributor with no push rights and no per-repository grant who can still open an Issue or Discussion.
- **stranger-wish monitor** — the scheduled process that converts each open stranger Issue or Discussion into one committed inbox file.
- **capture echo** — the line the sweep posts back on an item's source, naming what was heard, its route, its name, and its row.

---

## Requirement 1: Every process converges on a goal named as an artifact

**Context:** Every piece of work the pack runs walks toward a goal. So the work names that goal up front as a concrete artifact it can be measured against — a frozen norm, an exemplar bank, a failing test, a written acceptance — never a paraphrase. Each pass measures its distance to the goal itself rather than a stand-in, and a level once reached is locked by a mechanism so the work cannot slide back. The machines this whole section lists are that principle's hands.

**User Story:** As a person relying on the pack, I want every process to name its goal as a checkable artifact and lock each level it reaches, so that work converges toward the goal rather than drifting near a look-alike.

### Acceptance Criteria

**Case: the goal is a named artifact**

1. *when* a process begins, the system *shall* name its goal as a concrete artifact the work can be held against, and *shall* refuse a paraphrase as that goal. [INV-98]
2. *while* a process runs, the system *shall* measure each pass against the goal artifact itself rather than a stand-in, since a stand-in is where a look-alike is born. [INV-98]

**Case: a reached level locks**

3. *when* a process reaches a level, the system *shall* lock it by a mechanism — a norm template, a conformance test, a lint floor that only rises, or a cap that only ratchets down. [INV-98]
4. *if* a stretch of work is deliberately divergent, such as an exploration or a labelled prototype, *then* the system *shall* allow it only when it is named and bounded by its convergence point. [INV-98]

---

## Requirement 2: A behavioural rule that breaks twice earns a live channel

**Context:** A standing behavioural rule keeps its normative home in a once-read file — the loader, a profile, a skill's text. Prose in a once-read file loses to mid-turn momentum, and attention alone holds nothing across sessions. So a rule that breaks mid-turn a second time despite that home earns a live channel at that same moment, and the pick is recorded where the rule lives.

**User Story:** As a person whose standing rule the pack keeps breaking, I want the second mid-turn break to earn a live channel, so that a recurring failure gets a mechanism at once rather than a third suffering.

### Acceptance Criteria

**Case: the second break earns a channel**

1. *when* a standing behavioural rule breaks mid-turn a second time despite its once-read home, the system *shall* give it a live channel that same moment — an every-prompt hook line reminding at the decision point, or a mechanical after-the-fact check that turns the suite red. [INV-108]
2. *when* a live channel is chosen, the system *shall* record the pick where the rule lives and *shall* keep the once-read file as the rule's normative home. [INV-108]

**Case: the break-record lives in one home**

3. The system *shall* record a rule's mid-turn breaks in one home, the problem ledger (`PROBLEMS.md`), so the sweep reads one source. [INV-108]
4. *when* a live channel lands, the system *shall* point it back to that ledger entry rather than standing it as a second break-record. [INV-108]

---

## Requirement 3: The test matrix covers every fact both ways

**Context:** The test matrix is where "it works" is made accountable. Its rows are keyed by architecture node and spec fact, and coverage is total: no fact stands without a row, and no row stands without a pinned test level. Each row states both what the fact does and what it must never do, and that negative side is the regression fence.

**User Story:** As a person trusting a green suite, I want every fact to carry a matrix row pinned to a level and a stated negative side, so that a passing suite proves the facts were checked at the right depth and guarded against regression.

### Acceptance Criteria

**Case: total coverage, keyed by node and fact**

1. The system *shall* give every spec fact at least one matrix row, and *shall* leave no row without a pinned test level. [E-5]
2. The system *shall* key each row by one architecture node paired with one spec fact, derived from the proven architecture. [E-14, E-15]

**Case: each row states both sides**

3. The system *shall* state on each row both what the fact does and what it must never do, the negative side standing as the regression fence. [INV-6]

---

## Requirement 4: The feature-coverage trace and its heading convention

**Context:** Above the test matrix sits a second traceability layer keyed to the project's primary unit. Each project declares its type once, and the type names the unit — a web product counts features, a command-line tool its commands, a package its guarantees, a book its arguments. One table in the architecture maps each unit to the nodes that implement it and a test that exercises it, and a heading convention gives the reverse check teeth.

**User Story:** As a person asking whether every promised unit is covered, I want a two-way trace keyed to the project's own unit, so that a unit without an implementer or a test, and a promised unit that forgot its tag, both go red.

### Acceptance Criteria

**Case: the trace maps each unit both ways**

1. The system *shall* map each declared unit to the node that implements it and a test that exercises it in one coverage table in the architecture. [E-29]
2. *when* the feature-coverage check runs, the system *shall* fail the push *if* a tagged unit resolves to no real implementer node or no real test, and *shall* fail it *if* a promised unit carries no tag. [INV-73]

**Case: every heading declares its status**

3. The system *shall* have every third-level heading carry either its feature tag, marking a person-facing scenario the table maps, or a not-a-scenario marker, marking a machinery or reference section. [INV-132]
4. *if* a third-level heading carries neither marker, *then* the system *shall* read it as red, so a forgotten tag can no longer ship a scenario uncovered. [INV-132]

---

## Requirement 5: The guardrails wired to the push gate

**Context:** The guardrails are mechanical checks wired to the pre-push hook, running live for the pack's own repository. Each push must show a set of proofs before it reaches the remote. On a host these checks are offered rather than imposed, since the human may not know what a git hook is.

**User Story:** As a maintainer pushing the pack, I want each push to show its proofs mechanically before it reaches the remote, so that a structural defect turns the push red rather than landing on the remote.

### Acceptance Criteria

**Case: what each push must show**

1. *when* a push runs, the system *shall* require a prover record dated the same day, a green suite scoped to the diff's reach, every anchor owned by one node, and no unchecked matrix-coverage box. [E-6, INV-41]
2. *when* a push runs, the system *shall* require the prototype fence — no production file referencing into a prototype home — and the opt-in concurrent-edit fence on commit. [E-17, INV-17]

**Case: hosts are offered, never imposed**

3. *when* the checks reach a host, the system *shall* install the hooks only where the host uses git and only after asking the human in plain words. [E-6]

---

## Requirement 6: The push gate derives its reach from the diff

**Context:** Running every check before every push double-misses: a prose-only push pays for behavioural tests that read none of its changed lines, while the checks a prose diff can break never run. So the push gate derives its check-set from a declared reach map — which checks read which file classes — read mechanically from the diff's file list. The map is conservative: anything it cannot classify falls to the full run.

**User Story:** As a maintainer pushing a change, I want the gate to run every check the diff can reach and only those, so that a prose push stands down the behavioural suite by name while an unclassified file still pulls the whole run.

### Acceptance Criteria

**Case: the reach map decides the set**

1. *when* a push runs, the system *shall* derive its check-set from the declared reach map against the diff's file list, and *shall* run the full suite *if* any changed file is unmapped or new. [INV-45, INV-40]
2. *when* a diff is confined to the declared infra classes, the system *shall* run the test files that read its changed files plus the traceability net — the suite's own traceability tests, carrying the anchor-ownership assertion and riding every scoped run, a mechanism distinct from the feature-coverage check — log the picked set with its reason, and *shall* curate the infra-class list by incident and re-justify it at milestones. [INV-45, INV-212, INV-18]
3. *when* a full run completes, the system *shall* read its own wall-time against the architecture's stated number and red on an overrun naming both figures. [INV-41, INV-164]

**Case: the classes are the host's to declare**

4. The system *shall* read the reach map's directory classes from `guardrails.config.json` under a `reach_classes` key, the same layers the host's `project.layers` already carries. [INV-224, INV-135]
5. *if* the config names no classes, *then* the system *shall* leave every changed file unclassified and run the full suite on every push. [INV-224]

**Case: the cheap gates never scope**

6. The system *shall* run the prover-record, ownership, coverage, loadability, and prototype-fence checks at every push, never scoped, so nothing the diff touches is skipped. [INV-40]

---

## Requirement 7: A blocking gate speaks one typed language

**Context:** Today each gate script fails in its own words, so an agent parses prose and a human hunts for the fix. Every blocking gate instead emits, on red, one parseable failure object beside its human-readable lines, and every check declares itself blocking or advisory.

**User Story:** As an agent or a person reading a red gate, I want each blocking gate to emit one typed failure line carrying the fix, so that the reason and the remedy are read the same way from every gate.

### Acceptance Criteria

**Case: the typed failure line**

1. *when* a blocking gate reds, the system *shall* emit one typed failure object carrying a severity, a code, a message, and a fix field that reads as the sentence a person follows. [INV-47]
2. The system *shall* have every check declare itself blocking or advisory, an advisory check printing its finding and never flipping the exit code. [INV-47]

**Case: no half-written artifact**

3. *when* a script rebuilds artifacts, the system *shall* validate every output before it writes any, so no half-written artifact lands on disk. [INV-47]

---

## Requirement 8: The four project-side checks are attachable code

**Context:** The pack ships a generic runnable form of the four checks the pipeline names — completeness, tests-present, behaviour-traces-to-spec, and conflicts — parametrized by one host config file rather than by editing check code. A host attaches them by config, and each check proves itself red-first on one planted defect before it counts as attached.

**User Story:** As a person attaching the pack to a host, I want the four project-side checks configured rather than re-implemented, so that a host wires them by naming its own shape and each check proves it can fire.

### Acceptance Criteria

**Case: config, not re-implementation**

1. The system *shall* ship the four checks — completeness, tests-present, behaviour-traces-to-spec, and conflicts — under `scaffold/guardrails/` parametrized by one host config declaring the document paths, the tests directory, the source globs, the registry path, and the render command. [INV-97]
   [GAP: the source names the conflicts check as one of the four but never states what conflict it detects; the other three carry their subject in their own names.]
2. *when* a check runs, the system *shall* read the config and the tree, exit green or red, and on red emit the typed failure line beside its human sentence. [INV-97, INV-47]

**Case: failure is honest by construction**

3. *if* the config is missing, *then* the system *shall* red with an attach-me line rather than pass silently, and *shall* red *if* the config points at a path that does not exist. [INV-97]
4. *if* a host lacks a check's precondition, *then* the system *shall* require the waiver declared in the config where a reader sees it, so an undeclared gap never passes quietly. [INV-97]

**Case: attachment proves itself**

5. *when* the attach command runs, the system *shall* vendor the four checks, seed the config where the host carries none, leave a filled config unclobbered, and *shall* write the host's source pins into the ratchet manifest so the daily update check covers this kit. [INV-97, INV-177]
6. *when* a check is attached, the system *shall* prove it red-first on one planted defect before it counts as attached, the registry's own content staying the host's authorship. [INV-97, E-10]

---

## Requirement 9: The net-liveness meter reads every net

**Context:** A net that never fires is a fact about itself with two readings: the defect is gone and the net is dead weight, or the net is broken and its trigger sits where the work never passes. Two numbers tell those apart — how often the net ran and how often it fired — and no net keeps them on its own. The meter records both against the host's declared roster of nets and reads them back.

**User Story:** As a person maintaining a set of nets, I want each net's runs and fires recorded and read against a declared roster, so that a broken trigger is named while a merely quiet net is surfaced for a human retirement call rather than trusted or auto-retired.

### Acceptance Criteria

**Case: the two numbers are recorded**

1. *when* a net runs, the system *shall* record one line per invocation to `.live-spec/net-meter.jsonl`, and *shall* aggregate runs and fires against the host's declared roster of nets. [INV-202]

**Case: the three readings**

2. *when* a net's recorded run count is zero, the system *shall* red it by name as a broken trigger, since its condition sits where the work never passes. [INV-202]
3. *when* a net's runs reach its declared window with zero fires, the system *shall* surface it as a retirement candidate and *shall* leave the retirement as the human's call. [INV-202]
   [GAP: the source names a per-net declared window for the zero-fires retirement reading but does not state who declares the window or its default value.]
4. The system *shall* read every other net as live, and *shall* never auto-retire a net nor red one for staying quiet. [INV-202]

---

## Requirement 10: The register judge reads a class a word-list cannot

**Context:** A register law that names a class cannot rest on a list of literal words, since each escape earns one more pattern while the next word walks through and a human ends up working as the regular expression. So a model that reads meaning holds the class. It takes the outgoing text and the law and returns the sentences that carry no information or leak register, with the literal pattern list demoted to a first cheap filter.

**User Story:** As a person reading the pack's own words, I want a model to hold the register class rather than a word list, so that a register offence is caught in meaning while a broken judge falls back to the cheap list rather than blocking.

### Acceptance Criteria

**Case: the judge holds the class**

1. *when* the register law is applied, the system *shall* hand the outgoing text and the law to the cheapest model tier the routing rule names and take back the sentences that carry no information or leak register. [INV-203, INV-69]
2. The system *shall* keep the literal pattern list as a first cheap filter that earns no new entries by duty. [INV-203, INV-83]

**Case: the universal laws the judge reads**

3. The system *shall* read the universal laws that ship in the mechanism — naming a thing by denying its neighbour, opening a chat sentence with a bare internal code, grading importance or quality without a concrete fact, and showing a coined term with no plain gloss — and *shall* leave the personal laws to an overlay the personal layer owns. [INV-203, INV-221]

**Case: two surfaces, one mechanism**

4. *when* the seat finishes a turn on the chat surface, a Stop arm *shall* dispatch every message shown since the last human turn, and a prompt-submit arm *shall* report the verdict at the person's next message. [INV-203]
5. *when* a styled file is about to be shown, the same judge *shall* stand as the ceiling of the pre-show register gate pointed at that file. [INV-83, INV-203]

**Case: the judge stands down on its own breakage**

6. *if* the judge's own machinery breaks — a missing binary, a timeout, a non-zero exit, or a shape it cannot read — *then* the system *shall* leave the literal-list verdict standing rather than red, so a guard cannot train the guarded to route around it. [INV-203]

---

## Requirement 11: The answer-first arm reds a lead-less wall

**Context:** The answer-first law asks every reply to open with its answer in a few lines the reader may stop at, with reasoning underneath. Whether a text opens with its answer is undecidable, so the arm reds a measurable proxy: a reply over a length floor whose opening block is a wall with no short lead. It is honest about what it cannot see and corrects one message later.

**User Story:** As a person reading the seat's replies, I want a reply over the floor with no short lead flagged for a lead-first redo, so that a method-first wall is caught while a genuine lead-first reply is never falsely flagged.

### Acceptance Criteria

**Case: the proxy reds a lead-less wall**

1. *when* a reply runs past the length floor and its opening block fails all three lead signals — a short opening sentence, a short opening paragraph, or scannable opening structure — the system *shall* flag it and ask for a lead-first correction. [INV-220]
2. The system *shall* read the length floor and the lead thresholds from the host's own tunable defaults rather than a fixed law. [INV-70]

**Case: honest about its reach**

3. The system *shall* judge only whether an opening lead is present, and *shall* leave whether that lead answers the right question to the person. [INV-220]
4. The system *shall* judge only the final reply the person reads, and *shall* leave the short inter-tool narration lines alone. [INV-220]

**Case: a Stop-hook notice, not a push gate**

5. *when* the arm fires, the system *shall* flag the previous reply and deliver the correction one message later, since a chat reply is already emitted and cannot be blocked. [INV-220]
6. The system *shall* ship the arm as a universal pack hook covered by the config-health parity net — the check that reds an installed hook copy that is missing or differs from its source in the pack — and *shall* have its runs and fires read by the net-liveness meter rather than trusted. [INV-175, INV-180, INV-202]

---

## Requirement 12: Two Stop-hook soft signals: the hedge gate and the lean-orchestrator arm

**Context:** Two once-read behavioural laws gained a mechanical net. The first: a reply that offers to do a thing the seat could already derive and reverse, holding the offer open for a cue, is an offering-hedge. The second: a session that holds raw file content inline without dispatching a worker leaks the orchestrator's context. Each is a Stop-hook soft signal that reads after the fact and corrects one message later; each is honest that it catches only the frames it lists.

**User Story:** As a person relying on the seat to act rather than hedge and to delegate heavy reading, I want each law backed by a cheap literal net, so that a common hedge frame and a pure context-hoard are caught while the class in any phrasing stays with the conduct judge.

### Acceptance Criteria

**Case: the hedge gate**

1. *when* the seat's last reply carries an offering-hedge frame from the pattern list, after a quoted, backticked, or fenced span is stripped, the system *shall* block the stop with a rewrite instruction reaching the seat one message later, modelled on the scissors scan — the literal gate that blocks a sentence naming a thing by denying its neighbour — and installed by the setup walk. [INV-238, INV-173]
2. The system *shall* leave clear of a genuine taste, policy, or irreversible question that names its human-only fact, since that question is an honest admission rather than an offer. [INV-238, INV-152]
3. The system *shall* catch only the frames it lists, so a paraphrase it does not carry stays with the conduct judge that reads the class in meaning. [INV-238, INV-241]

**Case: the lean-orchestrator arm**

4. *when* cumulative inline raw file content across the session reaches the threshold and the worker-dispatch count is zero, the system *shall* warn that the reading rode no worker dispatch. [INV-246]
5. The system *shall* read the threshold as a tunable parameter defaulting to 50 kibibytes, and *shall* count only a main-thread Read or one of six literal file-dump verbs, a read inside a worker riding a sidechain never counted. [INV-246, INV-70]
6. *when* the seat dispatches its first worker, the system *shall* clear the warning, since one dispatch shows the session is delegating. [INV-246]

**Case: both stand down on their own breakage**

7. *if* a payload or transcript is unreadable, *then* the system *shall* stand the signal down silently, and *shall* have its runs and fires read by the net-liveness meter rather than trusted. [INV-203, INV-202]

---

## Requirement 13: The conduct judge reads the action trace

**Context:** The register judge reads what the seat said; the orchestration laws are about what the seat did — whether it dispatched a long artifact or a deep read to a worker, whether it routed each unit of work to the cheapest sufficient tier, whether it kept pulling unblocked work. No text arm can see an act. The conduct judge generalizes the register judge from the turn's text to the turn's action trace, reading it against the standing orchestration laws.

**User Story:** As a person relying on the orchestration laws that name no mechanical net, I want a model to read each turn's action trace against them, so that a missed act is named for a forward correction the same way a register offence is.

### Acceptance Criteria

**Case: the trace is read against the laws**

1. *when* the seat finishes a turn, the system *shall* read the turn's action trace against the standing orchestration laws and red a violation after the fact. [INV-241, INV-150]
2. The system *shall* render the trace to quotable text before the model reads it, so the reused hallucination guard — the check that each span a verdict quotes is found in the judged text itself — has spans to match. [INV-241, INV-203]
3. *if* a turn's trace is empty, *then* the system *shall* skip it, since a chat-only turn carries no act to judge. [INV-241]

**Case: the law body and its evidence**

4. The system *shall* judge the orchestration members carrying a reminder-history of two or more — worker-routing (each unit of work routed to the cheapest tier its step and kind allow), lean-orchestrator (heavy reading dispatched to a worker rather than held inline), pull-unblocked-work (the session keeps pulling unblocked queue work rather than idling), and classify-the-subtask (a subtask is the person's or the seat's by what the subtask itself needs, never by the heading it sits under) — their breaks recorded in the one home the break-record law names, the problem ledger (`PROBLEMS.md`), and *shall* leave the single-occurrence members as reminders until they recur. [INV-241, INV-108, INV-69, INV-137, INV-143]
5. *when* the evidence is partial — an idle or a parked step the trace cannot fully show — the system *shall* red only on a clear case and *shall* lean on the net-liveness meter and the human review window. [INV-241, INV-202]

**Case: async, and off the deterministic gate**

6. *when* the verdict is collected, a Stop arm *shall* write it to a slot distinct from the register judge's, and a prompt-submit arm *shall* surface it at the person's next message as a forward-looking correction. [INV-241, INV-203]
7. The system *shall* keep the conduct judge outside the deterministic suite and push gate, opt-in per host and off by default, since it reads the transcript and rests on a model call. [INV-241]
8. The system *shall* read the per-person strictness as a parameter it does not own, taking a built-in default a host overrides by environment until the parameters registry ships. [INV-241]
   [GAP: the source names a built-in strictness default the conduct judge reads before the parameters registry ships but never states that default's value or how hard it reds a borderline act.]

---

## Requirement 14: A cleanup says what it ended

**Context:** Every process the pack ends is reported with what it was and why the run owned it — the process identifier, the process group, or the owned path that proves ownership — so an ending nobody expected is visible the moment it happens rather than at the next unexplained loss of the person's work. This is the minimum owed on a machine shared with someone who runs the same programs the pack does.

**User Story:** As a person sharing a machine with the pack, I want every process the pack ends to announce what it was and how the run owned it, so that an unexpected ending is seen at once rather than discovered as lost work.

### Acceptance Criteria

**Case: the notice on every ending**

1. *when* a cleanup path ends a process, the system *shall* emit through the shared notice shape one line naming the identity ended, what it was, and the owned-via proof. [INV-204]
2. *if* a tracked cleanup path ends a process while emitting no notice, *then* the system *shall* red the gate that scans for it. [INV-204]

**Case: the notice ships ahead of the strict form**

3. The system *shall* ship this notice ahead of the stricter owned-identity check, so what the strict form would refuse is shown before the strict form starts refusing. [INV-204, INV-162]
4. *when* a cleanup is built through an indirection the patterns cannot read, the system *shall* leave the announcement to the forker, the same bound the muted-launch net keeps — the check holding that every browser a test launches starts muted, an unmuted launch redding. [INV-204, INV-157]

---

## Requirement 15: A finished worker leaves no runaway child, and teardown reaps its own group

**Context:** When a worker the run spawned completes, a descendant it left behind can keep burning a full processor core unnoticed while a frozen status line masks it. The run owns that descendant, since it sits in the run's own process group or under the run's own temp tree. One arm reports such a runaway; a second reaps the run's own process group at teardown; and a stalled worker is caught by its idle output. Because a coarse scope does real harm in process space, a target is identified only by provable ownership, never by a program name.

**User Story:** As a person whose machine the run shares, I want a finished run to report and reap only the descendants it provably owns, so that a runaway core-burn is caught without a broad sweep ever touching a foreign process.

### Acceptance Criteria

**Case: report a runaway the run owns**

1. *when* a stopping point is reached, the system *shall* report a descendant that is owned, orphaned, and burning — its identity, its processor share, and why the run owns it — reasoning over process group, parent liveness, and processor share alone. [INV-213]
   [GAP: the source gates the burning test on a host-settable processor-share threshold but names no default, so the reporter's out-of-box firing point is unstated.]
2. The system *shall* read no command or name field for that verdict, so a process whose command merely matches a known burner in a foreign group is never targeted. [INV-213, INV-162]

**Case: teardown reaps the owned group**

3. *when* a worker tears down, the system *shall* reap the process group the run itself spawned through `os.killpg` and *shall* refuse any group absent from the run's owned set. [INV-230, INV-162]
4. *when* the group is reaped, the system *shall* report what it ended through the shared cleanup-notice shape. [INV-230, INV-204]

**Case: a stall caught by idle output**

5. *when* a worker's status reads running while its output file has stopped growing, the system *shall* read the stall from that file's modification time and return the stalled worker with its owned process group for confirmation before any reap. [INV-230, INV-76]
6. The system *shall* keep the worker's brief carrying the setting lines it needs, so a worker session onboards no one. [ACT-3]

---

## Requirement 16: Every point of contact with the person has a kind

**Context:** A moment of contact is synchronous when the person is present and the work waits on the person, and asynchronous when the person reads on the person's own clock while the work keeps running. The kind licenses the traffic: an interruption belongs on a synchronous point, a teaching line on a point the person opens, and waiting traffic on every point. Each touchpoint declares its kind in one manifest, and a gate reds a surface that speaks in a kind its touchpoint lacks.

**User Story:** As a person met by the pack at many points, I want each touchpoint's kind declared and enforced, so that an interruption never rises from a point I read on my own clock and a teaching line only reaches a point I opened.

### Acceptance Criteria

**Case: the kind licenses the traffic**

1. The system *shall* declare each touchpoint's kind in the manifest `guardrails/touchpoints.json`, holding whether the person opens it and what traffic it affords. [INV-205]
2. The system *shall* afford an interruption only on a synchronous point, a teaching line only on a point the person opens, and waiting traffic on every point. [INV-205]

**Case: the gate reds a mismatch**

3. *when* a surface speaks in a kind its touchpoint lacks — an interruption from an asynchronous point, or a teaching line on a point the person did not open — the system *shall* red it. [INV-205]
4. *when* a surface interrupts through wording the marker cannot read, the system *shall* leave the declaration to the author, the same bound the cleanup-notice and muted-launch nets keep. [INV-205, INV-204, INV-157]

---

## Requirement 17: The waiting board outlives the scroll

**Context:** Chat is a display and it scrolls, so a question parked for the person and an answer the person never saw both evaporate. One small file at the host root, the waiting board, holds them, and chat renders it on occasion. An item clears on the person's acknowledgement alone and is never auto-expired, since expiring an item the person never read is a silent loss.

**User Story:** As a person who reads on my own clock, I want everything waiting for me kept in one board that never auto-expires, so that a parked question or an unseen answer is there when I open it rather than lost to the scroll.

### Acceptance Criteria

**Case: the board holds what waits**

1. The system *shall* hold every item waiting for the person in the board `WAITING.md`, and *shall* clear an item on the person's acknowledgement alone. [INV-206]
2. The system *shall* never auto-expire an item, moving a superseded one to the attic with a manifest line rather than deleting it. [INV-206]

**Case: the shown cap and its demotion**

3. The system *shall* show at most 12 items to the person at once, and *when* a new item arrives to a full shown set *shall* demote the oldest shown item into the list below, whole. [INV-206]
4. *if* a thirteenth item stands in the shown set, *then* the system *shall* read it as an over-cap defect. [INV-206]

**Case: the gate reds a silent loss**

5. *when* a closing report omits a still-open board item, or an item is demoted with no matching line, or the shown set runs over cap, the system *shall* red the board gate. [INV-206]

---

## Requirement 18: A recorded decision names the exchange it came from

**Context:** Every claim in the pack stands on an artifact a reader can check. A human's word is the one input with no artifact behind it, and so the one claim no agent, prover, or gate questions — which makes it the one slot a fabrication, once placed there, is never reached again. So a sentence carrying human authority names the exchange it came from, and a claim the pack reasoned out is written in the pack's own voice, challengeable by everything that reads it.

**User Story:** As a person whose recorded decisions the pack quotes back, I want each one to name the exchange it came from while the pack's own reasoning stays in the pack's voice, so that a fabricated decision cannot hide in the one slot nothing challenges.

### Acceptance Criteria

**Case: authority names its exchange**

1. The system *shall* have a sentence set down as the person's decision name the exchange it came from, at minimum a marker a reader can go to and check in the profile's own style. [INV-207]
2. The system *shall* write a sentence the pack reasoned out for itself in the pack's own voice with no such attribution, challengeable by every agent, prover, and gate. [INV-207]
3. The system *shall* treat an autonomy grant as room to act that the agent owns as its own judgment, and *shall* never record it as a decision of the person's for the record to quote back. [INV-207]

**Case: the read-back surface and its gate**

4. The system *shall* show the person the decision-set record (`DECISIONS.md`), each entry naming its exchange, rendered so the person reads on the person's own clock and strikes what the person never said. [INV-207, INV-205]
5. *when* a live on-record entry in a decision-record surface carries no exchange, the system *shall* red the authority-anchor gate, a struck entry being skipped. [INV-207]

---

## Requirement 19: The far backlog surfaces itself rarely and unasked

**Context:** Answering when the person asks is the far tier's floor; above it, the tier shows itself on its own once in a while, so a thought parked there is met again without the person having to remember it exists. The status report carries a rare line naming that a far backlog is kept, at a cadence that is a settings-ladder default, and records the last self-surfacing so the window is readable.

**User Story:** As a person keeping a far backlog, I want it to surface itself rarely and unasked on a report I already read, so that a parked thought returns to me without waiting on my memory and without a second offer inside its window.

### Acceptance Criteria

**Case: the rare self-surfacing**

1. The system *shall* answer the far tier when the person asks, and above that floor *shall* carry a rare status-report line naming that a far backlog is kept. [INV-222, INV-223]
2. The system *shall* propose at most one such offer per 14 days as a settings-ladder default, movable by the person's word, and *shall* record the last self-surfacing in a dated marker. [INV-223, E-13]

**Case: it rides an asynchronous point**

3. *when* the far-tier line rides the status report, the system *shall* treat it as an asynchronous touchpoint that may only wait, holding the entry `far-tier-surfacing` in the manifest. [INV-223, INV-205]
4. *when* a second offer would fall inside the last surfacing's window, the system *shall* red the report-shape check, and *shall* pass a first offer once the window has passed. [INV-223]

---

## Requirement 20: A release note may offer the reader next-step choices

**Context:** A release note is a surface the person opens on the person's own clock, and on it the pack may offer appealing things to do next, phrased as free choices. The offers section is optional, so a release with no worthwhile next step owes none; what the walk owes is a recorded decision, so the offer-or-none choice is never silently skipped.

**User Story:** As a person reading a release note, I want the pack free to offer me next steps and made to record whether it did, so that a worthwhile choice reaches me while the offer-or-none decision is never silently skipped.

### Acceptance Criteria

**Case: the recorded offer-or-none decision**

1. *when* the publish walk prepares a release note, the system *shall* record the offer-or-none decision on the note, carrying the optional offers section. [INV-228]
2. *when* a release-note record neither offers a next step nor records a no-offer marker, the system *shall* red the release-note check, and *shall* pass a record that offers a choice or records none by name. [INV-228, INV-83]

**Case: it rides an asynchronous point**

3. The system *shall* treat the release note as an asynchronous, person-opened touchpoint that affords an offer and not an interruption, holding the entry `release-note` in the manifest. [INV-228, INV-205]

---

## Requirement 21: A parked question carries a recommended default

**Context:** When a question's value is the person's own input yet the work cannot wait on the person's free minute, the pack does not stall: the question is born onto the waiting board already carrying the default the work took, so the work proceeds on the recommendation and the person's free minute picks when to read it. A parked question with no default is a stalled question in a parked question's clothes.

**User Story:** As a person the pack would enjoy asking, I want a parked question born with the default the work already took, so that the work keeps moving and I answer at my own free minute rather than blocking the lane.

### Acceptance Criteria

**Case: the default travels with the question**

1. *when* the pack parks a question whose value is the person's input, the system *shall* born it onto the waiting board already carrying the default the work took, and *shall* proceed on that recommendation. [INV-229, INV-4]
2. *when* a board item marked a parked question records no default, the system *shall* red the board gate, and *shall* pass a parked question naming its default. [INV-229]

**Case: an unanswered parked question keeps standing**

3. *while* a parked question stands unanswered, the system *shall* hold its default and record that the default stood unreviewed as a fact rather than an expiry. [INV-229, INV-206]
4. *when* a parked question is answered, the system *shall* route it through intake and close it, distinct from a decision an agent may not settle without the person. [INV-229, INV-152]

---

## Requirement 22: A skill-body change carries the review it owes

**Context:** A skill is instructions a model reads, and a change to those instructions can shift how every session that loads it behaves. So a push that changes a skill's body must carry the skill-creator review that catches a regression before it ships. A pure version stamp is the one carve-out, since it copies the version fact rather than changing instructions.

**User Story:** As a maintainer changing a skill's body, I want the push blocked until it carries a fresh skill-creator review, so that a change to instructions every session reads cannot ship unreviewed while a bare version bump passes quiet.

### Acceptance Criteria

**Case: a body change owes a fresh review**

1. *when* a push substantively changes a skill under `skills/`, the system *shall* require a committed review naming the skill, carrying a verdict, and at least as new as the skill's last change. [INV-208]
2. The system *shall* read the push range through the base ladder the prover-record gate uses — the declared base (`LIVE_SPEC_DIFF_BASE`), then `origin/main`, then the previous commit (`HEAD~1`), the first that resolves. [INV-208, INV-116]

**Case: the version-stamp carve-out**

3. *if* a skill diff's only changed lines are the machine-stamped version and base-reference lines, *then* the system *shall* pass it quiet as owing no review. [INV-208, INV-178]
4. *when* a substantive body change carries no fresh review, the system *shall* red, the review's judgment staying the skill-creator's own. [INV-208]

---

## Requirement 23: Append-only documents are rotated with nothing lost

**Context:** The pack's growable working documents grow with every delivery, and a guard's scan slows as they pass roughly half a megabyte. So a fully-closed portion of a growable document is rotated out of the live file into a dated archive, and the live file keeps only live material. This is the attic law applied to a document's own closed portion, and a gate holds that nothing rotated is lost.

**User Story:** As a person whose scans slow on ever-growing documents, I want each fully-closed portion rotated into a dated archive with a manifest, so that the live file shrinks while every rotated row stays findable and nothing is lost.

### Acceptance Criteria

**Case: rotate the closed portion**

1. *when* a growable document holds enough fully-closed material, the system *shall* move the closed rows into a dated archive under `docs/queue-archive/` and leave a manifest line naming which rows moved and where. [INV-209]
2. The system *shall* read a row as rotatable only when it carries a closed status and no open signal, reusing the existing signal rather than minting a marker. [INV-209, INV-164]

**Case: the gate holds nothing-lost**

3. *if* a row the manifest declares rotated is found in neither the live file nor its archive, *then* the system *shall* red as a nothing-lost violation. [INV-209]
4. *if* an archive file is pointed at by no live manifest line, or a row declared rotated still stands as a live table row, *then* the system *shall* red as ambiguous. [INV-209]

---

## Requirement 24: A node re-answers its fitness as it grows

**Context:** The three-question fitness test governs a node's birth, but a node born right and then grown carries a standing yes nobody re-reads. So each node re-answers the three questions at every architecture re-prove, and two nodes whose pins share one file answer the parallel-work question no by construction — which makes co-residence in one file the mechanical face of a failed growth answer. Raw size is rejected as the vanity metric: a large file owning one responsibility is healthy.

**User Story:** As a person watching an engine file swell, I want node co-residence counted and re-asked at re-prove, so that a file that has grown to hold several nodes is caught and a split is proposed rather than a standing yes passing forever.

### Acceptance Criteria

**Case: co-residence is the counted signal**

1. The system *shall* count nodes-per-file from the architecture's own pin column as the number of distinct nodes whose pins name a file, and *shall* reject raw size as the signal. [INV-233, INV-41]
2. *when* an architecture is re-proven, the system *shall* have each node re-answer the three fitness questions on its pins — can the node be tested alone, does a real second place need it, and can it be worked in parallel with its neighbour without queuing on shared files — two nodes sharing one file answering the parallel-work question no. [INV-233, INV-122]

**Case: the ratchet and the proposal**

3. The system *shall* hold a ratcheted per-file node cap seeded at the tree's current count, and *shall* red any increase while the cap ratchets down only. [INV-233, INV-164]
4. *when* a file's node count sits at its cap, the design review *shall* carry the split proposal in its two-objects shape — one question brought to the person with both compared objects in hand — naming the over-grown file and the split it offers. [INV-233, INV-142]

**Case: a split is a structure change**

5. *when* a split is taken, the system *shall* carve it by the architecture step alone and re-prove it there. [INV-233, INV-37, INV-113]
6. The system *shall* read what counts as a code file from the project's declared layers. [INV-233, INV-135]

---

## Requirement 25: Everything growable declares the number that bounds it

**Context:** When a thing just grows without end — a script, a spec, a test matrix — the system cannot do nothing. Where a node's fitness asks whether a file holds one thing or several, this asks whether a thing has grown past what it may weigh, where size is the signal and needs its own declared number. Each of the four large working documents declares a byte ceiling with a recorded reason, and a watcher reds a document past its ceiling.

**User Story:** As a person watching a document grow without bound, I want each growable artifact to declare a byte ceiling with a reason and a watcher to read it, so that crossing the bound earns a rotation while a silent creep upward has no door.

### Acceptance Criteria

**Case: a ceiling with a recorded reason**

1. The system *shall* have each of the four named working documents — the spec (PRODUCT_SPEC.md), the queue (ROADMAP.md), the test matrix (TEST_MATRIX.md), and the journal (JOURNAL.md) — declare a byte ceiling with a non-empty recorded reason in `guardrails/doc-bounds.json`, and *shall* red a document past its ceiling. [INV-234, INV-41]
2. *if* a declared bound carries no reason, *then* the system *shall* red it. [INV-234]

**Case: rotation is the remedy**

3. *when* a document over its ceiling carries a manifest naming an archive dated the same day, the system *shall* pass it, since the grooming that shrinks it back under the bound has just been applied. [INV-234, INV-209]
4. The system *shall* seed the ceilings above the current file sizes with rotation headroom, and *shall* let a ceiling rise only with a recorded reason. [INV-234]

---

## Requirement 26: The guards over the guards

**Context:** A gate can report green two ways: because the input was clean, or because it never fires at all. Four checks guard the gate machinery itself against that hollow class — the pushed gates must be mirrored into the remote check, every chat judge must be wired into settings, every gate must carry a proof it can fail, and every path a permission rule names must still exist.

**User Story:** As a maintainer trusting the push gate, I want the gate machinery itself checked, so that no gate silently protects nothing — mirrored into the remote, wired into settings, provably able to fail, and pointed at real paths.

### Acceptance Criteria

**Case: the remote mirror carries every local gate**

1. *when* the push gate runs a gate letter locally that the remote mirror does not run, the system *shall* red, naming the gate and the one fix, a legitimate remote-skip living in `guardrails/ci-mirror.json` with its reason. [INV-210, M-5]
2. *if* a carve-out names a letter that is no local gate, *then* the system *shall* red it as drift. [INV-210]

**Case: every chat judge is wired**

3. *when* a hook under `hooks/` is not classified in the wired-hook declaration, or a wired hook is missing from its array in the installed settings, the system *shall* red, naming the hook, the surface, and the fix. [INV-211]
4. *where* the personal-layer settings cannot be read, the system *shall* stand the wiring check down by name rather than falsely pass. [INV-211, INV-175]

**Case: every gate carries a known-red proof**

5. The system *shall* require each pushed gate letter to be classified with a red-first proof driving its check to a non-zero exit, or a covered entry naming the gate it rides and the reason. [INV-212]
6. *if* a gate marker is classified nowhere, or a gate can by construction never be made to fail, *then* the system *shall* red it loudly. [INV-212]

**Case: a permission rule points at a real path**

7. *when* a filesystem path named inside a permission rule is absent, the system *shall* red the rule, reading absolute and home-rooted paths and reporting the count of rules it resolved. [INV-216, INV-176]

---

## Requirement 27: The snapshot baseline advances only at delivery

**Context:** The snapshot is the saved artifact of the last accepted run of a surface, and the next run diffs against it as the baseline. The baseline advances only at a delivery, and only for the surfaces the change declared; an undeclared surface keeps its old baseline. That asymmetry catches the unasked change.

**User Story:** As a person guarding against an unasked change, I want the baseline to advance only at delivery and only for declared surfaces, so that a rendered surface that differs but was never declared turns the scope check red.

### Acceptance Criteria

**Case: the baseline advances by declaration**

1. The system *shall* advance a surface's baseline only at a delivery and only for the surfaces the change declared, an undeclared surface keeping its old baseline. [E-7]
2. *when* a rendered surface differs from its baseline while the delivery never declared it, the system *shall* red the declared-scope check. [E-7, E-6]

**Case: the snapshot is tracked and recoverable**

3. The system *shall* keep the snapshot folder git-tracked with one manifest line per surface, so any older baseline can be checked out, and *shall* keep only the last baseline in the working tree. [E-7]
4. *when* adoption begins, the system *shall* save the first baseline from the artifacts as found, and *shall* narrow the pack's shared settings for one project only where the host profile records it. [A-6, E-8]

---

## Requirement 28: Design-sync mirrors declared components for team review

**Context:** Design-sync is an optional machine for hosts with visual components. It mirrors the components a delivery declared to the team's design project, where the human reviews rendered cards, supplementing the in-session render — which stays the authority for the delivery gate. Every sync is gated by the human, since a sync publishes outside the machine, and the pack itself never syncs.

**User Story:** As a person reviewing a visual host's components, I want the declared components mirrored to the team design project under a human gate, so that the team reviews rendered cards while the in-session render stays the authority for the gate.

### Acceptance Criteria

**Case: the optional, off-by-default machine**

1. The system *shall* keep design-sync off by default in the base defaults table, and *shall* turn it on only where a host records a profile line. [E-18, INV-14]
2. *when* design-sync runs, the system *shall* sync the components a delivery declared and *shall* gate every sync by the human, since a sync publishes outside the machine. [E-18, ACT-1]

**Case: the work-kind axis stands it down**

3. The system *shall* apply design-sync to product-kind work on a visual host, and *shall* stand every other kind down by name. [T-16, INV-22]

---

## Requirement 29: The skill evals prove each skill at its behaviour

**Context:** The skill evals test the pack's own skills at the level that matters for a skill: behaviour. Each working skill owns at least one recorded eval — a scenario where a bare session errs and the skill's text fixes it, proven red at authoring. Evals re-run at milestones and at any delivery that changes a skill's behaviour.

**User Story:** As a person trusting the pack's skills, I want each working skill to own a behaviour eval proven red without it, so that a skill's own instructions are shown to change what a session does rather than assumed to.

### Acceptance Criteria

**Case: one eval per working skill**

1. The system *shall* have each working skill own at least one recorded eval — a scenario proven red without the skill and corrected by it — living in `evals/`, one file per skill. [E-19]
2. *if* a working skill carries no eval, *then* the system *shall* flag it a defect at the milestone audit. [E-19, M-1]

**Case: when the evals re-run**

3. *when* a milestone is reached or a delivery changes a skill's behaviour, the system *shall* re-run that skill's eval, a bump sweeping only a pin or version line owing no re-run. [E-19]

---

## Requirement 30: The surface registry is one self-closing list

**Context:** The surface registry is one host-authored list of every user-facing surface. Its preferred form is executable: the list lives as a declared map inside a completeness-gate test, so a mismatch is a failing test in both directions. A completeness check scans the real rendered artifact against the list, so a surface that renders but is not registered goes red — the registry is self-closing.

**User Story:** As a person guarding surface coverage, I want the registry read as an executable map both ways, so that a rendered-but-unregistered surface and a registered-but-empty one each fail a test.

### Acceptance Criteria

**Case: the executable list, both directions**

1. The system *shall* keep the registry as a declared map inside a completeness-gate test, a mismatch failing in both directions — rendered-but-unregistered and registered-but-empty. [E-10]
2. *when* the completeness check runs, the system *shall* scan the real rendered artifact against the list and red a surface that renders but is not registered. [E-10]

**Case: the honest fallback**

3. The system *shall* keep the list as a document for a host with no test harness, and *when* a host arrives with the executable form already working *shall* recognize it rather than ask it back into a document. [E-10]

---

## Requirement 31: Only an assigned session writes the pack repository

**Context:** The pack runs on its own method, and its repository is a shared surface whose push gates run mechanically on installed hooks. Only a session assigned to the pack itself writes this repository; every other session is read-only here, with one exception — creating a new file in the inbox. A developer's machine keeps its installed skills fresh by a named step, since a hand-copy syncs silently and tells the next breakpoint nothing.

**User Story:** As a maintainer of the shared pack repository, I want only the assigned session to write it and the installed skills synced by a named step, so that no outside session scrambles the tree and every skill version change is reported rather than silent.

### Acceptance Criteria

**Case: the write test**

1. *if* a session cannot say the human asked it in this conversation, or through a standing routine the human created for the pack, to change the pack, *then* the system *shall* not write the repository. [INV-10]
2. The system *shall* keep every other session read-only on this repository, with one exception — creating a new file in the inbox. [INV-10]

**Case: the developer machine syncs by a named step**

3. *when* a session edits a skill on the developer machine, the system *shall* sync the installed copy the same session through the named tool `scripts/sync-skills.sh`, reporting every version change from old to new as the line the re-read rule fires on. [E-23, D-4, A-7]
4. The system *shall* retire a hand-copy, since it syncs silently and tells the next breakpoint nothing that moved. [E-23]
5. The system *shall* run the repository's own push gates mechanically on installed hooks — a fresh prover record, a green suite, anchor ownership, and matrix coverage. [M-4]
6. The system *shall* mint each session a stable identity at its start, so two sessions racing one act tell themselves apart. [INV-117]

---

## Requirement 32: The inbox is the parallel-safe door: one committed file per outside item

**Context:** The inbox is the parallel-safe intake door for wishes and feedback born outside a pack session. Each item arrives as exactly one new file, named by date, source, and slug, since creating a fresh file cannot collide while a shared file can. An agent's own deposit names its source in the filename, and two source words are reserved.

**User Story:** As a person or agent handing an item to the pack from outside, I want each item to land as one new committed file naming its source, so that the deposit races nothing and the receiving gate reads who sent it.

### Acceptance Criteria

**Case: one new file per item**

1. *when* an outside item arrives, the system *shall* place it as one new file named `YYYY-MM-DD-<source>-<slug>.md`, and *shall* never edit an existing file, since a fresh file cannot collide. [E-11]
2. *if* the name is taken, *then* the system *shall* append a numeric ordinal, and *when* two sessions race one slug *shall* add a short session token to the source mark rather than a second identity scheme. [E-11, INV-117]

**Case: the deposit names its source**

3. The system *shall* have an agent's deposit name its source in the filename in the `from-<agent>` form the receiving gate reads. [E-11, INV-189]
4. The system *shall* reserve two source words — the owner's own wish and a stranger's bridged item — both owing no birth record, and *shall* treat an agent-initiated message as a proposal until the owner ratifies it. [INV-189, INV-193]

---

## Requirement 33: The inbox's remote and local arms

**Context:** The inbox opens to seats that share no filesystem and to sessions that share one. A remote seat reaches the repository only through git and deposits one new file committed touching the inbox alone, then pushes under a recorded grant. A co-located session shares one git index, so it writes its one file and stops there, never staging or committing. Each arm fails honestly when it lacks the grant or reach it needs.

**User Story:** As a person depositing from a remote seat or a co-located session, I want each arm to add exactly one new inbox file under its own safe path, so that the deposit races nothing and a missing grant fails by naming the one action that supplies it.

### Acceptance Criteria

**Case: the remote arm**

1. *when* a remote seat deposits, the system *shall* commit one new inbox file touching the inbox alone with the source named, and *shall* push it under a per-repository grant recorded in the host profile. [INV-112, INV-82]
2. *if* a remote push is rejected, *then* the system *shall* retry after a pull, and *shall* never edit an existing file. [INV-112]
3. *if* a remote seat holds no grant, *then* the system *shall* fail honestly, naming the grant it lacks and the one action that supplies it, and *shall* never guess a workaround. [INV-112, INV-67]

**Case: the local co-located arm**

4. *when* a session shares the assigned session's working tree, the system *shall* deposit by writing its one new inbox file and stopping there — no staging, no commit, no push — the assigned session's sweep committing the harvest. [INV-174]
5. The system *shall* read a fresh untracked inbox file as the fence's expected benign case, and a co-located neighbour's stage or commit as a fence stop. [INV-174, INV-11]

**Case: the remote read arm**

6. *when* a remote consumer reads a private producer repository, the system *shall* require a read grant recorded beside the push grant, and *shall* fail honestly naming the read grant it lacks rather than guess. [INV-232, INV-187]

---

## Requirement 34: The inbox's stranger arm and its monitor

**Context:** A stranger holds no grant but can open an Issue or Discussion. The git deposit is closed to them, so the stranger's door is a templated Issue or Discussion that requests a source, and one scheduled monitor converts each open un-surfaced item into one committed inbox file. From that file on, the item is an ordinary inbox wish. The monitor surfaces an item once per activity generation and answers the stranger on the source.

**User Story:** As a stranger with no write path, I want my Issue bridged into one inbox file and answered on its source, so that my wish reaches the queue exactly once and I learn it was heard and where it went.

### Acceptance Criteria

**Case: the monitor bridges the item**

1. *when* the monitor sees an open un-surfaced stranger item, the system *shall* convert it into one new inbox file naming the source Issue and its source field and commit it, touching the inbox alone. [INV-146]
2. The system *shall* keep a stranger's wish off the queue and the repository, the monitor and the sweeping sessions owning every write so no wish is lost. [INV-146, INV-1]

**Case: surfaced once per generation**

3. The system *shall* surface an item at most once per activity generation, reading the generation from comments that are not its own markers, so its own claim and confirm never read back as fresh activity. [INV-146]
4. *when* a swept item's activity generation is newer than the one last recorded, the system *shall* surface it afresh as a new inbox file. [INV-146]

**Case: the item is answered on its source**

5. *when* the sweep judges a surfaced item a wish, the system *shall* harvest it into a queue row and post the capture echo — what was heard, its door, its name, its row — as a comment on the source Issue. [T-10, INV-27]
6. *when* the row reaches a terminal exit, the system *shall* close the source Issue as the convergence an answered question reaches, a surfaced item judged no wish being closed with a recorded note. [T-20, INV-59]

**Case: the monitor's own single-instance law**

7. The system *shall* run the monitor as a single instance per host under a lock stolen by age near 1 hour, and *shall* fail a run that cannot reach the repository honestly, dropping no wish. [INV-147, INV-67]
8. *when* the pack repository runs its monitor, the system *shall* run it as a scheduled action pushing inbox commits only under a single-instance concurrency group, riding the inbox-only carve-out the push gate already grants. [INV-148, M-6]

---

## Requirement 35: Two hosts watching one repository converge on a single surfacing

**Context:** The single-instance lock holds inside one host. Where two hosts' monitors watch one repository, both can read a stranger item as owing a surfacing in the same window, and with no coordination each deposits its own file. The hosts already share the source item, so it carries the claim: a host posts a claim comment, re-reads the claims, and deposits only when its own claim is the winning one.

**User Story:** As a maintainer whose repository two monitors watch, I want the shared source item to carry a claim that picks one winner, so that two hosts converge on one surfacing and a dead winner delays rather than swallows the wish.

### Acceptance Criteria

**Case: the claim picks one winner**

1. *when* a host means to surface an item, the system *shall* post a claim comment carrying its host identity under a hidden marker, re-read the claims, and deposit only when its own claim wins. [INV-149, INV-117]
2. The system *shall* compute the winner identically on every host as the earliest claim by comment creation time, the lower host identity breaking a tie. [INV-149]

**Case: a dead winner is stolen by age**

3. *if* a claim is older than the stale bound the lock uses, *then* the system *shall* read it as abandoned so the next surviving host surfaces the wish. [INV-149]
4. The system *shall* keep a losing host standing down for the round and retrying on its next run, so one wish reaches the shared inbox once. [INV-149]

**Case: the claim rides the writes already held**

5. The system *shall* ride the claim on the comment writes the monitor already holds, asking no new grant, the claim marker staying distinct from the surfaced-generation record. [INV-149, INV-146]
6. *if* a run cannot reach the item to claim it, *then* the system *shall* fail honestly and retry, dropping no wish. [INV-149, INV-67]

---

## Requirement 36: The concurrent-edit fence, the harvest, and one canonical state directory

**Context:** Before writing to a repository, and again before every commit, the agent re-checks the repository's head and tree against what it last read; a moved head or an unexpected change stops it. A pack session sweeps the inbox first, harvesting each file into the home its route owns in one commit that both lands the route and removes the file. The host keeps one canonical state directory, and overlapping lanes default to worktree isolation.

**User Story:** As a person whose repository two sessions might share, I want the fence checked before every write and the harvest atomic, so that concurrent work cannot scramble the tree and every inbox item is harvested exactly once with nothing lost.

### Acceptance Criteria

**Case: the fence before every write**

1. *when* the repository head has moved or the tree holds changes the agent did not make, the system *shall* stop, re-read the changed files, and proceed surgically or back off to the inbox. [INV-11]
2. The system *shall* read a new inbox file as the expected benign case, and *shall* never push while another session is known live in the repository. [INV-11]

**Case: the atomic harvest**

3. *when* a pack session opens, the system *shall* sweep the inbox first and harvest each file into the home its route owns in one commit that both lands the route and removes the file. [T-10]
4. *if* a harvest is interrupted, *then* the system *shall* commit nothing and leave the file for the next sweep, which harvests it once. [T-10]

**Case: one canonical state directory**

5. The system *shall* keep one canonical state directory named `.live-spec`, and *shall* retire a near-miss look-alike to the attic under a manifest line naming the path, the reason, and the canonical directory. [INV-105, INV-7]
6. *when* two lanes' write-sets overlap, the system *shall* default the later lane to worktree isolation, its copy reaching the shared tree only through integration under the pen. [INV-105, INV-39, T-18]

---

## Requirement 37: A delivery that closes a roadmap row refreshes the forward map

**Context:** The movement-end report law asks the seat to refresh the forward map and report after every big movement without being asked; left as once-read prose it fired only on a reminder. Its checkable face is a commit: a delivery is a commit whose diff flips a roadmap row's status cell to the closed token `landed`, and such a commit that does not also touch the forward map reds. A commit that closes no row is not a delivery and owes nothing.

**User Story:** As a person relying on an up-to-date forward map, I want a delivery commit made to refresh the forward map in the same breath, so that a movement that ends never leaves the map stale.

### Acceptance Criteria

**Case: a delivery commit refreshes the map**

1. *when* a commit's diff flips a roadmap row's status cell to the closed token `landed`, the system *shall* require the same commit to touch `NEXT_STEPS.md`, reading the pushed commit range through the same base ladder the other range checks read — the declared base, then `origin/main`, then the previous commit. [INV-242]
2. *if* such a delivery commit does not touch the forward map, *then* the system *shall* red and name the one fix. [INV-242]

**Case: what is not a delivery owes nothing**

3. The system *shall* leave a commit that closes no row, and a row closed to `declined`, `deferred`, or `superseded`, owing no refresh. [INV-242]
4. *when* the push-gate letters are exhausted, the system *shall* ride this check on the suite, so a red here reds the suite gate and blocks the push. [INV-242, INV-222]
