# Prover record — row 477 MINOR gate (4.0.1 → 4.1.0), clean-seat adversarial pass, 2026-07-23

Prover skill: product-prover, live-spec pack v4.0.1 (base pin `live-spec-base` v4.0.1). This is the
minor-bump gate's clean-context release pass (SPEC INV-237) — a fresh seat with no authorship of the
row-477 changes, run over TODAY'S delta and its seams into the whole spec. Not a re-litigation of the
whole-spec 4.0.0 FULL audit or the 4.0.1 fold batch; the subject is row 477 (TEST_MATRIX.md converted to
the format family's second member; matrix-reference gate + matrix row lint; spec R283–285, glossary
additions, sharpened R124.2/R282/R283.7/R284; ARCHITECTURE.md INV-272..274 [target]; definition
`docs/test-matrix-format.md`).

Previous record checked: `docs/prover/2026-07-23-row477.md` (CROSS-LINK, 13 findings F1–F13, all folded).
Its retirement fan-out and the definition doc both stop at six/seven homes; neither names
`guardrails/README.md` — the seam F1 (guardrails/README.md gate-d text) below is new to this pass, not a
re-open of a folded row.

**Verdict: PASSES-WITH-FIXES.** One blocking defect (F1, a one-paragraph doc fix); two recommendations;
the full-suite gate-A red is the expected pre-bump prover-record freshness gap that committing this
record closes.

| # | Kind / severity | Evidence | Folded / open |
|---|-----|--------------------------|-----|
| F1 | defect / should-fix (blocks the bump) | `guardrails/README.md:20-21` | open — one-paragraph rewrite |
| F2 | recommendation | `guardrails/check-matrix-coverage.sh` (orphan, unwired) | open — cleanliness |
| F3 | recommendation | `prototype/2026-07-23-matrix-format/proof.py` exit-0-on-FAIL | open — read-by-eye, note present |
| N1 | note (not a finding) | full-suite gate-A red | closes on committing this record |
| N2 | note (not a finding) | eight matrix glossary entries vs the "four" framing | all backed; suite green |

## F1 — A surviving document still teaches the retired checkbox gate d

> "**d. The test matrix's coverage checklist is fully walked.** `TEST_MATRIX.md` ends with a 'Coverage
> validation' section of checkboxes; any box left unchecked (`- [ ]`) blocks the push" —
> `guardrails/README.md:20-21`

The conversion retired the coverage-validation checklist and repointed push-gate d to the
matrix-reference gate: `guardrails/pre-push:56` now runs `check-matrix-reference.py`, `.github/workflows/gates.yml`
mirrors it, and `TEST_MATRIX.md` carries no `## Coverage validation` heading. `guardrails/README.md`
still documents gate d as the checkbox walk, and never mentions the reference gate (grep for
`check-matrix-reference` / `row lint` in that file returns nothing). An adopter or maintainer reading the
guardrails README to understand the push gate learns a mechanism that no longer exists and blocks on a
section the matrix no longer has. The definition doc claims the retirement leaves "no surviving document
that teaches the retired form" (`docs/test-matrix-format.md:67`); this delta falsifies that claim because
`guardrails/README.md` was never in the six-home (nor the scaffold-template seventh) fan-out. The delta
introduced the falsehood — the paragraph was true before the conversion.

Rewrite the gate-d paragraph in `guardrails/README.md` to describe the matrix-reference gate (the
committed `## Reference` equals a fresh build off the body; body and Reference agree both directions; an
empty body reds by name — SPEC INV-273), matching `pre-push` gate d and the gates.yml step. Add
`guardrails/README.md` to the conversion's retirement fan-out so the class is closed.

`defect · hard-to-operate (ops-ux)`

## F2 — The retired gate script survives as an unwired orphan in the live tree

> "the checkbox gate that read that checklist retires with it. The retirement fans out to six homes … the
> gate script `guardrails/check-matrix-coverage.sh`" — `docs/test-matrix-format.md:67`

