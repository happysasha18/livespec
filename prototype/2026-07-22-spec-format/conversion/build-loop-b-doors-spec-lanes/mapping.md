# MAPPING — codes, consumed index rows, and atomic-claim coverage

This file proves the rewrite of `PRODUCT_SPEC.md` lines 277–620 — the second half of `### Throwing a wish` inside `## The build loop` (`#### Doors, kinds, and craft`, `#### Specifying and building a feature`, `#### Parallel lanes, one pen`) — dropped nothing. Part 1 maps every code the source cites to its new home. Part 2 states which codes carried a consumed Formal-index row and which stay pure cross-references. Part 3 maps every behavioural claim of the source to the criterion that now carries it.

`Rn` names Requirement n in `section.md`; a code in several requirements is anchored in each. **Zero codes are dropped: all 132 cited codes appear in `section.md`** (verified mechanically — cited-set minus present-set is empty; the assigned lines cite 132 distinct codes, and every one is anchored on a criterion).

## Part 1 — every cited code → its new home

| Code | New home |
|---|---|
| A-3 | R12, R17, R39, R40 |
| A-10 | R17 |
| A-11 | R52 |
| ACT-3 | R41 |
| C-1 | R17 |
| E-3 | R58 |
| E-4 | R61 |
| E-8 | R11 |
| E-10 | R25 |
| E-12 | R14, R15, R23 |
| E-13 | R11, R44, R53, R55 |
| E-15 | R17, R51 |
| E-17 | R16, R23, R39, R40 |
| E-22 | R33 |
| E-34 | R47, R49, R52, R55 |
| INV-1 | R28, R56, R60 |
| INV-2 | R41, R48, R50, R53, R54 |
| INV-3 | R42 |
| INV-4 | R9, R10, R20, R21, R33, R36, R40, R42, R44, R52, R53 |
| INV-5 | R4, R39, R40, R42 |
| INV-6 | R39 |
| INV-9 | R10, R36 |
| INV-10 | R54 |
| INV-11 | R41, R45, R53, R54, R55 |
| INV-12 | R11, R14 |
| INV-15 | R12 |
| INV-16 | R4, R5, R7, R9, R14, R16 |
| INV-17 | R9 |
| INV-18 | R10, R17, R21, R35, R36, R40 |
| INV-19 | R39 |
| INV-20 | R40 |
| INV-21 | R40 |
| INV-22 | R14, R15, R20, R23, R25 |
| INV-24 | R18 |
| INV-27 | R44, R50 |
| INV-28 | R18 |
| INV-29 | R21, R22, R27, R32 |
| INV-30 | R15, R23, R25, R29 |
| INV-31 | R10, R17, R35, R36 |
| INV-33 | R15 |
| INV-34 | R18 |
| INV-37 | R7, R10 |
| INV-39 | R45, R46, R49, R50, R54, R55 |
| INV-41 | R12 |
| INV-43 | R7, R37 |
| INV-46 | R32 |
| INV-49 | R46, R55, R56 |
| INV-50 | R22, R28, R31 |
| INV-59 | R25, R34 |
| INV-62 | R37 |
| INV-63 | R38 |
| INV-70 | R36 |
| INV-72 | R29, R31 |
| INV-73 | R51 |
| INV-74 | R12 |
| INV-75 | R12 |
| INV-83 | R18, R57, R58, R59 |
| INV-94 | R18 |
| INV-99 | R13, R32 |
| INV-101 | R18, R19, R20, R31, R49, R52, R54 |
| INV-103 | R8 |
| INV-104 | R6, R9 |
| INV-105 | R47, R52, R54 |
| INV-108 | R7 |
| INV-114 | R24 |
| INV-117 | R41, R43, R48, R53, R54 |
| INV-121 | R7 |
| INV-124 | R10 |
| INV-125 | R19, R25, R26, R27, R28, R30, R31, R34 |
| INV-126 | R31 |
| INV-127 | R29, R30, R31 |
| INV-128 | R7, R8 |
| INV-129 | R56, R57, R58, R59 |
| INV-130 | R33 |
| INV-131 | R5 |
| INV-133 | R2 |
| INV-134 | R8 |
| INV-135 | R31 |
| INV-136 | R25 |
| INV-138 | R16, R31 |
| INV-139 | R25 |
| INV-140 | R24, R25, R32, R33 |
| INV-141 | R19, R25, R26, R27, R32, R33, R34 |
| INV-142 | R32, R33, R34 |
| INV-143 | R20 |
| INV-144 | R10 |
| INV-145 | R32 |
| INV-150 | R19, R20, R50, R52, R54 |
| INV-151 | R9, R20 |
| INV-152 | R9, R20, R52, R57 |
| INV-153 | R20 |
| INV-154 | R34 |
| INV-156 | R31, R32 |
| INV-159 | R8, R11, R12, R21, R32, R40, R52 |
| INV-160 | R12 |
| INV-163 | R12 |
| INV-165 | R26, R27, R29 |
| INV-167 | R28, R29, R31 |
| INV-168 | R29, R31 |
| INV-169 | R27, R30, R32 |
| INV-170 | R30 |
| INV-171 | R30, R31 |
| INV-183 | R59 |
| INV-189 | R20 |
| INV-191 | R20 |
| INV-198 | R46, R49, R51, R53, R54, R55 |
| INV-199 | R50 |
| INV-200 | R51 |
| INV-201 | R47, R52 |
| INV-206 | R58 |
| INV-214 | R46, R55 |
| INV-222 | R58, R59 |
| INV-223 | R58 |
| INV-226 | R16 |
| INV-231 | R59 |
| INV-247 | R57 |
| M-1 | R13, R44, R56 |
| M-6 | R24, R36 |
| T-7 | R39 |
| T-8 | R56, R59, R60 |
| T-9 | R1, R44, R45, R50 |
| T-10 | R41, R43 |
| T-11 | R3 |
| T-12 | R4, R14 |
| T-13 | R16 |
| T-14 | R39 |
| T-15 | R4 |
| T-16 | R11, R12 |
| T-18 | R44, R45, R46, R49, R53 |
| T-19 | R36 |
| T-20 | R9 |
| T-23 | R48, R50, R54, R55 |

