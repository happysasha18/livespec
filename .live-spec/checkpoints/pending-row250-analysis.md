# Row 250 pre-run analysis — closing evidence (already built)

Written 2026-07-12 by an Opus analyst preparing row 250's pipeline run.

## Verdict

Row 250 is fully covered. It asks for the prover cross-cutting sweep — the
declared-laws station in the prover plus spec-author's twin habit. That work
already landed as **row 223 / INV-101** on 2026-07-12 ~00:22 (session 36).
Rows 223 and 250 are the same wish: both were born of the tlvphoto inbox on
2026-07-10 ~10:38 (analytics covered some beats while whole surfaces emitted
nothing; the human's eye found it, not the prover). The wish was captured
twice and split into two roadmap rows. Row 223 built it first. Nothing in
row 250 is uncovered. Row 250 closes as already-built; this file is the
closing evidence.

## Row 250's Done-when, clause by clause

Row 250 (ROADMAP.md line 148) reads: "the station stands in the prover and
the twin habit in spec-author, both red-proven, one real sweep run on a host
spec." Each clause is met.

1. **The station stands in the prover.** MET.
   `skills/product-prover/SKILL.md:278` — the "Declared cross-cutting laws"
   station. Per declared law it enumerates every surface and transition and
   demands the clause or a dated exemption on each item; a missing clause
   ranks as a broken invariant. It cites SPEC INV-101 and names spec-author
   as the law's owner.

2. **The twin habit stands in spec-author.** MET.
   `skills/spec-author/SKILL.md:250` — "The declared-laws line rides every
   new section (SPEC INV-101)." A new surface's section states its line
   against each declared law before the prover reads the delta, so the
   prover station audits instead of discovers.

3. **Both red-proven.** MET.
   `tests/test_declared_laws.py` — four tests
   (`test_the_home_and_the_packs_own_list`, `test_the_prover_station`,
   `test_the_author_habit`, `test_spec_anchor_and_index`). Matrix row M-237
   (TEST_MATRIX.md line 164) records them red-proven against the pre-delta
   tree on 2026-07-12 and marks the row BUILT.

4. **One real sweep run on a host spec.** MET.
   `docs/prover/2026-07-12-row223-declared-laws.md` — the first real run
   walked the pack's own spec on a fresh Opus reviewer: 11 items x 3 declared
   laws, 31/33 covered, 2 n/a, 0 MISSING, clean, 0 must-fix, one homing
   observation recorded.

## Supporting spec anchors

- **The declared-laws home clause:** `PRODUCT_SPEC.md:379` [INV-101] — the
  spec keeps its cross-cutting laws in one home; each new surface states its
  line; the prover's station audits per law per item.
- **The index row:** `PRODUCT_SPEC.md:1706` [INV-101].
- **The pack's own declared list:** register [INV-28, INV-34, INV-83] +
  clock-honesty [INV-24] + no-self-certification [INV-94], with two dated
  exemptions (measurement deferred; accessibility carried by the GitHub
  markdown renderer), both dated 2026-07-12.

## No new invariant or matrix row is owed

Because nothing is uncovered, row 250 mints nothing. The next free
invariant slot (INV-112) and the next free matrix slot stay free for a
genuinely new law. The resume note's warning — "the declared-laws station
may already cover part of it; de-dup first" — resolves to: it covers ALL of
it.

## Recommended close for the applier

Mark row 250 landed as a de-duplication of row 223 / INV-101 (no new files,
no invariant, no test). Point its Done-when at the row 223 evidence above:
the two skill homes, M-237's red-proven tests, and the real sweep record at
`docs/prover/2026-07-12-row223-declared-laws.md`. Cite this file as the
closing analysis.

ACCEPTED + CLOSED 2026-07-12 — row 250 closed as duplicate of row 223 (this
file is the closing evidence).
