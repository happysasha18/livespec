# spec-author — register rewrite notes (2026-07-22)

Register-only rewrite of the spec-author pack skill. Two files touched:
`skills/spec-author/SKILL.md` and `skills/spec-author/README.md`. Meaning, scope, force,
code anchors (INV-x, T-x, E-x), the frontmatter description's trigger semantics, and
references to base rules were all held constant. Only the register (how it is phrased) changed.

## Pins recorded

None. Before every change I grepped `tests/` and `guardrails/` for distinctive fragments of the
sentence being touched. **No changed sentence was pinned by any test or guardrail.** Every register
fix landed on a sentence that no test asserts against, so no OLD→NEW pin swap needs recording and no
pinning file needs a later edit.

Cross-check performed the other direction too: I confirmed every load-bearing pinned phrase that a
test asserts against `skills/spec-author/SKILL.md` still exists verbatim after the rewrite — e.g.
`the rule, the actor as a role (the user, the producer, the target user), and the reason`,
`personal attribution and candid process voice`, `a dated decision keeps the date`,
`declared-laws home`, `before the prover`, `carries its net`, `no named net`, `no mechanical lint`,
`cognitive-load`, `three or more`, `how that axis is delivered`, `asks magnitude beside existence`,
`can the pack ship a single identical body that every host runs`, `binds forward [INV-159]`,
`interactive controls that belong to different layers occupy separate screen space`,
`The list is curated, each facet earning its place by named incident`,
`how each behaviour landed in code`, `landed in engine commit`, `the three faces of a wait`,
`Name the future with the [target] tag`, `the reversibility of the means`,
`the exit's motion mirrors the enter's`, `only a missing sentence is a hole`, `veto becomes a new wish`.
All intact.

(One incidental grep hit, the bare substring `the classic`, appears in `tests/test_broad_kill_guardrail.py`
and `tests/answer_first_fixtures/lead_long_finding.txt` — both unrelated to spec-author content, so my
removal of "the classic stranding bug" pins nothing.)

## Counts

**Contrast-by-denial frames fixed (the primary register defect): 21.**
Each was a definitional "X — not Y" / ", not Y" / "not X but Y" / "rather than" / "instead of" used to
say what a thing IS by naming its denied neighbour. Each became a positive sentence, with any real
boundary given its own plain sentence.

- SKILL L44 "in whole sentences rather than machine fragments with markup" → positive + boundary sentence.
- SKILL L62 "is said so in one short clause rather than left silent" → "is stated in one short clause".
- SKILL L104 "Terseness is not the goal — a headline ... is" → boundary sentence + positive "The goal is ...".
- SKILL L131 "a person's name carries nothing they can" → "a person's name gives them nothing to act on".
- SKILL L133 "impersonally ... rather than scrubbing names at publish time" → "; do not scrub names at publish time".
- SKILL L137 "a completeness checklist rather than a table of contents" → "... checklist. It is not a table of contents."
- SKILL L222 "a decided sentence rather than a silence" → "written as a decided sentence".
- SKILL L233 "scope dials richness, never the safety net" → "scope dials richness; it never trims the safety net".
- SKILL L252 "an explicit statement rather than a silent assumption" → "state it explicitly".
- SKILL L271 "rather than assuming a codebase's" → "; do not assume a codebase's".
- SKILL L289 "rather than assuming another kind's set" → "; it does not assume another kind's set".
- SKILL L305 "meets a stated layout rather than a blank" → "meets a stated layout".
- SKILL L320 "asks instead of guessing" → "asks the person; it never guesses".
- SKILL L325 "surfaced as a real question rather than shipping ... silently" → "... a real question. A pair that enters with craft and exits instantly is never shipped silently."
- SKILL L354 "audits instead of discovers" → "audits the declared lines. It no longer has to discover them."
- SKILL L442 "implement guarantees rather than user-facing features" → "implement guarantees; they are not user-facing features".
- SKILL L470 "the reader can follow, rather than a fork's delta ..." → "... the reader can follow. It is not a fork's delta ...".
- SKILL L496 "confirm rather than infer" → "confirm; never infer it".
- SKILL L516 "stated, not just implied?" → "one stated explicitly?".
- SKILL L553 "writing the spec ... rather than letting the spec lead ..." → "... what was built. The spec should lead, and the prover should find the holes before code exists."
- SKILL L383 "every entry door, not just the main one" → "every entry door, including the ones past the main one".
- README L35 "not machine fragments with markup (and not a textbook either ...)" → positive "in whatever register fits, whether or not it reads like a textbook" + boundary sentence "Machine fragments with markup have no place in it."

