# The rules and who applies them

This section states the shared rulebook every skill works by, who holds authority over what, and how the work scales down when money or time run short. It is written for a reader who has never seen the pipeline before.

Bracket codes like `[INV-69]` and `[E-13]` point to the rule's home in the project spec; a reader can ignore them, a maintainer follows them. The letter before the number names the kind: `INV-` an invariant (a numbered rule that must always hold), `E-` an entity (a numbered part of the product), `T-` a transition (a numbered change of state), `M-` a rhythm rule (a numbered recurring routine), `A-` an adoption step, `D-` a recorded decision, and `ACT-` an actor. The keywords *when*, *while*, *if*, *then*, and *shall* are set in italics and carry their standard requirements meaning: *shall* states a duty, *when* and *while* open a situation, *if* and *then* open a condition and its result.

Terms already defined in the intake glossary, the founding section, and the machinery section — request, inbox, pipeline, spec, architecture, invariant, guardrail, suite, host, pack, session, journal, attic, backlog item, queue, movement, delivery, delivery report, footprint, door, tripwire, narration, milestone, project layers, settings ladder, personal profile, profile, resume file, project kind, freshness check, net, push gate, prover record, seat, pen, adversarial read, expensive decision, design review, and their kin — carry their meanings unchanged. The block below adds only the new nouns this section needs.

## Glossary additions

- **base skill** — the pack skill that holds the shared rulebook and the default settings, stated once, so every working skill points at one home rather than restating them.
- **working skill** — a pack skill that elaborates one domain and opens by naming the base skill and the base version it was written against.
- **senior agent** — the seat that owns judgment, orchestrates the pipeline, briefs workers, and reports to the person.
- **worker** — a delegated agent session the senior agent briefs for a bounded piece of mechanical work, narrowed to the files its brief names.
- **tier** — the model level a unit of work runs at: a no-decision one-shot worker, a multi-step mechanical worker, or the senior agent for judgment.
- **brief** — the written instruction set a worker runs from, carrying its files, its steps, its clock, and its stop conditions.
- **checkpoint** — the persistent file a worker keeps under the host's `.live-spec/checkpoints/`, holding its resume point and touched on a fixed interval as a heartbeat.
- **routing rule** — the rule that proposes the cheapest tier that can pass a brief for each unit of work before the senior agent may overrule it.
- **economy ladder** — the setting `budget.pressure`, whose three rungs — full, lean, and tight — name what rigor a tight budget may shed.
- **done-claim** — a statement that a piece of work is finished, settled by walking its evidence rather than answered from memory.
- **method version** — the pack-and-skill version set a piece of work was carried out under, read from the host's installed set.
- **delegation accounting** — the line a delivered queue row carries naming how its work was delegated, or why the senior agent kept it.
- **never-bend list** — the set of protections that holds at every rung of the economy ladder and does not bend.

---

## Requirement 1: The shared rules live once in the base skill

**Context:** Open any skill in the pack and the same working rules meet the reader. The five rules every skill works by are these: ask and never guess, plain words with the code trailing quietly, one surface with one name, one canonical home per fact, and a junior resuming from a checkpoint. These rules live once in the base skill, the pack's shared rulebook, and each working skill references them rather than restating them.

**User Story:** As a reader opening any skill in the pack, I want the shared rules stated once in the base skill and only referenced elsewhere, so that every skill reads one authoritative copy and no near-copy drifts.

### Acceptance Criteria

**Case: the shared rules have one home**

1. The base skill *shall* state each shared rule normatively beside the pack's default settings, and every working skill *shall* reference the shared rules rather than restate them. [E-12, E-13]
2. *when* a working skill states a shared rule in full a second time, the system *shall* read it as drift and fold it back, since a shared rule has one normative home in the base skill. [INV-13]
3. The pack *shall* treat the package as the source and the standalone repositories as read-only mirrors of it. [D-4]

**Case: a working skill names the base and stands alone**

4. Every working skill *shall* open with one line naming the base skill and the base version it was written against, swept in the same session that bumps the base so the pin never goes stale. [E-12]
5. The system *shall* keep a working skill usable outside the pack, its opening line reading as plain advice and nothing in its own domain needing the base installed. [E-12]

**Case: restatements are pruned at milestones**

6. *when* a milestone is reached, the compaction pass *shall* prune restatements older than the base one skill at a time, so no single rewrite is needed. [M-1, INV-13]

---

## Requirement 2: Every place the pack lists its skills names the same set

