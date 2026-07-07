# ARCHITECTURE.md humanize — scope finding for Alexander (2026-07-07, session 25)

His 19:07 scope: rewrite ARCHITECTURE.md in the register too. Investigation before touching it:

## What its prose actually is
ARCHITECTURE.md is 168 lines. Its prose (before `## Nodes`) splits into:
- **~15 lines of genuine reader-facing text**, already fairly clean: "How the pack is built" (one node =
  one name = one responsibility), "What 'pin' means here", "When this doc changes". These are register-
  cleanable with real value.
- **A ~90-line inline assignment-history log** (lines 8–92): one running run-on paragraph recording every
  anchor→node assignment landing by landing ("the row-X landing DATE session N: ANCHOR → node (reason) —
  assignment + pin only, no re-prove"). This is provenance machinery, not product prose.

## Test protection (unlike SPEC)
No test asserts any ARCHITECTURE PROSE literal. The tests check only STRUCTURE: the Nodes table
(node→anchor ownership, ≥10 nodes, no orphans), the pins (`path:line` exist and are in range), the
target-node pin honesty, the header format, and anchor-set equality across SPEC↔ARCH↔MATRIX. So the tables
must stay structurally intact; the prose has no phrase-net (rely on the code multiset + a prover fact-check).

## The real question (his decision — NOT auto-done)
"Rewrite the architecture in the register" for this doc is ~85% not a readability job. The 90-line log is
history, and the method's own rule is history → JOURNAL, the doc states today's truth. Three options:
- **(a) Migrate the log to JOURNAL (recommended).** Replace it with a 1-2 line pointer. VERIFIED SAFE: every
  anchor in the log also lives in the Nodes/Seams tables, so anchor-set equality holds after removal (0
  anchors would drop). Then register-clean the ~15 reader-facing lines. Result: ARCHITECTURE.md states the
  current structure cleanly; its assignment history lives where history belongs.
- **(b) Rewrite the log in the register in place.** Low value (a dated assignment ledger is inherently
  list-like and code-dense) and keeps history in the wrong home.
- **(c) Leave the log inline** — he wants the provenance in ARCHITECTURE.md; only touch the 15 reader lines.

## Why the loop stopped here
The SPEC.md humanize movement (his primary ask) is 100% done and gated green. Two genuine decisions now
block further meaningful progress: this ARCHITECTURE structure call, and the "Asking what the product does"
tested-scissors/Russian-trigger finding (separate doc). Both are his policy calls; auto-deciding either
would churn or overreach. Clean handoff point.
