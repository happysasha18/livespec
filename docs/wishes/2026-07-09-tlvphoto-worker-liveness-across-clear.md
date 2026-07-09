# Wish: the resume protocol must handle a background worker that outlives a memory wipe

## The item (plain words)
When a session spawns a background sub-agent (a worker) and then the context is cleared (/clear) or handed off,
that worker **keeps running and keeps writing the shared tree**. The next session has no reliable way to know it
is still alive, and the pack gives no protocol for it. Teach the pack two things:

1. **Detecting a live worker after a resume.** `ps` and the harness `TaskList` are NOT proof of death — a
   background agent runs inside the harness with no distinct OS process, and a prior-context agent does not
   appear in the new session's `TaskList`. The reliable signals are: file mtimes / md5 sampled over a few
   seconds (is anything writing the tree right now?), and SendMessage to the recorded agentId (a live agent
   replies; a dead one never does). The resume/handoff note (NEXT_STEPS-style) that records a worker's agentId
   must also state HOW to verify its liveness and reconnect, and must not frame the worker's output as
   "finished" when it may still be running.

2. **The concurrent-writer fence, extended.** Never spawn a second worker onto a shared tree until the first is
   confirmed halted by its own reply. Prefer to **halt background workers before a /clear** (or let them finish)
   so the next session starts single-writer. Same failure family: a worker dies when the window closes or the
   Mac sleeps — a handoff should say so, so nobody is told "safe to wipe, the worker will be recognized."

## Why (what broke)
2026-07-09, tlvphoto: the pre-wipe session told the human "safe to wipe, the worker is live but it'll be
recognized." After the wipe it was not. The resume note recorded the worker's agentId but treated its output as
done. The resuming session declared the worker dead off `ps` + `TaskList` (both empty/misleading) and spawned a
SECOND worker onto the same files, causing a two-writer race on `exhibition.js` and a test file. The human caught
it from the status-line worker label; the true tell was file mtimes. No corruption shipped, but only by luck.
Relevant existing pack matter: the concurrent-edit fence in live-spec-base, and the checkpoint/handoff discipline.

## Who threw it
The tlvphoto host session (Alexander's window), 2026-07-09. Alexander explicitly asked that this case be captured
for the pack.
