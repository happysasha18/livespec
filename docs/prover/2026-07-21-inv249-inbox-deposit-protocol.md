# Prover record — INV-249, the inbox deposit protocol for concurrent windows (2026-07-21)

PROVER-RECORD

Prover skill version: product-prover under live-spec-base v3.6.0.
Mode: FULL adversarial pre-push review of the INV-249 delta (ROADMAP 439), run in a FRESH independent
context — not the seat that authored the clause (SPEC INV-237). Opening hypothesis: "tasks completed,
goal missed."

Verdict: **PASS with folds — one must-fix and two recommendations, all folded before this record.** The
prose protocol closed the sweep-side race and composed cleanly with E-11, INV-174, INV-189, and INV-247,
but the first pass fenced the discipline and forgot the machine. The audit caught it; the fold closes it.

## The delta judged

- PRODUCT_SPEC.md — the INV-249 clause in the earned-message scenario + the Formal-index row.
- inbox/README.md — the `.draft`-then-rename protocol, the gate agreement, the collision-scan, the reap.
- skills/feedback-intake/SKILL.md — the receiving-sweep fence + the reap.
- guardrails/check-earned-message.py — the gate fence (added in the fold).
- ARCHITECTURE.md — owned by the inbox node.
- TEST_MATRIX.md — M-434 under [node: inbox].
- tests/test_inbox_deposit_protocol.py — 7 tests (six string arms + the real-gate arm).

## Findings

**F1 — the mechanical gate was not fenced against `.draft` (MUST-FIX, FOLDED).** The first pass fenced the
receiving sweep (a prose discipline) but left `guardrails/check-earned-message.py` (gate m of the pre-push
hook) reading `.draft` files. The auditor proved it empirically: the gate's `_targets` included a
`X.md.draft` name, `_source_stem` judged it agent traffic, and running the real gate against a mid-write
draft with no birth field exited 1 — a spurious red on the exact truncation-class event INV-249 exists to
prevent, relocated from the sweep into the gate. Folded: `_targets` now skips any name ending `.draft` (both
the directory scan and an explicit file path), inbox/README.md states the gate passes over `.draft` exactly
as the sweep does, and the spec clause states gate and sweep agree. The evasion worry the "whatever its
extension" rule guarded against does not apply — a file left `.draft` forever is never harvested or delivered
either, so skipping it grants no evasion. Red-proven: `test_inv249_gate_passes_over_a_draft` runs the real
gate against a mid-write draft fixture and reds against the un-fenced gate, greens against the fenced one.

**F2 — an orphan `.draft` was a new permanent-red gap (RECOMMEND, FOLDED).** A writer that stopped mid-write
would leave an incomplete `.draft` forever; combined with F1 it would have red every pre-push until a human
removed it. Folded: a `.draft` stale across a full sweep — unchanged modification time, its writer gone — is
reaped the way a harvested file is, stated in inbox/README.md, the feedback-intake sweep, and the spec clause.

**F3 — the collision law was blind to an in-flight `.draft` (RECOMMEND, FOLDED).** While a deposit is in
flight only its `.draft` name exists, so a second writer's "is `X.md` taken?" check answered no, wrote the
same `X.md.draft`, and its rename clobbered the first writer's `X.md` — one of two same-slug deposits silently
lost, a case the `.draft` name made worse than a plain write by hiding the in-flight peer. Folded: the
name-taken collision check reads the `.draft` names too, and two co-located writers on one slug carry their
session tokens so their names cannot collide (base rule 18), stated in inbox/README.md and the spec clause.

## Scope, composition, self-application

- **Scope correct.** The clause scopes atomicity to two windows on one filesystem (the co-located case); the
  remote and stranger arms get atomicity from git commit-and-push, and the clause does not over-claim `.draft`
  for them.
- **Composition clean.** The protocol composes with E-11 (one committed file), INV-174 (the co-located
  deposit is the file alone, a rename being no commit), INV-189 (the earned-message gate, now in agreement),
  and INV-247 (a routed deposit left earned in place).
- **INV-237 self-application.** The two live inbox deposits stay `.md`, not `.draft`: they are complete
  at-rest deposits, and a complete deposit's final name is `.md`. The protocol binds the write, not files at
  rest — forward-binding, the correct self-application result.

## Register, stubs, traceability

No banned contrast-frame scissors in the new clauses; no sentence leads with an internal code. No
TODO/FIXME/placeholder in the delta. M-434 sits under [node: inbox], cites the 7 real test defs, all green;
INV-249 owned exactly once (the inbox node).