**Context:** The pack lists its skills in more than one reader-facing place — the working-skills sentence, the closing lists the skills carry, and the README table. A list is the kind of fact that drifts as the pack grows. A check runs at every commit and reds a list that names fewer skills than the complete set.

**User Story:** As a reader trusting any skill list in the pack, I want every list to name the identical complete set under a mechanical check, so that a list that has fallen behind the pack turns the suite red instead of misinforming a reader.

### Acceptance Criteria

**Case: the lists agree or the suite reds**

1. The system *shall* name the identical complete set of skills in every place the pack lists them — the working-skills sentence, the closing lists, and the README table. [INV-66]
2. *when* a commit leaves a skill list naming fewer than the complete set, the system *shall* red the suite. [INV-66]

---

## Requirement 3: The human owns the taste calls and the working contract

**Context:** The human owns taste, design, the irreversible and publish and push gates, domain wording, and the human's own working contract. The settings ladder resolves to that contract before every human-facing exchange. Mode and trust are set only on the human's word; the agent may propose a level and never raises its own.

**User Story:** As the person a project serves, I want taste and the gates and my own working contract to stay mine and my mode and trust set only on my word, so that every call that turns on taste or preference rests with me.

### Acceptance Criteria

**Case: the human owns the taste calls**

1. The system *shall* keep taste, design, the irreversible and publish and push gates, domain wording, and the human's working contract with the human. [ACT-1, INV-9]
2. Communicator *shall* resolve the whole settings ladder to the working contract before every human-facing exchange, reading the resolved contract rather than one file. [E-13]

**Case: mode and trust move only on the human's word**

3. The system *shall* set proactivity mode and trust only on the human's word, and the agent *shall* propose a level while it never raises its own. [INV-9]
4. The system *shall* hold the lines about the human — proactivity mode, trust, language, and domain vocabulary — in the human's personal profile, following the human across every project. [E-13]

**Case: the host profile lives with the host**

5. The system *shall* create the host profile at attach and keep it git-tracked in the host repository beside the adopt artifacts. [A-8, E-8]
6. The system *shall* keep only the checkpoints ignored inside `.live-spec/`, every other host-profile line staying tracked. [ACT-3, E-8]

---

## Requirement 4: A done-claim is settled by an evidence walk

**Context:** A fluent story can answer any done-claim and might even be right, yet it does not tell a verified fact from a narrated one. So no one answers a done-claim from memory: every claim pins to a checkable artifact walked fresh — an adoption record, a prover record, a suite run with its count, a git commit, a matrix row. The answer states what the walk verified apart from what it merely asserts and names the method version the work was done under.

**User Story:** As a person asking whether a piece of work is done, I want the answer walked fresh from claim to artifact to method version, so that a done-claim rests on checked evidence rather than a fluent story.

### Acceptance Criteria

**Case: the claim walks its evidence**

1. *when* a done-claim is answered, the system *shall* walk it fresh from the claim to a checkable artifact to the method version, and *shall* state what the walk verified apart from what it merely asserts. [INV-25]
2. The system *shall* read the method version from the host's installed set, naming the pack and skill versions from their version homes. [INV-25, M-7]
3. The system *shall* answer no done-claim from memory, treating a claim with no walked artifact behind it as unproven. [INV-25]

**Case: the version is named or its absence is**

4. The system *shall* name the method version on the claim line, so one claim line reads claim, then artifact, then version. [INV-25, M-7]
5. *if* the host carries no installed set, *then* the system *shall* say exactly that, an absent version being an honest answer and never an invented one. [INV-25, M-7]

---

## Requirement 5: Settings climb a four-scope ladder and the narrowest word wins

**Context:** Every way the pack behaves for the human is a named setting with a home in exactly one of four nested scopes: the package defaults, the personal profile, the host profile, and the session's live word. The scopes nest, and resolution reads from the narrowest outward — the session word over the host, the host over the personal profile, the personal profile over the package default. Profiles are re-read at the same freshness points as skills.

**User Story:** As a person whose preferences live at different scopes, I want each setting resolved from the narrowest scope outward, so that a project or a single sitting can override a broader default on my word.

### Acceptance Criteria

**Case: each setting has one scope and the narrowest wins**

1. The system *shall* give every setting a home in one of four nested scopes — the package defaults in the base skill, the personal profile, the host profile, and the session's live word. [E-13, E-12, E-8]
2. The system *shall* resolve a setting from the narrowest scope outward, the session word overriding the host, the host overriding the personal profile, and the personal profile overriding the package default. [E-13]

