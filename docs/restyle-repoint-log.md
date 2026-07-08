# SPEC re-style — traceability needle re-point log

When a section's prose is re-styled (clean-agent rewrite, linter-gated), a brittle traceability
needle keyed to an old exact phrase is re-pointed to an anchor plus a register-invariant domain
term that survives in the new prose and names the same law. Re-points narrow (a more specific
phrase for the same law), never weaken. One line per re-point.

| Date | Section | Test | Old needle | New needle | Why |
|------|---------|------|-----------|-----------|-----|
| 2026-07-08 | Asking what the product does | test_traceability.py::TestProblemLedger::test_feature_map_on_demand | `the whole map comes only when` | `the whole map only on request` | Clean-agent rewrite phrased the "map returned only when asked, never uninvited" law as "The ask returns the whole map only on request." New needle is a narrower phrase naming the same INV-38 law and present verbatim in the new prose. Anchor `[INV-38]` and `Asking what the product does` heading still gate the same law. |
| 2026-07-08 | Reuse before reinventing | test_traceability.py (INV-65 borrow-license) | `with the notice kept — never republish unlicensed text` | `Unlicensed text is never republished` | Old needle pinned the scissors construction itself. Removing the em-dash contrast split it into two statements; new needle is the prohibition sentence, register-invariant and narrower, present verbatim in new prose. Anchor `[INV-65]` still gates the same borrow-license law. |