## Part 2 — consumed Formal-index rows

The unit cites **132 distinct codes. 131 carry a Formal-index row**; the single exception is `T-7`, an inline-only transition code the source anchors ("the landing line stays its one-line self [T-7]") that has no row in the `### Formal index` table — the same inline-only case the founding-section pilot noted. Every consumed index row's meaning now lives at the home named in Part 1; no consumed row is left without a home in `section.md`.

**Codes this rewrite fully converts** (their Formal-index home is `Throwing a wish` and their defining bold-lead paragraph sits inside the assigned lines 277–620, so the requirement carries the full behaviour): E-4, E-22, E-34, INV-2, INV-3, INV-4, INV-5, INV-12, INV-16, INV-18, INV-19, INV-20, INV-21, INV-22, INV-27, INV-28, INV-29, INV-30, INV-31, INV-33, INV-39, INV-49, INV-50, INV-62, INV-63, INV-70, INV-99, INV-101, INV-104, INV-128, INV-129, INV-131, INV-133, INV-134, INV-140, INV-141, INV-142, INV-144, INV-150, INV-151, INV-153, INV-154, INV-156, INV-159, INV-165, INV-167, INV-168, INV-169, INV-170, INV-171, INV-198, INV-199, INV-200, INV-201, INV-214, INV-222, INV-231, INV-247, T-8, T-11, T-12, T-13, T-14, T-16, T-18, T-23 (66 codes).

**Pure cross-references** — a rule owned by another section, or by the first half of `### Throwing a wish` (the sibling unit, lines 130–276), that this unit leans on rather than restates. The full behaviour stays defined in its home; here it is preserved as a trailing anchor at the requirement that leans on it: A-3, A-10, A-11, ACT-3, C-1, E-3, E-8, E-10, E-12, E-13, E-15, E-17, INV-1, INV-6, INV-9, INV-10, INV-11, INV-15, INV-17, INV-24, INV-34, INV-37, INV-41, INV-43, INV-46, INV-59, INV-72, INV-73, INV-74, INV-75, INV-83, INV-94, INV-103, INV-105, INV-108, INV-114, INV-117, INV-121, INV-124, INV-125, INV-126, INV-127, INV-130, INV-135, INV-136, INV-138, INV-139, INV-143, INV-145, INV-152, INV-160, INV-163, INV-183, INV-189, INV-191, INV-206, INV-223, INV-226, M-1, M-6, T-7, T-9, T-10, T-15, T-19, T-20 (66 codes).

