# Prover cross-link — SPEC humanize batch: "From the spec to the tests: two layers that must not be skipped" (2026-07-07, session 25)

Register rewrite of one scenario section (the densest so far — four bold blocks + a bridge + a close).
Gates green: 12/12 tested phrases re-matched section-scoped; bracket-code multiset identical to baseline
(11 occurrences: [E-27], [E-14], [INV-37], [INV-41], [INV-36] embedded in a tested phrase, [E-5], [INV-6],
[E-15], [INV-15]×2, [target]); full suite 175 green.

One caught-and-fixed slip: the rewrite opened a sentence "The NORMATIVE pin is the named thing", which
capitalized the lowercase tested phrase "the NORMATIVE pin is the named thing". Reworded to keep it
lowercase ("owning place, and the NORMATIVE pin is the named thing"). Meaning unchanged. (Second
case-sensitivity slip of the session — pattern noted for the remaining batches.)

## Facts carried (all KEPT)
- BLOCK A: test-author owns matrix derivation + test writing (steps 5–6), the level ladder, real-artifact
  assertions, red-first, pinned skip-set, traceability; invoked by build-pipeline like steps 1–2; one home
  = the skill; origin story (two bugs past ~660 string tests; track-coach 2026-07-02..04, extracted
  2026-07-07) [E-27].
- BRIDGE: spec says WHAT; tests prove the shipped artifact; two once-implicit docs; an implicit layer is a
  lost layer (Alexander 2026-07-05).
- BLOCK B (ARCHITECTURE.md): named nodes, one responsibility + name each; every fact owned by one node;
  normative pin = the named thing, `:line` a lagging cache; drift re-greps (7 of 17 pins drifted in one
  session); drafting reconciles claims against shipped reality (pins from real commands); proven with the
  architecture lens (every fact owned · no node without backing · seams named); large/surface wish updates
  doc before matrix; bug/small wish cites or ASSIGNS its node (no re-prove); re-proven on structure change;
  iterative, [target] nodes with empty pins allowed, never designed ahead; re-carving legal via a
  restructure queue row [INV-37] [E-14].
- BLOCK C (numbers): MEASURABLE quality budgets + each budget's INSTRUMENTATION home; measurable is
  kind-shaped — the project's KIND [INV-36] proposes the dimensions; five per-kind examples kept as a list;
  no-honest-number → SAYS so by name, no vanity metric; budget asserted by a matrix row that can see it;
  a surface with no budget + no instrumentation home is a derivation defect the prover flags; numbers are
  host's taste, set on the human's word at the surface's first budget landing; binds from first touching
  landing not retroactively [INV-15]; gallery origin story (2026-07-06) [INV-41].
- BLOCK D (matrix DERIVED): matrix [E-5] organized architecture node × spec fact; ≥1 row/fact; every row
  pins a level; coverage validation kept as a 5-item list incl. negative-side rows [INV-6] and stale-row
  retirement; a missing/too-weak row is a derivation defect caught at derivation time [E-15].
- CLOSE: no wish lands whose facts lack an owning node + a right-level row; bridge walked layer by layer;
  predating projects bring the layers up as an OWNED landing, binding from that landing not retroactively
  (bring-up is queue row 50) [INV-15].

## Wording changes worth naming (meaning intact)
- Long compound sentences split; the per-kind dimensions and the coverage-validation checklist pulled into
  two lists.
- "A budget is asserted by acceptance — a matrix row… — never a hope in prose" → two plain sentences
  ("…a matrix row at a level that can see it. A hope in prose does not count."). No dash-contrast.
- One sentence reworded to keep the lowercase tested phrase intact (see slip above).

Verdict: **CLEAN.** Every fact and code carried; 12/12 tested phrases section-scoped; 11-occurrence code
multiset identical; suite 175 green. No must-fix.
