# MAPPING — codes, consumed index rows, and atomic-claim coverage

This file proves the rewrite of `### Composing across axes` (PRODUCT_SPEC.md lines 2031–2092, the composition-lens essay and the document-provenance subsection inside `## Reference`) dropped nothing. Part 1 maps every code the source cites to its new home. Part 2 states which codes carried a consumed Formal-index row. Part 3 maps every behavioural claim of the source to the criterion that now carries it.

`Rn` names Requirement n in `section.md`; `Rn.k` means Requirement n, criterion k. A code in several requirements is anchored in each. Zero codes are dropped: all 57 cited codes appear in `section.md`, and no extra code is present — verified mechanically (`comm` of the source's cited set against `section.md`'s present set is empty in both directions).

## Part 1 — every cited code → its new home

The `Owned` column marks the codes whose Formal-index home is `Composing across axes` — this section is their prose home, and this rewrite converts them in full. The rest are cross-references: a rule owned by another section that this essay leans on, preserved as a trailing anchor with its behaviour left in its home section.

| Code | New home | Index row consumed here? |
|---|---|:--:|
| INV-11 | R13 | no |
| INV-14 | R16 | no |
| INV-18 | R2, R4, R6, R7, R8 | no |
| INV-30 | R4, R6, R8 | no |
| INV-31 | R2, R4, R6, R8 | no |
| INV-36 | R8 | no |
| INV-41 | R7 | no |
| INV-50 | R5 | no |
| INV-72 | R1, R2, R3, R4, R5, R6, R8 | yes |
| INV-74 | R5 | no |
| INV-91 | R17 | no |
| INV-97 | R3, R11, R12 | no |
| INV-98 | R11 | no |
| INV-108 | R12 | no |
| INV-124 | R3 | no |
| INV-125 | R3, R6, R7, R9, R10 | yes |
| INV-126 | R4, R6, R7, R9 | yes |
| INV-127 | R5 | yes |
| INV-135 | R8 | no |
| INV-136 | R6, R7, R8, R9, R10 | no |
| INV-138 | R6, R7, R8, R9 | yes |
| INV-139 | R10 | no |
| INV-141 | R6, R17 | no |
| INV-150 | R6 | no |
| INV-157 | R15 | no |
| INV-158 | R10 | no |
| INV-159 | R5, R8, R9, R10, R18 | no |
| INV-163 | R3, R10 | yes |
| INV-164 | R13, R15 | no |
| INV-172 | R11, R15, R18 | yes |
| INV-173 | R12, R18 | yes |
| INV-174 | R13 | no |
| INV-175 | R13, R14, R18 | yes |
| INV-176 | R15 | yes |
| INV-177 | R18 | no |
| INV-178 | R16, R17, R18 | yes |
| INV-180 | R18 | yes |
| INV-214 | R9 | no |
| INV-217 | R17 | yes |
| INV-226 | R1, R6, R7, R8, R9 | yes |
| INV-243 | R14, R18 | yes |
| INV-244 | R1, R8, R9 | yes |
| INV-248 | R9 | yes |
| A-3 | R19 | no |
| A-7 | R11, R18 | no |
| A-10 | R8 | no |
| A-11 | R15 | no |
| C-1 | R1, R2, R8, R19 | yes |
| D-4 | R18 | no |
| E-10 | R3 | no |
| E-14 | R2 | no |
| E-23 | R18 | no |
| E-25 | R18 | no |
| E-26 | R10 | no |
| M-6 | R2 | no |
| M-7 | R18 | no |
| T-13 | R6 | no |

## Part 2 — consumed Formal-index rows

The section cites 57 distinct codes. **18 carry an index row whose home is `Composing across axes`**, and this rewrite consumes each of those rows in full: `C-1`, `INV-72`, `INV-125`, `INV-126`, `INV-127`, `INV-138`, `INV-163`, `INV-172`, `INV-173`, `INV-175`, `INV-176`, `INV-178`, `INV-180`, `INV-217`, `INV-226`, `INV-243`, `INV-244`, `INV-248`. Each row's facts now live at the requirement named in Part 1. Several of these rows are among the longest in the index (`INV-244` and `INV-248` carry two dense description columns), and each was read for facts present only in the index and absent from the prose — for example the manifest-merge-across-installer-runs fact in `INV-172`'s row (now R11.2) and the class-membership map in `INV-180`'s row (now R18.2–R18.5).

