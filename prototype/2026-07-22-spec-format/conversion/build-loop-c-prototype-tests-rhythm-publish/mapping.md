# MAPPING — codes, consumed index rows, and atomic-claim coverage

This file proves the rewrite of the last four subsections of `## The build loop` (source lines 621–927: `### A prototype stays a sketch`, `### From the spec to the tests`, `### The rhythm: breakpoints, milestones, pushes`, `### Publishing`) dropped nothing. Part 1 maps every code the source cites to its new home. Part 2 states which codes carried a consumed Formal-index row. Part 3 maps every behavioural claim of the source prose to the criterion that now carries it.

`Rn` names Requirement n in `section.md`; a code cited in several requirements is anchored in each. Zero codes are dropped: all 110 cited codes appear in `section.md` (verified mechanically — cited-set minus present-set is empty, and no code outside the cited set was introduced).

## Part 1 — every cited code → its new home

| Code | New home | Index row consumed? |
|---|---|:--:|
| A-7 | R28, R39 | yes |
| ACT-1 | R47 | yes |
| ACT-2 | R3 | yes |
| ACT-3 | R31 | yes |
| E-5 | R27 | yes |
| E-6 | R5 | yes |
| E-10 | R5 | yes |
| E-12 | R47 | yes |
| E-14 | R21, R27 | yes |
| E-15 | R27, R33 | yes |
| E-16 | R33 | yes |
| E-17 | R1, R2, R6, R7 | yes |
| E-18 | R48 | yes |
| E-19 | R33 | yes |
| E-20 | R47, R49 | yes |
| E-24 | R33 | yes |
| E-27 | R8 | yes |
| E-29 | R25 | yes |
| INV-1 | R33 | yes |
| INV-2 | R43 | yes |
| INV-6 | R27 | yes |
| INV-9 | R42 | yes |
| INV-10 | R3 | yes |
| INV-11 | R31, R42, R44 | yes |
| INV-16 | R2, R4, R50 | yes |
| INV-17 | R1, R5, R6 | yes |
| INV-18 | R21 | yes |
| INV-22 | R47, R49 | yes |
| INV-23 | R15, R17 | yes |
| INV-24 | R40 | yes |
| INV-26 | R30 | yes |
| INV-30 | R7, R11 | yes |
| INV-35 | R43 | yes |
| INV-36 | R24, R25, R26 | yes |
| INV-37 | R21, R23 | yes |
| INV-39 | R33 | yes |
| INV-41 | R21, R24 | yes |
| INV-43 | R6, R7 | yes |
| INV-44 | R42, R49 | yes |
| INV-45 | R45 | yes |
| INV-46 | R15, R34 | yes |
| INV-48 | R30 | yes |
| INV-56 | R33 | yes |
| INV-59 | R24 | yes |
| INV-61 | R45 | yes |
| INV-70 | R34, R42 | yes |
| INV-74 | R21, R25 | yes |
| INV-75 | R21, R26 | yes |
| INV-76 | R31 | yes |
| INV-77 | R11 | yes |
| INV-78 | R12 | yes |
| INV-79 | R13 | yes |
| INV-80 | R14 | yes |
| INV-82 | R42 | yes |
| INV-83 | R35 | yes |
| INV-84 | R32 | yes |
| INV-91 | R18 | yes |
| INV-96 | R50, R51 | yes |
| INV-98 | R35 | yes |
| INV-100 | R9, R17 | yes |
| INV-102 | R10 | yes |
| INV-106 | R43 | yes |
| INV-107 | R29, R34 | yes |
| INV-109 | R33 | yes |
| INV-110 | R18 | yes |
| INV-111 | R33 | yes |
| INV-112 | R44 | yes |
| INV-113 | R23 | yes |
| INV-114 | R53 | yes |
| INV-115 | R33, R34 | yes |
| INV-116 | R33, R34, R44 | yes |
| INV-118 | R52, R54 | yes |
| INV-120 | R53, R54 | yes |
| INV-122 | R22, R33 | yes |
| INV-123 | R33 | yes |
| INV-125 | R19 | yes |
| INV-141 | R33, R34 | yes |
| INV-145 | R34 | yes |
| INV-150 | R17 | yes |
| INV-154 | R33 | yes |
| INV-155 | R15, R17 | yes |
| INV-156 | R19 | yes |
| INV-157 | R17, R18, R19, R20 | yes |
| INV-158 | R18, R19 | yes |
| INV-159 | R7, R24, R25, R26, R27 | yes |
| INV-160 | R19 | yes |
| INV-162 | R20 | yes |
| INV-163 | R18, R36 | yes |
| INV-164 | R24, R35 | yes |
| INV-166 | R36 | yes |
| INV-173 | R36, R38 | yes |
| INV-181 | R51 | yes |
| INV-183 | R38 | yes |
| INV-203 | R37, R38 | yes |
| INV-204 | R20 | yes |
| INV-215 | R37 | yes |
| INV-218 | R16 | yes |
| INV-220 | R38 | yes |
| INV-221 | R38 | yes |
| INV-226 | R24 | yes |
| INV-245 | R54 | yes |
| M-1 | R33 | yes |
| M-2 | R28 | yes |
| M-3 | R39 | yes |
| M-5 | R41 | yes |
| M-6 | R44, R47 | yes |
| M-7 | R39 | yes |
| S-0 | R5 | yes |
| T-12 | R4 | yes |
| T-16 | R46 | yes |