A code cited in both halves of `### Throwing a wish` is anchored in both units by the brief's own rule; the split above is by defining paragraph, and a handful of lane-and-reporting codes (INV-2, INV-3, INV-4, INV-5, INV-27, INV-28) whose home column reads `Throwing a wish` are counted owned here because the four-things-that-hold block and the declared-laws paragraph that state them sit in the assigned lines.

**Cross-section glossary note.** A handful of domain nouns the unit uses are owned by other sections and defined in their home glossary, not repeated here (per the reuse-by-reference rule): *movement*, *milestone*, *worker*, *the setup walk*, *the economy ladder*, *feedback-intake*, *the batched decision page*, *checkpoint*, *the departures board*, *the surface registry*, *the settings ladder*. In a whole-document conversion these live once in the pooled glossary; this unit's `## Glossary additions` block adds only the nineteen nouns this unit introduces (door, tripwire, work-kind, spec-delta, standard facet, regression fence, fit walk, prover, design review, lens, defect, recommendation, confidence read, declared-laws home, milestone gate, lane, lane branch, non-goal, success measure).

## Part 3 — atomic-claim coverage

Every behavioural claim of the source, in source order by its bold-lead rule, mapped to the criterion (or criteria) that now carries it. "R7.4" means Requirement 7, criterion 4.

### `#### Doors, kinds, and craft` (source lines 277–374)

| # | Source claim | Criterion |
|---|---|---|
| 1 | A critical bug lands before everything, heading the waiting-bug line; only the bug door preempts the in-work lane; the change is recorded. | R1.1, R1.2 |
| 2 | A critical non-bug heads the queue at the pen-holder's next pen-stage boundary and never preempts the rolling lane; the bound is echoed at intake so the human can re-door it a bug; priority stays the human's. | R2.1, R2.2, R2.3 |
| 3 | A small wish may be promoted ahead of larger queued wishes, marked in its row; after one promoted landing the queue head goes next. | R3.1, R3.2 |
| 4 | An inbox wish is registered at arrival; a file's date never competes with a spoken timestamp; arrival ties resolve by row order; a sweep registers in filename-sorted order. | R3.3, R3.4 |
| 5 | The door is named before any code by fixed rules, not personal judgment; the intake line states size, priority, and door; a too-big wish is renegotiated in scope, never time. | R4.1, R4.2 |
| 6 | The five tripwires and the ordered procedure decide feature / bug / refactor / docs-only / skip; a reworded spec rule routes feature-or-bug not docs-only. | R4.3, R4.4, R4.5, R4.6 |
| 7 | The tripwire verdict outranks a casual label; a re-doored wish records it in the intake line. | R4.7 |
| 8 | Queue-cutting is bug-door-only, so a re-doored wish gets no preemption; the human may raise priority; no word lets a feature skip the spec step. | R5.1 |
| 9 | The door is re-checked mid-work when work is about to create a surface or state its door does not grant; the re-doored wish keeps its lane and re-enters in place, no re-queue, no parking. | R5.2 |
| 10 | A mid-work re-door that creates a surface re-runs the independence edges; a new edge pulls the lane back to serial and the board says so. | R5.3, R5.4 |
| 11 | The bug and skip doors carry the spec-backed-literal tripwire; a yes lands docs and test in the same session; the tripwire reads the edit's content; the diff size grants no exemption. | R6.1, R6.2 |
| 12 | Every request gets a three-source impact read (spec, architecture, code) at intake, producing one named footprint; the footprint is spoken in the echo and written in the row's footprint note. | R7.1, R7.2 |
| 13 | The footprint composes with the door, never promoting a feature past the spec step nor demoting the door; each footprint sizes the reach — cross-cutting opens the full pipeline, single-module scopes to the module, presentation-only takes the lightest road. | R7.3, R7.4 |
| 14 | Source disagreement is named and routed to its owner (bug row / spec fix / restructure row), not silently resolved; the read tells whether an artifact already settles a question so the only fork heard is genuinely open. | R7.5, R7.6 |
| 15 | The footprint re-classifies mid-work when an edit reaches past its layer, the landing report recording held or re-classified; repeated cross-cuts on one module pair signal a boundary move through the architecture step. | R7.7, R7.8 |
| 16 | A landed feature-or-refactor row carries its footprint note; a suite check reds a landed row missing it; the duty binds forward from the impact-station's own arrival. | R8.1, R8.2, R8.3 |
| 17 | A request enters at the highest document whose sentences must change; a tripped technical request lifts to the spec at the door. | R9.1, R9.2 |
| 18 | The door set is closed — each request-kind routes to its own entry, an unmatched request becomes one plain question, and a held item that cannot name its human-only fact is the same finding. | R9.3, R9.4 |
| 19 | On divergence the spec defines correct: the divergence is named and routed; a wrong product is fixed to the spec. | R10.1, R10.2 |
| 20 | A silent spec is completed with a pinned test and reported as a default unless correctness is itself open; a confirmed-wrong spec changes only on the human's understood word; the spec is never silently rewritten. | R10.3, R10.4 |
| 21 | The intake line names the work-kind (product / infra / skill / prose), one kind per wish; a two-kind wish splits; an uncallable kind is asked. | R11.1, R11.2 |
| 22 | A single-kind host records a default; a multi-kind host records none; the vocabulary is curated by incident and re-justified at milestones; a pre-axis row owes no retroactive kind. | R11.3, R11.4, R11.5 |
| 23 | A duty binds forward from the first landing after its clause; what landed stays; a pre-clause item carries it on next move; a predating project brings it up as a landing; each such duty cites this one law; a bare binds-forward cite is a net's finding. | R12.1, R12.2, R12.3, R12.4 |
| 24 | A skill-kind landing's verify runs the skill-creator review, findings folded or rejected by name; the walk fires on every skill-kind landing; earlier skills ride the milestone gate. | R13.1, R13.2 |
| 25 | The kind scales each step's form, never whether the pipeline runs; each step applied-or-stood-down by name at landing; an open kind scales nothing down; no kind changes the door law, the mandatory delta sentences, or ask-at-intake. | R14.1, R14.2, R14.3, R14.4 |
| 26 | Each step is worked wearing its craft's head, judged by that craft; the craft follows the kind. | R15.1, R15.2, R15.3 |