**Case: profiles are re-read and an unreadable line is ignored aloud**

3. The system *shall* re-read profiles at the same freshness points as skills. [A-7]
4. *when* a profile line falls outside the current pack's vocabulary, the system *shall* ignore it aloud through a dated journal note and a line in the session's next status report, the journal note standing even *if* the session dies before its report. [E-13]

---

## Requirement 6: No override is ever silent

**Context:** An override exists only as a written line in the profile it governs, and setting one leaves a dated note in that home's journal — the host's journal for a host line, the package's journal for a default change. This is the no-silent-micro-decisions rule applied to settings.

**User Story:** As a person auditing how the pack was tuned, I want every override written as a profile line and journaled where it governs, so that no setting changes silently and the record stays readable.

### Acceptance Criteria

**Case: an override is written and journaled**

1. The system *shall* record every override as a written line in its profile file and *shall* leave a dated journal note in the home it governs. [INV-14, INV-5]
2. The system *shall* journal a host line in the host's journal and a default change in the package's journal. [INV-14]

**Case: a tighter host line is recorded, not assumed**

3. The system *shall* let a host contract tighten a package default and *shall* record the tighter line where a reader sees it rather than assume it. [M-6, INV-14]
4. The system *shall* keep the push gate's own cadence as the worked example, the package default asking a full prover pass before a minor bump and a host contract tightening it to before every push. [M-6]

---

## Requirement 7: The session scope is never a file

**Context:** The session scope is the one scope that is never a file: a session override lives only in the human's spoken word and dies with the conversation, and the agent never writes it on its own. Should it outlive the session, that is a promotion into the profile it describes, made on the human's word and journaled. A full wipe ends the sitting and the session lines die with it by design.

**User Story:** As a person setting something for one sitting, I want the session override to live only in my spoken word and die with the conversation unless I promote it, so that a passing choice never silently becomes permanent.

### Acceptance Criteria

**Case: the session word dies with the sitting**

1. The system *shall* keep a session override only in the human's spoken word and *shall* never write it to a file on its own. [INV-14]
2. *when* a session override should outlive the session, the system *shall* promote it into the profile it describes on the human's word and journal it like any other override. [INV-14]

**Case: a wipe ends the sitting**

3. *when* an announced self-compaction runs, the system *shall* carry the live session lines forward in its summary. [M-2, INV-14]
4. *when* a full wipe ends the sitting, the system *shall* let the session lines die with it, since that loss is the human's own move. [INV-14]

---

## Requirement 8: The personal layer has one home and the loader stays thin

**Context:** Everything personal lives in one place, the personal profile, and the machine-global instruction file shrinks to a thin loader carrying only the bootstrap lines that must hold before any pack file loads. Migrating an existing rule file into this shape forks each rule to the scope it describes — a method rule stays the pack's, a personal line moves to the profile, a project line moves to that project's host profile. A rule-by-rule mapping proves the move lossless and the old file stays in the attic.

**User Story:** As a person consolidating a tangled rule file, I want each rule forked to the scope it describes with the old file kept in the attic, so that the personal layer has one home and one move rolls the whole change back.

### Acceptance Criteria

**Case: one home and a thin loader**

1. The system *shall* keep the personal layer in the personal profile and *shall* shrink the global instruction file to a thin loader carrying only the bootstrap lines that must hold before any pack file loads. [E-16, INV-13]
2. The system *shall* keep the loader the one home for those bootstrap lines and *shall* never restate them in the profile. [INV-13]

**Case: a rule file forks by scope, losing nothing**

3. *when* an existing rule file is migrated, the system *shall* fork each rule to the scope it describes — a method rule staying the pack's, a personal line moving to the profile, a project line becoming a migration note for that project's own session to land. [E-16, INV-10]
4. The system *shall* prove the move lossless rule by rule and *shall* keep the old file in the attic, so one move rolls the change back. [E-16, INV-7]
5. *while* the promotion sits outside any repository fence, the system *shall* re-read the file immediately before appending, its git home standing as the recovery net. [INV-11, E-16]

---

## Requirement 9: The senior agent owns judgment and workers run the tiers

**Context:** The senior agent owns every judgment call — spec deltas, matrix levels, findings triage, and this document. Workers own mechanical execution, each keeping a persistent checkpoint file under the host's `.live-spec/checkpoints/`. Three tiers stand: a no-decision one-shot worker, a multi-step mechanical worker, and the senior agent for judgment.

