# Wish: before resuming a deferred/queued item, re-derive its current state from the CODE

**The item.** The method should hold an explicit instruction: before a session resumes a DEFERRED or
queued item, it re-derives that item's current state from the code, not from the resume's description of
it. A resume file (NEXT_STEPS / a queue row) records a PAST moment; its technical description of how the
code works can go stale as the code moves on, so the first act of resuming is a freshness check of the
item's own subject against the shipped source — read the code the item touches, confirm the problem
described still matches reality, and re-derive the real current state before designing anything.

**Why (the lived instance).** tlvphotos, 2026-07-20. The session resumed the "trackpad swipe sometimes
advances 2 frames" bug. The resume described the old implementation — absolute magnitude rails
(PEAK20 / FLOOR12 / RISE20 on |deltaY|). But the wheel handler had been refactored since that entry (to a
timing + ratio verdict, `wheelWalkStep`), so the session started designing a fix from a stale technical
model. A reader-worker mapping the code caught the staleness. The bug DID still exist (a diagnostic proved
the refactored code still double-steps on a sparse-late momentum tail and drops fast reswipes), so the work
was not wasted — but had the item already been fixed, the session would have designed a fix for a
non-problem before discovering it. The owner's concern, verbatim in spirit: "why did you start it again if
it was already handled — live-spec should have that instruction."

**The gap vs what already exists.** Adjacent rules cover spec↔code drift (the freshness checks,
reconcile-to-shipped-truth / base rule 13, build-pipeline's architecture step where "each pin comes from a
command you ran, never the doc's own prose", and the queue-take revisit-trigger re-scan INV-129). None of
them names the specific act: *the resume's problem STATEMENT for a deferred item may itself be stale, so
verify the current code state before treating the item's described internals as real.* It is the
resume-side twin of "pins come from commands, not prose", applied to a queued item's own description at the
moment of resuming it.

**Who threw it.** The tlvphotos window (session over ~/tlvphotos), relaying Alexander's own word — he
asked that live-spec hold this instruction.
