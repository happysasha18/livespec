# DELTA — every edit beyond plain concatenation

This file records how the eleven converted units — the ten under `conversion/` plus the pilot unit
`pilot/` (Starting and adopting a project, accepted by its own cold-read rounds at the pilot stage) —
were assembled into one requirements-format document, `assembly/PRODUCT_SPEC.md`, and every change made
past a straight concatenation. The eleventh unit, `conversion/composing-across-axes/` (converted from
the Reference section's "Composing across axes" essay, panel-accepted), closes the normative body after
"What holds the bounds": its cross-references all point backward, and the source's own order places it
last. The assembler script is `assembly/assemble.py` (stdlib only); it reads the eleven `section.md`
files read-only, so the edits below live in the script's transform, never in the source units. The two
per-unit `mapping.md` files touched by a declared sharpen are named under their items. This run also
picks up the open-decisions repairs landed in the unit files after the ten-unit run: the pilot's
R20.1/R20.2 gap lines with their `D-6`/`D-7` anchors, and the bounds unit's new R27 criterion 4 (the
too-heavy-surface rule under `E-7`) — both verified present in the assembled document.

The assembly covers every normative section of the source body. Two source blocks are intentionally
unconverted, each with a stated new home: the `## Reference` section's manual Formal index is retired,
replaced by the generated code-to-location table (built by `scripts/build-index.py`, embedded in the
document's own Reference section); and the Reference section's "Open decisions" block, whose three open
decisions now live in `DECISIONS.md` (the pilot's D-6/D-7 gap lines point there in the body).

## Size

| Document | Bytes (UTF-8) | Ratio to source |
|---|---:|---:|
| Source, pre-format `PRODUCT_SPEC.md` (`docs/attic/2026-07-22-pre-format/`) | 783,678 | 1.00 |
| Assembled `assembly/PRODUCT_SPEC.md` | 566,366 | 0.723 |

The assembled document holds 276 requirements, 1,301 criteria, and one 196-entry glossary. Measured
bytes-per-criterion: 209.2 (the size ratchet's seed value at the migration-end freeze).

The ratio is a whole-document basis. With the pilot and composing-across-axes units in place the
assembly covers every normative section of the source; only the retired manual index and the relocated
open-decisions block have no converted counterpart, so the ratio is close to a like-for-like
compression of the same text.

## Structure and order

Units are concatenated in the source's own section order (mirroring
`docs/attic/2026-07-22-pre-format/PRODUCT_SPEC.md`), with `what-live-spec-is` opening the document:

| Order | Unit | Source `##` section | Requirements |
|---|---|---|---|
| 1 | what-live-spec-is | What live-spec is | R1..R3 |
| 2 | build-loop-a-intake | The build loop (intake, naming, human exchange) | R4..R36 |
| 3 | build-loop-b-doors-spec-lanes | The build loop (doors, specifying, parallel lanes) | R37..R97 |
| 4 | build-loop-c-prototype-tests-rhythm-publish | The build loop (prototype, tests, rhythm, publishing) | R98..R151 |
| 5 | what-the-human-sends-back | What the human sends back | R152..R159 |
| 6 | when-something-breaks | When something breaks | R160..R167 |
| 7 | pilot | Starting and adopting a project | R168..R188 |
| 8 | agents-together | When agents work together | R189..R197 |
| 9 | rules-and-who-applies | The rules and who applies them | R198..R220 |
| 10 | bounds | What holds the bounds | R221..R257 |
| 11 | composing-across-axes | Composing across axes (the Reference essay) | R258..R276 |

**Title line.** `# live-spec — Product Spec (v4.0.0, 2026-07-22)`. The date sits in the preamble, which
`check-no-history` exempts (the gate scans the body from the first requirement on).

**Requirement renumbering.** Each unit's local `## Requirement N:` headings were renumbered into one
continuous 1..236 sequence with a cumulative per-unit offset. Cross-references between requirements did
not need updating: a mechanical check confirmed that no unit body references another requirement by
number — the format's cross-reference mechanism is the trailing code anchor, which renumbering leaves
untouched. Feature tags (`[feature: F-...]`) ride their scenario heading and are preserved verbatim on
renumber.

**Preamble.** One authored preamble replaces the eleven per-unit preambles. It states what the document
covers, one unified bracket-code legend (E, INV, T, M, A, B, ACT, C, D, S, F, plus the `[target]`,
`[default]`, range, and `[GAP: ...]` markers), and how the keywords read.

**Glossary pooling (ASSEMBLY-NOTES item 5).** The eleven per-unit "Glossary additions" blocks and the
eleven per-unit "carried-terms" sentences collapse into one preamble sentence plus one `## Glossary` of
196 entries. The per-unit carried-terms sentences disappear. With the pilot unit in place, its
glossary supplies the in-document definitions of pack, host, attic, migration chapter, ratchet
manifest, personal profile, settings ladder, and project layers, so those left the preamble's
carried-terms sentence; the remaining foundational method nouns (request, pipeline, spec,
architecture, invariant, guardrail, suite, session, journal, queue, movement, delivery, delivery
report, footprint, profile, resume file) stay named once in the preamble as carrying their base-method
meanings. The converse-direction "every body noun has an entry" is not a machine-checked law
(undecidable), so their absence from the glossary reds no gate.

## Glossary collision resolutions

209 raw glossary entries across the eleven units carry 185 distinct terms; 22 terms collide across two
or more of the nine original conversion units, while the pilot's 25 terms and the composing-across-axes
unit's 5 terms (stateful surface, composition axis, input-capability axis, config-health check,
document provenance) collide with none of the pooled set exactly. Each collision was resolved to one
clearest entry (the format's law 1, one entry per term). Where two entries described the same thing
from different angles, the merged sentence keeps both angles.

| Term | Resolution |
|---|---|
| user story | merged: the split-unit sense (what-live-spec-is) with the "one thing a person does and sees / a wish carrying more is split" sense (build-loop-a). |
| base skill | rules-and-who-applies wording (fuller). |
| working skill | merged and names all ten working skills (the nine plus text-audit, added by the row-458 cleanup below; also settles item 11's five-roles-vs-skills note). |
| target tag | what-live-spec-is wording; "or leg" added to cover build-loop-c's `[target]` on a leg. |
| checkpoint | one entry naming the shared root (a saved resume point) with its two specializations (a planned-work checkpoint; a worker's checkpoint) — the three unit senses reconciled under one name. |
| spec-delta | merged the two build-loop senses with the when-something-breaks "delta" sense; this is the one name (item 2). |
| door | build-loop-b wording (the fuller five-way set plus the labelled-sketch door). |
| work-kind | build-loop-b wording. |
| decision archive | merged (identical intent). |
| regression fence | build-loop-a wording (names the spec-delta). |
| non-goal | build-loop-a wording (fuller). |
| success measure | build-loop-a wording, kept in spec-delta terms. |
| status report | merged the chat-account sense (build-loop-a) with the agent-channel sense (agents-together). |
| lens | rules-and-who-applies wording (carries examples). |
| catch-up walk | merged (identical). |
| seat | one entry unifying build-loop-b (orchestrator judging lane independence) and bounds (the acting turn agent); names senior / senior agent / orchestrator as the source's other words and keeps "seat" throughout (item 12). |
| problem ledger | one entry folding the "workshop's own operational noise" sense (when-something-breaks) into the standard PROBLEMS.md definition (also part of item 9). |
| concurrent-edit fence | merged (identical). |
| grant | merged the session sense (agents-together) with the remote-seat sense (bounds). |
| stranger | merged (Issue/Discussion entry road). |

The `delta` entry from when-something-breaks is dropped; it folds into `spec-delta` (item 2). The
plural `checkpoints` entry from what-live-spec-is is dropped as a duplicate of the pooled `checkpoint`
entry. Two pilot-adjacent near-aliases were reconciled without renaming any body text: the pilot's
`catch-up` (the home section's own entity) keeps its entry, and the build-loop `catch-up walk` entry
was reworded to define the walk in terms of catch-up ("the ordered set of steps a session walks to run
catch-up on an adopted host"), so the compound reads as the run of the entity rather than a second
name; collapsing the compound across its five body occurrences is left as a prose-sweep candidate.

## Glossary additions (the worklist's demanded new entries)

Thirteen new entries were added, each sourced from a unit's own body and each a term the body uses (so
none is a dead glossary entry — verified by `check-vocabulary`): **milestone** (item 3), **gate**
(item 11), **expected-red note** (items 9, 12), **proactivity mode** (item 15), **revisit trigger**,
**Done-when**, **queue-take** (item 17), **deferral test**, **suite-honesty class** (item 18), **open
leg**, **echo-name** (item 13), **verify walk** (item 16), and **orient** (item 9's home pointer — see
the item below). The `senior agent` entry (already present in rules-and-who-applies) was reworded to a
role-pointer at the seat, so it names the same actor rather than competing with the seat entry.

## Declared body sharpens (text changes, with mapping.md kept true)

Two units' criterion or context text changed. Each edit lives in the assembler's `SHARPENS` table,
matched exactly once, and the unit's `mapping.md` was updated so code→text stays true.

1. **item 1 — E-12 → E-20 at R47.1 (build-loop-c).** The publish-checklist criterion cited `[E-12]`
   verbatim from a source mis-anchor; the Formal index homes that fact at `E-20`. Corrected to
   `[E-20, INV-22]`. `build-loop-c-prototype-tests-rhythm-publish/mapping.md` updated: the `E-12` Part-1
   row removed (E-12 is no longer cited in the unit), E-12 removed from the pure-cross-reference list and
   the Publishing header, and the "anchor anomaly" note rewritten to record the assembly correction.
   Code-set impact: none — E-20 already appeared elsewhere in the unit and E-12 elsewhere in the
   document, so the zero-drop set is unchanged.
2. **item 2 — "delta" → "spec-delta" (when-something-breaks).** R1.6 and R1.7 (assembled R160's
   criteria 6 and 7) renamed the artifact "delta" to the one name "spec-delta";
   `when-something-breaks/mapping.md` updated at claim row 9 and in its cross-section glossary note.
3. **item 9 (partial) — four moves enumerated (when-something-breaks R2 / assembled R161 Context).**
   The Context of the class-hunt requirement now names the four moves explicitly (name the class and
   hunt its siblings, check the architecture, check the spec, escalate a boundary call), where the
   criterion calls them a closed set. Context edit, no criterion or code touched.

## The 18 worklist items (the note file carries 18 numbered items; the task brief called it "17")

1. **DONE** — E-12 → E-20 at R47.1; declared sharpen above; mapping.md corrected.
2. **DONE** — "delta" → "spec-delta" as the one name; when-something-breaks renamed; one pooled entry.
3. **DONE** — `milestone` pooled-glossary entry added, sourced from the rhythm body (build-loop-b
   milestone gate + when-something-breaks milestone compaction).
4. **DONE (verified in conversion)** — "harness task list" already reads "harness task panel" and
   "landing report" already reads "delivery report" in the source units; no residual "task list"
   (a queue alias) or "landing report" remains anywhere. Consistent across the assembled document.
5. **DONE** — per-unit carried-terms sentences and glossary blocks collapsed into one preamble sentence
   plus one pooled glossary; the per-unit sentences are gone.
6. **DONE (verified)** — the lane-open reconciliation survived: build-loop-b R55 (assembled R91) reads
   the automatic independence-graph verdict as the seat's own independence judgment, matching R44
   (assembled R80) and INV-49's clause. The "spoken senior word" and "automatic graph verdict" are one
   act, not two, in the shipped text.
7. **DEFERRED** — the Req-19 (part C) member-count alignment (context says one member's net is the
   assertion shape while the criterion names three). Reworking criterion or context prose to align a
   count is a cold-reader-panel sharpen the reader rated non-blocking; a fresh-context prose pass owns
   it better than the assembler. No code or gate is affected. Queue candidate at landing.
8. **DONE (verified)** — feature tags carry no generated-index row. In the assembled document the
   `[feature: F-...]` tags ride their scenario (`## Requirement`) headings, and `build-index.py` indexes
   only criterion-anchored codes, so the F-codes map to headings and resolve there. The Reference section
   states this. All F-codes are present in the document (zero-drop holds).
9. **DONE (glossary + four-moves + orient pointer) / PARTIAL (naming sweep).** `workshop noise` is the
   single glossed artifact name, folded into the problem-ledger entry; `expected-red note` is glossed;
   the four moves are enumerated. Unifying the descriptive prose uses of "operational noise" /
   "operational hiccup" across user stories is left as a prose sweep (they read as ordinary English, and
   the glossed artifact name is already single). The "adoption's orient" home pointer is **DONE** now
   that the pilot (starting-and-adopting) unit is in the assembly: `orient` holds a pooled-glossary
   entry defining it as adoption's opening phase, sourced from the pilot's adoption-phases requirement
   (assembled R177), so the when-something-breaks reference resolves in-document with no body sharpen.
10. **DEFERRED (as the note prescribes)** — the source surface-registry defect (header lists the registry
    as planned while an ownership sentence states the host owns it today) stays GAP-marked in
    what-live-spec-is; the note itself says "at landing open a small queue row." Queue row owed at
    landing; no assembly edit.
11. **DONE** — `gate` pooled-glossary entry added; the working-skill entry now names all ten skills
    (the nine plus text-audit, per the row-458 cleanup below; settling the five-roles-vs-skills identity); the built/planned status vocabulary is stated
    once in the preamble via the `[target]` marker legend.
12. **DONE (glossary) / DEFERRED (Req-4 crit-5 unpack).** `seat`, `expected-red note`, and (via item 9)
    `adoption's orient` context are handled; the seat and expected-red entries are pooled. Unpacking the
    dense R4 crit-5 sentence into two criteria is deferred: splitting a criterion renumbers its case and
    shifts code placement, a structural change the cold-reader panel should drive in a clean context; the
    reader rated it non-blocking. The related/unrelated lane edge at R6 crit 1 reads clearly as shipped.
13. **DONE (verified) / DONE (glossary).** The "first two routes from the third" seam is already reworded
    clearly in the converted what-the-human R3 Context; `open leg`, `beat` (already glossed), and
    `echo-name` resolve in the pooled glossary (`open leg` and `echo-name` added).
14. **DEFERRED** — the two senses of "fence." The compound forms (regression fence, concurrent-edit
    fence, the prototype's one-way fence) are each disambiguated at their glossary or definition site, and
    no bare "fence" was flagged as a blocking finding. Sweeping 53 occurrences to force the "prototype
    fence" compound risks mis-tagging the regression-fence and mechanical-net uses; `check-one-name` does
    not list the pair. Left as a prose sweep; recorded as a quality candidate.
15. **DONE (glossary) / DEFERRED (queue candidate).** `proactivity mode` glossed (its sibling `trust`
    already had an entry); `verify walk` glossed and carried (item 16). The skill-list check's
    narrower-than-headline (fewer-only) trigger stays a queue-row candidate per the note. The
    senior-agent entry is smoothed to a role-pointer at the seat.
16. **DONE (glossary) / NOTED.** `verify walk` is the one pooled name for the verify step/walk/audit; the
    three surface spellings still occur in bodies and are noted as a prose sweep. The liveness "short
    window" at R31.2 (assembled R128) stays a GAP-candidate the reader rated mild — left as-is. The unit
    already uses "prod surface"; "prod file" occurs twice as ordinary phrasing.
17. **DONE (glossary) / NOTED.** `revisit trigger`, `Done-when`, `queue-take` glossed; `worker` and
    `brief` already had entries and are pooled. The roadmap file as the queue's home and the
    provisional-default-versus-guess distinction are stated in the build-loop-a body already; no new
    edit needed.
18. **DONE (glossary) / NOTED.** `deferral test` and `suite-honesty class` glossed; `economy ladder` and
    `delegation accounting` already had entries and are pooled. The three-axes/third-dimension row
    framings and the "no self-certification versus granted own-certification" pairing read consistently in
    the build-loop-b body as shipped; left unchanged.

## Zero-drop proof

A mechanical set-difference over every bracketed code-like token (`PREFIX-suffix`, including the
`F-...` feature codes and the `T-1..T-7` range) between the eleven `section.md` files (the ten
conversion units plus the pilot) and the assembled document:

```
eleven-unit section codes: 345   assembled codes: 345
MISSING (sections − assembled): EMPTY   → zero-drop holds
ADDED   (assembled − sections): EMPTY
```

Both directions are empty. The E-12 → E-20 sharpen did not change the set (both codes pre-existed
elsewhere in the corpus), so the assembled document carries exactly the codes the eleven units carried
— among them the restored `D-6`/`D-7` decision anchors and the composing-across-axes unit's `C-` codes.

## Gate results (run by hand against the assembled document)

The five lints and the seven format gates, run directly from `guardrails/`:

```
check-requirement-shape : OK — matched 1301 of 1301 rows; all 1301 criteria well-shaped across 276 requirements
check-vocabulary        : OK — matched 196 of 196 rows; every glossary term used in the body; no banned coinage
check-one-name          : OK — no known alias present across 11 aliases of 4 artifacts
check-weak-words        : OK — matched 1301 of 1301 rows; no weak word stands with an unfilled slot
check-no-history        : OK — matched 0 of 6306 body lines; no date or provenance marker in the body
build-index (builder)   : INDEX.md == a fresh build off the body (deterministic)
check-index-generated   : OK — matched 333 of 333 rows; committed index equals the fresh build; 333 codes agree body-to-table
check-size-ratchet      : OK — 209.2 bytes/criterion over 1301 criteria; bound not yet seeded (the freeze actor seeds it at 209.2)
```

`check-delta-record` is the delivery-time classifier: it diffs an old requirements-format criteria set
against a new one. No prior requirements-format `PRODUCT_SPEC.md` exists (this assembly is the first
conversion), so there is no baseline `old.md` to diff against and the classifier has nothing to
reconcile at the prototype step. It arms with the rest of the format gates at the conversion delivery
(INV-270), reading the last freeze's index as its baseline; at that point every code is declared `new`
under the migration delta record. No red is possible against an absent baseline here.

## The generated index

`scripts/build-index.py` was run against the assembled document; its 333-row code-to-location table is
written to `assembly/INDEX.md` and embedded verbatim in the document's `## Reference` section. It is
output only — `check-index-generated` confirms the embedded/committed table equals a fresh build and
agrees body-to-table both ways. Feature codes carry no row (they live on scenario headings).

## Seams

No seam needed a human taste call; each cross-unit choice was derived from the sources and is cited
above. The closest to a taste fork, recorded for the record:

- **checkpoint** carries three distinct senses across three units (a resume point; a planned-work group
  with a status; a worker's heartbeat file). Rather than mint three names, the pooled entry names the
  shared root and its two specializations under the one word, since all three sources describe a saved
  resume state. Settled by the three units' own bodies; a future pass may choose to split the name.
- **seat / senior agent** are one actor under two words in the sources. Settled by the build-loop-b seat
  entry, which explicitly declares "seat" the one name and names "senior agent" as the source's other
  word; the senior-agent entry is kept as a role-pointer, not a competing definition.

## Definitional-frame cleanup (ROADMAP row 445)

`scripts/spec-style-lint.py` gained a `_rather_instead_scissors` arm that flags a definitional
contrast frame of the shape "X rather than Y" / "X instead of Y" (a copula/naming lead, a
determiner-both-sides rename, or a parallel by/as/for) — the same "name a thing by denying its
neighbour" ban the dash/comma scissors arm already held, in its two English prose conjunctions. Run
with the arm the assembled document carried **90** such frames. The fix lands in the units (the
assembly is generated by `assemble.py`), so each frame was rewritten in its owning unit to a positive
sentence stating what the thing is; meaning, force, and every trailing code anchor were kept exactly.
A boundary that carried real information was given its own plain clause; where the positive already
implied the rejected alternative, the "rather than Y" tail was dropped.

**Per-unit fix counts** (line basis; two lines carried two frames each):

| Unit | frames fixed |
|---|---:|
| what-live-spec-is | 4 |
| build-loop-a-intake | 7 |
| build-loop-b-doors-spec-lanes | 15 |
| build-loop-c-prototype-tests-rhythm-publish | 19 (20 frames — R124's crit carried two) |
| what-the-human-sends-back | 3 |
| when-something-breaks | 5 |
| pilot | 5 |
| agents-together | 4 |
| rules-and-who-applies | 6 |
| bounds | 17 (18 frames — R229's user story carried two) |
| composing-across-axes | 5 |
| **units total** | **90 lines / 92 frames** |

**Four frames live in `assemble.py`'s authored regions, not a unit body**, and were fixed there
(recorded here because they are outside the units and outside the zero-drop token set):

- the preamble's `[target]`-marker legend — "planned rather than built" → "promised but not yet built";
- the `non-goal` glossary override — "an absence reads as a decision rather than an oversight" → "a
  deliberate absence reads as a decision";
- the `target tag` glossary override — "planned rather than built" → "promised but not yet built";
- the `deferral test` glossary addition — "run before a row is parked rather than worked" → "run
  before any row is parked".

The three unit-head frames the assembler overrides or re-authors (the what-live-spec-is legend and its
`target tag` entry, the what-the-human `target tag` entry, the build-loop-a `non-goal` entry) were
also cleaned in the units for unit-level cleanliness, so a unit re-lint is clean too.

**text-audit added (ROADMAP row 458).** Riding this landing, the pack's tenth working skill,
**text-audit**, entered the spec: the `working skill` glossary entry (its override in `assemble.py`
and its unit-head form in what-live-spec-is) now names it and states what it is — the audit-and-fix
loop for human-facing texts (mechanical lints, then fresh zero-context cold reads, fixes made at the
source, until two consecutive clean reads). It is named the way the other nine skills are, inside the
definition's prose rather than as a glossary headword, so the closed-vocabulary and one-name gates stay
green with no new entry and no criterion change. Recorded as a declared sharpen in
`what-live-spec-is/mapping.md`.

**Two declared sharpens touched a unit `mapping.md` claim row** (a Part-3 row that quoted the old
criterion wording): build-loop-a-intake claim 121 ("commentable rather than a read-only wall" →
"commentable and open", R28.2) and when-something-breaks claim 43 ("lands as a ledger line rather than
a silent retry" → "lands as a recorded ledger line").

**ARCHITECTURE.md.** The arm found **4** definitional frames there (build-pipeline, guardrails —
carrying two, design-reviewer, and the F-feature-map red-case row). Each was rewritten register-only,
meaning exact. A pin check first grepped `tests/` and `guardrails/` for each sentence's distinctive
fragments; **none was pinned**, so each was edited in place with no pinning file touched:

| Node / row | Old | New |
|---|---|---|
| build-pipeline (INV-235) | "the spec the law's one home rather than a skill-prose fork" | "the spec the law's one home, with no skill-prose fork" |
| guardrails (INV-213) | "a documented owner-run install step rather than an auto-wire into a running session's Stop hook" | "…install step, kept out of any auto-wire into a running session's Stop hook" |
| guardrails (INV-241) | "the ordered tool_use events in the transcript rather than the reply text" | "the ordered tool_use events in the transcript, the reply text set aside" |
| design-reviewer (INV-156) | "landing its verdict in the landing record rather than a dated file of the class" | "landing its verdict in the landing record, keeping no dated file of the class" |
| F-feature-map red-case cell | "an answer from memory rather than the read documents" | "an answer built from memory, bypassing the read documents" |

**Re-assembly and gates after the cleanup.** `assemble.py` was re-run and is byte-reproducible (a
second run yields an identical `PRODUCT_SPEC.md` and `INDEX.md`). Numbers held: 276 requirements, 1,301
criteria, one 196-entry glossary (text-audit added no headword), 565,709 bytes (down from 566,366 as
the register tightened), 208.9 bytes/criterion. The five lints and seven format gates re-run clean:

```
check-requirement-shape : OK — 1301 of 1301 criteria well-shaped across 276 requirements
check-vocabulary        : OK — 196 of 196; every term used; no banned coinage (text-audit is not a headword)
check-one-name          : OK — no known alias across 11 aliases of 4 artifacts
check-weak-words        : OK — 1301 of 1301; no weak word with an unfilled slot
check-no-history        : OK — 0 of 6306 body lines carry a date or provenance marker
build-index (builder)   : INDEX.md == a fresh build off the body (deterministic)
check-index-generated   : OK — 333 of 333 rows; committed index equals the fresh build
check-size-ratchet      : OK — 208.9 bytes/criterion; bound not yet seeded
```

**Zero-drop recount holds at 345/345, both directions empty** (DELTA's token method: literal
`PREFIX-number` tokens plus the ten `F-…` feature codes). The cleanup touched no bracketed code anchor,
so the code set is unchanged from before the cleanup.

**Definitional-frame residual: zero.** The new arm now flags **0** frames on the assembled document and
**0** on ARCHITECTURE.md (90 → 0 and 4 → 0). The legacy dash/comma arm's residuals — 16 `scissors`
errors, one `negation-opener` error, one `second-person` warning — were the last register debt on
`PRODUCT_SPEC.md`; the final register pass below clears them, and `spec-style-lint.py` now reports **0
errors, 0 warnings** on the assembled document. ARCHITECTURE.md stays fully clean (0 errors, 0 warnings).

## Final register pass: the legacy scissors arm (ROADMAP row 445)

The definitional-frame cleanup above closed the `rather than` / `instead of` arm; this pass closes the
older dash/comma `scissors` arm's residuals, the last register debt on the assembled document. All fixes
land in the owning units (the assembly is generated), meaning and every trailing code anchor kept exactly;
`assemble.py` was re-run and is byte-reproducible.

**Ten `Case: X, not Y` sub-headings → positive case names.** The case-naming convention itself had
carried the banned contrast frame; each heading now names what the case IS, and the boundary its old
tail carried already lives in the case body (the criterion cited in each row states it in its own
sentence). Renames:

| Unit | Old heading | New heading | Boundary now in body |
|---|---|---|---|
| build-loop-a-intake (R8) | `Case: a settled fork is derived, not asked` | `Case: a settled fork is derived` | crit 1 "offering no fork" |
| build-loop-a-intake (R9) | `Case: a cut moves scope, not order` | `Case: a cut moves scope alone` | crit 2 "only priority moves the lane order" |
| build-loop-a-intake (R26) | `Case: the harness panel is a courtesy, not the home` | `Case: the harness panel is a courtesy view` | crit 3 "shall not make it the home of the status" |
| build-loop-b-doors-spec-lanes (R41-footprint) | `Case: disagreement is routed, not silently resolved` | `Case: disagreement is routed to its owning home` | crit 5 "rather than pick a winner in silence" |
| build-loop-c-prototype-tests-rhythm-publish (R4) | `Case: the earned feature is specced, not merged` | `Case: the earned feature is specced fresh` | crit 1 "shall not merge the sketch's code" |
| agents-together (R8-messages) | `Case: a capability is used, not copied` | `Case: a capability is reached across its zone` | crit 14 "rather than keep a local copy of it" |
| rules-and-who-applies (R6) | `Case: a tighter host line is recorded, not assumed` | `Case: a tighter host line is recorded` | crit 3 "rather than assume it" |
| rules-and-who-applies (R11) | `Case: the proposal reads the work, not its size` | `Case: the proposal reads the work` | crit 2 "the size class a coarse prior only" |
| bounds (R8) | `Case: config, not re-implementation` | `Case: the checks attach by config` | Context "attached without editing check code" |
| bounds (R11) | `Case: a Stop-hook notice, not a push gate` | `Case: a Stop-hook notice` | crit 5 "a chat reply is already emitted and cannot be blocked" |

**Three legacy comma/dash appositives → positive statements.**

- build-loop-b crit (total order) — "read later by a total order, not by wall-clock:" → "read later by a
  total order that git ancestry defines: … ; a wall-clock timestamp never enters the ordering." The
  wall-clock boundary rides its own clause as an action prohibition (R4-lawful). `[INV-2, INV-117]` kept.
- rules-and-who-applies R11 Context — "proposes its tier from what the work is, not its size alone" →
  "proposes its tier from what the work is, its size only a coarse prior" (matches crit 2's "coarse prior
  only").
- bounds R1 Context — "a written acceptance — never a paraphrase." → "a written acceptance. A paraphrase
  cannot serve as that goal." (matches this unit's mapping claim 1, "a paraphrase cannot serve").

**One negation-opener heading → positive.** build-loop-c Requirement 16 heading "A check that looked at
nothing is not a pass" → "A check earns its pass only over a non-empty set"; the "empty set is not a
pass" boundary already lives in the Context and the User Story. Its mapping claim 49 (a claim row that
glossed the old heading) was updated to "A check earns its pass only over a non-empty input set; …" to
keep the mapping true; it still maps to R16.1, whose criterion text was untouched.

**One second-person warning → third-person, register-fixed.** build-loop-c "`Case: erase what you
create`" → "`Case: a test erases what it creates`". Verdict: **fix, not a lawful specimen.** The spec
format is the third-person requirements register ("the system *shall* …"), naming actors, not a skill
addressing its operating agent; the criterion body and the User Story already read "every test remove
what it creates" / "each test to erase what it creates", so the second person was a leak, not the
documented skill-to-agent voice. The new heading matches the body.

**Two specimen lines (they *describe* the banned frame verbatim) → backtick-wrapped, meaning unchanged.**
Both quoted the `"X, not Y"` frame as data the spec cites, and the style lint's `scissors` arm scrubs
inline code, so wrapping the quoted frame in backticks makes each lawful without touching its meaning:
build-loop-a-intake (the chat-law injection criterion, "the `"X, not Y"` shape") and
build-loop-c-prototype-tests-rhythm-publish (the contrast-frame-ban binding criterion, "the `"X, not Y"`
frame"). Both were unbackticked before; both carry their trailing anchors (`[INV-28, INV-69, INV-137]`,
`[INV-166]`) unchanged.

**`docs/spec-format.md`: no change.** The format's home already prescribes positive case naming — "A case
is one bold line **naming a situation**" — and its comprehension-gate list already bans "no
contrast-by-denial frames". Nothing in it prescribes or exemplifies the `Case: X, not Y` shape, so no
definition change was owed.

**Re-assembly and gates after the final pass.** `assemble.py` re-run, byte-reproducible (a second run
yields an identical `PRODUCT_SPEC.md` and `INDEX.md`). Numbers held: 276 requirements, 1,301 criteria,
one 196-entry glossary, **565,735 bytes** (up 26 from 565,709 — the added wall-clock clause and the
backticks net a few bytes), 209.0 bytes/criterion. `spec-style-lint.py` on the assembly: **0 errors, 0
warnings** (16 scissors + 1 negation-opener + 1 second-person → 0). The five lints and the format gates
re-run clean:

```
spec-style-lint         : OK — 0 errors, 0 warnings (was 16 errors + 1 warning)
check-requirement-shape : OK — 1301 of 1301 criteria well-shaped across 276 requirements
check-vocabulary        : OK — 196 of 196; every term used; no banned coinage
check-one-name          : OK — no known alias across 11 aliases of 4 artifacts
check-weak-words        : OK — 1301 of 1301; no weak word with an unfilled slot
check-no-history        : OK — 0 of 6306 body lines carry a date or provenance marker
build-index (builder)   : INDEX.md == a fresh build off the body (deterministic)
check-index-generated   : OK — 333 of 333 rows; committed index equals the fresh build
check-index-prose       : OK — 342 Formal-index anchors, each carried in its home prose
check-size-ratchet      : OK — 209.0 bytes/criterion; bound not yet seeded
check-delta-record      : N/A — no prior requirements-format baseline; arms at the conversion delivery
```

**Zero-drop recount holds, both directions empty.** The pass touched no bracketed code anchor (each of
the eighteen edits changed prose only — headings, a Context sentence, one criterion's boundary clause,
two backtick wraps — and every criterion kept its trailing anchors exactly), so the assembled code set is
unchanged from the count recorded above; the section-to-assembly set-difference is EMPTY in both
directions.

## Prover MUST-FIX wave (row-445 full audit, findings F1–F8)

The fresh clean-context FULL audit of the promoted 4.0.0 document (record
`docs/prover/2026-07-22-row445-4.0.0-full-audit.md`) returned LANDS WITH FIXES: eight MUST-FIX
findings. This wave lands all eight in the owning units, re-assembles, and re-proves. Every text
change is a declared sharpen recorded in the owning unit's `mapping.md`; the assembly becomes
twelve units.

**F1 — the false GAP at R160.3.** The GAP claimed a bug's critical priority is undecidable while
R9.4 states the three critical conditions ([INV-12]). The GAP line is deleted and the criterion
sharpened to cite INV-12's conditions directly (when-something-breaks R1.3; its `GAPS.md` G1 entry
retired as false). The document's GAP census drops by one.

**F2 — the cross-link-mode glossary entry.** The pooled entry defined the mode as a whole-document
pass, the reverse of R66's own text. Rewritten in build-loop-b's head to R66's meaning: the
seam-scoped pass at a surface add carrying one mandatory whole-document step, the
enumeration-and-quantifier re-verify.

**F3 — one name for the acting seat.** The body's 34 "senior agent" occurrences (rules-and-who-applies
31, build-loop-c 2, build-loop-b 1 — the last being the seat glossary entry's own source-alias
recital, kept) are swept to "the seat"; every occurrence named the same actor, judged one by one.
The duplicate `senior agent` glossary entry is dropped from both rules-and-who-applies' head and
the assembly's ADDITIONS list; the pooled `seat` entry (which records the source's other names)
is the one home. The glossary's "keeps the one name seat throughout" claim is now true.

**F4 — the description field's home.** R191.4, its Context, R191.7, and the `description field`
glossary entry still claimed a dedicated Formal-index field. All four are rewritten to the INV-271
decision: the criteria and the glossary are the authored home, the generated table carries
locations only, and `check-description-field.py` retires with that stated successor (agents-together
R3; R3.4 gains INV-271 beside INV-239).

**F5 — the document's self-description.** The intro (assembly-authored) is rewritten to the real
shape: the body is a flat list of requirements; a `[feature: F-...]`-tagged heading is a
person-facing scenario; "ten assembled sections" becomes "twelve". The `scenario` glossary entry
(what-the-human-sends-back) gets the same truth pass.

**F6 — the marker conventions the body now practices.** The two bare in-bracket `target` tokens
(R102.2, R102.4) move onto `[target]` lines of their own per the header convention — the only two
in the corpus (grep-verified). All sixteen architecture features now carry `[feature: F-...]`
heading tags: `F-wish` moved off R4.4's anchor list onto its owning heading; `F-bootstrap`,
`F-adoption`, `F-catchup`, `F-onboarding`, `F-pair` moved off the pilot's User Story brackets onto
their headings; `F-prototype`, `F-publish`, `F-roster`, `F-contract`, `F-agent-ask`,
`F-agent-birth` newly tagged on their owning headings. No F-code rides a criterion or User Story
bracket anywhere; the two-way feature trace (R224.2) has a heading for every ARCHITECTURE.md row.
`build-index.py` re-verified deterministic (two runs byte-equal) and the index gate green.

**F7 — ARCHITECTURE.md reconciled to 4.0.0.** The two Formal-index references are repointed (the
node-ownership preamble to the generated code-to-location table; the decisions section to
DECISIONS.md's D-1/D-6/D-7); ten skills becomes eleven; text-audit gains its architecture home — a
node row carrying the comprehension-gate codes INV-266..268 and the skill-roster ownership, pinned
to `skills/text-audit/SKILL.md`; the header reads "Last reconciled with the spec: 2026-07-23".

**F8 — the format-law requirements enter the spec.** The stage-1-approved delta (source
`docs/prover/2026-07-22-row445-spec-format-delta.md` + `docs/spec-format.md`) is authored as the
twelfth unit, `conversion/format-laws/` — six requirements, 57 criteria (the delta's 56 plus a
panel-added style-lint red condition), 34 glossary additions, homing all 22 codes INV-250..271 with
zero drop (mapping.md's `comm` empty both ways). Inserted into the assembly order right after
composing-across-axes, last before the Reference tail — meta-law about the document itself. The
unit ran the five lints clean and an eight-round cold-read panel (two fresh zero-context readers
per round, every blocking finding fixed at source; round 8's two reads both zero-blocking — the
two consecutive clean reads the comprehension gate demands). The panel's own finds folded back:
the criterion-form rule aligned with the practice the shape gate holds, the arming event one-named
("conversion delivery"), the R3.9 provenance tail moved to the journal per the section's own
no-history law, and vocabulary closure (entity, evaluative phrase, conversion delivery glossed).

**One restoration folded in (re-pin sweep finding).** The re-pin sweep's mapping-first audit of
`tests/test_agent_channels.py` surfaced one genuine content loss in the conversion: the recorded
owner decision that agents' zones may overlap (no forced disjointness, two cards claiming one area
both legal) and its consequence that no uniqueness check over zone claims is built. Restored as
agents-together R8's appended case (assembled R196.19–.20, [INV-197, INV-225]) — appended, so no
pinned criterion number moves.

### Numbers after the wave

```
units                   : 12 (was 11)
bytes                   : 587,179 (was 565,735)
requirements            : 282 (was 276)
criteria                : 1,360 (was 1,301)
glossary entries        : 229 (was 196)
generated-index codes   : 355 (was 333) — the 22 format-law codes INV-250..271
zero-drop recount       : 373/373 bracketed code tokens, twelve units vs assembled body,
                          set-difference EMPTY both ways (was 345/345 over eleven; +22 INV codes
                          +6 newly heading-tagged F-codes)
bytes-per-criterion     : 206.9 — BELOW the recorded 209.0 bound; the freeze actor lowers the
                          bound to 206.9 at freeze
byte-reproducible       : yes — two assemble.py runs byte-identical
```

### Gate results after the wave (run against the assembled document)

```
spec-style-lint         : OK — 0 errors, 0 warnings
check-requirement-shape : OK — 1360 of 1360 criteria well-shaped across 282 requirements
check-vocabulary        : OK — 229 of 229; every term used in the body; no banned coinage
check-one-name          : OK — no known alias across 13 aliases of 5 artifacts
check-weak-words        : OK — 1360 of 1360; no weak word with an unfilled slot
check-no-history        : OK — 0 of 6524 body lines carry a date or provenance marker
build-index (builder)   : deterministic — two runs byte-equal
check-index-generated   : OK — 355 of 355 rows; committed index equals the fresh build
check-size-ratchet      : OK — 206.9 bytes/criterion, at or below the 209.0 bound
check-delta-record      : N/A — arms at the conversion delivery per INV-270
```

The root PRODUCT_SPEC.md promotion of this re-assembly rides the landing step that owns it (the
re-pin sweep owns tests/ and the freeze; the fixed assembly promotes after both waves finish).

## Final restoration wave (the re-pin sweep's mapping-confirmed drops)

The re-pin sweep's final mapping audit (`prototype/2026-07-22-spec-format/REPIN-LOG.md`, the PASS-2
final-suite 17-red list) named fourteen mapping-confirmed content drops the conversion lost, plus one
deliberate signal. This wave restores each as criteria in the owning conversion unit — appended within
the requirement where possible so pinned criterion numbers stay — and re-assembles. Every restored
claim reuses codes already in the corpus, so the zero-drop code set is unchanged; each touched unit's
`mapping.md` gains a declared-addition row. No item was journal-bound rationale (the sweep pre-filtered
those): all fourteen carried a live behavioural claim, so none was skipped.

**The fourteen restored drops:**

1. **Forward-binding member enumeration + INV-159 bracket** (build-loop-c R19, assembled R116). The
   Context now enumerates the nine suite-honesty members (INV-77, INV-78, INV-79, INV-80, INV-100,
   INV-102, INV-155, INV-157, INV-158) and states the forward-binding law inline ("The class binds
   forward [INV-159]"); R19.3 co-cites INV-159, matching the sibling class INV-180's own bracket.
2. **Inbox-deposit fence carve-out** (bounds R33.7 + R36.7, assembled R253/R256). The live-session
   stand-down holds no bar over the one-file deposit (R33.7, `[INV-112, INV-82]`); a diff of exactly
   one new inbox file owes the fence and no re-check record, a diff carrying more riding the full gate
   (R36.7, `[INV-11, INV-112]`).
3. **`[target]` markers for nine promised anchors + the design-sync wiring note.** Own-line `[target]`
   markers restored under criteria citing E-7, A-6, E-18 (what-live-spec-is R1.4, the "mark as planned"
   criterion), INV-21 (build-loop-b R40.5), INV-198 (R49.5), INV-199 (R50.5), INV-201 (R52.6), INV-185
   (agents R6.15), and INV-244 (composing R8.15) — six of them appended as short single-anchor "the
   promised leg" criteria so each marker sits under a criterion citing exactly its anchor. The observed
   marker set is now exactly the twelve `TestTargetOwnership` owns: {E-6, E-7, E-10, E-18, INV-17,
   INV-21, A-6, INV-185, INV-198, INV-199, INV-201, INV-244}. The design-sync wiring note "Design-sync
   [target: the machine; the wiring is live]" and its E-7 declared-scope link were restored in bounds
   R28's Context.
4. **M-1 line-count** (build-loop-c R33.9): "the audit report states the line count" restored to the
   milestone gate's thin-loader item.
5–8. **ProblemLedger ×4:** adversarial-verify option — the method-edit carve-out "a rule whose meaning
   changed" (rules R16.3); narration-three-teeth — "a station a delegated worker closed becomes the
   senior's beat" and "token and test counts stay bookkeeping" (build-loop-a R19.9); offline-window —
   the four dropped edge rules, never a guess dressed as a promise / a window off its spoken range / a
   chat line awaiting his return, never a summons / no offline sentence fires when the very next beat
   needs the human (build-loop-a R19.10); snapshot-design — the `.live-spec/snapshot/` directory
   literal (bounds R27.3).
9. **Held-for-milestone state** (build-loop-b R44.8): T-18's distinct held-for-milestone lane state,
   named apart from bug-parked because nothing failed.
10. **Tight-rung re-apply** (rules R22.7): the batch reverts to its last green base and re-applies the
    clean landings, so `HEAD` never sits red across a breakpoint.
11. **Two-questions-never-collapsed** (build-loop-c R42.2): "one question per gap".

**The deliberate signal (DEFECT-1):** bounds R4.3 / R4.4 (INV-132) restated from the retired
third-level-heading tag-or-marker convention to the convention the document actually practices — the
feature tag on the requirement heading, and a promised leg not yet built taking a `[target]` marker on
its own line.

**Two needles carry the format's own laws, not the pre-format wording.** The offline rule's "blocked on
his word alone" is carried as "blocked on the human's word alone" — `check-no-history` bans the
recorded-word marker "his word" (INV-253). "HEAD never sits red" is carried as "`HEAD` never sits red"
— the caps law (INV-251) keeps a git ref backticked. Both are register conversions the eventual tests/
re-pin absorbs, the restored behaviour itself being present in full.

### Numbers after the wave

```
requirements            : 282 (unchanged)
criteria                : 1,372 (was 1,360 — twelve appended restoration criteria)
glossary entries        : 229 (unchanged)
generated-index codes   : 355 (unchanged — every restored anchor pre-existed in the corpus)
bytes                   : 590,695 (was 587,179)
bytes-per-criterion     : 206.8 — at or below the 206.9 ratchet bound (the freeze lowers it to 206.8)
zero-drop recount       : 373/373 bracketed code tokens, twelve units vs assembled body,
                          set-difference EMPTY both ways (unchanged — no code added or dropped)
byte-reproducible       : yes — two assemble.py runs byte-identical (PRODUCT_SPEC.md and INDEX.md)
```

### Gate results after the wave (run against the assembled document)

```
spec-style-lint         : OK — 0 errors, 0 warnings
check-requirement-shape : OK — 1372 of 1372 criteria well-shaped across 282 requirements
check-vocabulary        : OK — 229 of 229; every term used in the body; no banned coinage
check-one-name          : OK — no known alias across 13 aliases of 5 artifacts
check-weak-words        : OK — 1372 of 1372; no weak word with an unfilled slot
check-no-history        : OK — 0 of 6580 body lines carry a date or provenance marker
build-index (builder)   : deterministic — a fresh build equals the committed INDEX.md
check-index-generated   : OK — 355 of 355 rows; committed index equals the fresh build
check-size-ratchet      : OK — 206.8 bytes/criterion, at or below the 206.9 bound
check-delta-record      : N/A — no prior requirements-format baseline; arms at the conversion delivery
```

The root PRODUCT_SPEC.md promotion and the tests/ re-pin of the seventeen reds ride the landing step
that owns them; this wave restores the content in the conversion units and re-assembles, leaving the
promotion and the re-pin to their owner.