**Mechanical zero-drop check:** cited-set (110 codes) minus present-set (the codes carried on `section.md` criteria) is empty, and present-set minus cited-set is empty — no code was dropped and none invented.

## Part 2 — consumed Formal-index rows

The section cites 110 distinct codes, and **all 110 carry a Formal-index row** — this stretch names no inline-only feature code. Each row's meaning now lives at the home named in Part 1; no consumed index row is left without a home.

**Codes whose Formal-index home is one of these four subsections** (`A prototype stays a sketch`, `From the spec to the tests`, `Rhythm`, `Publishing`) are the ones this rewrite fully converts: E-17, INV-17, INV-43 (prototype); E-5, E-14, E-15, E-27, E-29, INV-6, INV-41, INV-74, INV-75, INV-77, INV-78, INV-79, INV-80, INV-100, INV-102, INV-113, INV-122, INV-155, INV-157, INV-158, INV-160, INV-162, INV-218 (spec-to-tests); M-2, M-3, M-5, M-6, M-7, INV-24, INV-48, INV-61, INV-76, INV-84, INV-106, INV-107, INV-115, INV-116, INV-123, INV-145, INV-164, INV-166, INV-215, INV-221 (rhythm); E-20, INV-44, INV-96, INV-118, INV-120, INV-181, INV-245 (publishing).

**Pure cross-references** — a rule owned by another section that this stretch leans on rather than restates — are preserved as trailing anchors at the requirement that leans on them; the full behaviour stays defined in the home section, not re-converted here: A-7, ACT-1, ACT-2, ACT-3, E-6, E-10, E-12, E-16, E-18, E-19, E-24, T-12, T-16, S-0, INV-1, INV-2, INV-9, INV-10, INV-11, INV-16, INV-18, INV-22, INV-23, INV-26, INV-30, INV-35, INV-36, INV-37, INV-39, INV-45, INV-46, INV-56, INV-59, INV-70, INV-82, INV-83, INV-91, INV-98, INV-109, INV-110, INV-111, INV-112, INV-114, INV-125, INV-141, INV-150, INV-154, INV-156, INV-159, INV-163, INV-173, INV-183, INV-203, INV-204, INV-220, INV-226.

**One anchor anomaly, carried as cited.** At source line 885 the prose reads "The publish skill owns the per-kind checklist [E-12]", yet the Formal index homes the publishing-checklist fact at E-20 ("Publishing owes the artifact's kind its checklist; one home: the publish skill"), while E-12 is the base-skill entity ("shared rules + defaults, stated once"). The rewrite carries the source's own citation: R47.1 trails [E-12] as the source does, and R47.2/R47.3 and R49 carry E-20 for the publishing-contract facts. Both codes therefore appear. This looks like a source mis-anchor (E-12 for E-20), but correcting an anchor would be invention, so the cited code is preserved verbatim and the observation is recorded here rather than silently changed.

**Cross-section glossary note.** Several domain nouns this stretch uses are owned by other sections and defined in their home glossary, not repeated here: *milestone*, *movement*, *feel pass*, *prover record*, *test matrix*, *feature-coverage trace*, *register judge*, *surface registry*, *content contract*, *design principle*, *project kind*, *proof kinds*, *grant*, *push gate*, *problem ledger*, *the three fitness questions*, *the scissors ban*, *the negation-opener rule*, *the muted-launch net*, *the catch-up walk*, *the setup walk*. In a whole-document conversion these live once in the pooled glossary; this section's `## Glossary additions` block adds only the twenty nouns this stretch introduces (prototype, prod surface, norm, norm pointer, architecture node, level ladder, real-device walk row, coverage validation, breakpoint, checkpoint, skill-creator, thin loader, shopfront, attribution line, standalone mirror, design project, publish gate, publish checklist, remote gate, work-kind).

## Part 3 — atomic-claim coverage

Every behavioural claim of the source, in source order, mapped to the criterion (or criteria) that now carries it. "R9.4" means Requirement 9, criterion 4.