**User Story:** As a person watching work split between judgment and mechanism, I want judgment held by the senior agent and mechanical work run by tiered workers with durable checkpoints, so that the calls that shape the work stay with the agent qualified to make them.

### Acceptance Criteria

**Case: judgment stays with the senior agent**

1. The senior agent *shall* own every judgment call — spec deltas, matrix levels, findings triage, and this document — and that judgment *shall* never route down to a worker. [ACT-2]
2. The routing rule *shall* propose which tier a unit of work runs at before the senior agent may overrule it. [INV-69]

**Case: workers run the mechanical tiers**

3. The system *shall* run mechanical work on tiered workers — a no-decision one-shot worker, a multi-step mechanical worker, and the senior agent for judgment. [INV-69]
4. Each worker *shall* keep a persistent checkpoint file under the host's `.live-spec/checkpoints/`, kept out of git and off the temporary directory so a reboot never erases a resume point. [ACT-3, INV-69]

---

## Requirement 10: The worker contract binds every delegation

**Context:** One contract binds every delegation. A worker inherits its session's write-ownership narrowed to the files its brief names, reads outside them, and never writes there. Its brief carries the clock, the live setting lines, and the problem-ledger duty, and it heartbeats its checkpoint so a busy worker is never mistaken for a dead one. At teardown the worker reaps only the process group it spawned.

**User Story:** As a person relying on delegated work, I want every worker bound by one contract — narrowed write-ownership, an inherited clock and settings, a ledger duty, a heartbeat, and a scoped teardown — so that parallel help never corrupts the tree or the record.

### Acceptance Criteria

**Case: write-ownership is narrowed to the brief**

1. A worker *shall* inherit its session's write-ownership narrowed to the files its brief names, reading outside them and never writing there. [INV-10]
2. *when* a brief names an isolated copy of the tree, the system *shall* let that copy's delta reach the shared tree only through the senior agent's integration under the pen. [T-18, INV-39]
3. *when* the senior agent means to spawn another concurrent writer, it *shall* confirm the brief's write-set is disjoint from every running writer's brief or give it an isolated worktree, since the concurrent-edit fence stays quiet between same-session siblings. [INV-11, INV-105, ACT-3]

**Case: the brief carries the clock, the settings, and the ledger**

4. The system *shall* ride the session's live setting lines into the brief verbatim, since a worker cannot resolve the ladder itself. [E-13]
5. The system *shall* carry the clock into the brief so a worker's stamps come off the brief's clock and are never invented, and *shall* carry the problem-ledger path so any noise the worker meets becomes one ledger line rather than a silent retry. [INV-24, INV-23]

**Case: the heartbeat and the scoped teardown**

6. A worker *shall* touch its checkpoint file on a fixed interval near 60 seconds as a heartbeat, so a compute-bound run that writes no product file for minutes is never read as dead. [INV-76]
7. *when* a result fails its brief's acceptance, the worker *shall* escalate one tier with a logged line and *shall* never retry silently on the same tier or skip a rung. [ACT-3]
8. *when* a worker tears down, the system *shall* reap only the process group it spawned, reading a stall from the checkpoint's modification time and confirming ownership before any reap, never a kill by name. [INV-162, INV-230, INV-76]

---

## Requirement 11: The routing rule proposes the cheapest tier and the senior may overrule

**Context:** Before anyone delegates a unit of work, the routing rule proposes its tier from what the work is, not its size alone — a judgment step to the senior agent and never down, a no-decision one-shot to the cheapest worker, a multi-step mechanical brief to the mid worker. The economy rung moves the threshold. The proposal is advisory: the senior agent may overrule it per wish, and the override rides one logged line reading proposed tier, chosen tier, and why.

**User Story:** As a person paying for the right tier on each unit of work, I want the routing rule to propose the cheapest tier that can pass the brief and the senior's override always logged, so that no tier changes silently and judgment work never routes down.

### Acceptance Criteria

**Case: the proposal reads the work, not its size**

1. The routing rule *shall* propose a judgment step to the senior agent and never route it down, a no-decision one-shot to the cheapest worker, and a multi-step mechanical brief to the mid worker. [INV-69, ACT-2]
2. The system *shall* treat the size class as a coarse prior only, the step inside the work deciding its tier. [INV-69]

**Case: the economy rung moves the threshold**

3. *when* the economy rung is lean, the system *shall* let an airtight brief — one that leaves the worker nothing to decide — ride one tier cheaper and *shall* raise the bar for keeping a step on the senior agent. [T-19, INV-69]
4. *when* the economy rung is tight, the system *shall* propose the cheapest tier that can pass the brief and *shall* spend the senior agent's hours on judgment alone. [T-19, INV-69]

