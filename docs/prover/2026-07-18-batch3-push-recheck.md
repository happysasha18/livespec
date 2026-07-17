# Prover record — 2026-07-18 — batch 3 push re-check

A pre-push re-check of the unpushed batch sitting on top of origin/main (`8f8eab4`), run
independently of the sessions that built it, before the orchestrator pushes.

## The batch

Four commits, HEAD `3f7a6b8`:

- `b112aac` — ROADMAP 420: habits-to-gates audit — ranked promotions + build order
- `92a5e6e` — ROADMAP 390 + 392: split-and-rotate the pack's working docs, nothing lost (INV-209)
- `b179e79` — ROADMAP 420: two gate-chain-integrity gates land — CI-mirror parity (u) and
  judges-listed (v)
- `3f7a6b8` — Add the meta-gate: every push gate carries a known-red proof (gate w, INV-212)

## What was checked

The full test suite ran clean: 1309 passed, no failures, no skips beyond the pinned set.

Every pre-push gate ran individually, a through w (23 gates in total, including the three this
batch adds): all green. Gate k (the compaction freeze) matched its frozen baseline on the first
check, so no re-freeze was needed. Gate g reported one pre-existing pin-drift note
(`templates/skill-review.template.md`) under its non-strict mode; that note is not new to this
batch and does not fail the gate.

Two spot-checks the orchestrator asked for by name both passed: the meta-gate
(`check-every-gate-can-fail.py`) reports all 23 gates a–w compliant, and the CI-mirror gate
(`check-ci-mirror.sh`) reports every local gate mirrored in CI or carrying a declared carve-out.

Every landed row carries its prover record dated 2026-07-18: rows 390/392
(`docs/prover/2026-07-18-row390-392-doc-rotation.md`), and row 420 in two records
(`docs/prover/2026-07-18-row420-ci-mirror-and-judge-listed-gates.md` for gates u/v,
`docs/prover/2026-07-18-row420-every-gate-can-fail.md` for gate w). The audit doc
`docs/gate-audit/2026-07-18-habits-to-gates.md` is present.

## What this batch encodes

Each landing in this batch turns a lesson this same movement paid for into a machine that checks
itself on every future push, rather than a note someone has to remember:

- Doc rotation (rows 390/392) keeps the pack's working docs split and archived so the guards stay
  fast as the docs grow, with nothing lost from the archive.
- The CI-mirror gate (gate u) closes the gap where a local gate and its CI copy could drift apart
  unnoticed.
- The judges-listed gate (gate v) catches a wired chat judge going dark without anyone noticing.
- The meta-gate (gate w) catches the case this movement actually hit: a gate that runs but can
  never turn red, so it passes without ever having checked anything. Alexander asked for this audit
  in person (2026-07-17, roughly 18:25 to 18:27), naming the hollow authority-anchor gate and a
  worker's false all-clear as the two cases that prompted it.

## Verdict

PUSH-READY. Suite green (1309 passed), all 23 pre-push gates green, both requested spot-checks
green, every prover record and the audit doc present and dated. No blocker found.
