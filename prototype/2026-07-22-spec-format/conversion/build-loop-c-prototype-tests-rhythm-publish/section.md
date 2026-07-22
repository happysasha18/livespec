# The build loop, part C — prototypes, the spec-to-tests bridge, the rhythm, and publishing

This section states the last stretch of the build loop: how a prototype stays a fenced sketch and how an approved sketch becomes the binding look; the two documents that bridge the spec to the tests and the test-infrastructure laws that keep a green suite honest; the working rhythm of breakpoints, milestones, versioning, time, and pushes; and what a piece of work owes its reader when it leaves the machine. It is written for a reader who has never seen the pipeline before.

Bracket codes like `[INV-157]` and `[E-14]` point to the rule's home in the project spec; a reader can ignore them, a maintainer follows them. The letter before the number names the kind: `INV-` an invariant (a numbered rule that must always hold), `E-` an entity (a numbered part of the product), `T-` a transition (a numbered change of state), `M-` a rhythm rule (a numbered recurring routine), `A-` an adoption step, `ACT-` an actor, and `S-` a header rule. A trailing `[target]` marks a leg promised but not yet enforced, and `[default]` marks a value the agent set that the human may retune. The keywords *when*, *while*, *if*, *then*, and *shall* are set in lowercase italics and carry their standard requirements meaning: *shall* states a duty, *when* and *while* open a situation, *if* and *then* open a condition and its result.

Terms already defined in the intake glossary, the founding section, the agents-together section, and the bounds section — among them request, inbox, pipeline, spec, architecture, invariant, guardrail, suite, host, pack, session, journal, attic, queue, movement, delivery, delivery report, project layers, settings ladder, personal profile, profile, resume file, migration chapter, ratchet manifest, project kind, proof kinds, design principle, engine, instance, content contract, milestone, feel pass, prover record, test matrix, feature-coverage trace, register judge, surface registry, grant, push gate — carry their meanings unchanged. The block below adds only the new nouns this section needs.

## Glossary additions

- **prototype** — an exploration of an idea kept as a sketch, living fenced off in its own clearly named home such as a `prototype/` folder or branch, so nothing in the shipped product reaches into it.
- **prod surface** — any part of the shipped product a user meets.
- **norm** — an approved prototype frozen as the binding record of a surface's look and feel, kept as a dated copy under `docs/norms/`.
- **norm pointer** — the `norm: <path>` reference a spec clause carries at its line end, pointing at the frozen norm artifact its behaviour is checked against.
- **architecture node** — one named unit in the architecture document carrying one responsibility and one name, owning the spec facts it implements and pinned to its place in the code.
- **level ladder** — the ordered set of test levels a matrix row pins to, running string, then document-text, then browser-computed, then pixel.
- **real-device walk row** — a matrix row for a behaviour living past a desktop headless browser, one the suite can never turn green, owed to the human's own hands before ship.
- **coverage validation** — the checklist that closes the matrix derivation, walked to confirm every spec anchor, artifact, and node carries the rows it owes.
- **breakpoint** — a point where a movement ends and session memory can be wiped with no loss, its live state replaced, a dated journal entry added, and the work committed.
- **checkpoint** — one grouped unit of planned work in the resume state, carrying a status the landing that ships its items flips to closed.
- **skill-creator** — the skill-making skill that reviews each skill file's craft, apart from the evals that test each skill's behaviour.
- **thin loader** — the personal layer's global instruction file, holding only what must be true before any pack file loads.
- **shopfront** — the public README as the reader-facing front of a repository, whose claims match the truth just pushed.
- **attribution line** — the single `made with live-spec` line a built-with publication carries on its landing surface, naming the pack version the project runs.
- **standalone mirror** — a public mirror repository rebuilt from the pack folder by the sync script, carrying its own generated banner, release history, and attribution line.
- **design project** — the team's own design project, an external destination where rendered cards go for human review.
- **publish gate** — the human's own gate over anything irreversible or outward, which the publish checklist runs ahead of.
- **publish checklist** — the per-kind walk the publish skill owns, run before any deposit leaves the machine.
- **remote gate** — the check set a host may mirror in its continuous-integration runner, whose verdict the pushing session reads after a push.
- **work-kind** — the kind a wish is tagged with at intake, one of product, infra, skill, or prose, which scales how much machinery each step spends.

---

## Requirement 1: A prototype is a fenced sketch that carries its label

**Context:** Exploring an idea before committing to it is allowed, and a prototype is that exploration kept as a sketch. It lives fenced off in its own clearly named home, and the fence runs one way — influence crosses out of the prototype and never into the shipped product. Every artifact the prototype produces announces itself.

**User Story:** As a person exploring an idea, I want the sketch fenced off and labelled in whatever form its kind can show, so that a try-it-out experiment never leaks into the product a user meets.

### Acceptance Criteria

**Case: the label rides every artifact**

1. *when* a prototype produces an artifact, the system *shall* mark it with the `PROTOTYPE` label in the form its kind can show — an on-screen banner for a rendered page, a `_prototype: true` field or header for an API or data payload, a first-line banner for a script, and the marker in the name or header line for a bare file. [E-17]
2. The system *shall* keep the prototype's code sitting apart in its own named home, with nothing in the shipped product reaching into it. [E-17]

**Case: the fence runs one way**

3. The system *shall* let influence cross out of a prototype and never into a prod surface: never wiring a prototype into a prod surface, never linking to a prototype from a prod surface, and never styling a prod surface to match a prototype. [INV-17]
4. *when* a prototype is shown to the human, the system *shall* show it only under its label, and *shall* let nothing reach the human as the product until its surface has walked the full pipeline. [E-17, INV-17]

---

## Requirement 2: The door step decides a feature from a sketch

**Context:** The boundary between a feature and a sketch sits at the door step, the point where a request becomes a product feature. A wish to have something in the product is a feature and walks the pipeline; a request to merely see or try something, with no commitment, may live as a sketch inside the fence. When the door is unclear, the agent asks rather than guesses.

**User Story:** As a person voicing a request, I want the door step to sort a feature from a sketch by a fixed rule, so that a commitment gets a spec and a lane while a no-commitment try stays a free sketch.

### Acceptance Criteria

**Case: the boundary at the door**

1. *when* a wish asks to have something in the product, the system *shall* read it as a feature and route it through the build pipeline. [INV-16]
2. *when* a request asks only to see or try something with no commitment, the system *shall* let it live as a sketch inside the fence, carrying no lane through the build pipeline and no spec. [INV-16, E-17]

**Case: the unclear door asks**

3. *if* which of the two was meant is unclear, *then* the system *shall* ask one plain question and *shall* not guess. [INV-16]

---

## Requirement 3: Opening a prototype home is a repo write

**Context:** A prototype home is a folder or branch, and creating it writes to the repository like any other write. So the write-ownership law governs it, the assigned senior agent makes the judgment call, and a session working from outside files an inbox wish rather than opening the home itself.

**User Story:** As a maintainer of the repository, I want opening a prototype home held to the write-ownership law, so that a worker never opens a prototype home on its own brief and an outside session routes through the inbox.

### Acceptance Criteria

**Case: the write is owned**

1. *when* a prototype home is opened, the system *shall* govern that write by the write-ownership law and *shall* leave the judgment call to the assigned senior agent. [INV-10, ACT-2]
2. *when* a session works from outside the assigned pack session, the system *shall* have it file an inbox wish rather than open a prototype home on its own brief. [INV-10]

---

## Requirement 4: Promotion enters a sketch's earned feature at the spec step

**Context:** When a sketch earns its place, its feature enters the pipeline at the spec step like any wish, without its code being merged. The prototype serves as evidence for that spec, and its code holds no rights.

**User Story:** As a person promoting a proven sketch, I want its feature to enter at the spec step with the code left behind, so that the earned idea is specced fresh and the sketch's code claims nothing.

### Acceptance Criteria

**Case: the earned feature is specced, not merged**

1. *when* a sketch earns its place, the system *shall* enter its feature at the spec step like any wish and *shall* not merge the sketch's code. [T-12, INV-16]
2. The system *shall* treat the prototype as evidence for that spec, its code holding no rights. [T-12]

---

## Requirement 5: The fence guardrail's three legs and the header's honesty

**Context:** A guardrails check enforces the one-way fence, and it has three legs. One leg runs live today; two are promised targets. When all three land, the header's honesty rule holds in both directions — the spec never claims what is not built, and the build never contains what the spec does not name.

**User Story:** As a person trusting the fence, I want a mechanical check with three named legs and one honest note of which run today, so that a prod file reaching into a prototype turns red while the promised legs are marked rather than pretended.

### Acceptance Criteria

**Case: the three legs**

1. *when* a prod file references anything inside a prototype home, the system *shall* turn the fence leg red. [E-6]
2. The system *shall* enforce the completeness scan over the surface registry and the behaviour-traces-to-spec check as the two remaining legs. [E-10, E-6, target]

**Case: the honesty in both directions**