**Case: the override is advisory and logged**

5. The senior agent *shall* be free to overrule the proposal per wish, and the system *shall* ride one logged line — proposed tier, chosen tier, and why — on the checkpoint and the delivery report. [D-2, INV-69]
6. The system *shall* keep this assignment-time override distinct from the failed-acceptance escalation, both logged on their own lines, so a silent tier change cannot stand. [ACT-3, INV-69]

---

## Requirement 12: A delivered row carries its delegation accounting

**Context:** Every delivered queue row records how its work was delegated: the unit that went to a worker with an estimated saving, or a stood-down line naming why the senior agent kept the work. The line lives in the row's status cell, and a suite check reds a delivered row that omits it. The duty binds the orchestrating seat whatever tier leads it.

**User Story:** As a person auditing how work was delegated, I want every delivered row to carry its delegation accounting under a suite check, so that the account of who did each piece of work is never silently dropped.

### Acceptance Criteria

**Case: the delivered row carries the line**

1. The system *shall* record on each delivered row's status cell how its work was delegated — the unit sent to a worker with an estimated saving, or why the senior agent kept it — and *shall* red the suite *when* a delivered row omits the line. [INV-103]
   [GAP: the delegation accounting records a saving for each delegated unit, but the source names no unit or baseline the saving is measured against — tokens, wall-time, or cost — so a correct saving figure is undefined and a test author cannot pin it.]
2. The system *shall* bind the duty to the orchestrating seat whatever tier leads it, and *shall* bind it forward from its own reach rather than over rows already delivered. [INV-103, INV-159]

---

## Requirement 13: The senior agent reads to decide and dispatches the discovery reads

**Context:** The senior agent keeps its context lean by dispatching reads rather than performing them. It holds orchestration material — the human's words, the decisions taken, the distilled results workers return, and the anchors it must cite — and dispatches any reading done to understand or design past a bounded glance to a reader worker that returns a distillation. A read done to verify a claim or settle a decision stays with the senior agent. The leanness is load-bearing: a context filled with raw source it could have distilled loses the room to hold the whole arc.

**User Story:** As a person relying on the senior agent's judgment across a long arc, I want discovery reads dispatched to reader workers and only distillations kept, so that the senior agent's context stays lean and its judgment does not degrade under raw source.

### Acceptance Criteria

**Case: discovery reads route to workers**

1. The senior agent *shall* dispatch any read done to understand or design past a bounded glance to a reader worker and *shall* keep only the distillation. [INV-137, INV-69]
2. The system *shall* bound a glance to one small file or a handful of targeted lines whose result is itself the deliverable, past which the read routes like any unit of work. [INV-137, INV-69]

**Case: verify reads stay, discovery reads show**

3. The system *shall* keep a read done to verify a claim or settle a decision with the senior agent, checking the real artifact and re-reading a primary source being its own hands. [INV-137]
4. The system *shall* dispatch the brief-owed read of the files a change will touch to the reader worker whose distillation returns the per-file lines, or make it a bounded decide-read for a small edit. [INV-53, INV-137]
5. The system *shall* name the reads dispatched in the delivery report's delegation accounting, so a session that slid into reading to discover shows it. [INV-103, INV-137]

---

## Requirement 14: The senior agent decides what it can and surfaces only what it cannot

**Context:** The senior agent decides what it can decide and reports the choice — a mechanical step, a value a proven artifact already determines, a sensible default it can pick and name. It surfaces a decision to the human only where the decision genuinely cannot be made without them: a taste call, a trade-off no artifact settles, or a change to the definition of correct. It never parks derivable work on the human's queue to avoid deciding, and the posture holds even on a session resumed from its files after a memory wipe.

**User Story:** As a person who should be asked only what genuinely needs me, I want the senior agent to decide every derivable question and report it, so that a taste call reaches me while derivable work never waits on my queue.

### Acceptance Criteria

**Case: it decides what an artifact or a default settles**

1. The senior agent *shall* decide a mechanical step, a value a proven artifact already determines, or a default it can pick, and *shall* report the choice with its `[default]` tag. [INV-143, INV-121, INV-70]
2. The system *shall* hold this posture on every session, including one resumed from its files after a memory wipe. [INV-143, INV-48]

**Case: it surfaces only what needs the human**