### A prototype stays a sketch (E-17, INV-16, INV-17, INV-10, ACT-2, T-12, E-6, E-10, S-0, INV-43, INV-30, INV-159)

| # | Source claim | Criterion |
|---|---|---|
| 1 | A prototype is a fenced exploration kept as a sketch, living in its own clearly named home; nothing in the product reaches into it. | R1.2 (glossary defines *prototype*) |
| 2 | Every artifact a prototype produces carries the label in its kind's form — page banner, `_prototype: true` field/header, script first-line banner, bare-file name/header marker. | R1.1 |
| 3 | The fence runs one way: never wire a prototype into a prod surface, never link to one from a prod surface, never style a prod surface to match one. | R1.3 |
| 4 | A prod surface is any part of the shipped product a user meets; show a prototype only under its label; nothing reaches the human as the product until its surface walked the full pipeline. | R1.4 (prod surface glossaried) |
| 5 | The boundary sits at the door step: a wish to have something in the product is a feature. | R2.1 |
| 6 | A request to merely see or try, with no commitment, may live as a sketch inside the fence — no lane, no spec. | R2.2 |
| 7 | When which was meant is unclear, ask one plain question; do not guess. | R2.3 |
| 8 | Opening a prototype home is a repo write the write-ownership law governs; the assigned senior makes the judgment. | R3.1 |
| 9 | An outside session files an inbox wish; a worker never opens a prototype home on its own brief. | R3.2 |
| 10 | Promotion enters the sketch's earned feature at the spec step without merging its code, like any wish. | R4.1 |
| 11 | The prototype is evidence for that spec; its code holds no rights. | R4.2 |
| 12 | The fence guardrail's live leg: a prod file referencing a prototype home turns red. | R5.1 |
| 13 | Two remaining legs: the surface registry completeness scan and the behaviour-traces-to-spec check (targets). | R5.2 |
| 14 | When all three land, the header honesty holds both directions: the spec never claims what is not built, the build never contains what the spec does not name. | R5.3 |
| 15 | Today only the fence leg is enforced; the rest is promised, marked, and owned by its rows. | R5.4 |
| 16 | Prose alone cannot record look and feel; a prose-only rebuild can pass tests and ship a look-alike. | R6 context |
| 17 | Once approved, the sketch becomes the norm; the clause cites its artifact via a `norm: <path>` pointer at line end. | R6.1 |
| 18 | Approval freezes a copy into `docs/norms/` with a dated provenance line (what, when, which sketch). | R6.2 |
| 19 | The pointer cites the frozen copy, never a live prototype home, so the fence stays absolute and the sketch stays free to die. | R6.3 |
| 20 | The build opens the artifact before the code step; the landing records a one-line plan-versus-prototype diff; a missing line is a defect at the code step. | R7.1 |
| 21 | The verify feel pass reads the same pointer. | R7.2 |
| 22 | The prover's norm lens flags a prototype-born clause with no pointer, or a clause contradicting its artifact. | R7.3 |
| 23 | A story may declare `entry: mockup-first`, held at the door step; only the human cancels it by name; a general "go build" moves priority but does not cancel. | R7.4 |
| 24 | The pointer binds forward — added at the first landing that touches the clause, never retroactively. | R7.5 |
| 25 | A pointer names only a human-approved look; an unapproved sketch stays plain evidence; a text-born clause carries none. | R7.6 |

### From the spec to the tests (E-27, INV-100, INV-102, INV-77, INV-78, INV-79, INV-80, INV-155, INV-218, INV-157, INV-158, INV-160, INV-162, E-14, INV-122, INV-113, INV-41, INV-74, INV-75, E-5, INV-6, E-15, and refs)

