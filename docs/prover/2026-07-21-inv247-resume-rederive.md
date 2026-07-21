# Prover record — INV-247, re-derive a deferred item's state from code before resuming (2026-07-21)

PROVER-RECORD

Prover skill version: product-prover under live-spec-base v3.4.0.
Mode: FULL adversarial pre-push review of the INV-247 delta (ROADMAP 430), run in a FRESH independent
context — not the seat that authored the clause (SPEC INV-237). Delta-scoped to the new invariant clause,
base rule 34, the Formal-index row, and the build-pipeline ownership entry.

Verdict: **PASS with two must-fix, both folded before this record.** The invariant is genuinely distinct
from every neighbour it borders, correctly anchored, and clean in register. Cleared to push once committed.

## The delta judged

A new method discipline: before a session resumes a deferred or queued item, it re-reads the code that
item touches and re-derives the item's real current state, so it never designs a fix from the resume
file's stale description of how the code works. Homes: SPEC INV-247 (clause beside INV-129 + Formal index),
base rule 34, ARCHITECTURE build-pipeline ownership, M-432, tests/test_resume_rederive.py.

## Distinctness — the headline lens (does it collapse into a neighbour?)

It does not collapse. Each border is a genuinely different object:

- **vs INV-129 (queue-take trigger re-scan).** INV-129 reads the row's TRIGGER — should the row come back.
  INV-247 reads the row's SUBJECT — is its stated premise still true against the code. Orthogonal reads on
  the same row; they compose, neither is redundant.
- **vs base rule 13 (primary source).** INV-247 is rule 13's "prose is a lead a fresh read confirms"
  applied at a NEW named breakpoint (resume), the way base rule 8 applies freshness at the version-check
  breakpoint. The named-breakpoint framing is what earns it a distinct invariant; the clause keeps it crisp.
- **vs INV-107 (resume/checkpoint defect).** INV-107 is a checkpoint stale because items shipped to git;
  INV-247 is a premise stale because the code moved. Different object.
- **vs INV-152 / base rule 29 (deferral re-test by derivability).** The sibling resume-time re-test asks
  whether the item is still the seat's to do or the human's; INV-247 asks whether its code premise still
  holds. Both fire at the same resume moment, and the clause now cross-references INV-152 so a resuming
  session is told it owes both reads.

## Safety / liveness

The clause fixes the WHEN precisely: the read fires at the moment one item is actually taken up for work,
narrower and later than INV-129's whole-deferred-set trigger scan. This closes the liveness gap where a
session could honour INV-129 (return the row) and then design without the subject re-read.

## The mechanical-net question (ROADMAP 430's open "a light net MAY check…")

Answered out loud, as every sibling with no gate does (INV-222 / INV-231 / INV-214): no sound push gate is
feasible — a resume is an in-session act at chat cadence with no committed artifact for a gate to scan
(INV-83) — so it stays a discipline the seat holds, open to a chat-law reminder at the resume the way the
deferral line rides the hook. Leaving the MAY unanswered would have been the gap.

## Two must-fix, both folded

1. The spec framing "a second read stands beside [the queue-take re-scan]" read as per-queue-take code
   reads of ALL deferred rows — a cost nobody intends and a disagreement with base rule 34's "first act of
   resuming." Fixed: the read is scoped to the single item being taken up for work.
2. The clause was silent on the mechanical-net question. Fixed: the no-sound-push-gate answer is now stated.

## Register / anchors

Clean. No denied-neighbour contrast frame, no calque, no coined mechanism-name without gloss. Anchors
verified: base rule 13 = primary source, base rule 8 = freshness at breakpoints, INV-129 = queue-take
trigger re-scan, INV-152 = deferral re-test, base rule 34 exists and anchors INV-247.
