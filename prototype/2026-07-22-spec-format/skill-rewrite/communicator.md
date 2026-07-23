# communicator — register rewrite notes (2026-07-22)

Register-only pass over the `communicator` skill. Every rule kept its exact meaning, scope, and force;
code anchors (INV-x, rule-N, base-rule-N), the frontmatter trigger semantics, and base-rule references by
number all stayed. Write set: `skills/communicator/{SKILL.md, README.md, references/writing-register.md,
references/field-examples.md}`.

## Counts

- **Contrast-by-denial frames rewritten into positive statements: 8**
  - SKILL.md — "is a record, not a message" (rule 8)
  - SKILL.md — "arrives as a new wish, not a reopening" (rule 10)
  - SKILL.md — rule-15 summary title: em-dash "— never name a thing…" changed to a period "…too*. Never name a thing…"
  - SKILL.md — "in front of you, not from memory" (pre-report walk step 1)
  - SKILL.md — "a BLOCK, not a warning" (pre-report walk step 4)
  - SKILL.md — "rather than learning at the next report" (rule 12, critical-echo)
  - SKILL.md — "done instead of asked" (question-scan gate)
  - field-examples.md — label "A beat, not silence" → "A beat breaks a silent stretch"
- **Negation-opener rewritten: 1** — README.md "Not about code. It's about the exchange." → "It works on
  the exchange with a human. Code is a separate concern."
- **Register-lint leak fixed: 1** — field-examples.md Russian leave-word example, transliterated pack term
  «воркера» → «фоновые задачи» (the profile's `language.no-calques`).
- **Other plainness fixes: 2** — SKILL.md capture-echo gloss "a wish hears itself land" → "the human hears
  the caught request read back"; coined verb "a wish is intaken" → "a wish is taken in".

## Lint verdict

- `scripts/spec-style-lint.py` (the scissors/negation-opener authority rule 15 cites): **all four files now
  clear** of `[scissors]` and `[negation-opener]` errors (baseline: SKILL.md had scissors on lines 197,
  326, 431, 446, 456; field-examples on line 19; README negation-opener on line 5).
- `scripts/preshow-register-lint.py`: README, writing-register, field-examples all **OK**. SKILL.md still
  reports 9 hits, **all lawful and all pre-existing** (none introduced by this pass):
  - Lines 211, 459, 460 — QUOTED SPECIMENS: banned patterns cited inside the rules that ban them
    ("we say so plainly" / «честно говоря» / «из честного» in rule 8; "the wish door", "work lean",
    «швы с соседями», «пайплайн» in pre-report-walk step 4). Lawful per the task's specimen exception.
  - Lines 220, 221 — "pipeline station": the skill's own defined pipeline-step vocabulary, grounded in
    place (line 221 lists every station spec→prove→…→commit) and normatively instructed by rule 9. It is
    a doc term, which the lint's own docstring permits ("internal coinages live in the DOCS only").
- Line budget: SKILL.md at **499 lines**, under the 500 ideal (`test_communicator_body_thinned.py`). All
  edits were inline; no physical line breaks added.

## Pins recorded

Grepped `tests/` and `guardrails/` for distinctive fragments of every changed sentence. One changed
sentence is pinned; recorded here, pinning file left untouched.

- **Pinned sentence:** SKILL.md "…is a record, not a message…"
  - **Pinning file:** `tests/test_prose_gate.py:67` — inside `TestScissorsCoverage.test_comma_appositive_is_caught`,
    which hardcodes the string `"It is a record, not a message."` as a NEGATIVE fixture the scissors linter
    must flag. The fixture is an independent literal, not a reference to SKILL.md, so the rewrite does not
    affect the test (verified: `test_prose_gate.py` passes).
  - **OLD verbatim (SKILL.md):** `("harvested into rows 19–21", "the inbox worked") is a record, not a message: if the sentence only lands`
  - **NEW verbatim (SKILL.md):** `("harvested into rows 19–21", "the inbox worked") is only a record; the message still needs speaking: if the sentence only lands`

- **Pinned title left UNCHANGED:** SKILL.md rule-15 title "Sarcasm is not instruction" is pinned in
  `tests/test_traceability.py:1687` (traceability). It is a genuine prohibition claim, not a define-by-denial
  frame (the scissors linter passes it); kept verbatim.

## Cold-read rounds

- **Round 1 — fresh zero-context cold reader** over all four files. Flagged 4 BLOCKING stops, all rooted in
  pack vocabulary read in isolation (`wish`, `door`, `lane`, `station`, `seat`, `passport`, `facet`,
  "three-source read") and two long enumerative law sentences (capture echo, leave-word). See the
  unchanged-risk list for the disposition.
- **Round 2 — confirming read** over the 12 specific rewritten passages: every one returned READS CLEAN
  (positive statement, intact grammar, no leftover contrast frame; the Russian example reads naturally).

## Left unchanged because rewriting risked meaning / scope, or was already lawful

- **"small is not a win"** (README.md rule 7 title; SKILL.md rule 7). A genuine factual claim (a micro-fix
  is not a breakthrough), not a thing-defined-by-its-denied-neighbour. The scissors linter passes it. Kept.
- **"Sarcasm is not instruction"** (SKILL.md rule 15). Genuine prohibition claim, and pinned in
  traceability. Kept verbatim.
- **Additive "not just / not only" forms** — SKILL.md "so the list informs, not just enumerates" (rule 9)
  and "in EVERY session, not just the one that asked" (rule 10). These are additive-scope forms, explicitly
  held LEGAL by the scissors linter's own suite (`test_additive_and_prohibition_forms_stay_legal`:
  "It informs, not merely enumerates." / "This governs replies, not only documents." stay legal) and by
  register rule 15. Kept.
- **Pack vocabulary flagged by the cold reader** — `wish`, `door`, `lane`, `station`, `seat`, `passport`,
  `facet`, "three-source read". These are the pack's shared terms, defined in `live-spec-base`, which the
  actual reader (an agent running the pack) always has loaded; SKILL.md's own preamble (its opening
  blockquote) states the shared vocabulary lives there and this skill only references it. The cold reader
  read one file in isolation without the base loaded. Renaming these is out of scope for a single-skill
  register pass and would violate one-name-per-thing across the other eight skills and break test pins.
  Kept. ("facet" at the standard-facet-sweep bullet is additionally grounded in place by its example,
  "on a phone this gallery stacks into one column".)
- **Two long enumerative law sentences** — the capture-echo field list (rule 12) and the leave-word
  shutdown walk (rule 13). Each is a lead clause plus an enumeration of the exact required fields/steps
  with anchor citations. Splitting them risks altering the enumerated normative scope, so structure was
  kept; only the coined verb "intaken" was plained to "taken in".
- **"pipeline station"** (SKILL.md rule 9) — see lint verdict above; defined step vocabulary, grounded in
  place, normative. Kept.
- **Quoted specimens** (SKILL.md rule 8 self-certification examples; pre-report-walk step 4 examples of
  what the register lint flags) — banned patterns cited inside the rules that ban them. Must stay.

## Test status (informational; tests/ not touched)

- Communicator-specific suites green: `test_communicator_body_thinned.py`, `test_communicator_register_extracted.py`,
  `test_prose_gate.py` (39 passed).
- `test_traceability.py`: 168 passed, 3 failed — all three PRE-EXISTING and outside this write-set:
  `test_skill_evals_present`, `test_real_repo_lists_complete` (a not-yet-present "text-audit" pack member;
  communicator contains zero "text-audit"), and `test_craft_ladder` (build-pipeline content, never touched
  here). None involve communicator wording.