The other **39 codes are pure cross-references**: their Formal-index home is another section, and this essay leans on them without restating their rule. Their rows are consumed by their home units, not here. They are: A-3 (Adoption step 3), A-7, A-10, A-11, D-4, E-10, E-14, E-23, E-25, E-26, M-6, M-7, T-13, INV-11, INV-14, INV-18, INV-30, INV-31, INV-36, INV-41, INV-50, INV-74, INV-91, INV-97, INV-98, INV-108, INV-124, INV-135, INV-136, INV-139, INV-141, INV-150, INV-157, INV-158, INV-159, INV-164, INV-174, INV-177, INV-214.

**A note on the composition floor and the provenance axis.** The `C-1` row's own text folds in the enumerated floor axes, the open kind-owed tail, and the document-provenance axis. This rewrite carries the floor into R1, the kind-owed tail into R1/R8, and the provenance axis into R19; `A-3` at R19 is the cross-reference to the adoption reconciliation rule that the provenance value `re-engineered` depends on.

**Dual-homing note.** Six owned codes are also cited in already-converted units (`INV-72`, `INV-125`, `INV-163`, `INV-226` in `build-loop-b`/`build-loop-c`; `INV-138` in `build-loop-b`; `INV-217` in `agents-together`/`rules-and-who-applies`). In every such case the other unit cites the code as a cross-reference; the rule's prose home is here, per the Formal index. The seven codes the stage-3 census flagged as single-homed — INV-126, INV-127, INV-138 (the gated-behaviour and viewport-quantifier clause), INV-163 (the root discriminator sentence), INV-180, INV-244, INV-248 — plus INV-172 and INV-243 (found in no other unit's `mapping.md` at all) have no other converted home; without this unit their rules would vanish from the new document.

**Cross-section glossary note.** Domain nouns owned by other sections — surface registry, prover, design review, facet, standard facet, lens, project kind, project layers, design principle, proof kinds, host, pack, guardrail, suite, push gate, net, ratchet manifest, migration chapter, catch-up walk, installer, snapshot, seat — are used with their existing meanings and get no new entry here. This section's `## Glossary additions` block adds only the five nouns it introduces: stateful surface, composition axis, input-capability axis, config-health check, document provenance.

## Part 3 — atomic-claim coverage

Every behavioural claim of the source, in source order, mapped to the criterion (or criteria) that now carries it.

### The composition floor and the axis-set shape (C-1, INV-244, INV-226)

| # | Source claim | Criterion |
|---|---|---|
| 1 | A stateful surface is a part of a host project that holds state — a screen, panel, or saved file the user can change and find again later. | Glossary (stateful surface); R1 context |
| 2 | Every stateful surface is reviewed against a kind-independent floor of axes: view, mode, user tier, viewport, close-and-reopen, concurrency. | R1.1 |
| 3 | The floor's last axis is every other live surface present at the same time — a sibling on the screen or the surface one step before or after in the flow, whether or not it holds state. | R1.2 |
| 4 | For each other live surface, the spec says what this surface does while that one is present — hold, clear, or hand off; the unwritten seam is the classic stranding bug. | R1.3 (stranding example in R1 context) |
| 5 | The axis set is a hybrid that declares its shape: an enumerated floor every surface answers plus an open kind-owed tail whose members a kind names one at a time. | R1.4 |
| 6 | A surface's spec is complete once every floor axis and every kind-owed axis has an answer. | R1.5 |

### The prover hunts the unwritten seam (INV-72)

| # | Source claim | Criterion |
|---|---|---|
| 7 | The prover reads the whole axis list actively, deriving each surface's reachable situations for itself rather than trusting the author. | R2.1 |
| 8 | For each situation it asks whether the surface's behaviour is stated there; a reachable situation with a blank answer is a finding, the same class as a fact no node owns. | R2.2 |
| 9 | The hunt rides both the whole-spec pass and the surface-add pass. | R2.3 |
| 10 | It reports the missing seam and leaves the sentence to the author, who writes it as a composition invariant, decided or default-tagged; the prover invents no answer and asks the human for nothing. | R2.4 |