3. The senior agent *shall* surface a decision to the human only where it cannot be made without them — a taste call, a trade-off no artifact settles, or a change to the definition of correct. [INV-143, INV-121]
4. The system *shall* never park derivable work on the human's queue to avoid deciding. [INV-143, INV-4]

---

## Requirement 15: A deferral must justify itself or the item is the seat's to do

**Context:** A backlog item carrying a needs-the-human's-word marker is re-tested for derivability every time it is touched, not only when first written. Where the answer pins to an existing artifact — a base rule, a spec sentence, the architecture, an approved prototype, or an already-answered decision — the item is the seat's to do, cite, and drop the marker. Where it needs a fact no artifact holds — a taste, a policy, or a move irreversible outside git — it is the human's and the marker stands, but writing the marker requires naming that human-only fact.

**User Story:** As a person handed only the questions that truly need me, I want every deferral marker re-tested for derivability and made to name its human-only fact, so that a derivable item becomes the seat's own instead of parking on me.

### Acceptance Criteria

**Case: a derivable item is the seat's**

1. *when* a held backlog item is touched, the system *shall* re-test it for derivability, and *when* the answer pins to an existing artifact the seat *shall* do the item, cite the artifact, and drop the marker. [INV-152, INV-59, INV-121, INV-143]
2. *if* the item needs a fact no artifact holds — a taste, a policy, or a move irreversible outside git — *then* the marker *shall* stand and *shall* name that human-only fact. [INV-152, INV-17]
3. The system *shall* default a marker that cannot name its human-only fact to the seat's own, the unnamed marker being the finding, the same shape as a request matching no kind in the closed door set. [INV-152, INV-151]

**Case: two arms enforce the deferral**

4. The system *shall* red a commit *when* a mechanical net finds a parked item in the resume file or a decision page naming no reason category — taste, policy, irreversible, or device-feel. [INV-152, INV-155]
5. *when* a marker is written or a question is opened to the human, a delivery arm *shall* re-fire the derivability test at that moment, reading the grammatical shape of a deferral rather than a closed list of phrasings. [INV-152, INV-28, INV-4]

---

## Requirement 16: A worker's green earns a second pair of eyes

**Context:** A worker's report is a lead and never counts as evidence, since the head that made the work is blind to its own gap. So the verify step carries an audit — a whole-read that sets out to break the work: a fresh-context checker briefed with the spec sentences the delivery claims and the artifact paths, never the worker's summary or the senior's plan. It walks each claimed fact up a fixed ladder — that it exists, that it is substantive, that it is wired, and that real values flow end to end — and its findings become rows or red.

**User Story:** As a person trusting a green suite, I want a high-stakes delivery whose only review is its author's checked by a fresh adversarial reader, so that a green machine that is actually hollow is caught before it is called done.

### Acceptance Criteria

**Case: the audit walks a fixed ladder from a fresh context**

1. The verify step *shall* brief a fresh-context checker with the delivery's spec sentences and artifact paths, never the worker's summary or the senior's plan, opening on the hypothesis that the tasks were done and the goal missed. [INV-46]
2. The checker *shall* walk each claimed fact up a fixed ladder — that it exists, that it is substantive against the placeholder-stub list, that it is wired, and that real values flow end to end — its findings becoming rows or red. [INV-46]

**Case: it fires mandatory on a high-stakes author-only delivery**

3. The system *shall* fire the audit mandatory *when* a delivery is high-stakes — a surface-sized delta or a change to the method itself — and its only review is the author's own. [INV-46]
4. The system *shall* count a review independent only *when* a differently-contexted head is briefed from the primary sources on the goal-missed hypothesis, a same-context prover pass never counting and delegation alone never making it independent. [INV-46]
5. One fresh checker *shall* cover every law in a delivery batch, the checker being a worker under its own contract whose verdict rides the delivery report. [INV-61, ACT-3]

---

## Requirement 17: An expensive decision earns an adversarial read before it lands

**Context:** A decision is expensive when unwinding it costs more than making it did, and the pack's expensive decisions are a closed, enumerable set: the birth of a new agent, a node carved or merged in the architecture, the shape of a contract once a consumer has pinned it, a project's kind, the split of a reusable product into engine and instance, and a repository going public. No machine tells an expensive decision from an ordinary one, so the duty is stated for the whole class and each member carries it at its own decision point as the pack wires it. The read is a fresh-context independent audit that closes by bringing the decision to the human with findings and a recommendation.

**User Story:** As a person owning the taste call on a costly decision, I want each expensive decision to earn a fresh adversarial read that reaches me with findings and a recommendation, so that the call rests on a broken-and-tested case rather than a first draft.