`guardrails/check-matrix-coverage.sh` is fully unwired — no caller in `pre-push`, `gates.yml`,
`ci-mirror.json`, or `gate-red-proofs.json`, and `tests/test_guardrails.py::test_retired_checkbox_gate_unwired`
asserts exactly that unwiring — but the script file itself still sits live in `guardrails/`, carrying
both retired strings the audit sweeps for ("Coverage validation", "check-matrix-coverage"). The authors'
own test defines retirement as unwiring, so this is a defensible reading of the definition doc's
"retired"; it is within the already-folded F5's accepted scope. Surfaced as cleanliness: under the
attic-never-delete discipline a dead gate script should move to `attic/` with one manifest line (or be
deleted), so a future reader browsing `guardrails/` does not mistake an unwired script for a live gate,
and the definition doc's "retired" reads true against the tree.

`recommendation · hard-to-operate (ops-ux)`

## F3 — The content-preservation proof prints FAIL but exits 0

`prototype/2026-07-23-matrix-format/proof.py` re-run against the current tree prints
"Verdict: FAIL — an unexplained token difference remains" yet returns exit 0. The proof is a one-shot
artifact read by eye (its PASS is captured in `gate-d-green.log`, and it is wired into no gate — grep
confirms no reference from `guardrails/`, `scripts/`, `tests/`, `.github/`), so the exit code gates
nothing. The FAIL on re-run is fully anticipated: PROOF.md carves out that re-running after the row-477
close flips M-448/M-449/M-450 from todo to built "is expected to show those three rows as a residual and
is not a conversion defect," and I verified the entire residual maps to exactly those three rows'
todo→built flip and owning-test repoint (built 411→414, todo 38→35; the added word tokens are the new
specific test-function names). The proof method and its captured PASS are sound. Minor: an exit code that
disagrees with the printed verdict is a latent footgun if the script is ever wired; the PROOF.md note
covers the human path today.

`recommendation · missing-outcome-check (postcondition)`

## N1 — Full-suite gate-A red is the expected pre-bump state, not a delta defect

`python3 -m pytest -q tests` → **1 failed, 1826 passed**. The one red is
`tests/test_guardrails.py::TestGateA_ProverRecord::test_real_repo_passes`: the newest committed prover
record (`docs/prover/2026-07-23-row477.md`, commit cc07a30) predates the last PRODUCT_SPEC.md change (the
redundancy fold, commit aaf9a15). This is precisely the freshness gate the minor-bump clean-seat pass
exists to satisfy — the fold's spec text (R283.7 leaning on INV-270, R284's merged single agreement
criterion) was written after the row-477 record and is proven by THIS pass. Committing this record makes
the newest prover-record commit post-date aaf9a15 and turns gate A green. No other test regresses; INV-39
(green on the merged tree) is met the moment this record lands with the bump.

## N2 — "Four glossary terms" undercounts; eight matrix entries are present and all backed

The delta adds eight matrix-related glossary entries (artifact inventory, matrix Reference,
matrix-reference gate, matrix row, matrix row lint, never side, node block, test-matrix format), not the
four the commit message names. Each is defined once and used in the R283–285 body; the vocabulary and
one-name gates pass in the green suite, so glossary closure holds mechanically. The count in the commit
message is loose; no spec defect.

## Pass 1 — Prover over the delta-in-context (R283–285, glossary, sharpened R124.2/R282/R283.7/R284, ARCHITECTURE INV-272..274)