### `#### Specifying and building a feature` (source lines 375–507)

| # | Source claim | Criterion |
|---|---|---|
| 27 | A feature-doored wish's spec-delta walks the standard-facet sweep — viewport bands, touch, empty/error/loading, accessibility, performance, hierarchy, two windows, missing source — the list homed in spec-author. | R16.1, R16.2 |
| 28 | The sweep scopes to visible surfaces (a surface-less feature satisfies with one explicit sentence); a mid-work re-door walks it before resuming; a prototype is not swept; the list is a curated closed set naming every member. | R16.3, R16.4, R16.5 |
| 29 | Every facet ends decided or `[default]`-tagged, deriving the test row either way; no per-facet ping and no confirm since silence is consent; a facet with no sentence is a prover-flagged defect. | R17.1, R17.2, R17.3 |
| 30 | On a live surface a default is read from shipped truth and reconciled; the sweep authors sentences while the axis rule composes them across views. | R17.4, R17.5 |
| 31 | Cross-cutting laws live in one declared-laws home; each surface states its clause or dated exemption; the prover's station demands the clause per item; this pack's three laws each name a mechanical gate; a missing net is a broken invariant. | R18.1, R18.2, R18.3, R18.4 |
| 32 | Every declared law names one of three nets by where its violation can be decided; the net is recorded in the declared-laws home; a watch-level law names the design review with a dated reason; declaration promotes a property to a blocking net, the architecture's one-owner check the backstop. | R19.1, R19.2, R19.3, R19.4 |
| 33 | The four controls are one routing principle; each thing routes to its governing home; a homeless thing is the finding; declaration is the lever; each control is verified adjacent to the thing it audits. | R20.1, R20.2, R20.3, R20.4 |
| 34 | A feature-doored wish walks the kind-scaled fit walk; it interrogates the feature not the person and derives from spec and shipped truth; trivial holes are closed and written, the rest decided/`[default]`-tagged, only taste calls batched; the prover gains the feature-fit mode; the walk binds forward. | R21.1, R21.2, R21.3, R21.4 |
| 35 | Every conditionally-entered face states its re-entry path or names its one-way; trigger wording owes a return sentence; the prover reads the entry-symmetry lens. | R22.1, R22.2 |
| 36 | Product-kind verify walks the visit (first, return, other-door, where-am-I, exits) and runs the feel pass against the prototype, findings becoming rows or red, in the medium's own form. | R23.1, R23.2, R23.3 |
| 37 | The prover labels each finding a defect (blocks until folded) or a recommendation (queues for a taste call), derivable from its ground; the gate folds every defect and queues every recommendation; a delta-scoped gate queues a pre-existing outside defect. | R24.1, R24.2, R24.3, R24.4 |
| 38 | The design review reads a proven spec, builds its own element inventory, writes one action sentence each, proposes same-kind groups and checks parity, stays silent where unclear; names two objects per finding, blocks nothing, writes a dated record; a confirmed kind becomes a class sentence, a difference a decided sentence; the inventory never enters the surface list; it runs in the kind's form or stands down by name. | R25.1, R25.2, R25.3, R25.4, R25.5 |
| 39 | A gesture/overlay/motion spec triggers the motion-parity lens naming three same-kind groups (entry mirrors exit, every object type alike, every position alike); each finding recommends or asks, held by the uniformity check once declared. | R26.1, R26.2, R26.3 |
| 40 | A feature delta adding a second member of a kind draws the scoped design review at intake; a delta with no sibling holds the stand-down and records the no; this closes the second-sibling window. | R27.1, R27.2, R27.3 |
| 41 | A re-enterable surface triggers the entry-state lens demanding entry position and reset-or-resume; a spec leaving them blank raises an open question before code; the prover's state-coverage holds it once declared. | R28.1, R28.2, R28.3 |
| 42 | Every stated transition carries a payload lens enumerating perceived parameters and demanding each; each unstated one is an open question; the motion-parity and entry-state lenses are instances this parent generalizes. | R29.1, R29.2, R29.3 |
| 43 | A surface add re-verifies the document's quantified claims (enumerations and universals) against the grown set, via the cross-link mode's mandatory whole-document step, firing on every member add. | R30.1, R30.2 |
| 44 | A full prover pass owes a coverage record: each mandatory sweep owes one verdict (hit/clean/not-applicable-with-reason), rendered as a surface-by-sweep table, imaginative probes discretionary; a missing verdict reads as skipped. | R31.1, R31.2, R31.3 |
| 45 | Every review pass writes a dated record of one shared shape naming skill and version with a per-finding disposition column and a same-day suffix; the feature-fit record lands in the prover's home; the design review alone carries a held-ask; the verify audit rides the landing record; the class binds forward. | R32.1, R32.2, R32.3, R32.4 |
| 46 | Each design review finding carries a confidence read; confident queues as a recommendation, a strong likely rides as one batched question with both objects; at most three per pass strongest first; the class sentence lands only on the human's word; an unanswered question is held and not re-fired. | R33.1, R33.2, R33.3, R33.4, R33.5 |
| 47 | The prover and design review loop, advanced only by a human-accepted declaration; the loop rests naming why (converges/waits/stands down); capped at three progressing rounds by default (host-settable); at the cap it surfaces unsettled groupings without holding the landing. | R34.1, R34.2, R34.3, R34.4, R34.5 |
| 48 | A taste call made without asking is written with its `[default]` tag and told in the landing report with an example, marked tweakable; no confirm, no re-ask, findable forever. | R35.1, R35.2 |
| 49 | A tunable knob is set to a default (cheaper/faster where quality allows), tagged, and told with what it trades; no re-ask owed; the agent moves every task it can and reserves real questions; where granted, it ships to prod on its own certification. | R36.1, R36.2, R36.3, R36.4 |
| 50 | A taste-heavy deliverable builds smallest-first — the cheapest judgeable sample judged before the full build spends — the agent's own discipline distinct from the human's show-me-first entry. | R37.1, R37.2 |
| 51 | A rejected artifact reopens its source (spec/card/brief), corrected first and rebuilt; line-patching an unchanged source is the banned five-round trap. | R38.1, R38.2 |
| 52 | Touching a live surface opens the spec-delta with regression fences citing existing clauses; a fence earns no matrix row and discharges through the clause's never-side proven by the full suite; a fenceless promise is reconciled and surfaced; fences are named by anchor in the row; fence-authoring is feature-door, bug/refactor inherit the catching, a prototype fences nothing. | R39.1, R39.2, R39.3, R39.4 |
| 53 | A feature closes with a non-goal sentence and a success measure, both always written; a narrowing non-goal rides the batched report; the success measure carries a number where one exists and derives no matrix row; both bind forward and a prototype writes neither. | R40.1, R40.2, R40.3, R40.4 |