### A cross-surface policy at the class level (INV-125)

| # | Source claim | Criterion |
|---|---|---|
| 11 | A decision governing a kind that recurs across sibling surfaces or elements is stated once at the surface-class level, naming the class and enumerating the surfaces. | R3.1 |
| 12 | A policy written for one surface while siblings of the same kind exist is a spec defect; consistency of this kind is itself an invariant; it is the preventive twin of the class hunt. | R3.2 |
| 13 | The prover enumerates the surfaces of that kind from the surface registry and flags any the clause misses, the same finding class as a blank-answer situation. | R3.3 |
| 14 | For a rendered product, the completeness guardrail asserts a one-surface policy across every registered sibling root, red until all covered. | R3.4 |
| 15 | The spec-class rule is the root; the pack ships the rule and the prover lens and leaves the page-wide assertion to the products it serves (the ship-the-shape pole of the pack-to-host split). | R3.5 |
| 16 | The trigger also fires on a kind-general principle written in prose inside one member's section; the author lifts it to a class clause or scopes it to the one member by a decided sentence. | R3.6 |

### Both directions of a paired state change (INV-126)

| # | Source claim | Criterion |
|---|---|---|
| 17 | A crafted transition in one direction of an opposite pair is a decision about the pair, so the other direction is stated too; the default is symmetry unless a reason is written. | R4.1 |
| 18 | The author writes the pair's answer as a spec sentence — mirror, a named shorter exit, or deliberately instant — decided or default-tagged on the facet sweep. | R4.2 |
| 19 | Where the author cannot judge the pair's feel, the question is surfaced to the human. | R4.3 |
| 20 | The prover flags a paired change with one direction described and the opposite unstated, the same blank-answer class. | R4.4 |
| 21 | The reversibility half: an opening gesture with a natural inverse offers that inverse as a way to close, or a decided sentence says why not; a missing inverse with no sentence is a finding the prover blocks. | R4.5, R4.6 |
| 22 | The magnitude half: where the pair rides a continuous reversible quantity, the spec states whether the inverse asks the same magnitude, symmetric or a named asymmetry; a missing magnitude sentence is the same finding. | R4.7 |

### Each scenario states its entry and exit (INV-127)

| # | Source claim | Criterion |
|---|---|---|
| 23 | A person-facing scenario states its entry (from where the walk arrives and what must hold) and its exit (where the person lands and what it leaves true). | R5.1 |
| 24 | This lifts the per-operation precondition and postcondition lenses to the scenario level, kin of the entry-symmetry lens and the runtime flow walks. | R5.2 |
| 25 | The prover flags a flow whose entry or exit is unstated, the same blank-answer class. | R5.3 |
| 26 | The duty binds forward: a new scenario states its edges from the first draft, and an existing scenario's unstated edge is a finding, not a lane block. | R5.4 |
| 27 | A trivially-none edge is stated as such in one short clause. | R5.5 |

### A gated behaviour and a scoped guarantee (INV-138)

| # | Source claim | Criterion |
|---|---|---|
| 28 | A behaviour gated on a quantity running on a line states both ends of the live range; a phrase naming one point and leaving an interval silent is incomplete until bounded both sides. | R6.1 |
| 29 | An async-filled slot names the pending, arrived, and failed faces of the wait, with a visible pending face wherever the slot reserves a place. | R6.2 |
| 30 | The pending face is that slot's loading state, sharpening the standard empty/error/loading facets for a reserved slot. | R6.3 |
| 31 | The prover carries a completeness sweep; the author writes each edge decided or default-tagged, surfacing timing to the human where only he can judge. | R6.4 |
| 32 | A guarantee scoped to a named part of its domain owes the same completeness across the whole domain, each remaining part decided or default-tagged. | R6.5 |
| 33 | A guarantee speaking for one part while the remainder is silent is the same unwritten-seam class. | R6.6 |
| 34 | Every layout guarantee names its viewport quantifier — every viewport or a named band — leaving other bands silent until stated, the short-viewport band among them. | R6.7 |
| 35 | An undeclared same-kind group is reached by the design review's group pass and held by the prover once a part-uniform guarantee is declared. | R6.8 |
| 36 | This is the range-and-lifecycle member of the composition-lens family, its set open-ended, naming the viewport as its worked instance. | R6.9 |