### Acceptance Criteria

**Case: the class is closed and enumerated**

1. The system *shall* treat the expensive-decision set as closed and enumerable — an agent's birth, a node carved or merged, a contract's shape once a consumer pinned it, a project's kind, an engine-and-instance split, and a repository going public — naming every member on the enumerate-versus-ride keying. [INV-235, T-22, INV-113, INV-122, INV-187, INV-36, INV-85, INV-44, INV-226]
2. The system *shall* state the duty for the whole class and have each member carry it at its own decision point, a traceability test holding that this clause names the read and that agent birth carries it. [INV-235]

**Case: the read is adversarial and closes with the human**

3. *when* an expensive decision is about to land, the system *shall* run a fresh-context independent audit at the best tier the pack's quality habit sets, set on breaking the case as the verify audit reads a delivery. [INV-235, INV-46, INV-145]
   [GAP: the read runs at the best tier the pack's quality habit sets, but the source neither defines that quality habit nor states which tier it yields for this read, so the read's out-of-box model tier is unstated.]
4. *where* the decision turns on whether members are one kind, the design review *shall* read the grouping with the two compared objects in hand. [INV-235, INV-141, INV-142]
5. The read *shall* close by bringing the decision to the human with its findings and a recommendation, the taste call staying the human's because it needs a fact only the human holds. [INV-235, INV-143, INV-152]

---

## Requirement 18: The authoring seat does not certify its own work

**Context:** The seat that authored a change drafts and accepts it but never provides its own adversarial certification, since a head marinated in the authoring context is blind to the gap it just wrote. Two carriers follow. A release's adversarial pass — the full prover re-prove at the release gate — is authored by a fresh, differently-contexted seat, and a newly added lens or rule is applied to the very document that introduces it before release. The release gate may require a dated clean-context review record naming a seat other than the release's.

**User Story:** As a person trusting a release, I want its adversarial pass run by a fresh seat and every new rule applied to its own introducing document, so that an authoring-blind gap is caught by a differently-contexted head before the release ships.

### Acceptance Criteria

**Case: the author drafts but does not certify**

1. The system *shall* let the authoring seat draft and accept a change and *shall* never let it provide the change's own adversarial certification. [INV-237]
2. The system *shall* author a release's adversarial pass — the full prover re-prove at the release gate — with a fresh, differently-contexted seat under the freshness the verify audit already defines. [INV-237, INV-116, INV-217, INV-46, INV-145]

**Case: a new rule is self-applied and the record names a fresh seat**

3. *when* a release is prepared, the system *shall* apply a newly added lens or rule to the document that introduces it and *shall* name the result in the release record. [INV-237]
4. The release gate *shall* be able to require a dated review record that exists, is dated to the release, and names a seat other than the release's. [INV-237]

---

## Requirement 19: A brief is born from read files, never from memory

**Context:** Before writing a brief that edits existing files, the brief-writer reads in full every file the work will modify. The brief records three lines per file — its current state, what changes, and what must survive — and every step back-references the spec sentence it serves while every technical claim cites its source. A brief written from memory hands the worker a guess dressed up as fact.

**User Story:** As a worker handed a brief, I want it born from a full read of the files it touches with three recorded lines each, so that I am handed evidence rather than the senior's guess.

### Acceptance Criteria

**Case: the brief is read from the files**

1. The system *shall* write a brief that edits existing files only after reading in full every file the work will modify, recording three lines per file — current state, what changes, and what must survive. [INV-53]
2. The system *shall* have every step back-reference its spec sentence and every technical claim cite its source as a file-and-line reference or a command's output. [INV-53]
3. The system *shall* dispatch this read to the reader worker whose distillation returns the three per-file lines, or make it a bounded decide-read for a small edit. [INV-53, INV-137]

---

## Requirement 20: A worker stops only on a named condition

**Context:** The brief carries a closed, short halt list: an ambiguous requirement, two consecutive unexplained failures of one command, a missing config or dependency, or an acceptance impossible as briefed. On any of these the worker stops with evidence; otherwise it runs to completion. This is sharper than an open standing instruction to ask when unsure, and it composes with the one-tier escalation.

**User Story:** As a person delegating a bounded job, I want the worker to stop only on a closed list of named conditions and otherwise run to completion, so that it neither pushes past a real blocker nor stalls on ordinary uncertainty.

### Acceptance Criteria

**Case: the closed halt list**

