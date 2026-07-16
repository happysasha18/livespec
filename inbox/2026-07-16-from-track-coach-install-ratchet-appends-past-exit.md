# Feedback: install-ratchet.sh wires gate r AFTER a host pre-push that ends in `exit` — dead code

**The item.** `adopt/install-ratchet.sh` step f wires the ratchet gate by appending the block to the
end of the host's push gate: `{ echo "-- gate r — ratchet caps --"; ... } >> "$PRE_PUSH"`. A host whose
`guardrails/pre-push` ENDS with a terminating `exit` (the common shape: a final `if [ "$fail" -ne 0 ]; then
... exit 1; fi; echo ...; exit 0`) gets gate r appended AFTER that `exit`. The gate is never reached — the
suite reads green and the adoption looks done, but the ratchet is not actually on the gate. This is the
silent-truncation failure mode the pack warns about, produced by the pack's own installer.

It compounds: the idempotency guard `grep -q "gate r — ratchet caps" "$PRE_PUSH"` then matches the dead
block on a re-run and prints "already wired", so re-running never repairs it.

**Where it bit.** track-coach adopted 2.1.0 on 2026-07-16. The installer ran clean and reported
`wired: guardrails/pre-push gate r`, but the block landed below the file's final `exit 0`. Caught by
running the live hook end-to-end and seeing gate r never print. Fixed locally by moving the block to
just before the final fail-check, next to the host's existing gate h.

**Suggested fix (pack side).** Don't blind-append. Either (a) detect a trailing terminating `exit` and
insert the gate immediately above it, or (b) insert before the last `if [ "$fail" ... ]` fail-check if one
is found, or (c) at minimum, when the tail is not a safe insertion point, PRINT the recipe for the host to
place by hand (the else-branch already does this well) instead of appending silently. Whatever the anchor,
the idempotency guard should also tolerate small wording drift in the gate label (track-coach's is now
"gate r: ratchet caps"), or key off a stable marker comment rather than the human-readable label.

**Who threw it.** The track-coach window, mid-adoption of live-spec 2.1.0 (the 2026-07-16 ratchet wish).