### Enumerate-or-ride declaration (INV-226)

| # | Source claim | Criterion |
|---|---|---|
| 37 | A general law over concrete instances makes one choice: name every member, or let an instance ride the general duty with no name. | R7.1 |
| 38 | A closed enumerable set (even one growing by named incident) names every member — the per-kind budgets name each project kind, the facet list names each facet. | R7.2 |
| 39 | An open-ended set names only its worked instances and leaves the remainder to the general duty, the scoped-guarantee law naming the viewport alone. | R7.3 |
| 40 | A law reaching the choice by feel is the defect; the member set decides; a borderline set states which side it took and why. | R7.4 |
| 41 | This is the declaration member of the composition-lens family. | R7.5 |

### A surface's composition axes are the kind's owed set (INV-244)

| # | Source claim | Criterion |
|---|---|---|
| 42 | A surface's axes are the floor plus the further axes its kind owes; the author reads them from the kind before composing, as the kind carries a node scaffold and design principles. | R8.1 |
| 43 | A visual kind (`static site`, `fullstack`) owes every visitor-facing surface an open axis set whose first named member is input-capability, beyond the viewport the floor carries. | R8.2 |
| 44 | The sibling axes (browser engine, locale/text direction, connection reach, first-vs-returning, accessibility, measurement reach) ride the per-kind duty as their own increments. | R8.3 |
| 45 | Every kind names its owed axis set as a mandatory founding declaration, like layers and proofs. | R8.4 |
| 46 | A kind may name none beyond the floor as an explicit stated decision, the empty case the design-principles set legitimises. | R8.5 |
| 47 | A kind recorded with no axis-set declaration is flagged, like a kind with no layers or proofs. | R8.6 |
| 48 | A non-visual backend kind owes its own non-empty set (load, version, tenant), disproving a conditional reading. | R8.7 |
| 49 | The gap between an owed axis and the code's coverage is a finding of the blank-answer class. | R8.8 |
| 50 | The author states the gap as a spec sentence, decided or default-tagged. | R8.9 |
| 51 | An owed axis is covered only once the author composes and tests the surface against each elementary value; the sentence half and the values half split one dimension by time. | R8.10 |
| 52 | An axis carries its own value space, a domain the same completeness reaches; input-capability values are combinable capabilities that co-occur on one device (touch, fine pointer, hover, keyboard). | R8.11 |
| 53 | The two poles (touch, fine pointer) are owed and answered up front; the co-occurrence answer rides with the deferred forcing step. | R8.12 (+ GAP: co-occurrence interim value) |
| 54 | Refinement values (stylus, keyboard-only, advanced-user device) are the human's taste, entering later, decided or default-tagged. | R8.13 |
| 55 | The rule binds forward: a surface authored after it reads its axes from the first draft; a predating surface carries the read at its next touching landing. | R8.14 |

### Delivery separability (INV-248)

| # | Source claim | Criterion |
|---|---|---|
| 56 | The dual of the composition law reads whether the delivered artifact divides along an owed axis or arrives as one piece. | R9.1 |
| 57 | An axis that adds runtime code carries one of two decided sentences. | R9.2 |
| 58 | A monolith named for a stated architectural reason (one never-torn-down bundle, a no-server delivery, a too-small payload) is a settled answer. | R9.3 (+ GAP: payload-size measure) |
| 59 | An axis that names the delivery road it owes (platform split, lazy load, per-value chunk) is carried by a later row. | R9.4 |
| 60 | The finding is the third case: an axis adding runtime code with neither sentence, shipping whole unexamined, byte weight its symptom. | R9.5 |
| 61 | The lens reaches any owed axis, each only where covering it ships runtime code (a viewport by media query or a locale by logical property draws no delivery question). | R9.6 |
| 62 | It stays a senior read the prover carries, not a gate, since a named-reason monolith is lawful. | R9.7 |
| 63 | The prover carries a discovery habit: for a lens it applies, it may ask whether that lens's dual bites, surfacing a missing lens and never a rule that every lens ship paired. | R9.8 |
| 64 | This is the delivery-separability member of the composition-lens family, binding forward. | R9.9 |