(That is 22 lines listed; the README line and one SKILL line together count as the pair for the same
"machine fragments" frame, so ~21 distinct scissors.)

**Inflation / drama flattened: 8.**
- "battle-tested on a real project" → "It was tested on a real project".
- "they drift apart and one rots" → "one goes stale".
- "which kills a spec" → "a spec no one reads stops doing its job".
- "This is the highest-value thing spec-author does" → "This move catches the bugs that pass every unit test".
- "the classic stranding bug" → "the stranding bug".
- "a checklist that grows by taste rots into a forty-row form" → "becomes a forty-row form".
- "— silence is not an option" (facet headline) → dropped; the rule stands positively.
- "silence is not a legal state for either" → "neither may be left out".

**Coined metaphor / poetic compression → plain words: 4.**
- Heading "Bold the headline, bury the threshold." → "Lead with the headline; put the exact threshold in the detail."
- "scars in the prose" → "edit-history notes in the prose".
- "a pack-marinated context writes ornate prose" → "a context that has loaded the pack writes ornate prose".
- Lint-tells list "(scissors, define-by-exclusion openers, ...)" → "(contrast-by-denial frames, define-by-exclusion openers, ...)" — grounded the coined term "scissors" with the plain mechanism name.

**Long tangled sentence split into short SVO: 2.**
- SKILL L88 the enumeration-threshold sentence (~65 words through two em-dash asides) → three sentences; pinned `no mechanical lint` and `cognitive-load` preserved.
- SKILL L299 the viewport-quantifier appositive ("... the author-side of the viewport-quantifier lens the prover holds, itself the worked instance of the range law's general sub-domain duty ...") → three sentences; anchor INV-138 and the parenthetical meaning preserved.

**Lint findings fixed: 0.** `scripts/preshow-register-lint.py` (a coinage/calque/transliteration
pattern lint) reported clean on both files BEFORE and AFTER the rewrite — its pattern set does not
cover the contrast-by-denial class, which is why this rewrite was manual. Final verdict on both files:
`OK (preshow-register): no coined metaphor, calque, or transliterated pack term found.`

## Cold-read rounds: 2

- Round 1 (fresh stranger): flagged as BLOCKING the opening base-rule-name blockquote, the coined
  tell "scissors", the tangled "viewport-quantifier lens ... sub-domain duty" clause, and the pervasive
  pack terms "door"/"wish". I fixed the two in-scope register defects (the "scissors" coinage and the
  tangled clause). The base-rule-name list, "door", and "wish" are shared pack vocabulary defined in
  `live-spec-base` and sibling skills; redefining them here would duplicate their one home and rewrite
  base-rule references, both out of scope — left by design.
- Round 2 (confirming, fresh stranger): reported the register now strong on the hype and denial axes.
  It surfaced two small inline contrast-by-denial cases (L131, L233) and three long sentences (L88,
  L289, L335). I fixed L131, L233, and split L88. L289 and L335 were left (see unchanged-risk below).
  It listed the recurring metaphors "the walk", "seam", "tripwire", "floor/ceiling", "legs/arms" as
  NON-BLOCKING and noted they read as shared house vocabulary.

## Left unchanged because rewriting risked meaning