3. *when* all three legs land, the system *shall* hold that the spec never claims what is not built and the build never contains what the spec does not name. [S-0, INV-17]
4. *while* only the fence leg is enforced, the system *shall* keep the other two legs promised, marked, and owned by their rows. [INV-17, target]

---

## Requirement 6: An approved look is frozen as the norm its clause cites

**Context:** Prose alone cannot record how a design looks and feels, so a rebuild made from prose with no artifact to check against can pass every test and still ship a look-alike. Once the human approves a sketch as the look, that prototype becomes the norm for look and feel. The clause it governs cites the frozen artifact, and approval freezes a dated copy into the project's records.

**User Story:** As a person who approved a look, I want the approving clause to cite a frozen copy of the artifact, so that a later rebuild is checked against the real look rather than a prose paraphrase.

### Acceptance Criteria

**Case: the clause cites its artifact**

1. *when* a clause is governed by an approved look, the system *shall* place a norm pointer of the form `norm: <path>` at the clause's line end beside its anchors, the prose carrying the laws and the artifact keeping the look. [INV-43]
2. *when* a sketch is approved as the look, the system *shall* freeze a copy into `docs/norms/` with a dated provenance line naming what it is, when it was approved, and which sketch it came from. [INV-43]

**Case: the pointer never reaches a live sketch**

3. The system *shall* have the norm pointer cite the frozen copy and *shall* never let it reach into a live prototype home, so the one-way fence stays absolute and the sketch stays free to die. [INV-43, E-17, INV-17]

---

## Requirement 7: The build and the prover read the norm

**Context:** A norm is only as good as the reads that enforce it. When a surface's clauses carry a norm pointer, the build opens the artifact before writing code and records a plan-versus-prototype diff; the verify feel pass reads the same pointer; and the prover reads visual clauses with a norm lens. A story may also demand the human see a mockup before the build starts.

**User Story:** As a person guarding an approved look, I want the build, the verify pass, and the prover all reading the norm pointer, so that a missing line is caught at the code step and a pointerless prototype-born clause is flagged.

### Acceptance Criteria

**Case: the build reads the artifact**

1. *when* a surface whose clauses carry a norm pointer is built, the system *shall* open the artifact before the code step and *shall* record a one-line plan-versus-prototype diff in the landing report, a missing line being a defect caught at the code step. [INV-43]
2. The system *shall* have the verify step's feel pass read the same norm pointer. [INV-43, INV-30]

**Case: the prover's norm lens**

3. *when* the prover reads a visual clause, the system *shall* flag a prototype-born clause carrying no pointer, and *shall* flag a clause whose text contradicts its own artifact. [INV-43]

**Case: the mockup-first entry condition**

4. *when* a story declares the human must see a mockup before the build starts, the system *shall* write the condition in the wish's queue row as `entry: mockup-first` and *shall* hold it at the door step until the human cancels it by name, a general instruction to build moving priority without cancelling it. [INV-43]

**Case: the pointer binds forward only**

5. The system *shall* add a clause's pointer at the first landing that touches it and *shall* never apply pointers retroactively across the whole spec at once. [INV-43, INV-159]
6. The system *shall* place a pointer only for a prototype the human approved as the look, leaving an unapproved sketch as plain evidence in its fence and a text-born clause with no pointer. [INV-43, E-17]

---

## Requirement 8: The test method lives in the test-author skill

**Context:** The test-author skill owns the test method, and the build pipeline calls it at the pipeline's matrix and test steps, the same way earlier steps call the spec-author and the prover. The method — the level ladder, real-artifact assertions, the red-first proof, the pinned skip-set, and traceability as a standing test — lives in the skill, and the pipeline keeps order and gates.

**User Story:** As a person deriving tests, I want the method held in one skill the pipeline calls, so that how to test lives in one place while the pipeline keeps the order and the gates.

### Acceptance Criteria

**Case: the pipeline calls the method**

1. *when* the pipeline reaches its matrix and test steps, the system *shall* run the test-author skill for the matrix derivation and the test writing, keeping order and gates in the pipeline. [E-27]
2. The system *shall* have the test-author skill hold the level ladder, real-artifact assertions, the red-first proof, the pinned skip-set, and traceability as a standing test. [E-27]

---

## Requirement 9: A test cleans up after itself and is born in a temp home

**Context:** Every test removes what it creates — temp files, fixtures on disk, spawned processes, mutated shared state — and a suite run leaves the machine as it found it. A test's files are born in the system temp home or the host's gitignored state directory and erased at the run's end; a user-visible folder is never a test's workspace, and a headless browser's download directory is pointed at the temp home. A leak is a defect of the test.

**User Story:** As a person whose machine runs the suite, I want each test to erase what it creates and write only into a temp home, so that a run leaves no residue in a folder the person can see.

### Acceptance Criteria

**Case: erase what you create**

1. The system *shall* have every test remove what it creates and *shall* have a suite run leave the machine as it found it, a surviving artifact being a defect of the test. [INV-100]
2. The system *shall* birth a test's files in the system temp home or the gitignored state directory and erase them at the run's end, and *shall* point a headless browser's download directory at the temp home. [INV-100]

**Case: a user-visible folder is never a workspace**

3. The system *shall* never use a user-visible folder — Downloads, Desktop, Documents — as a test's workspace. [INV-100]
4. The system *shall* fail the run on a surviving file through a session-scoped before-and-after diff of the temp home, the harness's own launch sweep clearing a prior run's litter that its own teardown never reached. [INV-100]

---

## Requirement 10: A test's expected value is independent of the code under test

**Context:** A test compares the code's output against an expected value, and that expected value comes from a source other than the code under test. Recomputing the code's own formula and asserting the result is a mirror that can never catch the formula being wrong. Three sources of an expected value are legal, and one boundary keeps property tests in.

**User Story:** As a person trusting a passing test, I want its expected value drawn from an independent source, so that the check proves the behaviour rather than asserting the code equal to itself.

### Acceptance Criteria

**Case: the expected value comes from elsewhere**

1. The system *shall* draw a test's expected value from a source other than the code under test — a hand-computed constant, an independent derivation, or a recorded real output reviewed by a human. [INV-102]
2. The system *shall* refuse an assertion whose expected value is produced by the same formula the code runs. [INV-102]

**Case: the boundary keeps property tests in**

3. The system *shall* allow a round-trip or property test over the outputs, since it asserts an invariant rather than a recomputed value. [INV-102]

---

## Requirement 11: The ladder tops out below the real device

**Context:** Touch physics, scroll snapping, and background throttling live past a desktop headless browser's reach. A behaviour living there gets a real-device walk row, a matrix row the suite can never turn green, owed to the human's own hands before ship, kin of the feel pass. The suite says what it cannot see.

**User Story:** As a person trusting a green suite, I want a behaviour past the headless browser's reach to carry a walk row the suite can never green, so that a passing run claims nothing about a fact only a real device shows.

### Acceptance Criteria

**Case: the boundary is named honestly**

1. *when* a behaviour lives past a desktop headless browser — a momentum swipe on a real phone, a tab throttled in the background — the system *shall* give it a real-device walk row the suite can never turn green, owed to the human's hands before ship. [INV-77, INV-30]
2. The system *shall* let a green run over such a fact claim nothing about it, the suite stating what it cannot see. [INV-77]

---

## Requirement 12: A geometry fact is asserted relative, wide, and long

**Context:** A centering or positioning fact asserts relative geometry, at two or more viewport sizes, and after several consecutive steps of the interaction, so cumulative drift shows. An absolute-pixel assertion at one viewport after one step passes forever while each next step lands further off, and the drift hides from it by construction.

**User Story:** As a person guarding against drift, I want a geometry fact asserted relatively across at least two viewport sizes and after consecutive steps, so that cumulative drift a single absolute check would hide is made to show.

### Acceptance Criteria

**Case: relative, at more than one size, after more than one step**

1. The system *shall* assert a geometry fact as relative geometry — the distance between an element's center and the viewport's center staying within a small bound — at two or more viewport sizes. [INV-78]
   [GAP: the source asserts the center-to-center distance stays within a bound over a run of consecutive steps but names neither the tolerance, the step count, nor who sets them or their defaults, so a test author cannot pin the pass-or-fail boundary of the assertion.]
2. The system *shall* assert it after two or more consecutive interaction steps, so cumulative drift shows, and *shall* refuse an absolute-pixel assertion at one viewport after one step as one that hides the drift by construction. [INV-78]

---

## Requirement 13: An extracted engine tests on its own generic fixtures

**Context:** When a generic engine is carved out of a working project, the donor's data keeps the donor's shape, and a suite running only on it proves the donor rather than the engine. So the engine's suite runs on engine-shaped fixtures, and every donor-specific constant the extraction finds becomes a named content-contract entry with a test that the engine works without it.

**User Story:** As a person carving an engine from an instance, I want its suite run on engine-shaped fixtures and each donor constant named in the content contract, so that the engine is proven independent of its first user.

### Acceptance Criteria

**Case: engine-shaped fixtures**

