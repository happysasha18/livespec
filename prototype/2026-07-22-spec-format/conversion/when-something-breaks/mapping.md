# MAPPING — codes, consumed index rows, and atomic-claim coverage

This file proves the rewrite of `## When something breaks` (PRODUCT_SPEC.md lines 1056–1162) dropped nothing. Part 1 maps every code the source cites to its new home. Part 2 states which codes carried a consumed Formal-index row. Part 3 maps every behavioural claim of the source to the criterion that now carries it.

`Rn` names Requirement n in `section.md`; a code in several requirements is anchored in each. Zero codes are dropped: all 24 cited codes and both feature tags appear in `section.md` (verified mechanically — cited-set minus present-set is empty, and no extra code is present).

## Part 1 — every cited code → its new home

| Code | New home | Index row consumed? |
|---|---|:--:|
| ACT-3 | R7 | yes |
| B-2 | R8 | yes |
| B-3 | R8 | yes |
| E-8 | R3 | yes |
| E-11 | R4 | yes |
| E-22 | R4 | yes |
| E-24 | R3, R5, R7 | yes |
| INV-4 | R4 | yes |
| INV-9 | R4, R5 | yes |
| INV-10 | R4, R7 | yes |
| INV-11 | R7 | yes |
| INV-15 | R2 | yes |
| INV-23 | R4, R7, R8 | yes |
| INV-26 | R2 | yes |
| INV-39 | R1 | yes |
| INV-56 | R2, R6 | yes |
| INV-62 | R8 | yes |
| INV-65 | R8 | yes |
| INV-124 | R2 | yes |
| INV-155 | R3 | yes |
| M-1 | R5, R7 | yes |
| T-9 | R1, R4, R6, R7 | yes |
| T-11 | R1 | yes |
| T-18 | R1 | yes |

Feature tags: `F-bug` carried in the titles of R1–R2; `F-problem-ledger` carried in the titles of R3–R8. Neither tag has a Formal-index row (they are feature-map tags, not codes), so neither enters the byte count of consumed index rows.

## Part 2 — consumed Formal-index rows

The section cites 24 distinct codes, and **all 24 carry a Formal-index row** — this scenario section names no inline-only feature code. Each row's meaning now lives at the home named in Part 1; no consumed index row is left without a home.

**Codes owned by this unit** (their Formal-index home is `Bug cuts the line`, `When a bug cuts the line`, `Workshop misbehaves`, or `When the workshop itself misbehaves`) are the ones this rewrite fully converts: T-9, INV-124, INV-56, E-24, INV-23, INV-65. INV-56 carries two facets — its index row states the class-rule facet (a confirmed bug is one sample of its class), converted at R2.1, while the source prose anchors INV-56 on the parking law, converted at R6; both facets land.

**Pure cross-references** — a rule owned by another section that this section leans on rather than restates — are preserved as trailing anchors at the requirement that leans on them; the full behaviour stays defined in the home section: T-11, T-18, INV-39, INV-15, INV-4, INV-26, INV-155, E-8, INV-9, E-22, E-11, INV-10, ACT-3, INV-11, M-1, B-2, B-3, INV-62.

**Cross-section glossary note.** A handful of domain nouns this section uses are owned by other sections and are defined in their home glossary, not repeated here: *bug*, *feature*, *wish*, *lane*, *checkpoint*, *station*, *node*, *feature door*, *bug lane*, *kill-list*, *the fence*, *the prover*, *worker*, *the batched report*, *compaction*, *milestone audit*, *spec-delta*, *feature map*. In a whole-document conversion these live once in the shared glossary; this unit's `## Glossary additions` block adds only the nouns it introduces (problem ledger, signature, workshop noise, class hunt).

## Part 3 — atomic-claim coverage

Every behavioural claim of the source, in source order, mapped to the criterion (or criteria) that now carries it. "R1.4" means Requirement 1, criterion 4.

### A bug cuts the line (T-9, T-11, T-18, INV-39)

