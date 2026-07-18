# Prover record — 2026-07-18 — ROADMAP row 406 — a dead permission rule, read by config-health (INV-216 / M-397)

Lane 2 of a three-lane run. SHORT-FORM per SPEC INV-61: the delta is a single-module infra extension
of an existing gate (config-health, gate m), no new surface, no new gate letter.

## Previous record

The last prover records in `docs/prover/` (rows 390/392, 420) close clean — no unfolded rows carried
into this landing.

## The delta in one line

config-health (gate m) gains an arm, `guardrails/check-config-health-perms.py`, that resolves every
filesystem path named inside a permission rule in the personal `~/.claude/settings.json` and the
host's project settings and reds a rule whose path is absent — a dead rule surfaces at the gate
instead of degrading silently into prompts.

## The law and its worked instance

The owner reported (2026-07-17 ~15:29) that the harness sometimes refused a push or a deploy. Three
deploy permissions were still written against `~/tlvphoto` after the tree was renamed to `~/tlvphotos`
on 2026-07-10, so for a week those rules pointed at a path that no longer existed. A stale allow rule
fails exactly like a missing one, so the action fell through to a prompt and no one could see why. A
permission rule whose target does not exist is a dead rule; the gate now reads it.

## Cross-link check (prover, CROSS-LINK mode)

- **Owning node.** The guardrails node owns INV-216 in ARCHITECTURE.md, and the new file is pinned in
  its owns-list (`guardrails/check-config-health-perms.py:1`). No new node — the arm extends the
  config-health gate that node already owns.
- **Seam with config-health (INV-175).** The arm is invoked by `guardrails/check-config-health.sh`
  after the hook-drift arms; it resolves the helper by the script's own directory, so it runs whether
  the script is called from the repo or from an installed copy. It accumulates into the same `fail`
  and rides the same exit. No gate letter added: it lives under gate m.
- **CI carve-out (INV-210).** Gate m is already declared a CI carve-out in `guardrails/ci-mirror.json`
  ("m") because it compares installed personal hooks a CI checkout does not carry; the whole script
  skips in CI before the arm runs. The personal-settings read rides that same carve-out, so the
  CI-mirror gate needs no new entry.
- **Known-red proof (INV-212).** Gate m already carries a known-red proof in
  `guardrails/gate-red-proofs.json` (`test_missing_installed_hook_reds`). The meta-gate classifies by
  gate letter, and the arm adds no letter, so no new entry is owed. The arm carries its own red-first
  proof besides (`test_dead_permission_path_reds`, and seven more), captured against the pre-arm tree.
- **Personal-layer stand-down (kin of INV-211).** The arm stands down by name where the settings
  cannot be read: an absent settings file is a legitimate stand-down (exit 0, named), a
  present-but-unreadable one reds (never a false pass). This mirrors the judge-listed gate's shape.
- **Row 384's law — a check that looked at nothing is not a pass.** The arm reports the count of rules
  it resolved and names any rule shape it cannot resolve (an unexpandable variable, a mid-path
  wildcard) rather than silently skipping it.

## No-false-red proof on the real settings

Run against the real `~/.claude/settings.json`: 69 rules, 9 name a filesystem path, all 9 resolved and
present, 0 dead, 0 unresolved — the arm is quiet. The `~/tlvphoto` deploy permissions were already
repointed to `~/tlvphotos` before this landing, so no real-settings fix was owed; the arm confirms the
repaired state passes. Space-containing paths (the Google Chrome binary) resolve whole rather than
splitting into a missing prefix, so they do not false-red.

## Red proof

`docs/prover/red-proof-2026-07-18-row406.txt` — 8 of the 11 M-397 tests red against the pre-arm tree
(the arm absent from `check-config-health.sh`; the spec, architecture, and matrix carrying no INV-216
/ M-397), green after the arm and the documents landed.

## Verdict

No open findings. The delta is owned, seamed, red-proven, and quiet on the real machine. Every
door-granted step applied: spec (INV-216 clause + formal-index row), architecture (owns-list +
file pin), matrix (M-397), test (red-first), code (the arm), verify (the runs above). Design-review
stands down (single-module infra extension of an existing gate, no new same-kind grouping surfaced).