Every new spec fact is owned and backed. R283 (family member) inherits the format family's laws by
reference and adds only the matrix-particular structure; R283.7 correctly leans on the shared arming rule
INV-270 (index maps INV-270 → R277.19, R277.20, R283.7). R284 (generated Reference) — the fold merged the
two agreement directions into the single R284.3 ("disagree in either direction — a body anchor absent
from the table, or a table anchor carried by no body row — then the gate reds"), which matches the gate's
actual two-direction check. R285 (row lint) carries the F11-fold shape: R285.1/2 red-on-missing, R285.3
the green pass with reach (INV-274 + INV-269), R285.4 the retirement. R124.2 sharpened with the era
clause naming the row lint and reference gate as the derivation's mechanical close. R282's family reach
enumeration extended to include both new gates. Family composition sound: the matrix is the second family
member, the quantifier re-verify (INV-170, run complete in the prior record and re-checked here) finds no
R277–282 sentence the newcomer falsifies. ARCHITECTURE.md INV-272..274 land as `[target]` entries in the
guardrails node, each pinning real machinery. The promised machinery exists and matches its contract:
`scripts/build-matrix-reference.py` (173 lines, the builder — sibling of build-index.py, reads the last
trailing bracket, expands ranges, refuses `-o` onto its input) and `guardrails/check-matrix-reference.py`
(120 lines, the gate — reuses the builder's one parser, holds the three faults, states reach via
`green_reach`). `python3 -m pytest tests/test_matrix_reference.py -q` → **12 passed**. No new contradiction
beyond the prior record's 13 folded findings.

## Pass 2 — Matrix audit of the converted TEST_MATRIX.md

The derivation law holds. `python3 guardrails/check-matrix-reference.py TEST_MATRIX.md` → green, reach
**449 of 449 rows scanned, 365 anchors agree body-to-table**. The row lint
(`test_matrix_rows_have_level_and_negative_side`, its home extended per R285) is green — every body row
pins a ladder level and states its never side, offenders named on red, reach on green. Node-block and
artifact-inventory coverage tests green (13 passed in the block/node/anchor/artifact/built slice).
M-448/M-449/M-450 are flipped `*built*` and name real, existing owning tests (all nine test functions
confirmed present; `test_matrix_built_rows_name_real_tests` guards every built row's owning cell).
`test_traceability.py` → **174 passed**. The one seam: stale references survive in the live tree —
`guardrails/README.md` (F1, defect) and the orphan `guardrails/check-matrix-coverage.sh` (F2,
recommendation). The `## Coverage validation` heading is gone from TEST_MATRIX.md; no surviving test runs
the retired gate; the six named homes plus the scaffold-template seventh are cleanly retired, repointed,
or re-taught.

## Pass 3 — Adversarial verify ("tasks completed, goal missed")

Content preservation is real. PROOF.md records PASS at conversion (word-token + punctuation multiset over
the inventory + rows region, modulo named deltas, all residuals empty), and I spot-verified five ordinary
rows independently (`git show HEAD:TEST_MATRIX.md` vs working tree — M-100, M-250, M-380, M-440 fact text
byte-identical modulo the anchor moved into a trailing bracket, six→five cells, status
lowercased/italicised; M-1 is a Reference-table row). The proof.py re-run FAIL is fully explained by the
M-448/449/450 todo→built flip the PROOF.md carve-out names (F3). Red-first machinery genuinely reds:
`test_reds_a_hand_edited_reference`, `test_reds_a_body_anchor_missing_from_the_reference`, and
`test_reds_a_reference_anchor_no_body_row_carries` mutate real-matrix copies and assert red + the named
anchor; `test_row_lint_names_a_levelless_or_one_sided_row` proves both directions on synthetic rows and a
clean row passing. My own independent seed — an orphan `| QQ-777 | M-000 |` appended to a copy of the real
Reference — red naming QQ-777 (two faults: drift + empty home). Stub sweep of the changed/new files clean:
no TODO/FIXME/placeholder/hardcoded-sample/XXX (the only "todo" hits are the legitimate status
vocabulary). Gate w (`check-every-gate-can-fail`) green — 26 gates, gate d reclassified with the real red
proof. The goal is met; the one gap is the documentation fan-out miss (F1), not a hollow landing.

## What is working

- The reference builder/gate reuse ONE parser (the gate imports the builder's module), so the two can
  never drift — the same one-reader discipline `specformat.py` holds for the index gates.
- The builder guards `-o` aimed at its own input (the row-478 root fix), so the body-clobber that F1 of
  the prior record diagnosed cannot recur through this tool.
- The delta repointed every mechanical consumer in one delivery — pre-push gate d, the CI mirror step,
  the traceability reader, the status assertions, gate-red-proofs.json, the scaffold template — leaving
  the gate chain internally consistent (gate w green).

## Mandatory-sweep note

This is a delta-scoped release pass, not a whole-spec FULL pass; the mandatory sweep table belongs to the
FULL audit (the 4.0.0 record). The quantifier re-verify (INV-170), the one whole-document step a scoped
pass keeps, ran clean against the newcomer: no R277–282 enumeration or universal is falsified by the
matrix becoming the second family member.

Overall readiness: **ready to bump once F1 is folded** — rewrite the `guardrails/README.md` gate-d
paragraph and commit it with this record; the gate-A suite red closes on that commit.