| # | Source claim | Criterion |
|---|---|---|
| 1 | A reported bug is fixed before anything else; the mid-build feature returns on its own; no work is lost. | R1 context, User Story |
| 2 | Mid-feature the human reports; the feature is set aside at a checkpoint; the bug takes the lane; once no bug waits the feature returns as the next thing. | R1 context |
| 3 | Precondition: a feature is in work when the bug arrives; with nothing in work the bug takes the lane. | R1 context |
| 4 | A bug mid-feature moves the feature to parked with a checkpoint written first (failing test names when red, hypothesis, touched files); red work is never committed. | R1.1 |
| 5 | The bug takes the lane and runs to completion; an arriving bug, critical included, joins the waiting line and interrupts nothing. | R1.2 |
| 6 | Waiting bugs order critical-first; equal priority by arrival. | R1.3 (+ GAP: bug-priority judge) |
| 7 | Once no bug waits, parked features resume ahead of the whole queue; a bubble jumps only fresh queued wishes, never a resume, a quick win included. | R1.4 |
| 8 | At most one feature parked per lane; more than one rolling lane parks them all, each at its own checkpoint, resuming in landing order. | R1.5 |
| 9 | On resume, before integrating, the feature re-fences and re-proves its spec-delta against the now-committed truth, since the fix may have moved the law; a spec-delta proven only against the pre-bug truth is re-verified on the new tree, never integrated blind. | R1.6, R1.7 |
| 10 | Postcondition: the fix landed; every parked feature back in work or landed in original order, each re-fenced and re-proven; no red work committed. | R1.7 |

### The class hunt (INV-124, INV-56, INV-15, INV-4, INV-26)

| # | Source claim | Criterion |
|---|---|---|
| 11 | A confirmed bug is one sample of its class; four moves run before the fix is done. | R2 context, R2.5 |
| 12 | Move one: name the defect abstractly (kind, scope too narrow, missing guard, an assumption holding in one place and failing in its neighbour), search every surface where the kind could live, and fix every sibling in the same change. | R2.1 |
| 13 | Move two: a structural cause (a boundary the architecture drew wrong or left silent, a node owning what it should not) updates the architecture in the same change. | R2.2 |
| 14 | Move three: a spec silent on the behaviour or under-describing its composition is the real defect, fixed first so the prover can flag it, the code fix landing under it. | R2.3 |
| 15 | Move four: escalate to the human when the class boundary needs their read; stop and ask rather than guess. | R2.4 |
| 16 | The prover carries a class lens on a found defect for the same three questions. | R2.6 |
| 17 | The four moves are the bug's close condition; a point fix that leaves siblings standing is a status, never a landing. | R2.5 |

### The problem ledger (E-24, E-8, INV-155)

