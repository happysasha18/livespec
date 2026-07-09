# Red-first slips on small voiced visual fixes — is the small-fix path stated?

_From: tlvphoto session, 2026-07-10 ~02:15. Wish: examine why the slip happens and state the rule._

## What happened (two fixes in one session, same size, different discipline)

1. **Rail fix** (the floating link and the sound player centred on different x in landscape):
   done BY the book — test row written first, run RED (12px apart measured), then the CSS fix,
   then green. Proper red-first.
2. **Toast fix** (the "link copied" line moved from centre-bottom to beside the link button,
   his voiced note minutes later): the CSS edit and the test row were authored IN ONE BATCH,
   so the row was born green over already-changed code. The red proof was recovered POST-HOC:
   the working CSS was swapped for the HEAD version, the suite re-run, both new rows shown
   FAIL, the fix restored. The evidence ended up complete, but the prescribed order was not.

## Why the slip happens (self-read)

A small voiced fix arrives mid-flow with the diagnosis already in hand; the CSS delta feels
"obvious" and the author batches fix+test to save a suite run (browser suites cost 2-4 minutes
each here). The pipeline's shortcut for tiny reversible edits says "straight to code + a test"
— it does not say in WHICH ORDER when the edit is tiny, so under time pressure the order decays
to fix-first.

## The ask

State the small-fix path explicitly in the pack (test-author or build-pipeline shortcut
paragraph), one of:

- **(a)** red-first holds at EVERY size — a one-line CSS fix still waits for its row to fail
  first; or
- **(b)** batch-authoring is allowed for tiny reversible edits IF a post-hoc red proof is
  mandatory and mechanical: revert the change (git show HEAD:<file>), run the suite, see the
  new rows FAIL, restore — and the commit message must name that proof.

Either answer closes the ambiguity; today each session re-decides under pressure. The human
asked for this examination himself (his 2026-07-10 word: if the order is written and was
missed, hand it to live-spec to understand why and rewrite the process).
