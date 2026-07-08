# SPEC re-style — traceability needle re-point log

When a section's prose is re-styled (clean-agent rewrite, linter-gated), a brittle traceability
needle keyed to an old exact phrase is re-pointed to an anchor plus a register-invariant domain
term that survives in the new prose and names the same law. Re-points narrow (a more specific
phrase for the same law), never weaken. One line per re-point.

| Date | Section | Test | Old needle | New needle | Why |
|------|---------|------|-----------|-----------|-----|
| 2026-07-08 | Asking what the product does | test_traceability.py::TestProblemLedger::test_feature_map_on_demand | `the whole map comes only when` | `the whole map only on request` | Clean-agent rewrite phrased the "map returned only when asked, never uninvited" law as "The ask returns the whole map only on request." New needle is a narrower phrase naming the same INV-38 law and present verbatim in the new prose. Anchor `[INV-38]` and `Asking what the product does` heading still gate the same law. |
| 2026-07-08 | Reuse before reinventing | test_traceability.py (INV-65 borrow-license) | `with the notice kept — never republish unlicensed text` | `Unlicensed text is never republished` | Old needle pinned the scissors construction itself. Removing the em-dash contrast split it into two statements; new needle is the prohibition sentence, register-invariant and narrower, present verbatim in new prose. Anchor `[INV-65]` still gates the same borrow-license law. |

## Phase 2 — whole-diff validation (2026-07-08 night pass, iteration 1)

A fresh reviewer read the full pre-restyle baseline (`ca78876`) → HEAD diff of SPEC.md. It reported 7 items;
5 were real and fixed in commit a9690c4: reinstated the "three standing questions, two answered elsewhere"
framing in the feature-map ask; dropped an added "otherwise the ask proceeds" clause; restored "what the
feature gives its person" (a rewrite had narrowed it to "value"); restored the "knob rather than a taste
call" contrast without a negation opener; fixed a dangling em-dash that made "never a silent retry" read as a
list item. Two minor notes (aloud→directly; wording) left as-is. Full-SPEC anchor multiset verified IDENTICAL
to the baseline. A confirming iteration 2 and full 0-errors convergence wait on the parked errors (preamble +
Formal index), which need Alexander's word.

## Stage 5 chunk 2 — economy ladder (2026-07-09)

Section "When money or time run short" converted through --gate (second person → named actor, caps
lowercased, 19 gate-errors → 0). Linter refined: CAPS_RE now captures hyphenated all-caps compounds whole
and CROSS-LINK/FEATURE-FIT/RE-ENTRY join the caps allowlist (defined mode names, not shout). Three needles
re-pointed by narrowing to the register-clean phrase in the new prose (test_traceability.py::test_economy_ladder):
`the economy rung is asked, or the standing default told` → `the pack asks the economy rung, or tells the standing default`;
`What NEVER bends, at any rung` → `What never bends at any rung`;
`a push still requires the full gate green at HEAD` → `a push still requires the full gate green at head`.
