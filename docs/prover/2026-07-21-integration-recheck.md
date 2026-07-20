# Prover record — four-movement integration re-check (2026-07-21)

PROVER-RECORD

Prover skill version: product-prover under live-spec-base v3.2.0 (the false-serialization lens present).
Mode: FULL adversarial pre-push re-check on the INTEGRATED state (HEAD `8d77882`), delta-scoped to
`git diff f46f037..HEAD` per the equivalence-gate discipline (SPEC INV-114). Fresh independent context —
not the seat that authored any lane; this is the combined check the four in-lane provers could not run
(SPEC INV-237).

Verdict: **PASS — zero must-fix. Cleared to push once this record is committed.** The four deltas cohere;
each new/changed invariant is sound as written; both new gates are non-hollow (verified by independent
execution, not by trusting the lanes); the formal index is intact. The suite is green but for one red that
IS this record's own precondition (below).

## The delta judged

Four movements: INV-49 sharpened (co-location in a shared living doc draws no serialization edge),
INV-245 (a core spec names no foreign project / tells no dated incident, enforced by a project-name arm
on gate i), INV-246 (a Stop-hook soft signal on inline-content hoarding), and the M3 prose sweep.

## Soundness of each new/changed invariant

**INV-49 sharpened — sound, and validated by this very integration.** The edge rule still draws an edge on
a true dependency (one movement needs another's landed output) or a same-section / same-behaviour collision
(the two rewrite one clause or one behaviour's rule); only *pure co-location* in PRODUCT_SPEC / ARCHITECTURE
/ TEST_MATRIX now draws none. Safety is preserved: two movements rewriting the same clause remain a
same-section collision and still serialize. Liveness is gained: co-located-independent movements parallelize.
The residual worry — two movements each appending a new row to the same shared table (e.g. two new
Formal-index rows) — is handled by the integration path the rule itself names: integration-only collisions
pre-roll with the landing order declared at claim (INV-49) and the integration re-fence catches any textual
merge conflict at landing (INV-39, INV-200 git-halts-on-conflict). This integration is the live proof: M1
appended INV-245 and M2 appended INV-246 to the same Formal index, landing contiguously at 2389/2390 with no
loss. No contradiction with INV-11 (fence unchanged), INV-198/INV-2 (claim commit under the pen unchanged),
or INV-39 (re-fence still the landing net).

**INV-245 — sound for its stated scope.** The clause states the rule impersonally; the arm is scoped to the
three core specs (STRICT: PRODUCT_SPEC + ARCHITECTURE red a bare name or a name within 40 chars of an ISO
date; DATED: TEST_MATRIX reds only the dated-incident turn). The deliberate non-coverage of skills/README
by the project-name arm is a stated design decision in the invariant ("scoped to the three core specs"), not
a gap — the owner-name arm still covers the whole shipped set.

**INV-246 — sound.** Soft signal, opt-in, library-classified in judge-hooks.json, never blocks a lane, honest
about its false-negative floor (dispatch-count-zero gate). Consistent with the orchestration-law family
boundary (INV-241) and the hedge/answer-first soft-signal shape (INV-238, INV-220).

## Cross-movement contradiction from integration — none found

**INV-214's reason-list is consistent with INV-49 everywhere.** The "surface" → "section or behaviour"
update is uniform across: prose (PRODUCT_SPEC:601), the formal row (PRODUCT_SPEC:2327), M-147
(TEST_MATRIX:339), build-pipeline SKILL.md:470/482-488, and live-spec-base SKILL.md:100-101. The new
product-prover lens (SKILL.md:380) states both sides of the edge rule. No stale "shared surface" /
"doc region" wording survives on any operative surface; `test_lanes_by_graph` (tests/test_traceability.py:1764)
actively guards against the refuted "doc region" wording returning and requires the "convergence point"
principle on M-147.

**No half-swept provenance.** `grep -E 'track-coach|tlvphotos|tlvphoto|promoter'` over PRODUCT_SPEC.md and
ARCHITECTURE.md returns zero. `scripts/check-shipped-language.py` reports rc=0 over the whole shipped set.
The WHY the gate is green: the sweep reworded the ~45 provenance lines to impersonal present tense and moved
the history to JOURNAL.md (dated entries confirmed present, nothing lost).

## Hollow-gate check — both gates verified non-hollow by independent execution

**INV-245's project-name arm genuinely detects.** Fired against a crafted temp tree:
`PRODUCT_SPEC.md` with a bare `track-coach` and a `promoter near 2026-07-01` both red [project-name] (STRICT);
`TEST_MATRIX.md` with an undated `tlvphotos` was correctly *ignored* while `track-coach on 2026-07-05`
red — proving the STRICT-vs-DATED scoping is real, not a check that looks at nothing. Word boundaries confirm
`\bpromoter\b` never matches inside `test_promoter_harvest_trio` and the forbidden names live only as
allowlist data (the detector source names no project).

**INV-246's hook genuinely fires and stays silent correctly.** Ran `hooks/lean-orchestrator-scan.py`
against four crafted transcripts (independent of the lane's own fixtures): 60 KiB inline Read with no
dispatch → FIRED; same hoard + one Agent dispatch → silent; hoard on a sidechain (worker) read → silent;
100-byte read → silent. Behaviour matches the spec on every axis.

## Formal-index integrity — intact

INV-245 and INV-246 each appear exactly once in the Formal index (grep count 1 each), contiguous at
PRODUCT_SPEC.md:2389-2390, each with its prose home (index-prose gate `check-index-prose.py` green, 339
anchors all carried). M-430 and M-431 present once each in TEST_MATRIX, each pinning INV-245/INV-246 with
named test functions in `tests/test_lean_orchestrator_arm.py` and `tests/test_guardrails.py`. The ARCHITECTURE
guardrails node owns both invariants. INV-11/39/198/200/214 unaffected.

## Suite

`1720 passed, 1 failed` (216s). The single red is `TestGateA_ProverRecord::test_real_repo_passes` — the
prover-record freshness gate (SPEC M-6) reddening because the newest committed prover record (`31437f6`)
predates the last PRODUCT_SPEC.md change (`8d77882`, the M3 sweep). That gate is demanding exactly THIS
re-check record; committing this file clears it. It is not a defect in the delta — it is the pre-push gate
working as designed. Every other gate (index-prose, shipped-language, guardrails, traceability, the two new
feature suites) is green.

## Mandatory-sweep note

This is a delta-scoped integration re-check of four already-proven, already-tested movements, not a
first-pass FULL prove of a new surface; the per-movement mandatory sweeps were run in each lane's own record
(`docs/prover/2026-07-21-inv245-project-name-arm.md`, `docs/prover/2026-07-21-axes-push-recheck.md`, and the
lane records). This pass adds the combined-integration read those isolated passes could not: cross-movement
contradiction, formal-index collision, and independent hollow-gate execution. All clean.

## Recommendations (non-blocking, taste-call)

1. `recommendation · later` — INV-245's arm scans only the three core specs by design. If a foreign project
   name later creeps into a *shipped skill file* (skills/*.md) or README, the project-name arm will not catch
   it (only the owner-name arm scans there). Worth a one-line note in the invariant that this non-coverage is
   deliberate, so a future reader does not read it as a gap and "fix" it into a broader scan that would red
   legitimate cross-references. No action owed now.
2. `recommendation · later` — INV-246's Bash file-dump detector matches six literal verbs; the spec is candid
   that grep/awk/python dumps escape. Fine as the honest first net; no change owed. Flagged only so the
   escape stays a known, documented boundary rather than an assumed-complete one.

## Bottom verdict

**Zero must-fix. The four movements cohere, both new gates are non-hollow, the formal index is intact — commit
this record and the tree is clean to push.**