### Where a capability's body lives — the pack-to-host split (INV-163)

| # | Source claim | Criterion |
|---|---|---|
| 65 | Where a body lives is placed by one question — can the pack ship a single identical body every host runs — resolving where base rule 4's one home sits. | R10.1 |
| 66 | A body the pack can ship identically centralizes to one pack home adopted by a package update, so a fix lands once and no divergent copy forms (the browser harness the centralize pole). | R10.2 |
| 67 | A host-specific body (names host surfaces, holds host data, reads host artifacts) ships as a shape each host fills. | R10.3 |
| 68 | Ship-the-shape sites: cross-surface uniformity, design principles with the pixel projection left to the project, the removal-list scanner. | R10.4 |
| 69 | A generic seam grown in a host instance lifts to the pack; the boundary moves toward centralization as a body proves uniform. | R10.5 |
| 70 | Binds forward: a new host-specific capability states its pole from the first landing; predating bodies stand as cited. | R10.6 |

### Adoption wires the ratchet gates (INV-172)

| # | Source claim | Criterion |
|---|---|---|
| 71 | The pack vendors the style lint, redundancy precheck, freeze tool, and shared library, each carrying a source pin (pack version + content hash) an update check reads. | R11.1 |
| 72 | The manifest is merged across installer runs so a prior install's keys survive a later run of the other kit. | R11.2 |
| 73 | The kit seeds the debt caps at the host's current measured size, so the gate is green at once and ratchets down, demanding no re-compaction. | R11.3 |
| 74 | A generated guard test pins the seeded caps: lowering the cap file is ordinary, raising it edits the test. | R11.4 |
| 75 | The installer wires the gates into the push gate at a safe anchor, verifies reachability, follows the four-checks shipping contract, and proves itself red-first. | R11.5 |
| 76 | A re-run that finds a block stranded past a terminating exit moves it back to the safe anchor. | R11.6 |

### The pack's hooks: one home, universal against personal (INV-173)

