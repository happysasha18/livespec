# Bump worker checkpoint — four-lane mechanical landing (composition fixes, test-helper extraction, bookkeeping, 1.1.0 MINOR)

Briefed: 2026-07-12, applier role, mechanical landing across four lanes. HEAD at brief time: 8125b2c,
VERSION 1.0.32, suite 422 green.

## Lane 1 — composition fixes (pending-draft-composition-fixes.md)

### Write-set
- tests/test_restructure_merge_gate.py (T.1 assert added)
- tests/test_docs_layout_vehicle.py (T.2 assert added)
- tests/test_inbox_remote_arm.py (T.3 asserts added)
- PRODUCT_SPEC.md (M.1, M.2, S1.1, S1.2, S2.1, S2.4, S3.1, S3.2 edits + header version bump)
- .live-spec/profile.md (M.3 pointer amendment)
- skills/product-prover/SKILL.md (S2.2 edit + version bump 1.0.2 -> 1.0.3)
- skills/build-pipeline/SKILL.md (S2.3 edit + version bump 1.0.9 -> 1.0.10)
- VERSION (1.0.32 -> 1.0.33)
- .claude-plugin/plugin.json ("1.0.32" -> "1.0.33")
- docs/audit/2026-07-12-composition-walk.md (addendum block appended)
- .live-spec/checkpoints/pending-draft-composition-fixes.md (closed)

### Anchors confirmed present before editing (2026-07-12)
All old_strings in the draft (M.1-M.3, S1.1-S1.2, S2.1-S2.4, S3.1-S3.2, T.1-T.3) were grepped and
Read-verified byte-exact and unique in their files before any edit — no drift from the draft's
8125b2c snapshot.

### Red-first proof
Ran the three extended test files alone before the prose fixes landed:
`python3 -m pytest tests/test_restructure_merge_gate.py tests/test_docs_layout_vehicle.py tests/test_inbox_remote_arm.py -q --tb=no`
-> `3 failed, 8 passed` — exactly the three new asserts (T.1/T.2/T.3), no other breakage. Confirms
red-before-fix per the draft's apply order.

### Version bump (live values read, +0.0.1 each — no drift from draft's V section)
- VERSION: 1.0.32 -> 1.0.33
- .claude-plugin/plugin.json: "1.0.32" -> "1.0.33"
- PRODUCT_SPEC.md header: v1.0.24 -> v1.0.25 (date unchanged, 2026-07-12)
- skills/product-prover/SKILL.md metadata.version: 1.0.2 -> 1.0.3
- skills/build-pipeline/SKILL.md metadata.version: 1.0.9 -> 1.0.10
- .live-spec/profile.md: no version line, no bump (per draft)
- live-spec-base header pins: untouched (per draft)

### Full suite after all edits
`python3 -m pytest -q --tb=short` -> `422 passed in 36.40s` — same count as baseline (422), all three
red tests now pass, nothing else broke.

### Status
Prose + tests + version landed. Addendum appended to docs/audit/2026-07-12-composition-walk.md, draft
closed. Commit next.