1. The system *shall* run an extracted engine's suite on engine-shaped fixtures carrying the engine's own ids and content model, letting the donor's data stay as an extra real-data suite and never as the only one. [INV-79]
2. *when* the extraction finds a donor-specific constant — an id format, a hardcoded wordmark, a path — the system *shall* record it as a named entry in the engine's content contract with a test that the engine works without it. [INV-79]

---

## Requirement 14: The suite's own plumbing must not lie

**Context:** Three legs of one class each cover a way the harness could lie about its own verdict. A skip path must execute even when never taken, a shim owes a re-export completeness test, and a background or delegated run's verdict is read from the suite log's own tail line rather than a wrapper's exit code.

**User Story:** As a person reading a suite's verdict, I want the plumbing that reports results held honest, so that a skip that cannot run reds, a missing re-export is caught, and a background run's verdict is read from its own log.

### Acceptance Criteria

**Case: the three plumbing legs**

1. The system *shall* import the skip helper at module load, so a skip path that cannot run reds instead of passing silently on the machine that needed it. [INV-80]
2. The system *shall* require an engine-or-instance shim to carry a re-export completeness test, a missing re-export otherwise keeping a whole suite silently red. [INV-80]
3. *when* a run is a background or delegated one, the system *shall* read its verdict from the suite log's own tail line rather than a wrapper's exit code, a foreground gate reading its own child's exit staying legal. [INV-80]

---

## Requirement 15: A test is green only when it passes deterministically

**Context:** A test is green only when it passes for the same reason on every run. A test that passes on some runs and fails on others is flaky, and one question routes the flake: is the source of the nondeterminism removable in code the project owns. When it is, the flake is a defect fixed at that root, masked by no retry and no raised timeout; when it is not, it is workshop noise on the problem ledger.

**User Story:** As a person trusting a green run, I want a flake rooted in owned code fixed at that root and an external flake routed to the ledger, so that green means deterministic and no mask hides a real race.

### Acceptance Criteria

**Case: the seam question routes the flake**

1. *when* a test's nondeterminism is removable in owned code — a dependence on wall-clock time, on test ordering, on shared or leaked state, on an unseeded random draw, on a timing assumption, or a missing wait on an external tool — the system *shall* fix it at that root so the test passes every run for the same reason. [INV-155]
2. The system *shall* mask a flake with nothing: no retry, no rerun-until-green, no raised timeout that hides the race, and no single pass accepted as a pass. [INV-155]
3. *when* the nondeterminism is not removable in owned code, the system *shall* route it to the problem ledger as workshop noise, a home apart from the owned defect. [INV-155, INV-23]

**Case: the enforcing nets**

4. The system *shall* grep the test configuration for a retry or rerun-until-green plugin and red the run when one appears, leaving the rest to the verify walk's discipline, kin of the fresh-eyes audit. [INV-155, INV-46]
5. *when* a flake's root is understood but not removable in one landing, the system *shall* quarantine it by name in the pinned skip-set with a dated reason and an owning queue row, an open quarantine holding no landing and standing as a debt the milestone audit reads. [INV-155]

---

## Requirement 16: A check that looked at nothing is not a pass

**Context:** A check whose input set is empty reports clean while testing nothing — a uniqueness scan over zero items finds zero collisions, and the green says only that nothing was looked at. An empty input set is nearly always the defect: the parse broke or the source moved. So a check declares the input set it expects to be non-empty, and an empty set reds by name in place of passing silently.

**User Story:** As a person trusting a clean check, I want an empty input set to red by name, so that a broken parse or a moved source cannot pass as a check that examined nothing.

### Acceptance Criteria

**Case: an empty set reds by name**

1. The system *shall* have a check declare the input set it expects to be non-empty and *shall* red by name when that set is empty, the way an unexpected skip is a failure outright. [INV-218]
2. *where* a check may legitimately read an empty set, the system *shall* have that call site name its own reason, the default being that empty is a finding. [INV-218]

---

## Requirement 17: The browser harness launches muted and reaps what it spawned

**Context:** A harness that drives a real browser starts it muted through the browser's own mute flag, so a run makes no sound on the machine it runs on. On teardown it reaps the whole process group it launched; on launch it sweeps any stale process group and temp litter a prior run left, found by its own profile marker, since the system temp is not self-purging. It bounds each command with a real per-command deadline, prefers the dedicated headless build, and runs a launch probe before any suite is trusted.

**User Story:** As a person whose machine runs the suite, I want the harness muted, self-reaping, deadline-bounded, and probed at launch, so that a run leaves the machine as it found it and a faulty browser fails loudly by name rather than bleeding false reds.

### Acceptance Criteria

**Case: muted, reaping, and self-sweeping**

1. *when* the harness launches a browser, the system *shall* pass the browser's own mute flag so the run makes no sound, and *shall* reap the whole process group on teardown so no orphan survives the run. [INV-157, INV-100]
2. *when* the harness launches, the system *shall* sweep any stale process group and temp litter a prior run left, found by the harness's own profile marker, leaving a young ownerless directory alone as a live sibling mid-launch. [INV-157, INV-100]
   [GAP: the sweep reaps an old ownerless profile directory and leaves a young one, but the source names no age boundary between young and old, nor its owner or default, so a test author cannot pin when the sweep reaps an ownerless directory.]

**Case: the bounded deadline**

3. The system *shall* bound each command it sends the browser with a real per-command deadline, so a slow machine waits while a genuine hang fails with a bounded error, and *shall* never inflate a timeout that would bury a real race. [INV-157, INV-155]

**Case: the right binary and the launch probe**

4. The system *shall* prefer `chrome-headless-shell` as the binary, newest install first, falling back to Chrome for Testing then a system Chrome, and *shall* drop the extra headless flag when the shell is the pick. [INV-157]
5. *when* a suite is about to be trusted, the system *shall* run a launch probe — one page served from the loopback address, loaded and then awaited for a single compositor frame, each leg under its own bounded window — and *shall* fail a stalling or frame-dead browser loudly under the probe's own name. [INV-157]

**Case: the nets and the owned-fault boundary**

6. The system *shall* assert in the pack's own suite that the shipped template carries the mute flag, the launch sweep, the process-group reap, and the bounded deadline, and *shall* assert by deed in a consuming product's suite through a post-run process-group check that reds on a surviving orphan. [INV-157, INV-150]
7. *when* a script both launches a real headless Chrome and carries the mute flag nowhere in its comment-stripped code, the system *shall* red the run through a guardrail that reads every tracked script whole, catching a hand-rolled harness's unmuted launch across the existing tree the same run the gate is added. [INV-157]
8. *when* a harness fault is caused by its own run hygiene, the system *shall* root-fix it here and *shall* route only a fault with nothing to correct in owned code to the problem ledger. [INV-157, INV-23]

---

## Requirement 18: The browser harness has one canonical home

**Context:** The harness that drives a real browser is one artifact, shipped once by the pack as a template rather than copied into each project. A consumer adopts it by updating the pack, layering its own project-specific driving methods on the shared core, so a fix to the core lands once and reaches every consumer.

**User Story:** As a person maintaining the harness, I want its core shipped once and adopted by an update, so that a hardening lands in one place and no divergent private copy can drift.

### Acceptance Criteria

**Case: one home, adopted by update**

1. The system *shall* ship the harness core once as a pack template and *shall* have a consumer adopt it by updating the pack through the catch-up walk, layering its own driving methods on the shared core. [INV-158, INV-110]
2. The system *shall* land a fix to the core — the launch flags, the teardown, the deadline — once and reach every consumer through the update, the migration path a package update carries. [INV-158, INV-91]

**Case: a fork owns its divergence**

3. *when* a project forks a private copy of the harness, the system *shall* have that project own the divergence it creates, the third mute-launch net still catching a forked unmuted launch in any tracked tree, this being the centralize pole of the pack-to-host split. [INV-158, INV-157, INV-163]

---

## Requirement 19: The suite-honesty invariants are one class, each naming its net

**Context:** The test-infrastructure family shares one role: each member closes a way the suite could pass green while the fact it claims is false, or leaves the machine worse than it found it. The class carries one parity — each member names its net past merely naming the fix. For most members the net is a mechanical check; one member's net is the real-device walk row the suite can never green.

**User Story:** As a person relying on the suite-honesty class, I want every member to name the net that reds a run on its violation, so that a member naming no net is caught as a class defect.

### Acceptance Criteria

**Case: every member names its net**

1. The system *shall* have each suite-honesty member name the net that reds a run on a regression, the assertion shape itself being the net for the real-device walk row, the relative-wide-long geometry, and the engine-shaped fixtures. [INV-160]
2. *when* a member names no such net, the system *shall* read it as a class defect the prover blocks, the same standing an under-enumerated review-record member has. [INV-160, INV-125, INV-156]

**Case: the class binds forward**

3. *when* a new suite-honesty invariant is stated, the system *shall* have it state its net against this parity and *shall* leave members declared before the class unreshaped. [INV-160, INV-157, INV-158]

---