| # | Source claim | Criterion |
|---|---|---|
| 77 | A pack hook lives as source in `hooks/` reached through an installer; a hook living only in an installed location is a defect. | R12.1 |
| 78 | The set splits universal (a pack law, ships) against personal (one human's patterns, in the personal layer). | R12.2 |
| 79 | The canonical universal hook reads the personal patterns as an overlay the personal layer owns, so one hook serves both. | R12.3 |
| 80 | Adoption and the setup walk install the universal set by the agent's own hand, said aloud. | R12.4 |
| 81 | A scan hook skips quoted or fenced text, since it names a pattern rather than using it. | R12.5 |

### The installed gate is the source gate (INV-175)

| # | Source claim | Criterion |
|---|---|---|
| 82 | A gate lives twice (source and installed copy) and drifts on a skipped install; the config-health check reds a missing or drifted hook, names the fix, runs in the suite and push gate. | R13.1 |
| 83 | It reads the whole hook source directory against the installed set, not a fixed name list, so every shipped hook is covered automatically. | R13.2 |
| 84 | A file living only in the installed set (a personal overlay) has no source and is left alone. | R13.3 |
| 85 | A CI checkout with no installed hooks skips by name. | R13.4 |
| 86 | The commit fence's second arm: a file both staged and holding unstaged edits at commit is a fence stop. | R13.5 |

### The installed skill copy is the source skill (INV-243)

| # | Source claim | Criterion |
|---|---|---|
| 87 | Config-health gains a skill-copy arm that diffs each installed skill against the pack's `skills/` source and reds an un-synced or drifted copy, naming the fix (re-run `sync-skills.sh`). | R14.1 |
| 88 | It reads the whole skill source directory against the installed set, covering every shipped skill and leaving a personal-layer skill with no pack source alone. | R14.2 |
| 89 | A shipped skill's copy is held byte-pristine: the recursive tree diff counts even an extra file inside the directory as drift. | R14.3 |
| 90 | The single top-of-file CI carve-out stands the whole check down on a runner, so the arm needs no skip of its own. | R14.4 |

### A retroactive gate scans the whole tree (INV-176)

| # | Source claim | Criterion |
|---|---|---|
| 91 | A law extracted into a gate scans the entire tracked tree, retroactive by construction, so pre-gate debt is found the day the gate lands (the browser-mute gate the worked example). | R15.1 |
| 92 | An over-big backlog is absorbed by the seeding law, the cap seeded at current size and ratcheting down. | R15.2 |
| 93 | Adoption and a catch-up walk run the current gate set backward over the host's tree. | R15.3 |

### The pack's version is one fact (INV-178)

| # | Source claim | Criterion |
|---|---|---|
| 94 | The root VERSION is the one home; skill frontmatter and in-text base references are stamped copies written by the sync script at each bump, a drifted copy redding a guard test. | R16.1 |
| 95 | A record's version line names the pack version from this law on. | R16.2 |

### A release's number reports its cost (INV-217)

| # | Source claim | Criterion |
|---|---|---|
| 96 | A release's number answers what taking it costs a host in the host's own action. | R17.1 |
| 97 | A patch fixes a machine to hold a stated law, no new capability or changed contract; the host does nothing. | R17.2 |
| 98 | A minor grows what a host may adopt, backward-compatible; the host re-runs its catch-up walk with nothing rewritten. | R17.3 |
| 99 | A major cannot be taken without the host changing what it carries; it ships a dated migration chapter. | R17.4 |
| 100 | The default is a patch, raised only where the release earns it. | R17.5 |
| 101 | The minor-versus-major call is a stated judgment held by no gate, the standing of a design-review finding. | R17.6 |
| 102 | Homes: base rulebook rule 32, build-pipeline's commit-and-show step, and this clause, beside version-is-one-fact. | R17.7 |

### Authored artifacts and installed copies are one class (INV-180)

| # | Source claim | Criterion |
|---|---|---|
| 103 | The pack's authored artifacts and their installed copies are one class, each member naming the net that tells its running copy stale. | R18.1 |
| 104 | Vendored kit scripts name the ratchet manifest's source pin. | R18.2 |
| 105 | Installed hooks and gates name the config-health check. | R18.3 |
| 106 | Stamped version copies name the stamp script and its guard test. | R18.4 |
| 107 | Installed skills name the config-health skill-copy arm, backed by the freshness compare, same-session sync, and daily update proposal. | R18.5 |
| 108 | The class binds forward: a new installable artifact states its own staleness net; members named before the class stand as cited. | R18.6 |

### The document-provenance axis (A-3, C-1)

| # | Source claim | Criterion |
|---|---|---|
| 109 | Adoption adds one axis, document provenance — where a spec claim came from. | R19.1 |
| 110 | A native claim was written fresh under the pack and is trusted from the start. | R19.2 |
| 111 | A re-engineered claim was recovered from pre-adoption documents; it stays unverified until reconciled against real code or removed. | R19.3 |

### Coverage result

111 behavioural claims mapped, covering all 19 requirements. Two source holes are recorded as `[GAP]` lines — the input-capability co-occurrence value (R8.12) and the delivery-separability payload measure (R9.3) — and detailed in `GAPS.md`. Several source items are stated deferrals with a named mechanism rather than holes (the sibling axes, the other kinds' axis sets, the value-space forcing step, the recursive axis-registry sweep); each is carried as a criterion that names its future step, not invented. No behavioural claim of the source is left uncovered, and no criterion carries a claim the source did not make (verified by reading each criterion back against the source paragraph its anchor names).

### Final restoration wave (re-pin sweep) — declared addition

- **R8.15 `[target]` (INV-244).** The axes value-space in-between forcing step and the recursive axis-registry similarity sweep, promised as later increments — retired Formal-index `[target]` mark restored as an own-line marker under a criterion citing INV-244. Owed by `TestTargetOwnership`.
