# design-reviewer register rewrite — notes (2026-07-22)

Register-only rewrite of `skills/design-reviewer/SKILL.md` and `skills/design-reviewer/README.md`.
Meaning, scope, force, code anchors (INV-x, E-x, M-x), the frontmatter description's trigger
semantics, and all references to base rules by number were preserved. No commits. tests/ untouched.

## Counts

- Contrast-by-denial (scissors) fixed: **11**
  1. SKILL L17 — "You question the concept, not the wording." → "You question the concept behind the spec; the wording is the prover's ground."
  2. SKILL L25 — "keys to the prover's FULL *mode* by name, not to any pass that merely re-reads…" → split into a positive sentence + a boundary sentence.
  3. SKILL L42 — "uses the person's own action words, never the author's category names — that is what frees…" → "uses the person's own action words. It leaves out the author's category names, which is what frees…"
  4. SKILL L52 — "reds an increase, but a red is not a split; the split is a design call…" → "reds an increase. A red marks the increase for attention; the split itself is a design call…"
  5. SKILL L52 — "(a shared wiring pin, not two owners)" → "— they share one wiring pin and are not two separate owners —"
  6. SKILL L84 — "a **whole behaviour** … rather than a parameter (a zoom … setting) — where the whole-behaviour-versus-parameter call is itself unclear…" → positive statement of the whole behaviour with the example inline, plus a plain sentence for the parameter boundary.
  7. SKILL L87 — "That default is not applied to the spec the way the pack's usual proceed-on-recommended arm would" → "The pack's usual proceed-on-recommended arm would apply that default to the spec on its own … Here the class sentence lands only on the human's word, so the default waits…"
  8. SKILL L104 — "keeps the loop live, not a fourth rest:" → "keeps the loop live. The three rests are where a round with no new declaration settles; the cap stands apart from them…"
  9. SKILL L110 — "it points at this record rather than restating its state" → "it points at this record and does not restate the state"
  10. SKILL L117 — "that is the prover's declared-class defect path [INV-125], not this pass's recommendation path — route it there." → "that belongs to the prover's declared-class defect path [INV-125]; route it there, since this pass owns only the groupings no clause has declared."
  11. README L35 — "so answering it is one decision rather than an open essay." → "so answering it comes down to a single decision."

- Coined metaphor / poetic compression → plain mechanism: **2**
  - SKILL L52 — "the mechanical face of a failed growth answer" → "the mechanical sign of a failed growth answer"
  - SKILL L59 — "a per-type special case is the smell" → "a per-type special case is the warning sign"

- Inflation adjective removed: **1**
  - SKILL L87 — "rare, high-value, and low-noise by construction" → "rare and low-noise by construction"

- Lint findings fixed: **0**. `scripts/preshow-register-lint.py` is a coinage/calque/transliteration
  gate, not a scissors gate. Both files passed it clean before and after the rewrite. Final verdict:
  OK on both files.

## Pins recorded

**None.** Every changed sentence was grepped (as a distinctive fragment) across `tests/` and
`guardrails/` before editing; no pinning file matched any changed sentence. The pinned substrings the
suite does assert on (`action words`, `whole behaviour`, `the tight ask`, `never written into the
surface registry`, `recommended default`, `at most three`, `strongest first`, `not re-raised`,
`docs/design-review/`, `per-finding outcome`, `routes by declaration status`, all INV-/E- codes) were
all preserved verbatim inside the rewrites. `tests/test_design_reviewer.py` passes 14/14 after the
edits.

## Cold-read rounds

- 1 fresh cold-reader (zero-context stranger) over both files, plus my own confirming read of every
  changed sentence in context.
- The README (the stranger-facing doc) read cleanly per the cold reader.
- The cold reader's BLOCKING findings on SKILL.md were all inherent pack vocabulary and code anchors
  (MINOR / M-6 / FEATURE-FIT, the surface registry, the node/pin/co-residence architecture vocabulary,
  proceed-on-recommended arm, the prove station). These are out of scope for a register-only rewrite:
  the task mandates keeping code anchors and base-rule references, their home is `live-spec-base`
  (loaded by the agents that read this skill), and grounding them inline would duplicate the base
  skill and violate one-home-per-fact. None of my rewritten sentences were flagged as newly tangled;
  my L87 rewrite is cleaner SVO than the passive it replaced. No blocking finding traced to my edits,
  so nothing required a fix in scope.

## Left unchanged because rewriting risked meaning / scope

- **Frontmatter `description` (SKILL L3)** — left entirely untouched. It carries the skill's trigger
  semantics (the "NOT for verifying… — that is product-prover… while this answers…" boundary is what
  routes triggering between design-reviewer and product-prover), and the task rule is that trigger
  semantics stay.
- **SKILL L110 — "an ask still unanswered, not to be re-raised on its own next pass"** — kept. This is
  a lawful directive describing the `held` outcome value (a rule about what happens to a held ask), not
  a thing defined by its denied neighbour.
- **"fly the thing home" / "fly the picture home" (SKILL L58, L62)** — kept. Mildly poetic, but the
  plain mechanism is stated right beside it ("lands back on its own on-screen rectangle"), it is a
  recurring self-consistent motion phrase, and L62 is a dated incident record where rewriting risked
  the historical account.
- **"younger sibling" / "older sibling" (README L6, L89 and Related)** — kept. Idiomatic, immediately
  grounded ("It runs after the prover, on the same spec"), not machine-dialect; reads fine to a
  stranger (cold reader confirmed the README clean).
- **Pack-vocabulary / code-anchor terms across SKILL.md** — kept by task mandate (anchors and
  base-rule references stay).

## Suite note (pre-existing, not caused by this rewrite)

`tests/test_traceability.py` has 2 failures (`test_skill_evals_present`,
`test_real_repo_lists_complete`) reporting a repo-wide gap: a `text-audit` skill missing from pack-list
footers across SPEC, README, OVERVIEW, communicator, feedback-intake, live-spec-base, test-author, and
design-reviewer alike. This is pre-existing and outside this write set — the rewrite never touched the
closing pack-list footer (SKILL.md L120-124). All other design-review-adjacent tests pass.
