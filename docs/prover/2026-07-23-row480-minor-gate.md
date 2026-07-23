# Prover record — row 480 MINOR gate (4.1.0 → 4.2.0), clean-seat adversarial pass, 2026-07-23

Prover skill: product-prover, live-spec pack. This is the minor-bump gate's clean-context release pass
(SPEC INV-237) — a fresh seat with no authorship of the row-480 changes, run over the delta and its
seams into the whole spec, opening hypothesis "tasks completed, goal missed". The subject is ROADMAP.md
converted to the format family's third member (the queue): `docs/roadmap-format.md` new; PRODUCT_SPEC.md
R286–288 + glossary; TEST_MATRIX.md M-451..453; ARCHITECTURE.md INV-275..277 (guardrails node);
ROADMAP.md converted — 227→228 closed rows moved to `docs/queue-archive/rotated-ROADMAP-2026-07.md`,
117 live; every parsing consumer repointed; `templates/ROADMAP.template.md` rewritten; converter + proof
under `prototype/2026-07-23-roadmap-format/`. Precedent record shape: `docs/prover/2026-07-23-row477-minor-gate.md`.

**The tree advanced under this audit.** The orchestrator was folding live: HEAD moved 6edcf32 (round-3,
118 live / 227 archived) → 0a85555 (round-4 cold-read fold, 117 live / 228 archived) → 9e6195a → 9a5a623 →
f1d9d1d ("density bound restored") during the walk. All observations below are pinned to **HEAD f1d9d1d**,
the tip when the walk closed. The one blocking finding names the offending landing commit explicitly so it
survives further movement.

**Verdict: PASSES-WITH-FIXES.** One blocking red on the merged tree (F1, a NEXT_STEPS refresh the round-4
override-fold omitted) with its class fix (F2); the format landing itself is substantive and
content-preservation is proven and reproducible. The gate-A prover-record red is the expected pre-bump
freshness gap this record closes (N1).

| # | Kind / severity | Evidence | Status |
|---|-----|--------------------------|-----|
| F1 | defect / must-fix (blocks the bump) | `check-landing-next-steps.py` + `tests/test_landing_next_steps.py::test_real_repo_range_refreshes_next_steps` red at HEAD | open — refresh NEXT_STEPS.md for the row-128 move |
| F2 | defect / should-fix (the class behind F1) | repoint fires on historical-landed relocation (row 128, landed 2026-07-06) | open — carve out fresh-landing vs relocation |
| N1 | note (not a finding) | gate-A prover-record red | closes on committing this record |
| N2 | note | `test_withdrawal_convergence` ERROR in the 6-min run | transient race with the moving tree; isolated re-run passes |
| N3 | note | row 480 wish says "five parsing consumers" | undercount; more were repointed and are green — loose count, no defect |
| N4 | note (design-review parity) | queue carries no generated code→location Reference gate | sound member asymmetry — the queue owns no codes; recorded, not a break |
| N5 | note (composition) | seven-day in-work staleness re-read defined but unenforced | its sweep is ROADMAP row 481 (queued, unbuilt) — forward reference |
| N6 | note | `templates/ROADMAP.template.md` lists four keywords, omitting *while* | illustrative preamble; the family set is five — minor |

## F1 — The round-4 override-fold archived an already-landed row without refreshing NEXT_STEPS.md

> `landing commit 0a85555c flips ROADMAP row(s) 128 to landed but does not touch NEXT_STEPS.md (INV-242)`
> — `guardrails/check-landing-next-steps.py` at HEAD f1d9d1d

Commit 0a85555 (the round-4 cold-read fold) moved row 128 from the body to the July archive with its
archived status reading `**landed 2026-07-06 ~13:52 …**`, and that commit did not touch `NEXT_STEPS.md`
(its diff touches ROADMAP.md, the archive, and the prototype only). The repointed gate — re-keyed by the
conversion delivery from "a Status cell flipped to landed" to "a body row moved to the archive whose
archived status reads *landed*" — therefore reds, and its committed test
`tests/test_landing_next_steps.py::test_real_repo_range_refreshes_next_steps` reds with it. No commit after
0a85555 (9e6195a, 9a5a623, f1d9d1d) touches `NEXT_STEPS.md`, so the red is persistent and reproducible at
HEAD.

