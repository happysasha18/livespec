# Prover pass — 2026-07-05, base skill + settings ladder (rows 24+36, SPEC v0.5 → v0.6)

Mode: CROSS-LINK (new surfaces [E-12, E-13, INV-13, INV-14, M-7, D-4, D-5] against every named existing
surface), per the surface-add rule; doubles as the push-gate whole-spec re-check [M-6]. Previous record
(2026-07-05-rule9-detail.md) has no unfolded rows.

Evidence base for the design itself: a full read of the four SKILL.md files + templates + ADOPT.md
(raw greps in scratchpad `base-skill-sweep.md`, spot-checked by re-running family 3) — the base skill's
rule list is the evidence's repeated-rule set, not a from-memory list.

| # | Finding | Severity | Status |
|---|---|---|---|
| F1 | E-8's sentence still had communicator reading ONE file ("host profile … read by communicator") while E-13 defines a three-step resolution — a reader could implement single-file reads and silently skip the personal layer | must-fix | FOLDED — contract paragraph rewritten: communicator reads the RESOLVED contract, not any single file |
| F2 | The contract paragraph enumerated personal-class settings (mode, trust, language) as the HOST profile's content, contradicting E-13's "about the human → personal step" placement rule | must-fix | FOLDED — same rewrite: personal lines live in the personal profile; the host narrows them per project on the human's word |
| F3 | The inherit note in four working skills pins the base version as a literal ("v0.1.0") — four copies of one fact, guaranteed stale on the first base bump; exactly the drift class INV-13 exists to kill | must-fix | FOLDED — E-12 now states the pin is swept by the same landing that bumps the base, never left stale; the sweep is mechanical (grep for the old pin) |
| F4 | The personal profile (`~/.claude/livespec/profile.md`) lives outside any git repo: no history, no backup, no concurrent-write fence (INV-11 speaks of repos). Two sessions writing it, or a disk loss, silently loses the human's contract | should-fix | QUEUE ROW 38 — candidate: make `~/.claude/livespec/` a private repo, or symlink into an existing private one (the playbook pattern that already paid off for CLAUDE.md) |
| F5 | "base skill" (spec concept) vs `livespec-base` (folder) — two handles for one surface | noted, no fold | The spec names the concept once and pins the folder via D-4; acceptable while D-4 is open, re-check at D-4's close |
| F6 | Defaults table sets `trust: low` as package default — checked against INV-9: a shipped default is not the agent setting trust; no violation | green | — |
| F7 | M-1 milestone compaction already covers pruning pre-base restatements from skills ("redundancy removed from … skills"), so INV-13's pruning path has a home; no new machinery needed | green | — |

Whole-spec re-check: anchor prose ↔ Formal index diff = zero mismatches after edits (re-run below, before
commit). Anchor-set delta vs v0.5 is a deliberate, named add: +E-12 +E-13 +INV-13 +INV-14 +M-7 +D-4 +D-5,
no removals; E-8's one-liner renamed (user → host profile) with its meaning narrowed by design, references
swept (SPEC contract paragraph, ADOPT.md Phase 6).

Verdict: green for push with F1–F3 folded (same-record folds do not re-trigger the gate, per M-6); F4 is
queue row 38.