### `#### Parallel lanes, one pen` (source lines 508–620)

| # | Source claim | Criterion |
|---|---|---|
| 54 | Intake is parallel, integration serial: one landing per repo under one pen (the right to write the shared truth), one lane at a time. | R41.1 |
| 55 | Claiming is an atomic committed flip then a re-check under the fence; the later claimant backs off; "later" is a total order by git ancestry, ties by session identity; the flip records identity so exactly one backs off. | R41.2, R41.3, R41.4 |
| 56 | Foreign hands never share the pen; workers overlap on disjoint files or an isolated tree with the fence armed; a new wish waits unless a bug preempts. | R41.5 |
| 57 | A pending question proceeds on the recommended option, staying open; no silent micro-decision — every choice asked or recorded and surfaced in the batched report; every landing cites its wish row. | R42.1, R42.2, R42.3 |
| 58 | Each session mints a stable identity before its first act, recorded in its checkpoint (harness id or start-time-plus-worktree-plus-nonce); the pen tie-break orders on it and the inbox source-mark reuses it. | R43.1, R43.2, R43.3 |
| 59 | One session rolls up to the profile cap (default three) of pairwise-independent lanes the senior names aloud; one more only on the human's word; read-only analysis never counts; penless stages overlap; pen-stages serialize. | R44.1, R44.2, R44.3, R44.4 |
| 60 | The board shows every train with waiting lanes naming whom they wait behind; cross-lane questions ride one page; a bug takes the pen at the current pen-stage end; a milestone runs one train only, others held and resumed in landing order. | R44.5, R44.6, R44.7 |
| 61 | The milestone gate is one indivisible pen-stage a bug waits out; a landing commit carries exactly one row's delta on a clean tree; after a landing every rolling lane re-fences and re-gates, landed-first winning. | R45.1, R45.2, R45.3 |
| 62 | Lanes are picked by a dependency graph (edge = true dependency or same-section collision); co-location draws no edge; the graph opens a pairwise-independent set, serializes edges, pre-rolls integration-only collisions; tiny rows ride serial; false-serialization is a senior read. | R46.1, R46.2, R46.3, R46.4 |
| 63 | A lane's isolated copy is a git worktree holding its own branch; a worker lane takes one through the ungated worktree isolation option naming the branch; overlapping lanes default to isolation reaching the shared tree only under the pen. | R47.1, R47.2, R47.3 |
| 64 | The claim's flip commits to main under the pen and the branch is cut from it, named `lane/<row>-<slug>`; the claim lands on main so ancestry ordering holds. | R48.1, R48.2 |
| 65 | Holding the pen is the sole right to move main, a lane's branch penless; git refuses another worktree's checkout/force/push with three named edges. | R49.1, R49.2 |
| 66 | The pen still keeps every shared document (two branch deltas would each prove against a moving spec); the shared tree stays clean, making the one-row-commit precondition structural. | R49.3, R49.4 |
| 67 | A lane lands by taking the pen, rebasing onto main's tip, gating on the rebased tree, and advancing main with no merge commit; a merge-base check reds an un-rebased lane. | R50.1, R50.2 |
| 68 | Teardown removes a landed lane's branch and worktree, keeps both on a parked lane, refuses a worktree with uncommitted work (a finding), and the config-health gate reds a lane worktree or branch with no open row. | R50.3, R50.4 |
| 69 | A textual conflict halts the rebase for the lane to resolve and re-gate; a semantic one meets the two nets (pen keeps documents together, the full suite reads diverging code); a semantic conflict surviving a green suite is a matrix gap routed to the matrix's home. | R51.1, R51.2, R51.3 |
| 70 | The isolation default and the worktree tool agree through one vendored line citing the law's write-set condition, scoped and versioned per host and carried by catch-up; the line records the host owner's word; the session lane stays shut until the pack owner's word; the adoption gate reds a missing line; a worker lane needs none. | R52.1, R52.2, R52.3, R52.4, R52.5 |
| 71 | The cap holds at three because the branch road touches none of its three costs (pen-wait, rebase-and-re-gate, review attention); the pack proceeds on the recommendation while the measurement is owed. | R53.1, R53.2 |
| 72 | The lanes law's cap/board/independence scope one session; the pen's arbitration fires across sessions; a second session on one repo takes its own worktree and branch under the stated road with no new law. | R53.3, R53.4 |
| 73 | Git's two machines run today with known edges; the pack's four build-half machines (merge-base, config-health, adoption gate, board lane-count) are mechanical gates under the net-routing law; the road's fences and non-goals hold. | R54.1, R54.2, R54.3, R54.4, R54.5 |
| 74 | Opening a lane is a performed act (flip on main, cut the branch and worktree, delegate to a worker) run when the graph shows independent rows and lanes stand free; `scripts/open-lane.sh` reads the cap, runs the fence, carries the claim commit alone. | R55.1, R55.2 |
| 75 | Going single-file while lanes stand free is a recorded serial-by-the-graph choice naming its standing reason; the recorded-reason duty is a discipline not a gate (torn-down branches leave no signal), the cap refusal the one mechanical guard. | R55.3, R55.4 |
| 76 | Deferred rows are re-scanned at every queue-take, a fired trigger returning the row to the runnable head; queue-take and milestone read the same triggers by the same rule; the trigger vocabulary stays free-form. | R56.1, R56.2 |
| 77 | A resuming session re-reads the code a deferred item touches and re-derives its current state before designing; it fires with the deferral re-test, both owed; it is a discipline (no committed artifact to gate). | R57.1, R57.2, R57.3 |
| 78 | The queue has a far tier (far status, no trigger, no plan) told apart from deferred both ways; the runnable report stands it down by name in one line; a report naming a far row among runnable work reds the report-shape check on the suite. | R58.1, R58.2, R58.3, R58.4 |
| 79 | A deferred row's trigger can be a mechanical one-shot check the queue-take runs; the listener-tripwire fires only on a non-empty socket field; on firing it returns the row, riding the queue-take scan and suite with no push-gate letter. | R59.1, R59.2, R59.3 |
| 80 | A wish can end declined, deferred, or superseded (a superseded row pointing to its absorber); a declined absorber lists its absorbed rows, each declined by name or returned to the queue; a superseded wish never dies by pointer. | R60.1, R60.2, R60.3 |
| 81 | What the wishes grow is the spec, the living statement of what the product is, one surface one name everywhere. | R61.1 |

