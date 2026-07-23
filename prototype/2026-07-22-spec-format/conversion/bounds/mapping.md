# MAPPING — codes, consumed index rows, and atomic-claim coverage

This file proves the rewrite of `## What holds the bounds` dropped nothing. Part 1 maps every code the source section cites to its new home. Part 2 states which codes carried a consumed Formal-index row. Part 3 maps every behavioural claim of the source to the criterion that now carries it.

`Rn` names Requirement n in `section.md`; a code in several requirements is anchored in each. Zero codes are dropped: all 113 cited codes appear in `section.md` (verified mechanically — cited-set minus present-set is empty).

## Part 1 — every cited code → its new home

| Code | New home | Index row consumed? |
|---|---|:--:|
| A-6 | R27 | yes |
| A-7 | R31 | yes |
| ACT-1 | R28 | yes |
| ACT-3 | R15 | yes |
| D-4 | R31 | yes |
| E-5 | R3 | yes |
| E-6 | R5, R27 | yes |
| E-7 | R27 | yes |
| E-8 | R27 | yes |
| E-10 | R8, R30 | yes |
| E-11 | R32 | yes |
| E-13 | R19 | yes |
| E-14 | R3 | yes |
| E-15 | R3 | yes |
| E-17 | R5 | yes |
| E-18 | R28 | yes |
| E-19 | R29 | yes |
| E-23 | R31 | yes |
| E-29 | R4 | yes |
| INV-1 | R34 | yes |
| INV-4 | R21 | yes |
| INV-6 | R3 | yes |
| INV-7 | R36 | yes |
| INV-10 | R31 | yes |
| INV-11 | R33, R36 | yes |
| INV-14 | R28 | yes |
| INV-17 | R5 | yes |
| INV-18 | R6 | yes |
| INV-22 | R28 | yes |
| INV-27 | R34 | yes |
| INV-37 | R24 | yes |
| INV-39 | R36 | yes |
| INV-40 | R6 | yes |
| INV-41 | R5, R6, R24, R25 | yes |
| INV-45 | R6 | yes |
| INV-47 | R7, R8 | yes |
| INV-59 | R34 | yes |
| INV-67 | R33, R34, R35 | yes |
| INV-69 | R10, R13 | yes |
| INV-70 | R11, R12 | yes |
| INV-73 | R4 | yes |
| INV-76 | R15 | yes |
| INV-82 | R33 | yes |
| INV-83 | R10, R20 | yes |
| INV-97 | R8 | yes |
| INV-98 | R1 | yes |
| INV-105 | R36 | yes |
| INV-108 | R2 | yes |
| INV-112 | R33 | yes |
| INV-113 | R24 | yes |
| INV-116 | R22 | yes |
| INV-117 | R31, R32, R35 | yes |
| INV-122 | R24 | yes |
| INV-132 | R4 | yes |
| INV-135 | R6, R24 | yes |
| INV-137 | R13 | yes |
| INV-142 | R24 | yes |
| INV-143 | R13 | yes |
| INV-146 | R34, R35 | yes |
| INV-147 | R34 | yes |
| INV-148 | R34 | yes |
| INV-149 | R35 | yes |
| INV-150 | R13 | yes |
| INV-152 | R12, R21 | yes |
| INV-157 | R14, R16 | yes |
| INV-162 | R14, R15 | yes |
| INV-164 | R6, R23, R24 | yes |
| INV-173 | R12 | yes |
| INV-174 | R33 | yes |
| INV-175 | R11, R26 | yes |
| INV-176 | R26 | yes |
| INV-177 | R8 | yes |
| INV-178 | R22 | yes |
| INV-180 | R11 | yes |
| INV-187 | R33 | yes |
| INV-189 | R32 | yes |
| INV-193 | R32 | yes |
| INV-202 | R9, R11, R12, R13 | yes |
| INV-203 | R10, R12, R13 | yes |
| INV-204 | R14, R15, R16 | yes |
| INV-205 | R16, R18, R19, R20 | yes |
| INV-206 | R17, R21 | yes |
| INV-207 | R18 | yes |
| INV-208 | R22 | yes |
| INV-209 | R23, R25 | yes |
| INV-210 | R26 | yes |
| INV-211 | R26 | yes |
| INV-212 | R26 | yes |
| INV-213 | R15 | yes |
| INV-216 | R26 | yes |
| INV-220 | R11 | yes |
| INV-221 | R10 | yes |
| INV-222 | R19, R37 | yes |
| INV-223 | R19 | yes |
| INV-224 | R6 | yes |
| INV-228 | R20 | yes |
| INV-229 | R21 | yes |
| INV-230 | R15 | yes |
| INV-232 | R33 | yes |
| INV-233 | R24 | yes |
| INV-234 | R25 | yes |
| INV-238 | R12 | yes |
| INV-241 | R12, R13 | yes |
| INV-242 | R37 | yes |
| INV-246 | R12 | yes |
| M-1 | R29 | yes |
| M-4 | R31 | yes |
| M-5 | R26 | yes |
| M-6 | R34 | yes |
| T-10 | R34, R36 | yes |
| T-16 | R28 | yes |
| T-18 | R36 | yes |
| T-20 | R34 | yes |

