# Wish — make long-running work's progress VISIBLE to the human (a pack rule)

**From:** the track-coach window, on Alexander's explicit word (2026-07-10 ~17:10):
«эту привычку пришли лайвспеку плиз». One inbox file, the allowed cross-project write.

## The problem (grounded)

Twice this afternoon Alexander lost the thread of a long-running background operation and
could not tell whether work was happening: «где сюита? я не вижу агентов», «где в фоне? я не
вижу агентов». Root cause is a UX asymmetry the pack should account for:

- A **foreground** command streams into chat — the human sees it.
- A **detached background** shell command (`run_in_background`) shows only a faint UI indicator
  and does NOT stream its output; the agent polls a log file. Invisible to the human.
- A **subagent** shows as an agent panel — but a plain background shell does NOT, so a human
  who looks in the "agents" list finds nothing and assumes work was lost.

So whenever the agent runs a multi-minute op quietly (a full test suite, a build, a deploy hook),
the human is left blind, and silence past a couple minutes reads as "stuck or lost."

## The wish

Add a pack rule: **any operation expected to run longer than ~2 minutes — a background command
OR a subagent — surfaces its progress proactively, without being asked.** Concretely:

- On START: one line — what is running, its log path, a rough ETA.
- WHILE running: a progress line every ~2 minutes or at each meaningful stage (don't wait for the end).
- On DONE: a short digest.

Alexander's stated indifference: background vs subagent is fine — **visibility is the requirement.**

## Where it likely belongs (for the live-spec window to judge)

- Most naturally an elaboration of **communicator's narration rule** (the "narrate while working /
  silence past ~10 minutes owes a line" rule) — tightening the cadence for detached/long work
  specifically, and naming the background-vs-subagent visibility trap.
- Or a shared line in **live-spec-base** if it's cross-skill.
- Relates to the existing "no running-theater in loop ticks" note (a scheduled wakeup is a timer,
  not live work) — this is its complement: real long-running work must NOT be silent.

Routing + final wording are the live-spec window's call. Push of that repo stays on Alexander's word.
