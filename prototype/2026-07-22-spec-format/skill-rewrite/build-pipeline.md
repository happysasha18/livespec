# build-pipeline — register rewrite notes (2026-07-22)

Register-only rewrite of the build-pipeline skill. Every rule/station/step keeps its exact meaning,
scope, and force; code anchors (INV-x, T-x, E-x, ACT-x, M-x) unchanged; frontmatter description trigger
semantics unchanged; base-rule references by number unchanged.

Files in write set: `skills/build-pipeline/SKILL.md`, `README.md`, and all `references/*.md`.

## Pinned strings changed (test not edited — records for a follow-on to update the pin)

1. **`tests/test_traceability.py`** (test_craft_ladder, line 1106)
   - OLD: `The craft ladder — whose head you wear at each step`
   - NEW: `The craft ladder — which craft's standards judge each step`
   - Reason: "whose head you wear" is a coined metaphor; replaced with the plain mechanism.

2. **`tests/test_class_hunt.py`** (line 51, `assertIn("four moves, not one", bp)`)
   - OLD: `A confirmed bug drives a class hunt before it closes (SPEC INV-124) —\n  four moves, not one:`
   - NEW: `A confirmed bug drives a class hunt before it closes (SPEC INV-124). The hunt is four moves:`
   - Reason: "four moves, not one" is contrast-by-denial (drama); the four enumerated moves carry the force positively.

No other pinned needle was changed. Verified still present verbatim after the rewrite:
`a strong product manager`, `QA automation lead`, `the visitor's own fresh eyes, the builder's own view
set aside`, `a careful release hand`, `Trains, one pen`, `HALT list`, `craft's standards` — all intact.

The `wish door` coinage removed from `request-kind-table.md` line 14 is NOT a skill-content pin: the only
tests carrying that literal are `test_preshow_register_lint.py` / `test_register_judge.py`, which hold
their OWN lint fixtures, not the skill text. Editing the skill does not touch them.

## Counts

- Contrast-by-denial (scissors) fixed: **30**
  - README.md: 4 (`not the code`, `not the delta`, `instead of restarting`, `not at the next minor bump`)
  - SKILL.md: 20 (`footprint, not the size`; `not a new net`; `four moves, not one`; `is not a pins-only
    change`; `not just its own`; `NUMBERS, not only names`; `instead of drifting behind it`; `derived,
    never just filled`; `is a defect, not a pass`; `not an option the release pass may waive`; `never
    instead of the in-session show`; `checkable instead of habitual`; `surfaced rather than improvised`;
    `dropped rather than sent`; `asks rather than guessing the boundary`; `judging the design rather than
    verifying it`; `resumes rather than restarts`; `rather than as a per-project patch`; `rather than
    guessing past ambiguity`; `continuously rather than once per MINOR`)
  - references: 6 (guardrails-catalog: `instead of a hand-list`, `not only the surface where it was born`,
    `rather than under a human's thumb`; minor-bump-gate: `not only at the milestone`, `rather than an
    instant in-place fix`; delegation-protocol: `not a second home`)