The gate is behaving exactly as the repoint's own contract specifies (`docs/roadmap-format.md:69`), so this
is not a gate bug — it is a genuine INV-242 violation by commit 0a85555. Round-3 (6edcf32), which moved 227
landed rows, did touch NEXT_STEPS.md (7 lines) and passed; the round-4 fold moved one more landed row (128)
and dropped the refresh. Under INV-39 (green on the merged tree) and the push gate, the bump is blocked
while this stands: the suite is red on a non-freshness gate, and Done-when leg 4 ("every parsing consumer
reads the new shape with its tests green") is unmet on the real repo — the consumer's fixtures are green,
but its real-repo test reds.

Fix: refresh `NEXT_STEPS.md` in the commit that relocates row 128 (fold it into the bump commit, or a
follow-up). This clears the red directly. F2 is the class fix that keeps it from recurring.

`defect · missing-outcome-check (postcondition)`

## F2 — The repointed gate treats a historical relocation as a fresh landing

Row 128 landed on 2026-07-06; it sat in the body carrying its inline landed report because the old format
kept landed rows live. The new live-body law relocates it to the archive — no new work landed, no "next"
changed. Yet the repointed gate keys purely on "moved to the archive with archived status *landed*", so it
demands a NEXT_STEPS refresh for a relocation that states nothing new. Every future override-fold, re-run
of the converter, or re-archival of a historical landed row will red the same way — the conversion's own
cleanup fights its own gate. This is the class behind F1, surfaced by the adversarial hypothesis: the tasks
(repoint the consumer, fixtures green) completed, but the goal (the consumer reads the real repo correctly
across the conversion's relocation moves) is missed.

Recommend the repoint distinguish a **fresh landing** — a row that was live-and-open before this commit, or
whose archived landed-date is ~the commit date — from a **historical relocation**, and owe the NEXT_STEPS
refresh only on the former. The strict-touch path (F1) unblocks the bump today; this carve-out is the
durable fix. Either is defensible; the class is recorded so the orchestrator chooses.

`defect · hard-to-operate (ops-ux)`

## Claim-by-claim — ROADMAP row 480 Done-when legs (read live/in-work in ROADMAP.md at HEAD)

- **Leg 1 — the format definition stands in the family's docs and is proven.** MET. `docs/roadmap-format.md`
  (74 lines) states the queue-particular rules and inherits the family laws by reference; R286–288 bind it;
  the "roadmap format" glossary entry is present (PRODUCT_SPEC.md:199). Proof PASS (below).
- **Leg 2 — body reads live-only, content preservation proven across body plus archive.** MET. The body holds
  117 live rows and no terminal-closed status (the armed-lint signal fires — R287.1). `proof.py`, now pinning
  OLD to git `859dcfc` via subprocess (the row-477 F3 re-run footgun fixed — reproducible from a clean
  checkout), re-runs to **PASS, both residuals empty, exit 0**. Independently verified: 345 = 228 archived +
  117 live; five random archived rows (128, 258, 340, 419, 470) byte-identical to `859dcfc:ROADMAP.md`.
- **Leg 3 — status and class vocabularies closed and lint-held.** MET. `queue_row_lint` (TestQueue, extended
  in place, no new standalone script — matches the matrix row lint's homing) proves six red modes by fixture
  (six-cell · out-of-order id · unknown status · dateless status · unknown class · trigger-less deferred),
  a clean body passing, plus the armed real-body run with its reach line and the arming discipline (INV-270).
  `test_roadmap_class_vocabulary`, `test_roadmap_in_work_cap` (386/412/480 = 3, at the T-18 cap) green.
- **Leg 4 — every parsing consumer reads the new shape with its tests green.** NOT MET on the merged tree —
  F1. `rotate-doc.py --close-row` (dry-run OK), `check-doc-rotation.py` (OK, nothing lost), `crosscut_counter.py`
  (runs), `check-doc-bound.py` (OK, ROADMAP within its ratcheted bound), and the union scans
  (`test_delegation_line`, `test_footprint_note`, `test_traffic_transport`) + TestQueue are green (39 passed);
  but `check-landing-next-steps` and its real-repo test red (F1).
- **Leg 5 — lints + cold reader reach two consecutive clean reads.** Process evidence only: the round-4 commit
  is a "cold-read fold" and later commits are density-bound restores, so the comprehension gate was being
  settled during the walk. Not mechanically provable by an auditor; recorded as the softest leg.
- **Non-goals.** Held: ARCHITECTURE format stays row 456 (INV-275..277 are queue-scoped, untouched); no
  re-prioritization — content preservation proves every open row's meaning survives.

## Stub sweep

Clean over the delta files (`docs/roadmap-format.md`, ROADMAP.md, the archive, `rotate-doc.py`, the
doc-rotation and landing-next-steps gates, `crosscut_counter.py`, the three union-scan tests,
`test_traceability.py`, the template, `convert.py`/`rowconv.py`/`proof.py`): no TODO/FIXME/placeholder/lorem/
hardcoded-sample/0000-00-00/XXX. The only *todo*-shaped hits are the legitimate status-vocabulary words.

## Design-review pass — the three format members (spec / matrix / queue)

Same-kind behaviour holds across the members with one recorded asymmetry (N4). Arming rule: the queue arms
in one delivery via a member-specific behavioural signal (no terminal-closed row in the body), the family's
INV-270 pattern. Row lints: the two row documents (matrix, queue) each carry a row lint homed in the
traceability suite, extended in place, stating reach on the green line (INV-269) — parity holds; the spec,
not a row document, carries the index/Reference gate instead. Generated section: spec and matrix each carry
a generated code→location Reference under a build-equality gate; the queue owns no codes of its own (its
trailing anchors point out to PRODUCT_SPEC.md), so it has no Reference table to rebuild and no build-equality
gate — its generated section is the rotated-manifest under the nothing-lost cross-check, which is the correct
member-specific form because the manifest is not rebuildable from the shrunken body. Recorded as a note, not
a parity break.

## Surface-composition pass — statuses × the laws

The deferred trigger re-read at queue-take and milestone (R287.4, format §status) holds; the terminal move
at the closing commit (R287.1, INV-276) holds and is proven by the archive being byte-identical to
`859dcfc`; the multi-leg whole-close (R287.5) is stated in both homes. The one composition hole the walk
surfaced empirically is the landing-move × historical-landed-status interaction (F1/F2). One documented gap
(N5): the seven-day in-work staleness re-read is defined in the format doc but its enforcing sweep is
ROADMAP row 481 (queued, unbuilt), so a stale in-work row has no mechanical catch today.

## Quantifier sweep — docs/roadmap-format.md and the new spec requirements

R286 correctly names the queue "the format family's third member, joining after the spec and the matrix";
`docs/spec-format.md` carries no member enumeration (member-agnostic, so a fourth member — ARCHITECTURE,
row 456 — widens nothing); the matrix's "second member" phrasing stays true. No two-member universal a
newcomer falsifies. Minor: `docs/roadmap-format.md:3` names only the spec as sibling family, not the matrix
(harmless); the template preamble lists four keywords, dropping *while* from the family's five (N6,
illustrative).

## Archive verification (task 6)

Five random archived rows (128, 258, 340, 419, 470) byte-identical to `git show 859dcfc:ROADMAP.md`. The
three recorded overrides carry as stated: row 445 archived with its corrected `**landed 2026-07-23
(v4.0.0)**` marker + delegation line, the old `IN-WORK 2026-07-22 …` cell riding verbatim inside the status
note; row 99 archived verbatim; row 128 archived verbatim (its INV-242 landing-refresh is F1); rows 55/129/131
now *deferred* with named riding-leg triggers; row 69 live and *deferred 2026-07-05 — revisit trigger: the
next edit to the product-prover skill*.

## What is working

- The proof is now reproducible from a clean checkout: `proof.py` pins OLD to git `859dcfc` via subprocess
  and returns exit 0 on PASS — the row-477 F3 re-run-staleness/exit-disagreement footgun is designed out.
- Content preservation is real and independently confirmed (arithmetic 345 = 228 + 117; five random archived
  rows byte-identical; residuals empty both multisets).
- The queue row lint carries the full red-first shape (six proven modes + clean-pass + armed real-body run +
  reach line), homed like the matrix row lint with no new standalone script.

## Overall readiness

**Ready to bump once F1 is folded** — refresh `NEXT_STEPS.md` for the row-128 relocation (or amend the fold
commit), which turns the landing-next-steps gate and its test green; the gate-A prover-record red closes on
committing this record (N1). F2 is the class fix recommended so the next override-fold or converter re-run
that relocates a historical landed row does not red spuriously. Every finding here is RECORDED; the folds
are the orchestrator's.