| # | Source claim | Criterion |
|---|---|---|
| 26 | test-author owns the test method; build-pipeline calls it at steps 5–6, the same way steps 1–2 call spec-author and the prover; the pipeline keeps order and gates. | R8.1 |
| 27 | The method holds the level ladder, real-artifact assertions, red-first proof, the pinned skip-set, and traceability as a standing test. | R8.2 |
| 28 | Every test removes what it creates; a suite run leaves the machine as it found it; a leak is a defect of the test. | R9.1 |
| 29 | Test files are born in the temp home or gitignored state dir and erased at run's end; a headless browser's download dir points at the temp home. | R9.2 |
| 30 | A user-visible folder (Downloads, Desktop, Documents) is never a test's workspace. | R9.3 |
| 31 | A session-scoped before/after diff of the temp home fails the run on a surviving file; the launch sweep clears a killed prior run's litter. | R9.4 |
| 32 | A test's expected value comes from a source other than the code under test (constant, independent derivation, or reviewed real output). | R10.1 |
| 33 | Never recompute the code's own formula as the expected value; that assertion is a mirror. | R10.2 |
| 34 | A round-trip or property test over outputs is legal, asserting an invariant not a recomputed value. | R10.3 |
| 35 | Touch physics, scroll snapping, background throttling live past a desktop headless browser; such a behaviour gets a real-device walk row the suite can never green, owed to the human before ship. | R11.1 |
| 36 | The suite says what it cannot see; a green run over such a fact claims nothing about it. | R11.2 |
| 37 | A geometry fact asserts relative geometry (center-to-center within a bound) at ≥ 2 viewport sizes. | R12.1 (+ GAP: tolerance/step-count unstated) |
| 38 | And after consecutive interaction steps so cumulative drift shows; an absolute one-viewport one-step assertion hides the drift by construction. | R12.2 |
| 39 | An engine extracted from an instance tests on its own generic fixtures (own ids, own content model); the donor's data stays as an extra real-data suite, never the only one. | R13.1 |
| 40 | Every donor-specific constant becomes a named content-contract entry with a works-without-it test. | R13.2 |
| 41 | The suite's plumbing must not lie — a skip path executes (skip helper imports at module load). | R14.1 |
| 42 | An engine/instance shim owes a re-export completeness test. | R14.2 |
| 43 | A background/delegated run's verdict is the suite log's tail line, not a wrapper's exit; a foreground gate reading its own child's exit is legal. | R14.3 |
| 44 | A test is green only when deterministic; a flake rooted in owned code is fixed at that root (named nondeterminism sources listed). | R15.1 |
| 45 | Masked by nothing — no retry, no rerun-until-green, no raised timeout hiding the race, no single pass accepted. | R15.2 |
| 46 | A flake not removable in owned code is problem-ledger workshop noise, a home apart from the owned defect. | R15.3 |
| 47 | A mechanical gate greps the test config for a retry/rerun plugin and reds; the rest is the verify walk's discipline, kin of the fresh-eyes audit. | R15.4 |
| 48 | A flake understood but not removable in one landing is quarantined by name in the pinned skip-set with a dated reason and owning row; an open quarantine holds no landing and is milestone-audit debt. | R15.5 |
| 49 | A check over an empty input set is not a pass; it declares its expected-non-empty input and reds by name when empty. | R16.1 |
| 50 | A call site that may legitimately read an empty set names its reason; the default is that empty is a finding. | R16.2 |
| 51 | The browser harness launches muted (the browser's mute flag) and reaps its whole process group on teardown. | R17.1 |
| 52 | On launch it sweeps a stale process group and temp litter a prior run left, by its own profile marker; a young ownerless dir is left alone. | R17.2 (+ GAP: young/old age boundary) |
| 53 | It bounds each command with a real per-command deadline; never inflate a timeout that buries a race. | R17.3 |
| 54 | It prefers `chrome-headless-shell` (newest first, then Chrome for Testing, then system Chrome) and drops the extra headless flag for the shell. | R17.4 |
| 55 | A launch probe loads one loopback page and awaits one compositor frame under bounded windows, failing a stalled/frame-dead browser loudly by name. | R17.5 |
| 56 | The pack's suite string-checks the shipped template (mute, sweep, reap, deadline); a consumer's suite asserts by deed via a post-run process-group check reddening on a surviving orphan. | R17.6 |
| 57 | A third net greps every tracked script and reds one that launches real headless Chrome carrying the mute flag nowhere (comment-stripped, whole-file, retroactive). | R17.7 |
| 58 | A harness fault from its own run hygiene is root-fixed here; only a fault with nothing to correct in owned code routes to the ledger. | R17.8 |
| 59 | The harness has one canonical home shipped once as a pack template; a consumer adopts it by a package update via the catch-up walk, layering its own driving methods on the shared core. | R18.1 |
| 60 | A core fix lands once and reaches every consumer through the update (the migration path a package update carries). | R18.2 |
| 61 | A project that forks a private copy owns the divergence; the third mute-launch net still catches a forked unmuted launch; the centralize pole of the pack-to-host split. | R18.3 |
| 62 | The suite-honesty family is one class; each member names the net that reds a run; three members make the assertion shape itself the net. | R19.1 |
| 63 | A member naming no net is a class defect the prover blocks, the same standing an under-enumerated review-record member has. | R19.2 |
| 64 | The class binds forward: a new member states its net; members declared before the class stand unreshaped. | R19.3 |
| 65 | A cleanup acts only on what the run provably owns or a prior run whose recorded owner is provably dead, never a shared resource in current use (process, temp dir, port, file, lock, display). | R20.1 |
| 66 | A kill targets a recorded PID, an owned process group, or an install path under the run's tree; on a shared machine the recorded process group is the sole safe target. | R20.2 |
| 67 | The guard refuses every name-based ending (a name pattern, or a name-to-id lookup). | R20.3 |
| 68 | The class covers every process the pack runs a copy of (browser, language runtime and its separation tool, bundler, media tool); a program the pack never launches is beside the point. | R20.4 |
| 69 | A guardrail reds a tracked script ending a process by name with no id/group/path proof, its probe corpus a committed fixture. | R20.5 |
| 70 | Every ending the pack performs announces what it ended and why the run owned it. | R20.6 |
| 71 | Two documents sit between the spec and tests; ARCHITECTURE.md names nodes, each one responsibility and one name, every spec fact owned by exactly one node. | R21.1 |
| 72 | Each node pins to its owning place by the named thing; the `:line` is a cache re-greppable; every pin comes from a command that was run. | R21.2 |
| 73 | The architecture is proven with the architecture lens at the kind's scale — every fact owned, no unbacked node, every seam named. | R21.3 |
| 74 | The lens also checks budgets with instrumentation homes and watchers, the runtime view over every flow, and the placement view. | R21.4 |
| 75 | A large/surface-class wish updates the doc before the matrix; a bug/small wish cites its node; an ownerless fact is assigned to the nearest node with no re-prove. | R21.5 |
| 76 | The doc maps the product as it stands plus the landing in flight; never a speculative node ahead; a re-carve arrives as its own row under a restructure placement and is re-proven. | R21.6 |
| 77 | Every new/carved node answers three fitness questions at birth (testable alone, real second place, parallel-workable). | R22.1 |
| 78 | One no is a flag to answer before the carve stands; two or more no make it premature. | R22.2 |
| 79 | The prover flags a one-caller node with no promised second on the second question, never auto-rejecting; birth gate and prover agree. | R22.3 |
| 80 | A deliberate redesign re-shapes ARCHITECTURE.md and re-proves it in the same movement. | R23.1 |
| 81 | The pins-only path is scoped to a boundary shift leaving the shape standing; fresh pins on a stale shape are a defect; the re-carve routes as its own row. | R23.2 |
| 82 | The architecture states measurable budgets each with its instrumentation home and its watcher, or a decided sentence naming why read by eye. | R24.1 |
| 83 | A budget with neither watcher nor decided sentence is a derivation defect, flagged like an unowned fact. | R24.2 |
| 84 | Measurable dimensions follow the project kind (product paint/interaction; backend latency/throughput/error; pipeline run time/per-unit cost; skill pack eval pass rate/suite time; prose an honest number) — a closed enumerated set. | R24.3 |
| 85 | A quality with no honest number is said by name, never a vanity metric; a budget counts only once a matrix row at the right level sees it. | R24.4 |
| 86 | The numbers are the host's taste — proposed by the architecture, set on the human's word at the first budget landing, binding forward. | R24.5 |
| 87 | For every promised flow the runtime view walks the running product (node per step, data per hop, failure points), one short walk per flow; the feature-coverage table names which nodes implement a feature. | R25.1 |
| 88 | Every failure point carries its fallback (degrade, retry, guard); one without is an unfinished walk. | R25.2 |
| 89 | A flow the doc cannot walk end to end is a finding; the view scales by kind (a book's one sentence). | R25.3 |
| 90 | Every node states its place; a load-bearing tech choice is named; the same table says where secrets live and which tier holds each non-client verdict. | R26.1 |
| 91 | Placement is first-class (a column or its own table), answered at a glance. | R26.2 |
| 92 | The doc reads tiers-first: shape at a glance, then nodes, then flows, then budgets. | R26.3 |
| 93 | Both views scale by kind; a fullstack/data project owes both in full; the duty binds forward. | R26.4 |
| 94 | The matrix organizes rows by node × fact; every fact ≥ 1 row; every row a pinned level. | R27.1 |
| 95 | Coverage validation: every anchor ≥ 1 row, every artifact-inventory entry ≥ 1 rendered row, every visibility/layout/colour/interaction fact ≥ browser-computed, every node's negative-side rows. | R27.2 |
| 96 | A stale row retires (never vanishes); a fact with no row or too weak a level is a derivation defect the prover catches early. | R27.3 |
| 97 | No wish lands whose facts lack an owning node and a matrix row at the right level; a predating project brings the layers up, binding from the landing that creates them. | R27.4 |

### The rhythm (M-2, INV-107, INV-48, INV-76, INV-84, M-1 and stations, INV-145, INV-164, INV-166, INV-215, INV-221, M-3, M-7, INV-24, M-5, INV-82, INV-106, M-6, INV-61)

| # | Source claim | Criterion |
|---|---|---|
| 98 | Every movement ends the same way: replace the resume live state (never stack), add a dated journal entry, commit; memory then wipes with zero loss. | R28.1 |
| 99 | The resume file may be gitignored, so the journal entry is the durable net; a full wipe is the human's move. | R28.2 |
| 100 | At a breakpoint the agent compacts its own context and says so; on the way back it re-checks skill freshness. | R28.3 |
| 101 | A landing that ships a checkpoint's items flips it closed in the same landing; the closing sweep rides the resume replacement. | R29.1 |
| 102 | A checkpoint whose items all live in git history is stale by definition; one left "not started" after its items shipped fails the landing. | R29.2 |
| 103 | The resume file holds ≤ 100 lines; a suite check owns the number, red on a synthetic bloated file. | R30.1 |
| 104 | An open leg restates as one terse line (name, what's open, where detail lives); the detail flows to its home. | R30.2 |
| 105 | Compaction moves prose to its home; it never drops an open leg. | R30.3 |
| 106 | A background worker outlives a memory wipe; the OS process list and harness task record are not proof of death; liveness is by deed; the handoff note records id, briefed write-set, and three checks. | R31.1 |
| 107 | The three checks: watch write-set file times over a short window, read the heartbeat on the checkpoint file, send one message to the id. | R31.2 |
| 108 | Life on any one check ⇒ reconnect, files claimed; a dead verdict needs all three quiet together, declared in one line. | R31.3 |
| 109 | Output never framed finished before the verdict; no second worker onto the shared tree until the first halts by reply or is declared dead by all three. | R31.4 |
| 110 | A dead verdict frees only the worker's owned files; doneness is read from the checkpoint's finished marker or the verify walk. | R31.5 |
| 111 | Human-facing durable prose is drafted by a fresh writer from a plain brief (facts, reader, register laws); the rules-loaded session reviews and lands. | R32.1 |
| 112 | The rule binds the section the edit touches; a whole page is redrafted only on the human's word. | R32.2 |
| 113 | A report typed live in chat stays the session's own words; a mechanical correction rides the ordinary hand. | R32.3 |
| 114 | A blanket rewrite of settled text is refused, since meaning can shift in bulk restructures. | R32.4 |
| 115 | The milestone gate re-proves the spec in full and the architecture beside it, recording the architecture pass in `docs/prover/` beside the spec's. | R33.1 |
| 116 | The design review runs in full on the re-proven spec (whole inventory, groupings, parity, ≤ 3 asks), its dated record landing; a confirmed grouping re-enters the prove step at the cap, typically resting by awaiting the human. | R33.2 |
| 117 | Matrix audit re-walks coverage validation; surface-composition check; re-run skill evals. | R33.3 |
| 118 | Walk the skills through skill-creator for craft, each finding folded/rejected with a written reason in a dated record; a joining skill walks it at birth. | R33.4 |
| 119 | Doc compaction audits every living document (spec, matrix, queue, skills, ledger, suite), removing only redundancy and keeping meaning, accounting for each substance removal. | R33.5 |
| 120 | Compaction widens to code (merge duplicates, remove dead weight with listing, extract only through the fitness gate); a second occurrence opens its own row landing at one delta per commit without blocking its lane. | R33.6 |
| 121 | Restructure only for a faster shape and only through the content-preserving layout vehicle with the multiset proof; queue compaction archives closed rows, never deletes. | R33.7 |
| 122 | Re-list every open human gate and unharvested inbox file; sweep deferred rows' triggers, sending fired rows to runnable; re-check the formal index against the prose. | R33.8 |
| 123 | Re-pin the derived docs' headers to the spec version and prove them; re-read the thin loader line by line, keeping only what must hold before any pack file loads and migrating the rest. | R33.9 |
| 124 | A full audit runs every ten landings (host-settable default), running the milestone whole-read even where no milestone is due. | R34.1 |
| 125 | The count is read from the landing history; a milestone gate resets the counter. | R34.2 |
| 126 | The whole-read takes the adversarial verify stance, set on breaking the work. | R34.3 |
| 127 | Compaction is continuous — every push held to the reached-clean floor (register lint 0, redundancy 0, debt cap ratcheting down), asserted against the live document. | R35.1 |
| 128 | The milestone whole-read runs above the push gate as the deep periodic audit. | R35.2 |
| 129 | Any quality a machine can verify is wired as a blocking gate, held by no pass's attention. | R35.3 |
| 130 | The style lint's universal tier (scissors ban, negation-opener, machine-jargon, provenance-narrative) binds every host's gate; provenance-narrative is a hard error in every tier. | R36.1 |
| 131 | The pack-register tier (caps-shout, second-person, reassurance, future-narration) is the pack's own taste, available to a host on its word. | R36.2 |
| 132 | One flag runs the universal tier as the gate (register tier advisory) or the union; the split is declared in `docs/spec-style.md`; the pack-to-host split applied to language. | R36.3 |
| 133 | A paragraph packing three or more distinct parallel facts earns bullet/numbered structure; prose stays for laws, reasoning, boundaries. | R37.1 |
| 134 | The rule is read by eye and by the prover's cognitive-load lens, earning no mechanical lint of its own; the register judge and prover make the meaning call. | R37.2 |
| 135 | Grading the size of a change is the reader's act; the size is content or a number; over-dramatization to the plus and minus are one bias. | R38.1 |
| 136 | The law binds every text (chat, docs, worker reports, agent-to-agent); a correction is described as a correction. | R38.2 |
| 137 | On chat/document surfaces the register judge holds the class with the literal overlays as first pass; the worker brief carries the law for the surface the judge does not read. | R38.3 |
| 138 | Documents are versioned like code; the queue and spec carry dated versions so a reader tells which roadmap version a decision was made under. | R39.1 |
| 139 | Version has named homes: the VERSION file, each SKILL.md frontmatter line, the host's installed-set record at attach and update. | R39.2 |
| 140 | The freshness check compares version against version as exact strings, not file times. | R39.3 |
| 141 | Time read off the clock: no file/journal/ledger date later than the current clock; a future stamp reds; a prose quote of a past date stays legal. | R40.1 |
| 142 | At commit, an added line pairing today's date with a time past the commit moment reds; the adjacent stamp shape against the commit clock; a quoted time stays green. | R40.2 |
| 143 | A chat timestamp is read off the clock at write time, never extrapolated; the law lives in communicator. | R40.3 |
| 144 | A harness hook injects the wall clock into every prompt where installed; otherwise the law stands alone. | R40.4 |
| 145 | A host may mirror the same checks in CI as a second net; one source of truth, the same scripts, never redefined; the reach map stays a local optimization. | R41.1 |
| 146 | The second net runs the full set. | R41.2 |
| 147 | Accepted (same-or-better, all reached gates green) work is pushed to the host's remote by rule under the standing push grant, never parked. | R42.1 |
| 148 | The remote is discovered from the tree first; one contextual question at the first push moment only where there is no remote or no recorded grant. | R42.2 |
| 149 | While another session is known live, the by-rule push stands down and coordination returns to the human; work waits local. | R42.3 |
| 150 | Every push re-walks the README against the pushed truth; a named milestone gate still waits for the human's word. | R42.4 |
| 151 | The push walk reads the remote gate's verdict (one `gh run`, minutes); a slow gate is watched on the detached-work cadence. | R43.1 |
| 152 | A red verdict is the session's own immediate bug, preempting by the bug lane, fixed and re-pushed the same session, so the human never meets it in a mailbox. | R43.2 |
| 153 | The flagship's push is preceded in the same session by the concurrent-edit fence and a fresh prover pass over spec and architecture, the record landing before the push; an architecture-stale record is as stale as a spec-stale one. | R44.1 |
| 154 | Defect findings are folded before pushing; a gate-pass fold ships with the same record; a wider fold re-triggers the gate; the rest become queue rows. | R44.2 |
| 155 | One carve-out: a diff of exactly one new inbox file owes the fence and no record; anything more rides the full gate. | R44.3 |
| 156 | The record is named `YYYY-MM-DD[-suffix].md` (suffix mandatory when the date's file exists); no record for the pushed state means the push should not have happened. | R44.4 |
| 157 | Process bookkeeping scales to the delta; a small delta (skill/prose/infra, no new surface/structure) ships a three-line short-form record. | R45.1 |
| 158 | A surface-sized or structural delta keeps the full walk. | R45.2 |
| 159 | Claims batch per lane, one commit; the journal chapter and resume rewrite come once per landing batch. | R45.3 |
| 160 | The irreducible core stays fixed regardless of scale (law text, red-first test, delta cross-link prove, gates). | R45.4 |

### Publishing (T-16, E-12, E-20, INV-22, ACT-1, M-6, E-18, INV-44, INV-96, INV-181, INV-118, INV-120, INV-245)

| # | Source claim | Criterion |
|---|---|---|
| 161 | Work leaves the machine (repo public, skill directory, release, cards to a design project); the work-kind axis applies again at the door of publishing. | R46.1 |
| 162 | Each kind owes its minimum: a skill its install/commands/when; a tool real runs; a visual product fresh screenshots; prose its reading path. | R46.2 |
| 163 | A comparison or diagram joins only when it carries the argument, never as decoration. | R46.3 |
| 164 | The publish skill owns the per-kind checklist; nothing is deposited without passing it; the result rides the landing report. | R47.1 |
| 165 | The human's publish gate guards anything irreversible/outward; the host's push gates guard the push; the checklist never bypasses them. | R47.2 |
| 166 | The checklist runs before the gate, so by approval it is already worth approving. | R47.3 |
| 167 | Each publish target embeds its own steps (GitHub README + release notes, a plugin directory's manifest/forms, the design project's cards). | R48.1 |
| 168 | The target adds steps, never removes the kind's owed minimum. | R48.2 |
| 169 | A version push re-opens the shopfront: the README's claims (behaviour, counts, commands, version homes) match the pushed truth, even when the diff touched no doc. | R49.1 |
| 170 | The kind-owed visuals ride along (skill pack diagrams, visual product re-shoot, tool re-run). | R49.2 |
| 171 | This shopfront check is the publish checklist at push scale; the commit-and-show step points at it; the outcome rides the landing report. | R49.3 |
| 172 | A push touching none of the claims says "shopfront checked — current" in one line; a stale claim is fixed before the push; freshness is about claims, not styling. | R49.4 |
| 173 | Every built-with publication carries one `made with live-spec` attribution line on its landing surface (README footer, and a skill's SKILL.md), naming the pack version read from the attach record. | R50.1 |
| 174 | The line is an offer, never a gate: the walk checks and proposes once when absent; the owner's word decides; a declined offer stays closed. | R50.2 |
| 175 | Each project applies the line through its own queue; the pack's own mirrors are stamped from the live VERSION file at every sync (a hand-written footer would carry an invented number and be wiped). | R50.3 |
| 176 | Every standalone mirror carries a generated release-history section (one line per version: version, date, one story line) harvested from git history, written fresh at every sync. | R51.1 |
| 177 | The journal is the one full home of each story; the mirror section points back; the history lives on the README, the mirror's SKILL.md staying free of reader blocks. | R51.2 |
| 178 | The mirror's generated blocks are one declared kind with three members (top banner, release-history, attribution line), each pinned by a test; the owner may move the section to a generated changelog. | R51.3 |
| 179 | Shipped product docs state each requirement as rule + role + reason; the reason stays, the personal attribution drops; a dated decision keeps the date and drops the name. | R52.1, R52.2 |
| 180 | Personal attribution and candid voice live only in the local-only diaries no publish ships; spec-author writes impersonally from the first draft; the publish floor reads for a stray name. | R52.3 |
| 181 | A shipped artifact carries no Cyrillic outside deliberate program strings and no personal name in a requirement; `guardrails/check-shipped-language.sh` reports each offence as file:line. | R53.1 |
| 182 | The name arm reads a declared alphabet (ASCII English + program strings) with name patterns as allowlist data, so the detector names no person; a collaborator's name is one data line. | R53.2 |
| 183 | A package declaring no alphabet leaves the name arm inert (the Cyrillic arm stands); deliberate program data and bylines are spared through the dated allowlist (new offence reds, listed one is counted debt). | R53.3 |
| 184 | A core spec (product spec, architecture, matrix) states the rule and leaves the project and date to the diaries; a bare project name reds in the product spec/architecture, and a project name beside a date reds in any core spec. | R54.1 |
| 185 | The matrix reds a dated incident while permitting a bare fixture-ledger kind name and a project-name substring of a test-function name; a fixture name beside a date reds; a genuine one is waived as counted debt. | R54.2 |
| 186 | The forbidden project names live as allowlist data so the detector names no project; the arm is inert for a package declaring none. | R54.3 |
| 187 | The dropped history moves to the journal as a dated entry; a skill body and README stay free to cite a real case, since a teaching text names the project a lesson was drawn from. | R54.4 |

### Coverage result

187 behavioural claims mapped, covering all 54 requirements. Source policy and non-goal blocks are carried as context prose rather than converted to `shall` criteria, since the format keeps a deliberate non-behaviour as prose: the F-prototype landing's "facets are N/A" and its non-goals (no pointer-grep guardrail, the norm artifact's format free) sit in the R6/R7 contexts; the F-prototype success measure ("the next prototype-born surface lands with its pointer and diff line") and the publishing success measures are stated in context, their codes ([INV-43], [INV-44]) carried on criteria; the publishing non-goals (no README-vs-diff checker, no auto-regenerated images) sit in the R49 context. History carried by the source prose — dates, named-incident narratives, and person attributions ("the owner named it", "his word", worked-incident dates) — is dropped by law 6; it lives in the journal already. Two source holes are recorded as `[GAP]` lines at R12.1 and R17.2 and detailed in `GAPS.md`. No behavioural `shall`-claim of the source is left uncovered.
