# Prover record — ROADMAP 419: a skill change reds until its skill-creator review is on record (INV-208)

Date: 2026-07-17 · Doc version: v2.6.3 (unchanged; the version bumps once at the movement's MINOR gate) ·
Form: SHORT (small delta — a new pre-push gate + its record convention, infra kind, no new stateful
surface beyond the record home, no structure change) with the extra care a new gate warrants · Mode:
CROSS-LINK against the prover-record gate [INV-116] (the shape mirrored), the authority-anchor and
cleanup-notice nets [INV-207, INV-204] (kin structural scans), and the version-stamp law [INV-178]
(the carve-out).

## Previous records clean

The prior record (docs/prover/2026-07-17-row415-authority-anchor.md) closed with zero unfolded must-fix
rows. Its own out-of-scope note flagged the CI mirror gap (gates p and q missing from gates.yml); this
landing folds that hygiene fix in, so the note is discharged, not carried.

## The delta, in one line

INV-208: a push that substantively changes a skill under `skills/` reds unless a committed skill-creator
review record under `docs/skill-review/` names the change and carries its verdict; a pure
version-frontmatter stamp is exempt by construction. Gate `guardrails/check-skill-review.sh` (gate s),
wired into the local pre-push chain and the CI mirror.

## Checks that a new gate warrants

- **The gate has teeth.** Red-first proof captured in docs/prover/red-proof-2026-07-17-row419.txt: all
  18 tests red against the pre-delta tree (gate + review dir + template absent; spec/index/architecture/
  matrix carry no INV-208; pre-push and CI unwired), green after. The three named behavioural red-proofs
  run in scratch git repos so they never depend on the real HEAD: a skill BODY changed with no record
  reds; a version-frontmatter-only stamp (and its `live-spec-base (vX.Y.Z)` base-reference) does NOT red;
  a body change carrying a matching committed record passes. PASS.

- **The carve-out is precise (the row's explicit risk).** The exemption reads the actual changed lines
  (`git diff -U0`), not the file's identity: a changed line is a stamp only when it is exactly the
  `  version: X.Y.Z` frontmatter line or carries the `live-spec-base (vX.Y.Z)` token — the two things
  `scripts/stamp-versions.py` writes. A file whose only changed lines are stamps is not substantive; one
  non-stamp changed line makes it substantive. So a real body edit is never hidden behind a coincident
  version bump, and a pure bump never demands a review. The honest residual risk: a hand-edit landing on
  the base-reference line itself would be read as a stamp — that line is machine-stamped and not
  hand-edited, noted in the gate header. PASS.

- **Freshness, mirroring the prover-record gate.** A stale earlier review does not cover a later change:
  the newest commit touching `docs/skill-review/` must be at least as new as the skill's last change
  commit (equal or an ancestor), so a review committed before a subsequent edit reds. Proven by
  test_stale_record_does_not_cover_a_later_change. An untracked working-tree record does not count
  (test_record_must_be_committed_not_untracked). PASS.

- **Record shape is minimal and checkable.** The gate requires a committed file under the review dir that
  names the skill, carries a standalone `SKILL-REVIEW` marker, and a `Verdict:` line. The home doc
  (`docs/skill-review/README.md`) is excluded from being mistaken for a record. The template
  `templates/skill-review.template.md` ships the starting form. PASS.

- **Kin, no collision.** The gate joins the guardrails family beside check-prover-record, check-board,
  and check-authority-anchor; it reads a file range and requires a file, an internal read, no new seam.
  No new quality budget (a boolean-presence check read by the suite). Placement: a build-time check on
  the author's machine plus the CI mirror. The owns-list edit lands INV-208 on exactly one node
  (guardrails), traceability suite green — every index anchor owned once (a first draft that cited
  INV-116/INV-178 as cross-node tokens in the anchor column was caught by test_architecture_owns_every_
  anchor_once and reworded to plain words). PASS.

## Self-consistency (the gate against this very push)

This movement changes no file under `skills/` — it adds a guardrail, a record home, a template, tests,
and the four doc surfaces, and does NOT bump VERSION (so stamp-versions did not run). The gate run over
the actual push range reports "the push changes no skill body … stands down by name". So the new gate
does not red its own landing, and there is no misclassification to investigate.

## The CI-mirror sync (folded-in hygiene)

`.github/workflows/gates.yml` listed gates through o plus r; it was missing p (touchpoint-kind) and q
(board) from the prior two rows. This landing adds p, q, and the new s, so every local pre-push gate
script is now mirrored in CI. The workflow YAML parses clean.

## Verdict

HOLDS. Zero must-fix. The gate has teeth, the version-stamp carve-out is precise, freshness mirrors the
prover-record gate, and the gate stands down cleanly on this very push (no skill changed). Open ⟨DECIDE⟩
touched by the change: none.