## Part 2 — consumed Formal-index rows

The section cites 113 distinct codes, and **all 113 carry a Formal-index row** — unlike the founding-section pilot, this machinery section names no inline-only feature code. Each row's meaning now lives at the home named in Part 1; no consumed index row is left without a home.

**Codes owned by this section** (their Formal-index home is `Machines`, `The machines that hold the bounds`, or `Package repo`) are the ones this rewrite fully converts: INV-98, INV-108, E-5, E-6, E-7, E-8, E-10, E-11, E-18, E-19, E-23, E-29, INV-6, INV-45, INV-47, INV-97, INV-105, INV-112, INV-117, INV-132, INV-146, INV-147, INV-148, INV-149, INV-174, INV-202, INV-203, INV-204, INV-205, INV-206, INV-207, INV-208, INV-209, INV-210, INV-211, INV-212, INV-213, INV-216, INV-220, INV-223, INV-224, INV-228, INV-229, INV-230, INV-233, INV-234, INV-238, INV-241, INV-242, INV-246, M-4, T-10.

**Pure cross-references** — a rule owned by another section that this section leans on rather than restates — are preserved as trailing anchors at the requirement that leans on them; the full behaviour stays defined in the home section, not re-converted here: A-6, A-7, ACT-1, ACT-3, D-4, E-13, E-14, E-15, E-17, INV-1, INV-4, INV-7, INV-10, INV-11, INV-14, INV-17, INV-18, INV-22, INV-27, INV-37, INV-39, INV-40, INV-41, INV-59, INV-67, INV-69, INV-70, INV-73, INV-76, INV-82, INV-83, INV-113, INV-116, INV-122, INV-135, INV-137, INV-142, INV-143, INV-150, INV-152, INV-157, INV-162, INV-164, INV-173, INV-175, INV-176, INV-177, INV-178, INV-180, INV-187, INV-189, INV-193, INV-221, INV-222, INV-232, M-1, M-5, M-6, T-16, T-18, T-20.

**Cross-section glossary note.** A handful of domain nouns the section uses are owned by other sections and are defined in their home glossary, not repeated here (per the reuse-by-reference rule): *movement*, *milestone*, *prover record*, *prover*, *design review*, *feel pass*, *register lint / pre-show register gate*, *routing rule*, *checkpoint*, *worker*, *lane*, *economy rung*, *the setup walk*, *content contract*, *the three fitness questions*, *the scissors scan*, *the muted-launch net*. In a whole-document conversion these live once in the shared glossary; this section's `## Glossary additions` block adds only the nouns this section introduces (net, push gate, prover record, net-liveness meter, test matrix, feature-coverage trace, register judge, conduct judge, action trace, seat, touchpoint, far tier, waiting board, decision-set record, snapshot, design-sync, skill eval, surface registry, pen, remote seat, grant, stranger, stranger-wish monitor, capture echo).

## Part 3 — atomic-claim coverage

Every behavioural claim of the source, in source order, mapped to the criterion (or criteria) that now carries it. "R9.3" means Requirement 9, criterion 3.

### The two lead laws (INV-98, INV-108)