## Requirement 20: A cleanup touches only what it owns

**Context:** A cleanup — a teardown, a stray-process sweep, a temp purge — acts only on what this run provably created and owns, or a prior run of the same harness whose recorded owner is provably dead, and never on a shared resource another party is using. The guard denies every ending that names a name, because a name cannot tell this run's copy of a program from the person's own copy.

**User Story:** As a person sharing a machine with the pack, I want a cleanup scoped to what the run provably owns and every name-based kill refused, so that the person's own program is never reaped.

### Acceptance Criteria

**Case: the test is current use and provable ownership**

1. *when* a cleanup would touch a shared resource — a process, a temp directory, a port, a file, a lock, the display — the system *shall* act only on what this run provably owns or a prior run whose recorded owner is provably dead, and *shall* leave a resource in current use untouched. [INV-162, INV-157]
2. The system *shall* target a kill by a recorded process identifier, a process group the run holds, or an install path under the run's own tree, and *shall* read the recorded process group as the sole safe target on a machine shared with other sessions. [INV-162]

**Case: the guard refuses a name**

3. The system *shall* refuse a command that ends a process by a bare name — a name pattern, or a lookup that resolves a name to an identifier — since it reaches whatever on the machine answers to that name. [INV-162]
4. The system *shall* hold this class over every process the pack runs a copy of — the browser, the language runtime and its separation tool, the bundler, the media tool — and *shall* leave a program the pack never launches beside the point. [INV-162]

**Case: the nets and the notice**

5. *when* a tracked script ends a process by name with no identifier, process-group, or owned-path proof, the system *shall* red it through a guardrail carrying a committed probe corpus, so a later widening cannot silently narrow the check. [INV-162]
6. *when* the pack ends any process, the system *shall* announce what it ended and why the run owned it, so an ending nobody expected is visible the moment it happens. [INV-162, INV-204]

---

## Requirement 21: The architecture document names the nodes that own the spec's facts

**Context:** The spec says what the product is, and tests prove facts about the shipped artifact; two documents sit between them, and if they stay implicit they get skipped. The architecture document describes how the product is built as a list of named nodes — pipeline stages, modules, surface owners. Each node carries one responsibility and one name, every spec fact belongs to exactly one node, and every pin comes from a command that was run. It is written from the proven spec and proved with the architecture lens before anything derives from it.

**User Story:** As a person bridging the spec to the tests, I want the architecture written as named nodes each owning its facts and pinned from a real command, so that the layer between spec and tests is explicit rather than skipped.

### Acceptance Criteria

**Case: named nodes, one fact one owner**

1. The system *shall* have each architecture node carry one responsibility and one name, and *shall* have every spec fact belong to exactly one node. [E-14]
2. The system *shall* pin every node to its owning place by the named thing — a function, a marker comment, a selector, a heading — resolving the name and re-grepping it in a drift check rather than trusting the cached line number, and *shall* draw every pin from a command that was run rather than the doc's own prose. [E-14]

**Case: the architecture lens proves it**

3. *when* the architecture is written, the system *shall* prove it with the architecture lens at the project's kind scale, checking that every spec fact has an owning node, that no node stands without spec backing, and that every seam between nodes is named. [E-14]
4. The system *shall* have the lens check that the quality budgets are stated with their instrumentation homes and watchers, that the runtime view walks every promised flow, and that the placement view says where every node runs. [E-14, INV-41, INV-74, INV-75]

**Case: keeping the doc current**

5. *when* a surface-class wish lands, the system *shall* update the doc before the matrix is touched, a bug or small wish citing the node it lands in, and a fact with no owner being assigned to the nearest fitting node with no re-prove triggered by the assignment alone. [E-14]
6. *when* the structure is re-carved, the system *shall* carry the re-carve as its own row under a restructure placement and re-prove it, the doc mapping the product as it stands plus the landing in flight and never a speculative node built milestones ahead. [E-14, INV-37, INV-18]

---

## Requirement 22: Every new or carved node passes a three-question fitness test

**Context:** Before an extraction or a new node stands, it answers three questions: can it be tested alone, does a real second place need it, and can it and its neighbour be worked in parallel without queuing on shared files. Three yes answers make the node right; a single no is a flag to answer before the carve stands; two or more no make it premature. The prover's speculative-node flag is this flag raised on the second question.

**User Story:** As a person growing the architecture, I want each new node to answer three fitness questions at its birth, so that the architecture only grows a part that earns its place.

### Acceptance Criteria

**Case: three questions at birth**

1. *when* a node is born or carved, the system *shall* have it answer whether it can be tested alone, whether a real second place needs it, and whether it and its neighbour can be worked in parallel without queuing on shared files. [INV-122]
2. *if* one answer is no, *then* the system *shall* raise a flag to answer before the carve stands — naming the plan that turns it to a yes or folding the carve back — and *if* two or more answers are no *then* the system *shall* read the node as premature. [INV-122]

**Case: the prover shares the flag**

3. The system *shall* have the prover flag a node with one caller and no promised second on the second question, never auto-rejecting it, so the birth gate and the prover agree. [INV-122]

---

## Requirement 23: A deliberate redesign re-shapes the architecture document

**Context:** When structure is deliberately redesigned — layers restacked, a surface's ownership moved, nodes merged or split — the architecture document is re-shaped to the new form and re-proven in the same movement. Updating the pins alone is scoped to a boundary shift that leaves the document's shape standing; after a real redesign the old shape itself lies.

**User Story:** As a person redesigning structure, I want the document re-shaped and re-proven in the same movement, so that fresh pins never sit on a stale shape.

### Acceptance Criteria

**Case: re-shape, do not just re-pin**

1. *when* structure is deliberately redesigned, the system *shall* re-shape the architecture document to the new form and re-prove it with the architecture lens in the same movement. [INV-113]
2. The system *shall* scope the pins-only path to a boundary shift that leaves the document's shape standing, treating fresh pins on a stale shape after a redesign as a defect, the re-carve routing carrying such a redesign as its own row. [INV-113, INV-37]

---

## Requirement 24: The architecture owes numbers, not just names

**Context:** The document states measurable quality budgets for what it builds, each with its instrumentation home — where the number is measured and where a human reads it — and each budget names its watcher, the mechanical check that reds past the stated number. What is measurable depends on the project's kind, so the author asks what quality means here in numbers before writing any. The numbers are the host's taste, proposed by the architecture and set on the human's word.

**User Story:** As a person guarding quality, I want each budget stated with its instrumentation home and a watcher, so that a budget cannot silently rot and a quality with no honest number is said by name rather than faked.

### Acceptance Criteria

**Case: a budget, its home, and its watcher**

1. The system *shall* state each measurable quality budget with its instrumentation home and *shall* have each budget name its watcher, the mechanical check that reds past the stated number, or a decided sentence naming why it is read by eye. [INV-41, INV-59]
2. *when* a budget carries neither a named watcher nor that decided sentence, the system *shall* read it as a derivation defect, flagged like an unowned fact, the watcher holding it the way the suite wall-time budget was held once it earned its gate. [INV-41, INV-164]

**Case: what is measurable follows the kind**

3. *when* the architecture writes a budget, the system *shall* read the measurable dimensions from the project's kind — paint and interaction times for a user-facing product, latency and throughput and error rate for a backend service, run time and per-unit cost for a pipeline, eval pass rate and suite wall-time for a skill pack, and an honest number for prose — the kinds being a closed set each named in the clause. [INV-41, INV-36, INV-226]
4. *where* a quality has no honest number, the system *shall* say so by name rather than invent a vanity metric, and *shall* count a budget only once a matrix row at the right level can see it. [INV-41]

**Case: the numbers are the host's taste**

5. The system *shall* have the architecture propose the numbers with a recommendation and *shall* set them on the human's word at the surface's first budget landing, the duty binding forward from that landing. [INV-41, INV-159]

---

## Requirement 25: The architecture walks each flow at runtime

**Context:** The spec's person-facing scenarios are flows. The feature-coverage table names which nodes implement a feature; the runtime view shows how. For every flow the spec promises, the document walks the running product — which node serves each step, what data crosses at each hop, where the flow can fail, and what happens then. Every named failure point carries its fallback.

**User Story:** As a person tracing a promised flow, I want the architecture to walk it hop by hop with a fallback at each failure point, so that a flow it cannot walk end to end surfaces as a finding.

### Acceptance Criteria

**Case: one walk per flow**

1. *when* the spec promises a flow, the system *shall* walk the running product for it — which node serves each step, what data crosses at each hop, and where the flow can fail — in one short walk per flow, a table row or numbered line per hop. [INV-74, E-29]
2. The system *shall* have every named failure point carry its fallback — a degrade, a retry, a guard — so that a failure point with no fallback sentence reads as an unfinished walk. [INV-74]

**Case: a flow that cannot be walked is a finding**

3. *when* the document cannot walk a flow end to end, the system *shall* read it as a finding — a missing node or an unnamed seam — the view scaling by kind so a book's one sentence per flow satisfies the duty. [INV-74, INV-36, INV-159]