- Coined-metaphor / drama / inflation fixed (register, beyond scissors): **11**
  - `whose head you wear` → `which craft's standards judge` (heading, pinned)
  - `The hat each artifact was made under` → `The craft each artifact was made under`
  - `The craft wears the work-KIND's face` → `The craft takes the work-KIND's form`
  - `the pipeline's TEETH` → `the pipeline's mechanical enforcement` (heading) + `guidance and teeth
    agree` → `guidance and enforcement agree`
  - `the defect this line kills` → `the defect this line prevents`
  - `Five full packs once died on a failure` → `Five full packs once failed on a problem`
  - `the footgun that once closed` → `the mistake that once closed`
  - `shortcuts that kill the method` → `shortcuts that break the method` (SKILL.md + excuses-table.md)
  - `the senior drowning in junior work` → `the senior buried in junior work`
  - `rather than under a human's thumb` → plain mechanism ("so a human's review is not what has to
    catch it")
  - `the wish door` → `the door` (request-kind-table.md; forced by the register lint)
- Register-lint findings fixed: **1** (`en-wish-door` in request-kind-table.md line 14)

## Verify

- `scripts/preshow-register-lint.py` on all nine files: **OK — clean** (no coined metaphor, calque, or
  transliterated pack term).
- Post-rewrite grep for ` — not `, `, not `, `rather than`, `instead of` across all files: **zero
  contrast-by-denial hits.** Remaining `not`-hits are lawful scope-exclusion lists, judged and kept:
  - SKILL.md lines 155-156: the "When NOT to run it" exclusion list (`not for pure research…`, `not for a
    SEE/TRY ask`) — scope exclusions, not defining-by-denied-neighbour.
  - request-kind-table.md line 18: `not the agent's own output` — a table-cell category exclusion.
  - SKILL.md line 361: `a wording-only edit that changes no rule's meaning is not a method edit` — a
    category exclusion (scope of "method edit"), not a definitional contrast.

## Cold-read rounds

- **Round 1:** fresh zero-context cold-reader spawned. It reported one BLOCKING finding introduced by
  this rewrite: the reference doc `guardrails-catalog.md` line 3 pointed at `SKILL.md`'s old heading
  "Guardrails — the pipeline's TEETH", which the rewrite renamed to "…mechanical enforcement". FIXED —
  the pointer now resolves.
  - The cold-reader also flagged several BLOCKING reading-stops that are PRE-EXISTING and not introduced
    by the register pass — each is a forward-reference or a dense technical clause whose fix would require
    reordering the document or rewording a pinned technical gate, both out of scope for a register-only
    rewrite that must preserve meaning and anchors: (a) "door" used at lines 20/29 before the intake line
    grounds it; (b) "capture echo: heard · door · name · row · place on the map" (line 49, grounded inline
    by the five-token list that follows); (c) the "departures board / rolling lane" vocabulary at lines
    94–98, ~370 lines before the "Trains, one pen" section introduces it; (d) "load-bearing token identity
    … modulo the per-chunk named deltas" (line 148, the INV-114/INV-111 restructure-merge gate — precise
    pinned technical language). These are recorded, not changed.
- **Round 2 (confirming):** register lint re-run clean on all files; the fixed cross-reference resolves;
  no rewritten sentence was flagged BLOCKING by the cold-reader.

## Sentences left unchanged because rewriting risked meaning

- **SKILL.md line 38 / test_traceability pin:** `the visitor's own fresh eyes, the builder's own view set
  aside`. Mildly poetic but its meaning (verify with a fresh perspective, setting the builder's
  familiarity aside) is clear and grounded; pinned verbatim in test_traceability. Left to avoid meaning
  drift and an extra pin break for a low-value gain.
- **"Trains, one pen" and the pen / trains / departures-board vocabulary** (Trains section, SKILL.md).
  Established, consistently-used pack domain terms, pinned by test_traceability (`Trains, one pen`). "pen"
  is grounded shortly after first use ("Every shared-doc edit, the integration, and the closing of a row
  take the pen one lane at a time"). De-coining the whole system risks both meaning and pins; left in
  place as established vocabulary.
- **"the door" coinage** (the change's entry classification). Left as an established domain term; grounded
  at first use by the immediately-following enumeration of its values (feature · bug · refactor ·
  docs-only · skip).
- **The mega-sentences** (e.g. commit & show, step 9, SKILL.md line ~385; the delegation block, lines
  ~514-532). Their internal banned patterns were fixed in place; full SVO one-idea-per-sentence
  restructuring was NOT attempted — splitting these anchor-dense, pin-dense sentences risked altering
  meaning, scope, or a pinned needle. Register bar met on the banned-pattern classes; structural
  splitting deferred as meaning-risky.