| # | Source claim | Criterion |
|---|---|---|
| 18 | Workshop noise (a flaking harness or tool, a missing dependency, a shell command failing outside the product, a timeout) is retried and forgotten, eating the same minutes each session; a flaky test the project owns is instead a defect fixed at its root, never workshop noise and never a retry. | R3 context, R3.2 |
| 19 | The problem ledger is the host's list of operational noise, one git-tracked file `.live-spec/PROBLEMS.md`, born on its first entry, with only the checkpoints ignored within `.live-spec/`. | R3.1 |
| 20 | Each entry is a signature — a short greppable plain phrase carrying its dated occurrences and one status. | R3.3 |
| 21 | The four statuses: watched (seen once), owned (a named queue row will solve it), an agreed non-problem (dated, on the human's word), and solved (its row landed, the date kept). | R3.4 |

### The ledger walk (INV-23, INV-9, INV-4, E-22, E-11, INV-10, T-9)

| # | Source claim | Criterion |
|---|---|---|
| 22 | Noise fires mid-work, the session greps the ledger for the signature, and the result decides the next move. | R4 context |
| 23 | Not listed: write one watched line (signature, date, one line of context) and keep working, replacing the silent retry and never taking the lane; a product defect is a bug, sent to the bug lane. | R4.1, R4.2 |
| 24 | Second occurrence: an owner that moment (a queue row or the human's dated word closing it as no problem, the verdict the human's alone); the recommended owner is written right away and the ask rides the batched report; the lane never stalls. | R4.3, R4.4 |
| 25 | Third unowned recurrence: a method defect reaching past a single day, filed as one inbox file to the pack's own queue citing the signature and its dates. | R4.5 |

### An owned entry collects dates (E-24, INV-9, M-1)

| # | Source claim | Criterion |
|---|---|---|
| 26 | After the owner is written, a recurrence on an owned or agreed entry appends its date and changes nothing else. | R5.1 |
| 27 | Re-raising an agreed non-problem is the human's move, from the growing date list. | R5.2 |
| 28 | A landing that closes an owned entry's row flips the entry to solved the same session, never waiting for an audit. | R5.3 |
| 37 | At the milestone compaction, solved and agreed entries move to a dated archived tail of the same file, one file staying the one home so the ledger never grows without bound. | R5.4 |

### A known owned problem stays parked (INV-56, T-9)

| # | Source claim | Criterion |
|---|---|---|
| 29 | A known, owned problem never blocks unrelated work; it stays parked while unrelated lanes keep rolling — a recurring defect with a named mechanical owner, or a check held red for an understood, recorded reason. | R6.1 |
| 30 | Its ledger line, owning row, or expected-red note holds it in place. | R6.1 |
| 31 | Rule one: hand-fixing loops cap at two strikes; the second occurrence buys an owner, never another hand-pass. | R6.2 |
| 32 | Rule two: a defect with a named mechanical owner is serviced in batch, the fence fixing instances silently and appending one ledger line at session's end, with no per-instance ceremony. | R6.3 |
| 33 | A real new bug still preempts; this law governs only the known, owned problem. | R6.4 |

### The seams and this landing's scope (ACT-3, INV-11, M-1, T-9, E-24, INV-10, INV-23)

| # | Source claim | Criterion |
|---|---|---|
| 34 | Sessions write the ledger; a worker reports noise in its checkpoint for the session to carry over, or writes it directly when its brief names the ledger; the brief states the write-ownership law. | R7.1 |
| 35 | Two sessions on one host share the file under the concurrent-edit fence, like any document. | R7.2 |
| 36 | Grep and eyes decide when two entries are one problem; short signatures keep the grep honest; one problem under two wordings merges at the milestone compaction. | R7.3 |
| 38 | This is the workshop's law while the product keeps its own; a recurring product bug re-doors to a feature under the pipeline's rule, distinct by what broke. | R7.4 |
| 39 | The ledger carries no visible surface, so its facets do not apply. | R7.5 |
| 40 | Non-goal: no mechanical guard yet; the candidate (a pre-push check that no entry crosses a milestone unowned) earns its row after real usage. | R7.6 |
| 41–42 | Non-goal: no automated signature matching; this landing opens the pack's own ledger while a foreign host opens its own from its own window. | R7.7 |
| 43 | Success measure: the next operational hiccup lands as a recorded ledger line, checked at the milestone audit. | R7.8 |

### Reuse before reinventing (INV-65, B-2, B-3, INV-23, INV-62)

| # | Source claim | Criterion |
|---|---|---|
| 44 | Before reinventing a fix, search for an existing skill; two moments trigger the search. | R8 context |
| 45 | At setup (founding, or adoption's orient, beside the founding questions), the pack scans installed skills and reachable catalogs, matches the project's kind and crafts, and proposes a fit list with a recommendation the human's word picks. | R8.1 |
| 46 | At a struggle (a ledger entry's second occurrence, a taste artifact rejected twice, any recurring failure family), the next attempt waits for one search; a found skill is adopted or rejected by name and the verdict recorded where the struggle lives. | R8.2 |
| 47 | Borrowing: invoke a found skill as it ships, paraphrase a lesson into the project's own documents with named credit, carry verbatim text only under its license with the notice kept, and never republish unlicensed text. | R8.3, R8.4 |

### Coverage result

Forty-seven source claims mapped, covering all 8 requirements. One source hole is recorded as a `[GAP]` line at R1.3 (the judge or measure for a bug's critical priority) and detailed in `GAPS.md`. The section's non-goal and scope statements — what this landing deliberately does not add (a mechanical guard, automated signature matching, foreign-host ledgers) — are carried as policy criteria at R7.6 and R7.7, and the ledger's no-visible-surface facet at R7.5. No behavioural `shall`-claim of the source is left uncovered.

### Prover MUST-FIX wave (row 445 audit, F1) — declared sharpen

- **R1.3 (assembled R160.3)**: the `[GAP]` line beneath it claimed a bug's critical priority is undecidable, while the intake section's classification criterion (assembled R9.4, [INV-12]) states the three critical conditions in full. The audit named it the one false GAP of 42 (finding F1). The GAP line is deleted and the criterion sharpened to carry the pointer: waiting bugs order critical-first, a bug being critical *when* the shipped product is broken for its user — the same three conditions the priority mark carries [INV-12]. The criterion's anchor set gains INV-12 beside T-9. The coverage-result line counting "one source hole ... at R1.3" is superseded by this note: that GAP is retired as false, and the unit now carries zero GAP lines of its own.