- **SKILL L289–295, the delivery-separability sentence** ("And where an owed axis adds runtime code to
  cover it (SPEC INV-248), the delta states how that axis is delivered — ..."). Long, but it carries the
  pinned phrase `how that axis is delivered` and a dense enumeration of named architectural reasons;
  restructuring risked both the pin and the decided-sentence meaning. Left intact (only the adjacent
  "rather than assuming another kind's set" scissors just before it was fixed).
- **SKILL L335–340, the magnitude/asymmetry sentence** ("The second half asks magnitude beside
  existence: where the pair rides a continuous, reversible quantity ..."). Carries pinned `asks
  magnitude beside existence` and `same magnitude`, plus an incident record; splitting risked meaning.
  Left intact.
- **SKILL L118, the lawful instructional substitution** "carries a dated 'Last reconciled' provenance
  line instead of a version string" — this is a directive to write A in place of B (lawful per the
  brief), not a definitional contrast. Left as-is.
- **Frontmatter `description` (L3)** — its trigger semantics must stay verbatim, so it was not touched
  even though it describes the OLD spec shape (flagged CONTENT-STALE below).
- **The recurring house metaphors** ("the walk", "seam", "tripwire", "the door", "wish", "lens",
  "floor/ceiling") — shared pack vocabulary with one home elsewhere and used identically by sibling
  skills; rewriting them here would break one-name-per-concept and is out of scope for a register pass.

## CONTENT-STALE passages (13) — flagged, NOT rewritten

The spec format this skill teaches is the OLD shape: use-case-first **prose scenarios** with a
**manually maintained Formal index** closing the doc, and the "Entities/States/Actors chapters" it
names as the rejected alternative. The genre migrating in tonight (`docs/spec-format.md`, 4.0.0) is a
requirements genre — Context / User Story / Acceptance Criteria per requirement, a closed-vocabulary
glossary, trailing anchors, no manual Formal index, no history in the spec. The following passages
describe the old shape and will need a CONTENT rewrite (a separate task); this register pass left their
meaning intact:

1. **Frontmatter `description` (L3)** — "use-case-first ... scenarios ... lead ... a Formal index closes the doc".
2. **"How it reads" — Scenarios-lead bullet (L50–56)** — "Scenarios lead; the formal content lives inside them (use-case-first)"; "Never organize the document as Entities / States / Actors chapters"; the flagship v0.3/v0.4 rejection story.
3. **"How it reads" — scenario entry/exit bullet (L57–65)** — each scenario states how it is entered and exits (INV-127), framed on prose scenarios.
4. **"How it reads" — "A Formal index closes the doc" (L70–73)** — the manual Formal index; the new genre has no such derived table.
5. **"How it reads" — lists-inside-a-scenario + enumeration threshold (L77–94)** — framed on "inside a scenario"; references the rejected structure-first document.
6. **"How it reads" — the "how to read" note (L95–97)** — describes the old preamble ("each section is a scenario ... the Formal index at the end").
7. **The spine section (L135–158)** — "The document is organized use-case-first (scenario sections ...)".
8. **The primary-unit heading convention (L446–453)** — the `[feature: F-x]` / `[not a scenario]` tag on H3 **scenario** headings, tied to the scenario shape.
9. **Standard vocabulary (L481–484)** — "our spec stays a single use-case-first document (never the Entities/States/Actors chapters ...)".
10. **"How spec-author works" step 1 (L488)** — "use-case-first: find (or open) the scenario ... the Formal index updated in the same edit".
11. **Completeness pass — "Shape (use-case-first)" (L534–537)** — "Is every section a scenario ... Does every anchor in the prose appear in the Formal index".
12. **"What spec-author produces" (L541)** — "use-case-first — scenarios lead, anchors trail, the Formal index closes the doc".
13. **Anti-patterns (L566, L569–570)** — "Structure-first layout" (Entities/States/Actors chapters) and "An index that drifts" (the Formal index), plus README.md's "prose-first PRODUCT_SPEC.md ... a plain-language headline per rule" and the spine list "Purpose → Entities → ... → Glossary" (README L5, L35, L37) present the old shape.

Note: parts of "How it reads" are NOT stale and were kept as current — "The spec states the current
truth — a changelog lives elsewhere" (no history) and "codes trail at the line-ends" (trailing
anchors) both survive into the new requirements genre.

---

# Content update (2026-07-22) — teaches the new requirements genre

Second pass over the same two files (`SKILL.md`, `README.md`). The register pass above left meaning
intact and flagged 13 CONTENT-STALE passages that still taught the OLD shape (use-case-first prose
scenarios + a hand-kept Formal index). This pass rewrites that content to the format defined in
`docs/spec-format.md` (VERSION 4.0.0): a closed-vocabulary glossary, then a body of requirements, each
carrying a Context block, a one-sentence User Story, and acceptance criteria grouped into NAMED CASES;
lowercase-italic keywords (*shall*/*when*/*while*/*if*/*then*); codes as trailing bracket anchors;
`[GAP: ...]` lines for source holes; a generated code-to-location table (`scripts/build-index.py`,
gated by `guardrails/check-index-generated.py`) in place of any hand-kept index. Surviving content
(no-history, trailing anchors, one-home-per-fact, ask-never-guess, the axis/facet/delivery duties,
the [target] tripwire, the norm pointer, the primary-unit table, content contract, instance→engine
boundary) was left untouched. No code anchor was renumbered or removed.

## The 13 flagged passages — what each became

1. **Frontmatter `description` (L3)** → now describes the requirements genre: "a closed-vocabulary
   glossary, then a body of requirements, each with a Context block, a one-sentence User Story, and
   acceptance criteria grouped into named cases; short codes trail as bracket anchors, and a generated
   code-to-location table replaces any hand-kept index." All trigger phrases ("start a spec", "spec
   this out", "write the spec for X", the pairing note, the when-not-to-use) kept verbatim.
2. **Scenarios-lead bullet** → replaced by "The body is a list of requirements; each opens with its
   situation" (Context → User Story → acceptance criteria) plus a new bullet "Acceptance criteria group
   into named cases, one criterion carrying one trigger and one response" teaching the case form, the
   lowercase-italic keywords, the no-all-caps rule, and `check-requirement-shape.py`. The
   Entities/States/Actors rejection story and the v0.3/v0.4 flagship narrative were dropped.
3. **Scenario entry/exit bullet** → the pinned headline "Each scenario states how it is entered and how
   it exits (SPEC INV-127)" kept; body reframed onto the Context block (it states how the situation
   arises and what it leaves true). "Scenario/walk" language became "requirement".
4. **"A Formal index closes the doc"** → "A generated code-to-location table closes the doc": the
   `## Reference` section, built from body criteria by `scripts/build-index.py`, output only, never
   hand-edited; feature codes ride scenario headings; the authored home of each code is its criterion +
   glossary noun; `check-index-generated.py` reds drift/missing/orphan.
5. **Lists-inside-a-scenario bullet** → reframed onto "a Context block or a criterion" and the
   structure-first-rejection reference dropped; notes that criteria are already a numbered list. The
   adjacent INV-215 enumeration-threshold bullet (pins "three or more", "cognitive-load", "no
   mechanical lint", "enumeration") was left verbatim — it survives the migration.
6. **"how to read" note** → "A preamble and a glossary open the doc": teaches the preamble (what the
   doc covers, the bracket-code kinds, how the keywords read, history-in-JOURNAL) and the closed-
   vocabulary glossary before the first requirement, with `check-vocabulary.py` named.
7. **The spine section** → intro now "a glossary followed by a list of requirements"; each spine item
   lives in a requirement's criteria or (for a domain noun) the glossary, findable through the generated
   table. Items 1–7 reworded off "in bold where a scenario first meets it" / "inside their scenario" /
   "in place, in bold" onto the glossary + criteria homes. The anchor-set guard's example changed from
   "structure-first → use-case-first" to "a genre migration, a resection" and gained the keep-the-anchor,
   state-today's-home instruction.
8. **Primary-unit heading convention (INV-132)** → "H3 heading" became "requirement heading —
   `## Requirement N: …`, the level every person-facing scenario uses"; sub-parts are now `### Acceptance
   Criteria` and the bold case lines. `[feature: F-x]` and `[not a scenario]` kept. (Pin change recorded
   below.)
9. **Standard vocabulary** → "our spec stays a single use-case-first document (never the
   Entities/States/Actors chapters …)" became "our spec stays a single requirements-genre document — a
   glossary and a body of requirements". Pins "measurable or verifiable here" and
   "docs/spec-format-by-project-type.md" kept.
10. **How-spec-author-works step 1** → "find (or open) the requirement the change belongs to … grow its
    Context, its User Story, and its named-case criteria … add any new domain noun to the glossary … the
    code-to-location table is regenerated at freeze by build-index.py". Pin "the scenario is the wish's
    place on the feature map (SPEC INV-37)" kept.
11. **Completeness pass** → the Entities item now asks for a glossary definition; the Readability item
    reworded onto cases/criteria, lowercase-italic keywords, no all-caps, and "open with a preamble and a
    glossary"; the Shape item retitled "(requirements genre)" and rewritten to check Context/User
    Story/named-case criteria, `check-requirement-shape.py`, and the generated table vs a fresh build.
12. **What spec-author produces** → "in the requirements genre — a glossary and a body of requirements,
    each with a Context block, a User Story, and named-case criteria, anchors trailing, closed with a
    generated code-to-location table".
13. **Anti-patterns + README** → "Structure-first layout" replaced by "Prose where a criterion belongs";
    "An index that drifts" replaced by "A hand-edited code-to-location table" (naming build-index.py +
    check-index-generated.py); "A wall of undifferentiated prose" fix reworded to named cases + numbered
    criteria; "Codes opening the line" reworded to "a criterion's first word". README L5 "prose-first" →
    "requirements-genre"; README "Human-first" bullet's "plain-language headline per rule" → the
    glossary + requirements shape; README "The spine" bullet made a completeness checklist with a
    closed-vocabulary glossary.

## New teaching added (required by the brief, absent from the old skill)

- **The comprehension gate** (new `## The comprehension gate` section): the mechanical lints —
  `check-vocabulary.py`, `check-one-name.py`, `check-requirement-shape.py`, the register lint,
  `check-weak-words.py` — then a panel of fresh cold readers per changed section until two consecutive
  zero-blocking reads. Also folds in the `[GAP: ...]` rule (judge + inputs, fill every relational slot).
- **The change record** (new `## The change record` section): the delta classifier's four kinds
  (new / sharpen / retire / scenario-only), the `docs/deltas/*.json` record, `check-delta-record.py`, the
  500-byte new-criterion cap, and the bytes-per-criterion ratchet (`spec-ratchet.json`,
  `check-size-ratchet.py`, lower-or-leave, never raise on a landing).

## Additional stale shape-teaching found and fixed (beyond the 13, same class)

- **"Lead with the headline; put the exact threshold in the detail"** bullet — taught a bold headline
  per rule (the old rule-per-line shape). Reframed to "Name the situation in the case; put the exact
  threshold in the criterion". No test pins it.
- **Two "prose-first" descriptors** (SKILL L17, README L5) — changed to "requirements-genre" so the
  intro does not contradict the new teaching. No test pins them.

## Pins changed (OLD → NEW) — one

The register pass recorded zero pin changes. This content pass forces exactly one, and it is a
consequence of the migration itself (scenario headings moved from `###` to `## Requirement N:`):

- **`tests/test_scenario_heading_tag.py::TestScenarioHeadingTag::test_spec_author_carries_heading_convention`**
  asserts the literal `untagged, unmarked H3 is unambiguously red` in `skills/spec-author/SKILL.md`.
  - OLD: "an untagged, unmarked **H3** is unambiguously red. Put the convention on **H3 headings, the
    level every scenario uses**; sub-parts nest under a heading …"
  - NEW: "an untagged, unmarked **requirement heading** is unambiguously red. The parts under it — the
    `### Acceptance Criteria` sub-heading and the bold case lines — nest inside a requirement …"
  - WHY FORCED: in the new format a person-facing scenario is `## Requirement N:` (H2), so teaching
    "H3" is factually wrong. The same test's sibling assertions read the OLD "every H3 heading in this
    spec" phrasing out of PRODUCT_SPEC.md; the test is migration-coupled and is updated by the tonight
    delivery, not here (the pinning file is not edited, per the brief). The other pinned literal in the
    same test, `[not a scenario]`, is preserved.

## Verify

- `scripts/preshow-register-lint.py` — clean on both changed files (`OK (preshow-register): no coined
  metaphor, calque, or transliterated pack term found`), before and after.
- Spec-author test files (the 16 files that read `skills/spec-author/SKILL.md`, plus `test_prose_gate.py`
  and `test_derived_doc_header_policy.py` for the lint-extension lines): 430 passed, 4 failed on the
  final run.
  - 1 failure is the recorded forced pin change above (`test_spec_author_carries_heading_convention`).
  - 3 failures are pre-existing and unrelated to spec-author content:
    `TestSkillEvals::test_skill_evals_present` (a working skill lacks an `evals/*.md` file),
    `TestPackListParity::test_real_repo_lists_complete` (the `text-audit` skill has drifted out of the
    pack lists), `TestWorkerContract::test_craft_ladder` (build-pipeline SKILL.md is missing the craft
    ladder phrases). None read a passage this pass touched.
- Cold read, round 1 (fresh zero-context reader over all changed sections): zero hard blocking findings.
  One borderline referent wobble — the entry/exit bullet's pinned headline says "scenario" while the two
  bullets around it say "requirement", and the two words are not strictly synonyms elsewhere (a scenario
  is a person-facing, `[feature: F-x]`-tagged requirement). The pinned headline cannot lose "scenario", so
  I grounded the term once in the first "How it reads" bullet: "A person-facing requirement is also called
  a **scenario** — its heading carries a `[feature: F-x]` tag; a machinery or reference requirement is not
  a scenario." Register lint stayed clean after the edit.
- Cold read, round 2 (fresh zero-context reader over "How it reads" + the two new sections): confirmed
  the requirement/scenario definition lands; found three blockings — the entry/exit bullet mixed
  "requirement" into a duty its pinned headline scopes to scenarios (fixed: the bullet now says
  "scenario" throughout, matching the pin); the "scenario-only" delta-kind gloss leaned on an
  unintroduced classifier and collided with the scenario definition (fixed: plain in-place
  disambiguation, classifier named in the intro); "the sum of its declared new criteria" left the summed
  quantity unstated (fixed: "the sum of the byte counts of its declared new criteria").
- Cold read, round 3 (fresh reader, two new sections + "How it reads"): the two round-2 fixes confirmed
  clean; four new findings — two in this pass's text ("free script" ambiguous, the code↔criterion
  one-to-one link unstated; both fixed) and two in register-pass-era prose this pass never touched ("the
  register judge" introduced without definition in the machine-gate bullet, and "traceability
  check-phrase" in the same bullet — left, out of this content pass's scope; a candidate for the next
  polish pass). Also reworded the INV-215 incident tail ("the human language already right and the
  fine-tuning reading efficiency" — flagged unparseable) into two plain clauses; the phrase lives only in
  a test docstring, no assertion pins it.
- Cold read, round 4 (fresh reader, the two new sections): **zero blocking findings.** The gate's
  two-consecutive-clean bar is met for the round-2/3 fixes on their final wording.
- Style lint extension (mid-pass instruction): `scripts/spec-style-lint.py` was extended to catch
  definitional rather-than/instead-of frames; it flagged two lines in SKILL.md, both rewritten positive:
  - OLD: `carries a dated "Last reconciled" provenance line instead of a version string, so a reader
    never meets a stale number that reads as the current version.` NEW: `carries a dated "Last
    reconciled" provenance line, so a reader never meets a stale number that reads as the current
    version. A version string has no place in that header.` (The old fragment survives verbatim as a
    frozen lint SPECIMEN in `tests/test_prose_gate.py` — the test feeds the string to the lint via
    stdin and never reads SKILL.md, so this is no pin; no test edit needed.)
  - OLD: `a behaviour told as a narrative paragraph instead of a numbered criterion carrying one
    trigger, one response, and a trailing anchor. Each rule is a criterion sitting in a named case.`
    NEW: `a behaviour told as a narrative paragraph, leaving the reader no numbered line to key on. Each
    rule is a criterion carrying one trigger, one response, and a trailing anchor, sitting in a named
    case.`
  - The same lint also erred on two other lines, both fixed positive: the spine intro's "It is not a
    table of contents." became "it constrains what the document contains, and the section order stays
    free" (unpinned), and the comprehension-gate's "not the whole document" became "and the whole
    document stays out of the reading". Final verdict: `OK (spec-style): no register tells found`,
    0 errors 0 warnings on SKILL.md; README.md 0 errors, 6 advisory second-person warnings (the README's
    established public voice, exit 0).