| # | Source claim | Criterion |
|---|---|---|
| 1 | Every process names its goal up front as an artifact the work can be held against; a paraphrase cannot serve. | R1.1 |
| 2 | Every iteration measures distance to the goal itself; a proxy never replaces it, and a proxy is where a look-alike is born. | R1.2 |
| 3 | A reached level locks by a mechanism (norm template, conformance test, lint floor that only grows, cap that only ratchets down). | R1.3 |
| 4 | A deliberately divergent stretch is legal only when named and bounded by its convergence point. | R1.4 |
| 5 | A rule breaking mid-turn a second time earns a live channel that moment (hook line or after-the-fact check). | R2.1 |
| 6 | The pick is recorded where the rule lives; the once-read file stays the normative home. | R2.2 |
| 7 | Mid-turn breaks are recorded in one home (the problem ledger). | R2.3 |
| 8 | The live channel points back to that ledger entry rather than standing as a second break-record. | R2.4 |

### The coverage machines (E-5, E-14, E-15, INV-6, E-29, INV-73, INV-132)

| # | Source claim | Criterion |
|---|---|---|
| 9 | Coverage is total: no fact without a row, no row without a pinned test level. | R3.1 |
| 10 | Rows are keyed by architecture node × spec fact, from the derivation. | R3.2 |
| 11 | Each row states both sides; the negative side is the regression fence. | R3.3 |
| 12 | The feature-coverage trace maps each project-type unit to its implementer node(s) and a test. | R4.1 |
| 13 | The check reads both directions and fails the push either way. | R4.2 (named "the feature-coverage check"; the round-1 draft's "coverage net" was a stray second name for it and is retired — the source's own "traceability net" is a distinct mechanism, the suite's traceability tests, distinguished at R6.2) |
| 14 | Every H3 carries its feature tag or a not-a-scenario marker. | R4.3 |
| 15 | An H3 carrying neither is red, so a forgotten tag can no longer ship uncovered. | R4.4 |

### The guardrails and the push gate (E-6, E-17, INV-17, INV-41, INV-45, INV-40, INV-18, INV-164, INV-224, INV-135, INV-47, INV-97, INV-177, E-10)

| # | Source claim | Criterion |
|---|---|---|
| 16 | Each push shows a same-day prover record, a green scoped suite, one-node anchor ownership, no unchecked coverage box. | R5.1 |
| 17 | The prototype fence and the opt-in concurrent-edit fence on commit. | R5.2 |
| 18 | On a host, hooks install only where git is used and only after asking in plain words. | R5.3 |
| 19 | The push gate derives its check-set from a declared reach map; an unmapped/new file → full suite. | R6.1 |
| 20 | An infra-confined diff runs the tests that read its files plus the traceability net, logging the picked set; the infra list is curated by incident, re-justified at milestones. | R6.2 |
| 21 | A full run reads its wall-time against the architecture's number and reds an overrun naming both figures. | R6.3 |
| 22 | Reach classes are read from `guardrails.config.json`, the same layers `project.layers` carries. | R6.4 |
| 23 | A config naming no classes leaves everything unclassified → full suite every push. | R6.5 |
| 24 | The cheap gates never scope; nothing the diff touches is skipped. | R6.6 |
| 25 | Every blocking gate, on red, emits one typed failure object with severity/code/message/fix. | R7.1 |
| 26 | Every check declares itself blocking or advisory; an advisory never flips the exit code. | R7.2 |
| 27 | A rebuild validates every output before writing any; no half-written artifact lands. | R7.3 |
| 28 | The four project-side checks (completeness, tests-present, behaviour-traces-to-spec, conflicts) ship parametrized by one host config, not by editing code. | R8.1 (+ GAP: the conflicts check's detected conflict is unstated) |
| 29 | Each check reads config and tree, exits green/red, emits the typed line on red. | R8.2 |
| 30 | Failure is honest: missing config → red with attach-me line; a bad path → red. | R8.3 |
| 31 | A genuinely absent precondition is a declared waiver a reader sees; an undeclared gap never passes. | R8.4 |
| 32 | Attach vendors the checks, seeds config where none, leaves a filled config unclobbered, writes source pins to the ratchet manifest. | R8.5 |
| 33 | Each check proves itself red-first on one planted defect; the registry stays the host's authorship. | R8.6 |

### The net-liveness meter (INV-202)

| # | Source claim | Criterion |
|---|---|---|
| 34 | Every net records runs and fires (one line per invocation) against the host's declared roster. | R9.1 |
| 35 | A zero-run net reds by name as a broken trigger. | R9.2 |
| 36 | A net with runs at/over its window and zero fires is a retirement candidate; retirement is the human's call. | R9.3 (+ GAP: window owner/default) |
| 37 | Everything else reads live; the meter never auto-retires and never reds a quiet net. | R9.4 |

### The register judge (INV-203, INV-69, INV-83, INV-221)

| # | Source claim | Criterion |
|---|---|---|
| 38 | The judge holds the class: hands text and law to the cheapest sufficient tier, takes back info-less/register-leaking sentences. | R10.1 |
| 39 | The literal list is a first cheap filter earning no new entries by duty. | R10.2 |
| 40 | The universal laws ship in the mechanism (denied-neighbour, bare-code opener, ungrounded grading, unglossed coinage); personal laws ride an overlay. | R10.3 |
| 41 | Two surfaces: a chat Stop arm dispatches the whole turn's shown text; a prompt-submit arm reports next message; the document judge is the pre-show gate's ceiling. | R10.4, R10.5 |
| 42 | The judge stands down silently on its own breakage, leaving the literal-list verdict. | R10.6 |

### The answer-first arm (INV-220, INV-70, INV-175, INV-180, INV-202)

| # | Source claim | Criterion |
|---|---|---|
| 43 | A reply over the floor whose opening fails all three lead signals is flagged for a lead-first correction. | R11.1 |
| 44 | The floor and thresholds are the host's tunable defaults. | R11.2 |
| 45 | It reads only whether a lead is present, leaving whether it is the right answer to the human. | R11.3 |
| 46 | It judges only the final reply, leaving inter-tool narration alone. | R11.4 |
| 47 | A Stop-hook notice, correcting one message later since a chat reply is already emitted. | R11.5 |
| 48 | Ships as a universal pack hook, covered by config-health parity; runs/fires read by the meter. | R11.6 |

### The hedge and lean-orchestrator soft signals (INV-238, INV-246, INV-152, INV-173, INV-70, INV-241, INV-203, INV-202)

| # | Source claim | Criterion |
|---|---|---|
| 49 | An offering-hedge frame (after stripping quoted/backticked/fenced spans) blocks the stop with a rewrite instruction, one message later, modelled on the scissors scan. | R12.1 |
| 50 | It stands clear of a genuine taste/policy/irreversible question naming its human-only fact. | R12.2 |
| 51 | It catches only listed frames; the class in any phrasing stays with the conduct judge. | R12.3 |
| 52 | The lean-orchestrator arm warns when cumulative inline raw content reaches the threshold with zero dispatches. | R12.4 |
| 53 | The threshold is a tunable parameter defaulting to 50 KiB; only a main-thread Read or six literal file-dump verbs count; a worker read is never counted. | R12.5 |
| 54 | The warning clears on the first worker dispatch. | R12.6 |
| 55 | Both stand down silently on their own breakage; runs/fires read by the meter. | R12.7 |

### The conduct judge (INV-241, INV-150, INV-203, INV-69, INV-137, INV-143, INV-202)

| # | Source claim | Criterion |
|---|---|---|
| 56 | The judge reads the turn's action trace against the standing orchestration laws and reds a violation after the fact. | R13.1 |
| 57 | The trace is rendered to quotable text so the reused hallucination guard has spans. | R13.2 |
| 58 | An empty-trace (chat-only) turn is skipped. | R13.3 |
| 59 | The law body is the two-plus-reminder members (worker-routing, lean-orchestrator, pull-unblocked, classify-subtask); single-occurrence members stay reminders. | R13.4 |
| 60 | Partial-evidence members red only on a clear case, leaning on the meter and human review. | R13.5 |
| 61 | Async two-arm shape with a distinct verdict slot; a forward-looking correction one turn later. | R13.6 |
| 62 | Outside the deterministic suite and push gate, opt-in and off by default. | R13.7 |
| 63 | Per-person strictness is a parameter it does not own; a built-in default overridable by env until the registry ships. | R13.8 (+ GAP: default value) |

### A cleanup says what it ended (INV-204, INV-162, INV-157)

| # | Source claim | Criterion |
|---|---|---|
| 64 | Every process the pack ends emits one notice naming the identity, what it was, and the owned-via proof. | R14.1 |
| 65 | A tracked cleanup path ending a process with no notice reds the gate. | R14.2 |
| 66 | The notice ships ahead of the stricter owned-identity check, making it safe to land. | R14.3 |
| 67 | An ending through an indirection the patterns cannot read stays the forker's to announce. | R14.4 |

### Runaway child and the reap (INV-213, INV-230, INV-162, INV-204, INV-76, ACT-3)

| # | Source claim | Criterion |
|---|---|---|
| 68 | At a stopping point, report an owned-orphaned-burning descendant by process-group/parent-liveness/processor-share alone. | R15.1 (+ GAP: burning-threshold default) |
| 69 | No command/name field is read for the verdict, so a foreign-group match is never targeted. | R15.2 |
| 70 | Teardown reaps the run's own process group via `os.killpg`, refusing any group absent from the owned set. | R15.3 |
| 71 | The reap reports what it ended through the shared cleanup-notice shape. | R15.4 |
| 72 | A stalled worker (status running, output file idle) is read by mtime and returned with its owned group for confirmation before reap. | R15.5 |
| 73 | A worker's brief carries its setting lines; a worker session onboards no one. | R15.6 |

### The touchpoint frame (INV-205, INV-204, INV-157)

| # | Source claim | Criterion |
|---|---|---|
| 74 | Each touchpoint declares its kind in `guardrails/touchpoints.json` (person-opens, afforded traffic). | R16.1 |
| 75 | An interruption on a synchronous point, a teaching line on a person-opened point, waiting traffic everywhere. | R16.2 |
| 76 | A surface speaking in a kind its touchpoint lacks reds. | R16.3 |
| 77 | An interrupt through unreadable wording stays the author's to declare. | R16.4 |

### The waiting board (INV-206)

| # | Source claim | Criterion |
|---|---|---|
| 78 | The board holds every waiting item; an item clears on the person's acknowledgement alone. | R17.1 |
| 79 | Never auto-expired; a superseded item moves to the attic with a manifest line. | R17.2 |
| 80 | At most 12 shown; a new item to a full set demotes the oldest, whole. | R17.3 |
| 81 | A thirteenth shown item is the over-cap defect. | R17.4 |
| 82 | The board gate reds a closing report omitting an open item, a demotion with no matching line, or an over-cap set. | R17.5 |

### The authority anchor (INV-207, INV-205)

| # | Source claim | Criterion |
|---|---|---|
| 83 | A sentence set down as the person's decision names the exchange it came from. | R18.1 |
| 84 | A claim the pack reasoned out is in the pack's own voice, challengeable by every reader. | R18.2 |
| 85 | An autonomy grant is room to act the agent owns, never a decision quoted back. | R18.3 |
| 86 | The decision-set record shows the person each decision with its exchange, on the person's own clock, to strike what was never said. | R18.4 |
| 87 | A live decision-record entry with no exchange reds the authority-anchor gate; a struck entry is skipped. | R18.5 |

### The far backlog (INV-223, INV-222, INV-205, E-13)

| # | Source claim | Criterion |
|---|---|---|
| 88 | The far tier answers on ask (floor) and above it carries a rare status-report line. | R19.1 |
| 89 | At most one offer per 14 days as a settings-ladder default, movable by the person; last surfacing dated. | R19.2 |
| 90 | It rides the status report, an asynchronous point that may only wait (`far-tier-surfacing`). | R19.3 |
| 91 | A second offer inside the window reds the report-shape check; a first offer past the window passes. | R19.4 |

### The release note (INV-228, INV-205, INV-83)

| # | Source claim | Criterion |
|---|---|---|
| 92 | The publish walk records the offer-or-none decision on the note, carrying the optional offers section. | R20.1 |
| 93 | A record with neither an offer nor a no-offer marker reds; an offered or no-offer record passes. | R20.2 |
| 94 | The release note is an asynchronous, person-opened touchpoint affording an offer, not an interruption. | R20.3 |

### The parked question (INV-229, INV-4, INV-206, INV-152)

| # | Source claim | Criterion |
|---|---|---|
| 95 | A parked question is born onto the board already carrying the default the work took; the work proceeds. | R21.1 |
| 96 | A parked question with no default reds the board gate; one naming its default passes. | R21.2 |
| 97 | An unanswered parked question keeps standing, default holding, recorded as unreviewed — a fact, not an expiry. | R21.3 |
| 98 | An answered question routes through intake and closes; distinct from the decision law. | R21.4 |

### The skill-review gate (INV-208, INV-116, INV-178)

| # | Source claim | Criterion |
|---|---|---|
| 99 | A substantively changed skill needs a committed review naming the skill, a verdict, at least as new as the change. | R22.1 |
| 100 | The gate reads the push range through the same base ladder as the prover-record gate. | R22.2 |
| 101 | A diff whose only changed lines are version stamps owes no review. | R22.3 |
| 102 | A body change with no review reds; the review's judgment stays the skill-creator's. | R22.4 |

### Doc rotation (INV-209, INV-164)

| # | Source claim | Criterion |
|---|---|---|
| 103 | A fully-closed portion rotates into a dated archive with a manifest naming moved rows and their archive. | R23.1 |
| 104 | A row is rotatable only when closed with no open signal; the existing signal is reused. | R23.2 |
| 105 | A manifest-declared rotated row found in neither live nor archive reds (nothing-lost). | R23.3 |
| 106 | An unpointed archive, or a rotated row still standing live, reds as ambiguous. | R23.4 |

### Node growth (INV-233, INV-41, INV-122, INV-164, INV-142, INV-37, INV-113, INV-135)

| # | Source claim | Criterion |
|---|---|---|
| 107 | Nodes-per-file is counted from the pin column; raw size is rejected as the signal. | R24.1 |
| 108 | Each node re-answers the three fitness questions at re-prove; two nodes sharing a file answer parallel-work no. | R24.2 |
| 109 | A ratcheted per-file node cap seeded at the current count; an increase reds; the cap ratchets down only. | R24.3 |
| 110 | A file at its cap draws the design review's two-objects split proposal naming the file and the split. | R24.4 |
| 111 | A split is carved by the architecture step alone and re-proven there. | R24.5 |
| 112 | What counts as a code file is read from the declared layers. | R24.6 |

### Doc bounds (INV-234, INV-41, INV-209)

| # | Source claim | Criterion |
|---|---|---|
| 113 | The four large docs declare a byte ceiling with a recorded reason; a doc past its ceiling reds. | R25.1 |
| 114 | A bound with no reason reds. | R25.2 |
| 115 | A doc rotated today (manifest naming a same-day archive) passes even over ceiling; another day's rotation does not clear today's overflow. | R25.3 |
| 116 | Ceilings seeded above current sizes with rotation headroom; a rise needs a recorded reason; the ratchet is down. | R25.4 |

### The guards over the guards (INV-210, M-5, INV-211, INV-212, INV-216, INV-175, INV-176)

| # | Source claim | Criterion |
|---|---|---|
| 117 | A local gate letter absent from the CI mirror reds, naming the gate and fix; carve-outs live in `ci-mirror.json` with reasons. | R26.1 |
| 118 | A carve-out naming a non-gate letter reds as drift. | R26.2 |
| 119 | A hook unclassified in the wired-hook declaration, or a wired hook missing from settings, reds naming hook/surface/fix. | R26.3 |
| 120 | Where personal-layer settings can't be read, the wiring check stands down by name, never falsely passing. | R26.4 |
| 121 | Every pushed gate carries a red-first proof to a non-zero exit, or a covered entry naming the gate it rides and the reason. | R26.5 |
| 122 | A gate classified nowhere, or a gate that can never fail, reds loudly. | R26.6 |
| 123 | A permission rule naming an absent filesystem path reds; the arm reads absolute/home-rooted paths and reports the resolved count. | R26.7 |

### The snapshot (E-7, E-6, A-6, E-8)

| # | Source claim | Criterion |
|---|---|---|
| 124 | The baseline advances only at delivery and only for declared surfaces; undeclared surfaces keep their baseline. | R27.1 |
| 125 | A rendered surface differing from its baseline while undeclared reds the declared-scope check. | R27.2 |
| 126 | The snapshot folder is git-tracked, one manifest line per surface; only the last baseline is in the working tree; older baselines checkout-able. | R27.3 |
| 126a | A too-heavy surface keeps only its manifest line and content hash in git; the bytes live outside git, and only the hash is diffed (source line 1923; restored in the row-445 repair, source-ordered between claims 126 and 127). | R27.4 |
| 127 | Adoption saves the first baseline as found; the host profile narrows shared settings only where recorded. | R27.5 |

### Design-sync (E-18, INV-14, ACT-1, T-16, INV-22)

| # | Source claim | Criterion |
|---|---|---|
| 128 | Off by default in the base table; on only where a host records a profile line. | R28.1 |
| 129 | It syncs the components a delivery declared; every sync is human-gated since it publishes outside the machine. | R28.2 |
| 130 | It applies to product-kind work on a visual host; every other kind stands down by name. | R28.3 |

### The skill evals (E-19, M-1)

| # | Source claim | Criterion |
|---|---|---|
| 131 | Each working skill owns at least one eval proven red without it, in `evals/`, one file per skill. | R29.1 |
| 132 | A working skill with no eval is a defect at the milestone audit. | R29.2 |
| 133 | Evals re-run at milestones and behaviour-changing deliveries; a pin/version bump owes no re-run. | R29.3 |

### The surface registry (E-10)

| # | Source claim | Criterion |
|---|---|---|
| 134 | The registry lives as a declared map inside a completeness test, failing both ways. | R30.1 |
| 135 | The completeness check scans the rendered artifact and reds a rendered-but-unregistered surface. | R30.2 |
| 136 | The document form is the fallback; an arriving executable form is recognized rather than asked back. | R30.3 |

### Pack-repo write access and the skill sync (M-4, INV-10, E-23, D-4, A-7, INV-117)

| # | Source claim | Criterion |
|---|---|---|
| 137 | A session that cannot say the human asked it (this conversation or a standing routine) does not write the repo. | R31.1 |
| 138 | Every other session is read-only, with one exception: a new inbox file. | R31.2 |
| 139 | A skill edit syncs the installed copy the same session via `sync-skills.sh`, reporting each version change old→new. | R31.3 |
| 140 | A hand-copy is retired since it syncs silently. | R31.4 |
| 141 | The repo's push gates run mechanically on installed hooks. | R31.5 |
| 142 | Each session mints a stable identity at start. | R31.6 |

### The inbox door (E-11, INV-117, INV-189, INV-193)

| # | Source claim | Criterion |
|---|---|---|
| 143 | Each outside item lands as one new file `YYYY-MM-DD-<source>-<slug>.md`; never edits an existing file. | R32.1 |
| 144 | A taken name appends an ordinal; racing sessions add a session token, not a second identity scheme. | R32.2 |
| 145 | An agent's deposit names its source in the `from-<agent>` form the gate reads. | R32.3 |
| 146 | Two source words reserved (owner's wish, stranger's bridged item), owing no birth; an agent-initiated message is a proposal until ratified. | R32.4 |

### The remote and local arms (INV-112, INV-82, INV-67, INV-174, INV-11, INV-232, INV-187)

| # | Source claim | Criterion |
|---|---|---|
| 147 | A remote seat commits one inbox-only file with the source named and pushes under a recorded per-repo grant. | R33.1 |
| 148 | A rejected remote push retries after a pull; never edits an existing file. | R33.2 |
| 149 | A grantless remote seat fails honestly, naming the grant and the one action; never guesses. | R33.3 |
| 150 | A co-located session writes its one file and stops — no staging/commit/push; the sweep commits the harvest. | R33.4 |
| 151 | A fresh untracked inbox file is the benign case; a co-located stage/commit is a fence stop. | R33.5 |
| 152 | A remote consumer of a private producer repo needs a read grant beside the push grant; a grantless read fails honestly. | R33.6 |

### The stranger arm and its monitor (INV-146, INV-1, INV-147, INV-148, T-10, INV-27, T-20, INV-59, INV-67, M-6)

| # | Source claim | Criterion |
|---|---|---|
| 153 | The monitor converts each open un-surfaced stranger item into one committed inbox file naming the source Issue and field. | R34.1 |
| 154 | A stranger's wish never touches queue/repo; the monitor and sweeps own every write, so no wish is lost. | R34.2 |
| 155 | Surfaced at most once per activity generation, read from non-marker comments so its own claim/confirm never read as fresh. | R34.3 |
| 156 | A newer activity generation re-surfaces the item afresh. | R34.4 |
| 157 | A surfaced wish is harvested into a row and the capture echo posted on the source Issue. | R34.5 |
| 158 | A terminal row closes the Issue (convergence); a non-wish is closed with a recorded note. | R34.6 |
| 159 | The monitor runs one instance per host under a lock stolen by age (~1h); a run that can't reach the repo fails honestly. | R34.7 |
| 160 | The pack repo runs the monitor as a scheduled action pushing inbox commits only under a single-instance concurrency group, riding the inbox-only carve-out. | R34.8 |

### Two hosts converge (INV-149, INV-117, INV-146, INV-67)

| # | Source claim | Criterion |
|---|---|---|
| 161 | A host posts a claim comment carrying its identity, re-reads claims, deposits only when its claim wins. | R35.1 |
| 162 | The winner is the earliest claim by creation time, lower host identity breaking ties, computed identically everywhere. | R35.2 |
| 163 | A claim older than the stale bound reads abandoned; the next surviving host surfaces. | R35.3 |
| 164 | A losing host stands down and retries; one wish reaches the inbox once. | R35.4 |
| 165 | The claim rides the writes already held (no new grant); the claim marker stays distinct from the surfaced-generation record. | R35.5 |
| 166 | A run that can't reach the item fails honestly and retries, dropping no wish. | R35.6 |

### The fence, the harvest, and one state directory (INV-11, T-10, INV-105, INV-7, INV-39, T-18)

| # | Source claim | Criterion |
|---|---|---|
| 167 | Before every write and every commit, a moved head or unexpected change stops the agent to re-read or back off to the inbox. | R36.1 |
| 168 | A new inbox file is benign; never push while another session is known live. | R36.2 |
| 169 | A session sweeps the inbox first, harvesting each file into its route's home in one commit that lands the route and removes the file. | R36.3 |
| 170 | An interrupted harvest commits nothing and leaves the file for the next sweep, harvested once. | R36.4 |
| 171 | One canonical state directory `.live-spec`; a near-miss look-alike retires to the attic with a manifest naming path/reason/canonical. | R36.5 |
| 172 | Overlapping lanes default to worktree isolation, the copy reaching the shared tree only through integration under the pen. | R36.6 |

### The landing/forward-map gate (INV-242, INV-222)

| # | Source claim | Criterion |
|---|---|---|
| 173 | A commit flipping a roadmap row to `landed` must touch `NEXT_STEPS.md`, read through the same base ladder. | R37.1 |
| 174 | Such a delivery commit not touching the forward map reds, naming the one fix. | R37.2 |
| 175 | A commit closing no row, and a row closed to declined/deferred/superseded, owe no refresh. | R37.3 |
| 176 | With push-gate letters exhausted, the check rides the suite so a red blocks the push. | R37.4 |

### Coverage result

177 behavioural claims mapped, covering all 37 requirements — 176 in the round-3 conversion, plus one restored in the row-445 repair (claim 126a, the too-heavy-surface snapshot rule at source line 1923, added as R27.4 after the source-coverage audit found it uncovered; the criteria below it in R27 renumbered by one). After the cold-reader panel, six named sub-mechanisms gained an in-line plain gloss at first mention (the conflicts check via a GAP, the config-health parity net, the scissors scan, the hallucination guard, the muted-launch net) or a glossary entry (the far tier), and two criteria were expanded to enumerate what the source enumerates (the three fitness questions at R24.2, the four bounded documents at R25.1); no claim moved. Three source non-goal / policy blocks are carried as source policy statements in the requirement contexts rather than converted to `shall` criteria, since they state what the system deliberately does **not** do (which the format keeps as prose or negative-side fences): the push-gate reach's "no numeric budget" framing (folds into R6 via INV-41), the design-sync "the pack never syncs" statement (stated in R28 context and covered by R28.3's stand-down criterion), and the net-liveness "never auto-retires" stance (converted positively as R9.4). No behavioural `shall`-claim of the source is left uncovered; the four source holes are recorded as `[GAP]` lines at R8.1, R9.3, R13.8, and R15.1 and detailed in `GAPS.md`.

### Final restoration wave (re-pin sweep) — declared additions

- **R4.3 / R4.4 (INV-132, DEFECT-1 signal).** Restated from the retired third-level-heading tag-or-marker convention to the practiced one — the feature tag on the requirement heading, and a promised leg not yet built taking a `[target]` marker on its own line. Owed by `test_scenario_heading_tag::test_spec_criteria_match_the_practiced_convention`.
- **R27.3 (snapshot directory).** Restores the `.live-spec/snapshot/` directory literal. Owed by `test_snapshot_design`.
- **R28 Context (design-sync wiring note).** Restores "Design-sync [target: the machine; the wiring is live]" and the E-7 declared-scope link. Owed by `test_spec_states_founding_and_designsync` / `test_designsync_wiring`.
- **R33.7 (inbox stand-down carve-out).** Restores "the live-session stand-down holds no bar over the deposit" — the one additive inbox file races nothing. Owed by `test_inbox_remote_arm`. [INV-112, INV-82]
- **R36.7 (fence one-file carve-out).** Restores "owe the fence and no re-check record" for a diff of exactly one new inbox file. Owed by `test_inbox_remote_arm`. [INV-11, INV-112]