### Commit + self-reference note
Committed as 94f0a3f, then amended once to fill the addendum's `<commit>` placeholder with that hash
-> the amend itself produced a new hash, 94f206b (amending changes the tree, which always changes the
hash — a self-referential hash inside a commit's own content cannot converge by construction). Content
commit hash: **94f206b**. The addendum's printed hash (94f0a3f) is one generation stale by this
unavoidable git mechanic; recorded here as the authoritative pointer. Not chasing further amends.

### DEVIATION — Lane 1 landed as two commits, not one
After the content commit (94f206b), the full suite went to `1 failed, 421 passed`:
tests/test_guardrails.py::TestGateA_ProverRecord::test_real_repo_passes red — the M-6 push-gate
freshness check I had just amended correctly detected that PRODUCT_SPEC.md changed with no docs/prover/
record newer than it (the newest prior record, a30a299, predates this lane's spec edit). This is the
gate working as designed, not a content defect; the pre-commit "full suite green" check (422 passed,
run before staging) is what the lane's own instruction gated on. Resolving it requires a committed
docs/prover/2026-07-12*.md record — writing one and folding it into 94f206b via a second amend would
have re-broken the addendum's self-referential hash a second time, so instead landed it as a second
commit: **866f47c** — docs/prover/2026-07-12-composition-fixes-fold.md, short form per the row233-worker
precedent (0 must-fix, 0 should-clarify, citing the composition-walk audit + full-pass-pre-1.1.0 as
prior records). Full suite re-verified green after: 422 passed. check-prover-record.sh: OK.
Lane 1 final commits: 94f206b (content) + 866f47c (prover record).

## Lane 2 — test-helper extraction (compaction-pass audit, C1)

### Write-set
- tests/conftest.py (ROOT, read, read_flat added — plain module-level functions, not fixtures)
- 36 test files carrying a local ROOT line: local ROOT/read/read_flat defs deleted, replaced with
  `from conftest import ROOT[, read][, read_flat]` per file
- docs/audit/2026-07-12-compaction-pass.md ("C1 landed <commit>" note appended)

### Classification (mechanical, verified byte-exact before touching)
- ROOT line: identical in all 36 files (`ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))`) — one grep -u pass confirmed a single variant.
- read_flat: byte-identical in all 20 files carrying it (docstring + body diffed to one variant via awk dedup).
- read (plain): byte-identical in 8 of the 9 files carrying a function named `read` (one file used
  `fh` instead of `f` as the context-manager variable — behaviourally identical, extracted).
- **Deviation from the literal "read" merge**: tests/test_norm_conformance_law.py's `read(rel)` is
  NOT the same function — it whitespace-normalizes via `re.sub(r"\s+", " ", ...)`, a distinct
  semantic (kin to read_flat but without split()'s implicit strip). This is a same-named,
  different-bodied function, not a duplicate. Left it in place, untouched; only its ROOT line was
  replaced with an import. Merging it into the shared `read` would have silently changed its
  behavior (and every other file's `read`), so it was excluded from extraction by design, not
  overlooked — flagged here since the brief's "byte-identical semantics" instruction is exactly
  the check that ruled this file out.

### Mechanism
Wrote a one-off Python transform (regex-matched the exact ROOT line and the exact read_flat/read
function bodies, deleted them, inserted the equivalent `from conftest import ...` line) and ran it
across all 36 files in one pass; `python3 -m py_compile tests/*.py tests/conftest.py` confirmed no
syntax breakage before running the suite.

### Full suite after extraction
`python3 -m pytest -q --tb=short` -> `422 passed in 35.67s` — same count as Lane 1's post-fix
baseline; no test body was touched, only the helper-definition lines, so no behavior change
expected or observed.

### No version bump
Test-internal refactor only; no PRODUCT_SPEC.md, plugin.json, or VERSION touch — matches the
lane's instruction, and (bonus) means Lane 2 does not re-trigger M-6's prover-freshness gate the
way Lane 1 did.

## Lane 3 — bookkeeping, no version bump

### 3a — live-spec-base rule count
Body has 23 numbered rules (verified by grep-counting `^[0-9]+\.` between "## The shared rules" and
"## When NOT to load this"), description said "twenty-one" -> corrected to "twenty-three". Searched
tests/ for a pinned needle on the phrase: none found (only the SKILL.md itself carries the string),
so no test needle to update.

### 3b — ROADMAP rows 266-269 (new, five-cell format matching neighbors)
- 266: communicator body over size ideal (679 lines vs ~500 ideal), extract the 16-rule writing
  register to references/ — lifted from docs/audit/2026-07-12-skill-creator-walk.md finding #2.
- 267: INV-39 stated three times (lines 459/495/1481), spec-author judgment call — lifted from
  docs/audit/2026-07-12-compaction-pass.md finding D1.
- 268: eval-craft follow-ups S1 (communicator INV-27 PARTIAL x3) / S2 (build-pipeline delegation
  eval scenario gap) + N1/N2/N3 notes — lifted from docs/audit/2026-07-12-skill-evals-rerun.md.
- 269: CI's check-prover-record.sh needs the same inbox-deposit carve-out M-6's prose just gained —
  lifted from pending-draft-composition-fixes.md's disposition section ("Mechanical arm of FIX-M").
All four rows verified against TestQueue's parser (tests/test_traceability.py): 5 pipe-cells,
cells[0].isdigit(), cells[2] matches the class-vocabulary pattern ("small" for all four).

### 3c — ROADMAP row 192 trigger fired
Appended to the status/trigger cell: "Trigger fired 2026-07-12 (new prover lenses landed, rows
257/258); activates as its own movement (per docs/audit/2026-07-12-deferred-trigger-rescan.md)" —
wording matches the rescan doc's own line 29/50 verdict (FIRED, its own movement, not this gate's
rider).

### 3d — three checkpoints promoted to tracked audit records
Copied byte-for-byte (plus a one-line HTML-comment header naming source + date) — the checkpoint
originals are LEFT IN PLACE, this is copy-promote not move:
- .live-spec/checkpoints/pending-audit-minor-gate.md -> docs/audit/2026-07-12-minor-gate-walk.md
- .live-spec/checkpoints/pending-audit-once-read-rules.md -> docs/audit/2026-07-12-once-read-rules-sweep.md
- .live-spec/checkpoints/pending-audit-delegation-dedup.md -> docs/audit/2026-07-12-delegation-dedup.md

### Full suite after Lane 3
`python3 -m pytest -q --tb=short` -> `422 passed in 35.22s`. No PRODUCT_SPEC.md touch this lane, so
no M-6 prover-freshness re-trigger (unlike Lane 1).