---

## Requirement 26: The architecture says where everything runs

**Context:** Every node states its place — build-time on the author's machine, a static file on a content-delivery host, the client browser, an edge worker, an external service. Where a load-bearing technology choice exists, the place names it, and the same table says where secrets live and which tier holds each verdict that must not be decided on the client. The document reads tiers-first, opening with the shape at a glance.

**User Story:** As a person asking where a node runs, I want every node's place first-class and the document opening tiers-first, so that a reader answers where-does-this-run at a glance and a secret's tier is architecture rather than a footnote.

### Acceptance Criteria

**Case: every node states its place**

1. The system *shall* have every node state its place and name the load-bearing technology choice where one exists, and *shall* say in the same table where secrets live and which tier holds each verdict that must not be decided on the client. [INV-75]
2. The system *shall* make the placement first-class — a column in the node table or its own small table — so a reader answers where a node runs at a glance. [INV-75]

**Case: tiers-first reading, scaled by kind**

3. The system *shall* open the document with the tiers named in a few lines, then the nodes, then the flows walking those tiers, then budgets, so a reader lands oriented before any table detail. [INV-75]
4. The system *shall* scale both views by the project's kind — a book satisfying each with one sentence, a fullstack or data project owing both in full — the duty binding forward from the first landing that touches the architecture. [INV-75, INV-36, INV-159]

---

## Requirement 27: The matrix is derived, and no wish jumps the bridge

**Context:** The matrix organizes rows by architecture node and spec fact, a structured grid where every fact gets at least one row and every row pins a test level. Derivation closes with the coverage validation, a checklist walked to confirm the rows are complete. While both layers live, no wish lands whose facts lack an owning node and a matrix row at the right level.

**User Story:** As a person crossing from spec to tests, I want the matrix derived and the coverage validation walked, so that no fact ships without a row at the right level and no wish jumps the bridge.

### Acceptance Criteria

**Case: the matrix is derived by node and fact**

1. The system *shall* organize the matrix by architecture node paired with spec fact, giving every fact at least one row and pinning each row to a test level. [E-5, E-14]
2. The system *shall* close the derivation with the coverage validation, confirming every spec anchor owns at least one row, every artifact-inventory entry owns at least one rendered-level row, every visibility or layout or colour or interaction fact sits at browser-computed level or above, and every node carries its negative-side rows. [E-15, INV-6]
3. The system *shall* retire a stale row that cites an anchor or node no longer present rather than let it vanish, and *shall* read a fact with no row, or a row at too weak a level, as a derivation defect the prover catches before any user hits it. [E-15]

**Case: no wish jumps the bridge**

4. The system *shall* land no wish whose facts lack an owning architecture node and a matrix row at the right level, and *shall* have a project predating these layers bring them up as an owned landing, the invariant binding from the landing that creates the architecture document and matrix. [E-14, INV-159]

---

## Requirement 28: Every movement ends at a safe breakpoint

**Context:** Every movement ends the same way: the resume file's live state is replaced rather than stacked, a dated journal entry is added, and the work is committed. Session memory can then be wiped with no loss, and the journal entry is the durable net where the resume file is gitignored. At a breakpoint the agent compacts its own context and says so, and on the way back it re-checks skill freshness.

**User Story:** As a person handing off a session, I want every movement to end with the resume state replaced, a journal entry added, and a commit, so that memory can be wiped with zero loss.

### Acceptance Criteria

**Case: the movement-end routine**

1. *when* a movement ends, the system *shall* replace the resume file's live state rather than stack it, add a dated journal entry, and commit, so session memory can be wiped with no loss. [M-2]
2. The system *shall* treat the journal entry as the durable net, since the resume file may be gitignored, and *shall* leave a full wipe or clear as the human's move. [M-2]

**Case: compaction and the way back**

3. *when* a breakpoint is reached, the system *shall* compact its own context and say so rather than silently, and *shall* re-check skill freshness on the way back. [M-2, A-7]

---

## Requirement 29: A landing closes the checkpoints it shipped

**Context:** A landing that ships a checkpoint's items flips that checkpoint to its closed state in the same landing. The movement that writes the work into git history also marks the checkpoint done, so a returning session never reopens finished work. The closing sweep rides beside the resume-file replacement.

**User Story:** As a returning session, I want a checkpoint whose items shipped flipped closed in the same landing, so that finished work is never reopened.

### Acceptance Criteria

**Case: the closing sweep**

1. *when* a landing ships a checkpoint's items, the system *shall* flip that checkpoint to its closed state in the same landing, the closing sweep riding beside the resume-file replacement. [INV-107]
2. The system *shall* read a checkpoint whose items all live in git history as stale by definition, and *shall* fail the landing on a checkpoint left reading as not started after its items shipped. [INV-107]

---

## Requirement 30: The resume file is a digest under a hard cap

**Context:** The resume file is read in one minute at a cold start, so growth is a design failure. The whole file holds at most 100 lines, and a suite check owns the number, going red on a bloated file proven with a synthetic one. The cap and the restate-every-open-leg law are reconciled by form: an open leg is restated as one terse line, and its detail flows to its home.

**User Story:** As a returning session, I want the resume file capped and each open leg stated in one terse line, so that a cold start reads a short current picture rather than a bloated log.

### Acceptance Criteria

**Case: the hard cap and its check**

1. The system *shall* hold the whole resume file at 100 lines or fewer and *shall* have a suite check own the number, reddening on a bloated file proven with a synthetic one. [INV-48]
2. The system *shall* restate an open leg as one terse line — its name, what stays open, and where the detail lives — and *shall* move the detail to the journal, the queue row, or the record the line points at. [INV-48, INV-26]
3. The system *shall* have compaction move prose to its home and *shall* never let it drop an open leg. [INV-48, INV-26]

---

## Requirement 31: A background worker outlives a memory wipe

**Context:** A worker spawned in a session keeps running and keeps writing the shared tree after the chat's memory is cleared. The operating system's process list and the harness task record show nothing for it, so neither is proof of death; liveness is proven by deed. The handoff note records the worker's id, the files its brief lets it write, and three checks a resuming session runs before touching those files.

**User Story:** As a resuming session, I want a background worker proven dead or alive by three checks before I touch its files, so that a live writer is reconnected and a dead one's files are freed with nothing scrambled.

### Acceptance Criteria

**Case: the handoff note records three things**

1. The system *shall* have the handoff note record the worker's recorded id pointing at its checkpoint file, the exact files its brief lets it write, and the three liveness checks. [INV-76, ACT-3]
2. The system *shall* run the three checks before touching the write-set: watching the write-set's file times over a short window, reading the worker's heartbeat on its checkpoint file, and sending one message to the recorded id. [INV-76]

**Case: the verdict**

3. *when* any one check shows life, the system *shall* reconnect and treat the worker's files as claimed, and *shall* declare a dead verdict only when all three are quiet together — a still write-set, a stale heartbeat, and an unanswered probe — in one written line. [INV-76]
4. *while* no dead verdict stands, the system *shall* never frame the worker's output as finished and *shall* spawn no second worker onto the shared tree until the first is halted by its own reply or declared dead by all three checks. [INV-76, INV-11]
5. The system *shall* have a dead verdict free only the files the worker owned, reading whether the work is done from the worker's checkpoint finished marker or the verify walk. [INV-76]

---

## Requirement 32: Human-facing prose is drafted by a clean writer

**Context:** Any text a human will read is drafted by a fresh writer session that does not have the package rules loaded — documentation pages, product-spec prose, reports, decision pages, product copy, and the package's own rule texts while being edited. The rules-loaded session writes a plain brief carrying the facts, the reader, and the register laws; the writer returns the draft; the rules-loaded session reviews and lands it. A blanket rewrite of settled text is refused.

**User Story:** As a person reading the pack's durable prose, I want it drafted by a fresh writer from a plain brief, so that human-facing writing stays clear of the insider register and settled text stays stable.

### Acceptance Criteria

**Case: the clean-writer road**

1. *when* durable human-facing prose is written or a section of it is edited, the system *shall* have a fresh writer session draft it from a plain brief carrying the facts, the intended reader, and the register laws, then review and land it in the rules-loaded session. [INV-84]
2. The system *shall* bind the road to the section the edit touches and *shall* redraft a whole page only on the human's word. [INV-84]

**Case: what rides the ordinary hand**

3. The system *shall* let a report typed live in chat stay the session's own words under the register laws, and *shall* let a mechanical correction — a typo, a broken link, a version number — ride the ordinary hand as no drafting. [INV-84]
4. The system *shall* refuse a blanket rewrite of settled text, since meaning can shift during a bulk restructure. [INV-84]

---

## Requirement 33: The milestone gate re-proves and audits the whole

**Context:** A milestone runs the full gate over the accumulated landings before they are called a release. It re-proves the spec and the architecture, runs the design review, walks the matrix and surface-composition audits, re-runs the skill evals and the skill-creator craft review, compacts the documents and the code, and closes with a sweep of open gates, deferred rows, the formal index, the derived headers, and the thin loader.

