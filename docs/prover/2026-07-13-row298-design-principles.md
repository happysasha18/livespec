# Prover record — row 298, per-kind design principles (INV-136)

Date: 2026-07-13. Session: build worker (opus orchestrator seat). Mode: FULL on the new law +
CROSS-LINK of its seams against the existing laws it composes with; architecture lens on the new
ARCHITECTURE section. Doc version proven: v1.1.17. Feature door, kind: skill.

## What was proven
The new invariant INV-136 (a project kind carries its own design principles; the verify/feel pass
reads and runs them; a visual kind declares them at founding; the frontend starter set gathers the
pack's frontend guidance plus the interactive-overlap rule) across its homes: the spec founding
clause + Formal-index row, the ARCHITECTURE per-kind design-principles table + interactive-overlap
statement + Prover-record row, TEST_MATRIX M-278, spec-author + build-pipeline verify + ADOPT wiring,
and the founding check in tests/test_design_principles.py.

## Phase findings

| # | Phase | Finding | Verdict |
|---|---|---|---|
| F1 | Entities/owner | INV-136 owned by exactly one node (base-rulebook owns-list), like INV-135. | OK — traceability green |
| F2 | Composition vs INV-135 | Design principles are a THIRD founding companion beside layers+proofs, not a re-home of either. The founding check for design principles is scoped to visual kinds; INV-135's check binds all kinds. No double home. | OK |
| F3 | Composition vs INV-125 | The interactive-overlap rule is a member of the cross-surface-composition family INV-125 names; the spec clause cites INV-125 as its blind-spot kin and takes the SAME ship-the-law/leave-the-pixel-assertion split. No duplicated mechanism — INV-125 is policy-uniformity across sibling surfaces, INV-136 adds a per-kind design-principle SET that the verify pass runs, the overlap rule being one principle in it. | OK — sibling, not duplicate |
| F4 | Composition vs INV-30/INV-77 | The verify pass reads declared design principles BESIDE the visitor walk and feel pass (INV-30); a principle the suite cannot green is the human's eye-walk (INV-77). The frontend starter set names the visitor walk / feel pass as declared principles so they stop being scattered — this HOMES existing INV-30 material under the new set rather than restating it. | OK |
| F5 | Register — contrast frames | The interactive-overlap principle states what must hold in its own positive sentence and states the non-interactive allowance as a separate sentence; no "X not Y" frame. The initial draft carried one comma-appositive scissors ("lives in the adopting project, not here") caught by spec-style-lint and removed (both spec and ARCHITECTURE). | FOLDED |
| F6 | Stub scan | No TODO/FIXME/placeholder/lorem/hardcoded-sample in the new prose. | OK |
| F7 | Red-first | The wiring doc-assertion tests (spec-author, build-pipeline, ADOPT) went red before the wiring was written; the founding-check teeth tests (visual-without -> red, non-visual-without -> pass) green from the start. | OK — red-proven |
| F8 | Adopting-project projection | The pixel/DOM overlap check is specified to live in the adopting project's own suite; live-spec ships the law + starter set only, no faked pixel test in its own suite. | OK |

## Architecture lens (6 checks, skill-pack scale)
- Every spec fact owned: INV-136 -> base-rulebook owns-list. OK.
- No node without spec backing: no new node added. OK.
- Seams: the new section is a per-kind scaffold table; no new seam between nodes. OK.
- Quality budgets: unchanged. OK.
- Runtime view: the F-wish flow already walks build-pipeline verify (where the feel pass runs the
  declared design principles); no new flow. OK.
- Placement view: unchanged. OK.

Must-fix on the documents: 0 (the one scissors folded during authoring). Should-clarify: 0 open.

## Fresh-context adversarial audit (INV-46) — 1 must-fix folded
An independent fresh-context checker ran over the law before commit. It refuted the "goal missed"
hypothesis on the documents but caught one real must-fix in the founding-check code: `kind_is_visual`
used bare substring matching, so the token "ui" misclassified non-visual kinds ("build tool", "test
suite", "guide", "requirements" — each carries the letters u-i mid-word) as visual, and real visual
kinds named without the fullstack/static-site words ("mobile app", "dashboard", "iOS client") escaped
the requirement. Folded: the detector is word-boundaried and the token list widened, locked by two new
tests (`test_ui_lookalike_kinds_are_not_misclassified_visual`, `test_real_visual_kinds_are_caught`).
The checker also noted a cosmetic traceability gap (M-278 named 11 of 12 test functions) — folded by
naming all functions in the matrix row. Suite 604 green after the fold. A further external audit is
scheduled per the task.