1. The system *shall* carry a closed halt list in the brief — an ambiguous requirement, two consecutive unexplained failures of one command, a missing config or dependency, or an acceptance impossible as briefed. [INV-54]
2. *when* a halt condition holds, the worker *shall* stop with evidence, and otherwise *shall* run to completion, composing with the one-tier escalation. [INV-54, ACT-3]

---

## Requirement 21: A brief is sized to its worker's head

**Context:** A brief targets a bounded share of its worker's context and splits above it, the default bound being the brief's own text within about 300 lines and at most about 8 files to edit. Above either limit the work splits into staged briefs. A brief passes paths and never inlined file bodies, since an inlined body goes stale the moment a sibling edits the file.

**User Story:** As a worker with a bounded head, I want a brief kept under a concrete size bound and passing paths not file bodies, so that I read my own current truth from disk and no pasted copy goes stale.

### Acceptance Criteria

**Case: the size bound and the split**

1. The system *shall* keep a brief within its default bound — about 300 lines of brief text and at most about 8 files to edit — and *shall* split the work into staged briefs above either limit. [INV-55]
2. The system *shall* pass paths in a brief and never an inlined file body, so the worker reads its own current truth from disk. [INV-55]

---

## Requirement 22: The economy ladder names what a tight budget may shed

**Context:** Rigor costs money and time, so the pack names what a tight budget may legally shed and makes it a setting the human moved rather than an improvisation under pressure. The pressure lives as one setting, `budget.pressure`, with package default full, and it moves only on the human's word. Three rungs each name their legal sheds, and every shed actually taken is said in the delivery report.

**User Story:** As a person under a money or time pressure, I want the sheds named as a rung I set rather than improvised, so that cost-cutting is a recorded choice and every shed appears in the delivery report.

### Acceptance Criteria

**Case: the rung is a setting the human moved**

1. The system *shall* hold the pressure as one setting, `budget.pressure`, defaulting to full, moved only on the human's word — a session word for today or a profile line to stand. [T-19, E-13, INV-9]
2. *when* the human names a money or time pressure, the agent *shall* propose a rung and *shall* never set one, and the pack *shall* ask the rung or state the standing default at project setup beside the project kind. [T-19, INV-36]

**Case: each rung names its legal sheds**

3. *when* the rung is full, the system *shall* run the full suite at every delivery gate, run the prover at its recorded cadence, and route tiers by the routing rule. [T-19, INV-69]
4. *when* the rung is lean, the system *shall* scope mid-work test runs to the touched architecture node's rows while running the full suite at every delivery gate and before every push, and *shall* write a deferred full pass as a dated debt line in its queue row. [T-19, INV-69]
5. *when* the rung is tight, the system *shall* batch consecutive small deliveries into one full-suite run at the batch's end, keep each commit at one row's delta, and bisect a batch-end red by delivery order before reverting to the last green base. [T-19, INV-39]
6. *when* a push runs under any rung, the system *shall* still require the batch's reach-scoped gate green at the tree's head and the host's recorded prover cadence. [INV-45, M-6]

---

## Requirement 23: The never-bend list holds at every rung

**Context:** A short list of protections holds at every rung of the economy ladder no matter how tight the budget, and this never-bend list does not bend. It carries the door law and its tripwires, red-before-fix, the human's gates, the delivery report with its taken defaults and named sheds, delivery purity, the push gate running every check the diff can reach, the safety net, and whole narration. An explicit host line outlives any rung.

**User Story:** As a person cutting cost under pressure, I want a named never-bend list that no rung touches, so that a tight budget slows spend without dropping the guarantees that matter.

### Acceptance Criteria

**Case: what never bends**

1. The system *shall* hold at every rung the door law and its tripwires, red-before-fix, and the human's gates over irreversible moves, publishing, authored content, and taste. [INV-40, T-12, INV-16, INV-9]
2. The system *shall* hold at every rung the delivery report carrying its taken defaults and named sheds, delivery purity at one row's delta per commit, and whole narration. [INV-40, INV-5, INV-31, INV-39, INV-35]
3. The system *shall* hold at every rung the push gate — work leaving the machine only when every check the diff can reach is green at the tree's head, plus the host's recorded prover cadence — and the safety net no work-kind or scope cut touches. [INV-40, INV-45, M-6, T-15, T-16]

**Case: an explicit host line outlives the rung**

4. *when* a host profile pins a tighter cadence, the system *shall* keep it even under the tight rung. [E-13, INV-40]
5. The system *shall* move `budget.pressure` only by the human's word and *shall* switch no rung automatically. [T-19, INV-40]