**User Story:** As a person cutting a release, I want the milestone gate to re-prove and audit the whole as one pass, so that an accumulation of small landings is re-checked before it ships.

### Acceptance Criteria

**Case: the two re-proves and the design review**

1. *when* a milestone is reached, the system *shall* re-prove the spec in full and re-prove the architecture beside it, the prover reading the architecture the way it reads the spec and recording the architecture pass in `docs/prover/` beside the spec's. [M-1, INV-116]
2. The system *shall* run the design review on the re-proven spec in full — the whole element inventory, every proposed same-kind grouping, behaviour parity within each, and its likely divergences echoed as three asks or fewer — folding its outcome into a dated design-review record, a confirmed grouping re-entering the prove step under the round cap and typically resting at the gate by waiting for the human's answer. [M-1, INV-141, INV-154]

**Case: the audits and the eval runs**

3. The system *shall* re-walk the coverage validation against the current spec and architecture, run the surface-composition check, and re-run the skill evals. [M-1, E-15, E-19]
4. The system *shall* walk the pack's skills through the skill-creator to review each skill file's craft, folding or rejecting each finding with a written reason in a dated record, a newly joining skill walking this at birth before it reaches the gate. [M-1]

**Case: the compaction stations**

5. The system *shall* audit every living document — spec, matrix, queue, skills, ledger, and the test suite — for redundant information and compact it, a fact living once in one home with a pointer from everywhere else, removing only the redundancy and keeping anything whose removal would change the meaning, and accounting for each removal that takes substance. [M-1, INV-115, E-24, INV-109]
6. The system *shall* widen the station to code — merging duplicate logic, removing dead weight with its listing, and extracting a ripened abstraction only through the three-question fitness gate — the second occurrence of one problem opening its own compaction row that lands through the ordinary pipeline at one row's delta per commit without blocking its lane. [M-1, INV-123, INV-122, INV-39, INV-56]
7. The system *shall* restructure a document only for a faster reading shape and only through the content-preserving layout vehicle with its multiset proof, and *shall* archive a closed queue row rather than delete it. [M-1, INV-111, INV-1]

**Case: the closing sweep**

8. The system *shall* re-list every open human gate and every unharvested inbox file one line each, sweep the deferred rows' revisit triggers once more and send any fired row back to runnable, and re-check the formal index against the prose as a derived map. [M-1, INV-1]
9. The system *shall* re-pin the derived docs' headers to the spec version and prove them, and *shall* re-read the thin loader line by line, keeping only a line that must hold before any pack file loads and migrating any other to its real home. [M-1, E-16]

---

## Requirement 34: A periodic full audit catches the drift no lint names

**Context:** Two layers guard the living documents against rot. The continuous lints run on every push and hold each known drift class the moment it reappears. Beside them, a full audit runs on a landing-count cadence — every ten landings since the last full audit — running the milestone gate's whole-read even where no milestone falls due, so an unknown drift class caught between milestones is found by a fresh whole-read. The whole-read takes the adversarial stance the verify audit defines.

**User Story:** As a person guarding against slow rot, I want a full adversarial audit on a landing cadence, so that a drift class no lint yet names is caught before a human reads it late.

### Acceptance Criteria

**Case: the cadence and its whole-read**

1. *when* ten landings have passed since the last full audit, the system *shall* run the milestone gate's whole-read — the full spec and architecture re-prove, the design review, and the doc-compaction sweep — even where no milestone falls due, the count being a host-settable default. [INV-145, INV-70, INV-116, INV-141, INV-115]
2. The system *shall* read the count from the landing history and *shall* reset the counter at a milestone gate, since the gate already runs the whole-read. [INV-145, INV-107]

**Case: the adversarial stance**

3. The system *shall* take the audit's whole-read as a read set on breaking the work, refuting its claims and finding its holes, the same stance as the verify audit. [INV-145, INV-46]

---

## Requirement 35: Compaction is continuous, a gate on every push

**Context:** The doc- and code-compaction stations run at every push, above the milestone that once held them alone. Every push is held to the reached-clean floor by a mechanical gate, so no bloat accumulates between milestones. The deeper rule this carries reaches every project: any quality a machine can verify is wired as a blocking gate, since a quality left to attention is a defect of the method.

**User Story:** As a person guarding against bloat, I want the clean floor held by a gate on every push, so that no bloat accumulates between the milestone whole-reads and no verifiable quality rests on attention.

### Acceptance Criteria

**Case: the reached-clean floor at every push**

1. *when* a push runs, the system *shall* hold it to the reached-clean floor: the register lint at zero errors, the redundancy gate at zero open pairs, and the debt cap ratcheting down only, each asserted against the live document. [INV-164, INV-83, INV-98]
2. The system *shall* run the milestone whole-read above the gate as the deep periodic audit, so the two stations layer rather than duplicate. [INV-164]

**Case: a machine-verifiable quality is a gate**

3. The system *shall* wire any quality a machine can verify as a blocking gate held by no pass's attention, since a quality left to attention is a defect of the method. [INV-164]

---

## Requirement 36: The style lint has two tiers

**Context:** The style gate's rules divide by whom they bind. The universal tier states the plainness and normative-informative separation every live-spec document holds, so it binds every host's gate. The pack-register tier is the pack's own reference-documentation taste, right for the pack's docs and available to a host for its own. The lint names the tiers in one flag.

**User Story:** As a host adopting the gate, I want the universal language laws as my floor and the pack-register taste optional, so that I adopt the plainness laws while keeping an intentional voice.

### Acceptance Criteria

**Case: the two tiers**

1. The system *shall* bind the universal tier — the contrast-frame ban (it bars naming a thing by denying its neighbour, the "X, not Y" frame), the negation-opener rule, the machine-jargon rule, and the provenance-narrative rule — to every host's gate whatever its register, running the provenance-narrative rule as a hard error in every tier. [INV-166]
2. The system *shall* keep the pack-register tier — the caps-shout, second-person, reassurance, and future-narration rules — as the pack's own taste, right for the pack's docs and available to a host on its word. [INV-166]

**Case: the tiers named in one flag**

3. The system *shall* run the universal tier as the gate and leave the register tier advisory under one flag, and run the union under the other, declaring the split in `docs/spec-style.md` rather than inferring it, this being the pack-to-host split applied to language. [INV-166, INV-173, INV-163]

---

## Requirement 37: Enumerable facts earn bullet structure

**Context:** A prose paragraph that carries an enumeration of three or more distinct, parallel facts earns bullet or numbered structure, so a reader scans the members instead of parsing them out of a run-on sentence. Prose stays for the laws, their reasoning, and their boundaries. The rule earns no mechanical lint of its own, since a regex flagging every three-comma sentence would trip on a rhetorical triad; telling a list-owed enumeration from a triad is a meaning call the register judge and the prover make.

**User Story:** As a reader meeting a packed paragraph, I want three or more parallel facts rendered as a list, so that I scan the members rather than parse them out of a run-on sentence.

### Acceptance Criteria

**Case: the threshold and its home**

1. *when* a paragraph carries three or more distinct, parallel facts, the system *shall* render the enumeration as a bulleted or numbered list, keeping prose for the laws, their reasoning, and their boundaries. [INV-215]
2. The system *shall* leave the rule read by eye and by the prover's cognitive-load lens, earning no mechanical lint of its own, the register judge and the prover making the meaning call a regex cannot. [INV-215, INV-203]

---

## Requirement 38: Grading the size of a change is the reader's act

**Context:** A text states what changed and what follows from it; the size of a change is given as content or a number, and grading that size — its importance or drama, up or down — belongs to the reader. Over-dramatization to the plus and to the minus are one bias, so the law covers both poles at once. It binds every text — chat, docs, worker reports, and agent-to-agent messages.

**User Story:** As a person reading the pack's texts, I want the size of a change left for me to judge on every surface, so that a change is described plainly rather than oversold either way.

### Acceptance Criteria

**Case: both poles, every surface**

1. The system *shall* state what changed and what follows, giving the size as content or a number, and *shall* leave grading that size — to the plus or to the minus — to the reader. [INV-221]
2. The system *shall* bind this law across every text — chat, docs, worker reports, and agent-to-agent messages — and *shall* describe a correction as a correction. [INV-221, INV-183]

**Case: the nets it rests on**

3. The system *shall* have the register judge read this class on the chat and document surfaces, running the regex pattern files — the universal list plus any host's own overlay — as the cheap first pass ahead of the model judge, and *shall* carry the law in the worker brief for the surface the judge does not read, since chat and inter-agent text are emitted before any gate reads them. [INV-221, INV-203, INV-173, INV-220]

---

## Requirement 39: Documents are versioned, and each version has one home

**Context:** The queue and the spec carry dated versions the way code does, so a reader can tell which roadmap version a decision was made under. Each version fact has one named home: the repository's `VERSION` file, a skill's `SKILL.md` frontmatter line, and a host's installed-set record. The freshness check compares version against version rather than bare file times.

