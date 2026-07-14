# Design review — the cross-host coordinator (INV-149)

Date: 2026-07-14. Scoped pass (a surface add), run right after the prover (SPEC INV-141).
Recommendations and questions only; nothing here blocks the landing.

## Same-kind groupings the text now declares, and behaviour parity within each

**Single-instance guards.** Members: the per-host filesystem lock (`single_instance`, an `O_EXCL`
lockfile stolen by age) and the cross-host claim (`claim_winner` over the shared item's claim
comments, stolen by age). Parity holds by deliberate reuse — both use the same stale bound
(`LOCK_STALE_SECONDS`), and both are stolen by age so neither can blind the door permanently. The
justified divergence: the filesystem lock is a mutual exclusion (one holder over an atomic `O_EXCL`),
while the claim is a leader election (one winner arbitrated from a shared append-only comment log,
because the shared medium offers no compare-and-swap). The spec names the lift ("the per-host lock
lifted from the filesystem onto the repo"), so the divergence is declared rather than silent.

**Hidden markers on the source item.** Members: the surfaced-generation record (`SURFACED_MARKER`,
carrying a generation) and the claim (`CLAIM_MARKER`, carrying host plus generation). Parity in form
(both hidden HTML-comment markers read by a dedicated parser), distinct in role and in string, so a
claim never cross-reads as a surfaced-generation record. This distinctness is the fold for prover
finding #1.

## The strongest likely divergence, surfaced to the human (a taste call, not a defect)

The claim posts a comment on every contended round (post-then-read is the atomic claim primitive over
a medium without compare-and-swap), so a losing host leaves a claim comment behind. In steady state a
surfacing settles to one claim plus one surfaced-generation record; a contended round adds one extra
claim comment. The alternative — read-first-then-post — would reduce comment noise but reopens a
time-of-check/time-of-use race that could let two hosts both deposit. The design keeps the
post-then-read primitive for correctness. Worth Alexander's eye: is a claim comment on the source
Issue/Discussion acceptable visual noise for a stranger reading their own thread, or should the claim
live on a quieter shared point (a git ref, a state file) at the cost of more machinery?
