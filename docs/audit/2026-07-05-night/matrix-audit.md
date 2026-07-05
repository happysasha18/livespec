# Matrix audit — pass 2 of 3, 0.8.0 milestone (2026-07-05 night)

Scope: TEST_MATRIX.md re-walked BY HAND against SPEC.md's Formal index (v0.14.0), ARCHITECTURE.md's
Nodes table (v0.1), and the coverage-validation checklist in the matrix template. The mechanical half
(`tests/test_traceability.py`, `tests/test_guardrails.py`) is green and does the union-coverage,
level-present, NEVER-side, and BUILT-names-real-test checks; this pass adds the judgment the machine
cannot: correct *owning-node* placement, level honesty, live TODO owners, new-row quality, and inventory
completeness against `git ls-files`.

**Key structural gap the machine misses:** `test_matrix_covers_every_anchor` checks each anchor appears
in the UNION of all blocks — it does NOT verify a row sits under its anchor's OWNING node (matrix header
line 7). So node-placement errors pass green; findings F1/F2 below are exactly that class.

## Findings

| # | Finding | Severity | Outcome |
|---|---|---|---|
| F1 | **Wrong owning node.** M-079 (anchor **B-2**) sits under `[node: product-prover]`, but ARCHITECTURE assigns B-2 to **attach** (and B-2 is a bootstrap/adopt-orient fact — the row text itself cites the A-1 adopt pointer). `attach` has no B-2 row, so B-2 has ZERO rows under its owning node — a direct violation of the matrix's own "every index anchor sits in ≥1 row under its owning node" rule. Move the row into the attach block (product-prover owns only M-6). | must-fix | **FOLDED** (same sitting) |
| F2 | **Cross-node row cites the guarded anchor, not the guardrails anchor.** M-082 sits under `[node: guardrails]` but cites **E-14**, owned by build-pipeline (whose home row M-026 already covers E-14). The drift gate (gate g) is a pre-push gate — its guardrails-owned anchor is **E-6**. Either re-cite M-082 to E-6, or state explicitly it is a cross-node guard row so a reader knows E-14's home is build-pipeline. | should-clarify | **FOLDED** (same sitting) |
| F3 | **Stale TODO owner — a closed queue row named as the future owner.** M-017, M-019, M-023, M-037 name "guardrails row 3" and M-061 says "machine lands at row 3" — but ROADMAP row 3 is already **landed/archived** (only the pack slice shipped; the host-facing bounds / behaviour-traces-to-spec / surface-registry checks these rows await were explicitly deferred to E-6 [target] and rows 55+). Naming a closed row as the pending owner is an orphan reference; re-point these to the live future owner (rows 55+ / E-6). | should-clarify | **FOLDED** (same sitting) |
| F4 | **Stale TODO — owner event already occurred.** M-065 (E-16) is TODO with owner "row 52 migration landing"; row 52 **landed 2026-07-05** and the thin-loader is live. Either reconcile the row to BUILT/verified (its check — diff-proven fork map + loader shown before flipping — happened as process) or re-state what still gates it. | should-clarify | **FOLDED** (same sitting) |
| F5 | **Coverage-validation and header provenance are stale.** The walked checklist claims "Every spec anchor … 70/70" and the header says "kept current through SPEC v0.10.0"; SPEC is now **v0.14.0** with ~78 index anchors (tonight added B-2, E-18, T-13..T-15, INV-18..INV-21 plus rows M-072..M-083, none named in the header provenance). Mechanized coverage is still green, but the hand-walked count/version undercut the "walked by hand" claim — re-pin at this milestone (M-1 says headers re-pin here). | should-clarify | **FOLDED** (same sitting) |
| F6 | **Shipped skill files missing from the inventory.** Each skill folder ships a `README.md` and a `LICENSE` (10 files: `skills/{live-spec-base,spec-author,product-prover,build-pipeline,communicator}/{README.md,LICENSE}`) — a host installing a skill folder receives them — but the inventory lists only each `SKILL.md`. Per the inventory's own rule ("every file a host … receives") either add them (a per-folder or glob entry) or state they are non-inventoried skill scaffolding. | should-clarify | **FOLDED** (same sitting) |
| F7 | **Shipped script missing from the inventory.** `scripts/sync-mirrors.sh` (the D-4 package-is-source mirror machinery) is committed and reader-received but has no inventory entry and no owning test — the only top-level `scripts/` artifact and it is invisible to `test_artifact_inventory`. | should-clarify | **FOLDED** (same sitting) |
| F8 | **Inconsistent docs/ dir coverage.** The inventory lists `docs/prover/` and `docs/decisions/` as record dirs but omits `docs/research/`, `docs/prior-art*.md`, `docs/queue-archive/`, and `docs/audit/` — all reader-received in this flagship repo. Either include them for consistency or write the scoping rule that separates ships-with-repo records from research-only material. (`.gitignore` similarly uninventoried, but standard-config omission is defensible.) | worth-considering | **FOLDED** (same sitting) |
| F9 | **Closed row named as a co-owner.** M-018 (T-8) names "queue archive rule (row 30) + milestone audit"; row 30 is landed/archived. The live owner (milestone audit, M-1) is present, so this reads as a source-of-rule cite rather than a pending owner — lower risk than F3, but tidier to phrase it as "the archive rule (landed row 30)". | worth-considering | **FOLDED** (same sitting) |

## Checks that came back clean

- **(b) Level honesty.** Every row is level `string`, consistent with the matrix's recorded text-product
  interpretation (structural facts testable now; behavioral facts string-level but TODO with a named
  owner). No behavioral discipline is marked BUILT while only text-presence is tested — the BUILT rows
  are all `test_*_states_*` / `test_*_carry_*` structural checks or genuine parse-the-shipped-file state
  checks (e.g. `test_roadmap_single_in_work`). No mislabels found.
- **(d) New-anchor rows.** M-072..M-083 and the rows for T-13..T-15, INV-18..INV-21, B-2, E-18 each
  carry a meaningful, specific DO side and a non-boilerplate NEVER side (e.g. "a fenced prototype is
  never swept", "never lane order moved by appetite", "never a rotten pin trusted silently"). No filler.
- **(e) Stale test refs.** Every test named in a BUILT row exists in `tests/*.py` (also mechanized by
  `test_matrix_built_rows_name_real_tests`). Every inventory PATH resolves against the repo. No stale
  citations.
- **Node-block completeness.** All 12 architecture nodes have a matrix block; apart from F1, every
  anchor's home row sits under the correct node.
</content>

All nine findings folded same sitting by the senior: F1 = M-079 moved under attach AND the class mechanized (`test_matrix_rows_sit_under_their_owning_node`); F2 re-cited to E-6; F3/F4 owners refreshed; F5 header re-pinned to v0.14.0; F6/F7/F8 inventory extended (skill READMEs/LICENSEs, sync script, records dirs, prior-art); F9 reworded. Suite 61 green after folds.