**User Story:** As a reader tracking versions, I want documents versioned and each version fact homed in one place, so that the freshness check compares exact version strings and every reader knows where the current version lives.

### Acceptance Criteria

**Case: documents carry versions**

1. The system *shall* carry a dated version on the queue and the spec the way code does, so a reader can tell which roadmap version a decision was made under. [M-3]

**Case: version has named homes**

2. The system *shall* keep each version fact in one named home — the repository's `VERSION` file, each skill's `SKILL.md` frontmatter line, and a host's installed-set record written at attach and every update. [M-7]
3. The system *shall* have the freshness check compare version against version as exact strings rather than bare file times. [M-7, A-7]

---

## Requirement 40: Time is read off the clock, never invented

**Context:** Every date a session writes — a file name, a journal or queue stamp, a ledger occurrence — comes from the machine's clock at write time, and git is the arbiter in doubt. The rule takes four forms, two mechanical and two about the chat surface.

**User Story:** As a person reading the records, I want every date read off the clock at write time, so that no record carries an invented or extrapolated date.

### Acceptance Criteria

**Case: the two mechanical fences**

1. *when* a repo file name, journal heading, or ledger date is written, the system *shall* keep it no later than the current clock, turning a future-dated stamp red as a real defect while a prose quote of a past incident's date stays legal. [INV-24]
2. *when* a commit adds a line pairing today's date with a clock time later than the commit moment, the system *shall* red it, reading the adjacent stamp shape against the commit clock so a legally quoted time stays green. [INV-24]

**Case: the chat surface**

3. The system *shall* read a human-facing timestamp off the clock at write time rather than continue it from an earlier stamp, this law living in the communicator skill. [INV-24]
4. The system *shall* inject the wall clock into every prompt's context through the harness hook where it is installed, the law above standing alone where the hook is not. [INV-24]

---

## Requirement 41: The push checks may be mirrored in a remote gate

**Context:** The guardrails' native home is the local pre-push hook. A host may also mirror the same checks in its continuous-integration runner as a second net. There is one source of truth: the runner runs the same scripts and never redefines them, and the second net runs the full set rather than the local reach map's scoped subset.

**User Story:** As a host wanting a second net, I want the remote gate to run the same scripts as the local hook, so that the gates are re-run on another machine with one source of truth.

### Acceptance Criteria

**Case: one source of truth, the full set**

1. *when* a host mirrors the checks, the system *shall* run the same scripts in the remote gate and *shall* never redefine them, the local reach map staying a latency optimization and never a shortcut for the remote gate. [M-5]
2. The system *shall* have the remote gate run the full check set as the second net. [M-5]

---

## Requirement 42: Accepted work reaches the project's remote

**Context:** Where the host has a remote, work is pushed by rule rather than parked locally waiting for perfect. Same or better means the work matches or improves on the tree before the change; the gates its diff reached hold that reading, each one green and none showing a regression against that prior tree. The remote is discovered from the tree first. The rule runs inside the human's standing push grant, stands down while another session is live in the repo, and re-walks the shopfront on every push.

**User Story:** As a person shipping accepted work, I want green work pushed by rule under the standing grant, so that sound work reaches the remote rather than sitting local and a named milestone still waits for the human's word.

### Acceptance Criteria

**Case: push by rule under the grant**

1. *when* work matches or improves on the tree before the change, and every gate its diff reached passes green with no regression against that prior tree, the system *shall* push it to the host's remote by rule under the human's standing push grant rather than park it locally. [INV-82, INV-70, INV-9]
2. The system *shall* discover the remote from the tree first rather than ask what `git remote -v` answers, and *shall* ask one contextual question at the first push moment only where the host has no remote or the profile records no push grant. [INV-82]

**Case: coordination and the shopfront**

3. *while* another session is known live in the repo, the system *shall* stand the by-rule push down and return push coordination to the human, the accepted work waiting local until the repo is single-session again. [INV-82, INV-11]
4. *when* a push reaches the remote, the system *shall* re-walk the README against the pushed truth and *shall* still wait for the human's word on a milestone gate he named in person. [INV-82, INV-44]

---

## Requirement 43: The push walk reads the remote gate's verdict

**Context:** A push does not end at the push. Where the host mirrors its checks in a remote gate, the push step reads the remote gate's own verdict — the run the push triggered — with one command in minutes and no human wait. A red verdict is the pushing session's own immediate bug.

**User Story:** As a person who just pushed, I want the session to read the remote gate's verdict and fix a red the same session, so that the human never meets a failed run first in a mailbox.

### Acceptance Criteria

**Case: the verdict is read**

1. *when* a push triggers a remote gate, the system *shall* read the gate's verdict with one `gh run` in minutes, watching a slow gate to its verdict on the detached-work cadence. [INV-106, INV-35]
2. *when* the remote verdict is red, the system *shall* treat it as the session's own immediate bug, preempting by the bug lane, fixing it the same session, and re-pushing before anything else, so the human never learns of the red from a mailbox. [INV-106, INV-2]

---

## Requirement 44: The push gate for the flagship runs a fresh re-check

**Context:** The pack's own repository is public and the method's flagship, so every push is preceded in the same session by the concurrent-edit fence and a fresh prover re-check over the spec and the architecture, its record landing before the push. One carve-out is scoped by the diff.

**User Story:** As a maintainer pushing the flagship, I want the fence and a fresh prover record before every push, so that nothing reaches the remote until its claims are re-verified.

### Acceptance Criteria

**Case: the two preceding steps**

1. *when* a push runs on the flagship repository, the system *shall* run the concurrent-edit fence and a fresh prover pass over the spec and the architecture, landing the record in `docs/prover/` before the push, a record predating the last architecture change being as stale as one predating the last spec change. [M-6, INV-11, INV-116]
2. The system *shall* fold defect findings before pushing, a fold produced by the gate's own pass shipping with the same record and a fold reaching wider re-triggering the gate, the rest becoming queue rows. [M-6]

**Case: the inbox-only carve-out**

3. *when* a push's diff is exactly one new file under `inbox/`, the system *shall* owe the fence and no re-check record, a diff carrying anything more riding the full gate. [M-6, INV-112]
4. The system *shall* name the record `YYYY-MM-DD[-suffix].md` with the suffix mandatory when the date's file exists, and *shall* treat no re-check record for the pushed state as a push that should not have happened. [M-6]

---

## Requirement 45: Process bookkeeping scales to the delta

**Context:** A tiny row pays the same fixed bookkeeping as a whole surface — its claim commit, its full-page re-check record, its journal chapter, and a resume rewrite — running a large share of its wall time. The re-check keeps its rigor always but scales its form, and the irreducible core stays fixed regardless of scale.

**User Story:** As a person landing a small change, I want the bookkeeping's form scaled to the delta while its rigor holds, so that a tiny row runs short without sacrificing the safety core.

### Acceptance Criteria

**Case: the re-check scales its form**

1. *when* a delta is a skill, prose, or infra kind with no new surface and no structure change, the system *shall* ship a short-form re-check record of three lines — previous records clean, the delta in one line, and the verdict. [INV-61, INV-45]
2. *when* a delta is surface-sized or structural, the system *shall* keep the full re-check walk. [INV-61]

**Case: the irreducible core**

3. The system *shall* batch claims per declared lane in one commit and take the journal chapter and resume rewrite once per landing batch rather than per tiny row. [INV-61]
4. The system *shall* keep the irreducible core fixed regardless of scale — the law's own text written well, the red-first test, the delta's cross-link prove, and the gates. [INV-61]

---

## Requirement 46: A publish owes the reader what the artifact's kind owes

**Context:** Sooner or later a piece of work leaves the machine — a repo goes public, a skill enters a plugin directory, a release is cut, rendered cards go to a design project. The work-kind axis used at wish intake applies again at the door of publishing, and each kind owes its reader a different minimum.

**User Story:** As a person publishing an artifact, I want its kind to set the minimum it owes its reader, so that a skill shows its commands, a tool shows real runs, a visual product shows fresh screenshots, and prose shows its reading path.

### Acceptance Criteria

**Case: each kind owes its minimum**

1. *when* a piece of work is published, the system *shall* apply the work-kind axis at the door of publishing and owe the reader the minimum that kind owes. [T-16]
2. The system *shall* have a skill show how to install it, the commands to run, and when to use it and when not; a tool show real runs with real output; a visual product show fresh screenshots; and prose show its reading path. [T-16]

**Case: a comparison earns its place**

3. The system *shall* let a comparison or a diagram join only when it carries the argument, never as decoration. [T-16]

---

## Requirement 47: The publish skill owns the checklist, run before the gate

**Context:** The publish skill owns the per-kind checklist, and this spec sets the contract it follows. Nothing is deposited outward without passing the checklist first, and its result rides the landing report. The checklist never bypasses the gates already standing — the human's publish gate and the host's push gates — and it runs before the gate, so by the time the human approves it is already worth approving.