### Coverage result

81 source bold-rules, covering all 61 requirements and 223 criteria. History stripped by law 6 — dates, named-incident narratives, row-number provenance, and recorded-word attributions ("the owner's word 2026-07-17", "recorded live 2026-07-12", "his report ~15:59", the probe-repo verification dates) — carries no behavioural claim and is dropped to the journal. Two source holes are recorded as `[GAP]` lines at R3.1 and R46.4 and detailed in `GAPS.md`. Three source blocks state what the delta deliberately does **not** do (the branch road's fences, its non-goals, and the cap's held-measurement recommendation); the fences and non-goals are carried in R54.5 as one criterion and in the requirement contexts, and the held recommendation as R53.2, since the format keeps a deliberate not-doing as a positive criterion or a context statement. No behavioural `shall`-claim of the source is left uncovered.

### The mechanical zero-drop check

`cited-set` (132 codes from lines 277–620) minus `present-set` (codes anchored on criteria in `section.md`) is **empty**. Verdict: zero drop.

### Prover MUST-FIX wave (row 445 audit, F2) — declared sharpen

- **Glossary entry `cross-link mode`**: the pooled entry defined the mode as "the prover's whole-document pass", the opposite of R30's own Context (assembled R66: "A seam-scoped pass misses these, so the cross-link mode carries one mandatory whole-document step"). Audit finding F2. The entry is rewritten to the requirement's own meaning: the prover's focused pass at a surface add, scoped to the new surface's seams, carrying one mandatory whole-document step — the enumeration-and-quantifier re-verify. No criterion changed.

### Final restoration wave (re-pin sweep) — declared additions

- **R44.8 (held-for-milestone state).** Restores T-18's distinct held-for-milestone lane state, named apart from bug-parked because nothing failed. Owed by `test_traceability::TestSmallDesignHoles::test_176`. [T-18, M-1]
- **R40.5 `[target]` (INV-21), R49.5 `[target]` (INV-198), R50.5 `[target]` (INV-199), R52.6 `[target]` (INV-201).** The success-measure reading machinery, the config-health primary-tree check, the merge-base/stale-lane checks, and the adoption-gate build leg — each a promised leg whose retired Formal-index `[target]` mark is restored as an own-line marker under a criterion citing its anchor. No new code (all four anchors pre-existed elsewhere in the unit). Owed by `TestTargetOwnership`.
