# [Project Name] — Roadmap

The wish queue. Intake is continuous — a wish lands here the moment it is spoken. Execution is serial:
the current landing finishes before the next starts.

| # | Wish (plain words) | Class | Status | Decision / acceptance |
|---|---|---|---|---|
| 1 | [Wish in plain producer/user language] | bug / small / surface / large | queued / in-work / landed / waiting | [Who decides, what they need to see, or what was decided] |
| 2 | | | | |

**Class = size, plus a priority mark when it isn't normal.** Size speaks the spec's four words — **bug**
(something shipped is wrong) · **small** (one landing, no new surface) · **surface** (a new stateful
user-facing surface — enters the pipeline in full) · **large** (decomposes into several landings). Priority
is normal unless marked: **· critical** (the shipped product is broken for its user — lands before
everything) or **· quick win** (low effort, immediate value — may bubble up between landings, the jump
marked in the row). Ambiguous size or priority is asked at intake, never guessed.

**Status values:** `queued` (ready to enter the pipeline) · `in-work` (active) · `waiting` (blocked on a
person or event) · `landed` (acceptance met, committed) · `declined` / `deferred` / `superseded` (closed
without landing; the row stays).