**User Story:** As a person depositing outward, I want the publish checklist run before the human's gate, so that nothing leaves unchecked and the gate approves work already worth approving.

### Acceptance Criteria

**Case: the checklist is the one home**

1. The system *shall* have the publish skill own the per-kind checklist and *shall* deposit nothing outward without passing it first, the walk's result riding the landing report like any other step. [E-12, INV-22]

**Case: the standing gates hold**

2. The system *shall* keep the human's publish gate over anything irreversible or outward and the host's push gates over the push, the checklist never bypassing them. [E-20, ACT-1, M-6]
3. The system *shall* run the checklist before the gate, so by the time the human approves it is already worth approving. [E-20]

---

## Requirement 48: Each publish target embeds its own steps

**Context:** Each publish target is a plugin that embeds its own steps into the walk. The target adds steps and never removes the kind's owed minimum.

**User Story:** As a person publishing to a named target, I want the target to add its own steps without removing the kind's minimum, so that a destination's demands ride on top of what the reader is already owed.

### Acceptance Criteria

**Case: the target adds, never removes**

1. *when* a publish target joins the walk, the system *shall* embed its own steps — a README at the door plus release notes for a code host, a manifest and forms for a plugin directory, its cards for the design project. [E-18]
2. The system *shall* have the target add steps and *shall* never let it remove the kind's owed minimum. [E-18]

---

## Requirement 49: A version push re-opens the shopfront

**Context:** Every push that ships a new version changes the truth a public reader will read tomorrow, even when the diff never touched a doc, so the shopfront rides every push. The README's claims still have to match the truth just pushed, and the kind-owed visuals ride along. A stale shopfront is a false claim, exactly like a stale screenshot.

**User Story:** As a public reader, I want every version push to re-check the README and its kind-owed visuals against the pushed truth, so that I never meet an out-of-date front.

### Acceptance Criteria

**Case: the shopfront rides every push**

1. *when* a push ships a new version, the system *shall* re-check the README's claims — behaviour, counts, commands, version homes — against the truth just pushed, even where the diff touched no doc. [INV-44]
2. The system *shall* have the kind-owed visuals ride along — a skill pack re-checking its diagrams, a visual product re-shooting what changed on screen, a tool re-running its example. [INV-44]

**Case: one home, its outcome recorded**

3. The system *shall* read this shopfront check as the publish checklist at push scale, the commit-and-show step pointing at it and the walk's outcome riding the landing report. [INV-44, INV-22, E-20]
4. *when* a push's changes touch none of the shopfront's claims, the system *shall* say so in one line and *shall* fix a stale claim before the push, freshness being about the claims rather than styling. [INV-44]

---

## Requirement 50: Everything built with the method carries its attribution line

**Context:** Every publication of an artifact built with the pack carries one attribution line, `made with live-spec` linking to the pack repo, on the publication's landing surface. The line names the pack version the project runs, read from the host's attach record, so it doubles as the adoption tracker. The line is an offer, never a gate — the owner's taste rules his own shopfront.

**User Story:** As a person publishing built-with work, I want one attribution line offered on its landing surface naming the pack version, so that who runs the method is readable from the shopfronts while the owner keeps the final say.

### Acceptance Criteria

**Case: the line and its version**

1. *when* a built-with artifact is published, the system *shall* carry one attribution line on its landing surface — the README footer, and for a skill also its `SKILL.md` — naming the pack version read from the host's attach record at write time rather than an invented number. [INV-96]

**Case: an offer, never a gate**

2. The system *shall* treat the line as an offer, the publish walk checking for it and proposing it once when absent, the owner's word deciding and a declined offer staying closed. [INV-96, INV-16]
3. The system *shall* apply the line to each built-with project through its own queue and *shall* stamp it onto each standalone mirror from the live `VERSION` file at every sync, since a hand-written footer on a mirror would carry an invented number and be wiped by the next sync. [INV-96]

---

## Requirement 51: Every standalone mirror shows its release history

**Context:** A standalone mirror's README carries a release-history section: one line per shipped version giving the version, its date, and a single story line. The sync script harvests those lines from the pack's git history and writes them fresh at every sync, the same way it stamps the attribution line. The full home of each release's story stays the journal.

**User Story:** As a reader of a mirror, I want a generated release-history section refreshed at every sync, so that the public mirror always shows a current history that never drifts.

### Acceptance Criteria

**Case: the generated history**

1. The system *shall* carry a release-history section on a standalone mirror's README, one line per shipped version giving the version, its date, and a single story line, harvested from the pack's git history and written fresh at every sync. [INV-181]
2. The system *shall* keep the journal as the one full home of each release's story, the mirror section pointing back to it, and *shall* keep the history on the README alone while the mirror's `SKILL.md` stays free of reader-facing blocks. [INV-181]

**Case: the generated blocks are one pinned kind**

3. The system *shall* read the mirror's generated blocks as one declared kind with three members — the read-only banner at the README's top, this release-history section, and the attribution line — each pinned by a test, and *shall* let the owner's word move the section to a generated changelog file. [INV-181, INV-96]

---

## Requirement 52: Shipped product docs state each requirement impersonally

**Context:** A product's shipped docs — the spec, the test matrix, the README, a skill card — reach everyone the project touches. Each requirement reads as three plain parts: the rule, the actor as a role, and the reason it holds. The reason stays because a reader has to know why the rule stands, while the personal attribution drops; a dated decision keeps its date as a plain anchor and drops the name.

**User Story:** As a reader of shipped docs, I want each requirement stated as rule, role, and reason with personal names dropped, so that what ships reads as neutral product truth while the reason a reader can act on survives.

### Acceptance Criteria

**Case: rule, role, and reason**

1. The system *shall* write each shipped requirement as the rule, the actor as a role — the user, the producer, the target user — and the reason it holds, the reason staying and the personal attribution dropping. [INV-118]
2. The system *shall* keep a dated decision's date as a plain anchor while dropping the name, so the provenance a reader can act on survives. [INV-118]

**Case: candid voice has one home**

3. The system *shall* home personal attribution and candid process voice in the local-only diaries that no publish ships, spec-author writing each shipped clause impersonally from the first draft and the publish floor reading the shipped docs for a stray personal name before the deposit leaves. [INV-118]

---

## Requirement 53: A machine holds the shipped tree's language line

**Context:** A shipped artifact carries no Cyrillic outside a user-language string the program deliberately emits, and no personal name in a requirement's statement. The publish gate holds this with a machine that reports each offence as file and line. The name arm reads a declared alphabet rather than a fixed spelling list, and the specific out-of-alphabet name patterns live as data in an allowlist, so the detector's own source names no person.

**User Story:** As a person shipping an artifact, I want a machine flagging stray script and personal names as file and line, so that the fix is mechanical while candid notes stay in the diaries.

### Acceptance Criteria

**Case: the two mechanical offences**

1. The system *shall* hold that a shipped artifact carries no Cyrillic outside a deliberate program string and no personal name in a requirement's statement, reporting each offence as file and line through `guardrails/check-shipped-language.sh`. [INV-120]
2. The system *shall* read the name arm against a declared alphabet — `ASCII` English plus deliberate program strings — with the out-of-alphabet name patterns held as allowlist data, so the detector's own source names no person and covering a collaborator's name is one data line. [INV-120, INV-114]

**Case: the arms stand down by declaration**

3. *if* a package declares no alphabet, *then* the system *shall* leave the name arm inert while the Cyrillic arm still stands, and *shall* spare deliberate program data and authorship bylines through the same dated allowlist, a new offence redding and a listed one counted as debt. [INV-120]

---

## Requirement 54: A core spec names no foreign project and tells no dated incident

**Context:** A core spec — the product spec, the architecture, and the test matrix — states the rule that holds and leaves the project it was first met on and the day it was met to the local-only diaries. A sibling project's name couples the spec to a neighbour it should not know, and a dated-incident turn is history the diaries own. The shipped-language machine gains a project-name arm scoped to the three core specs.

**User Story:** As a reader of a core spec, I want it to state the rule and leave the project and the date to the diaries, so that the spec stays free of cross-project coupling and leaked history.

### Acceptance Criteria

**Case: the project-name arm**

1. The system *shall* red a bare project name in the product spec or the architecture, and *shall* red a project name standing beside a calendar date in any of the three core specs. [INV-245]
2. The system *shall* have the test matrix red a dated incident while permitting a bare fixture-ledger kind name and a project-name substring of a test-function name, a fixture name that ever falls beside a date redding and a genuine one waived as counted debt through the dated allowlist. [INV-245]

**Case: the data-held names and the moved history**

3. The system *shall* hold the forbidden project names as data in the shipped-language allowlist so the detector's own source names no project, and *shall* leave the arm inert for a package that declares none. [INV-245, INV-120]
4. The system *shall* move the history a reworded line drops — who met the rule, when, and why — to the journal as a dated entry, the way a dated decision keeps its date while the attribution comes off, and *shall* leave a skill body and the README free to cite a real case since a teaching text names the project a lesson was drawn from. [INV-245, INV-118]
