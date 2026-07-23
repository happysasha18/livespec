# Junior delegation protocol

The full protocol referenced from `SKILL.md`'s "Gates worth remembering" section — decided from the
request, BEFORE the first tool call (SPEC INV-69).

**Junior delegation (decided from the request, BEFORE the first tool call):** the trigger is judgment
against mechanical — work whose steps can be written precisely (known edit strings, a known command,
fan-out fact-gathering, a report or list or dump to produce) routes to a worker, while anything carrying
judgment or design stays senior. Size is a weak hint only, never the decider. The trigger, the tier
ladder, and the raw-output law all live in the base skill's rule 5 and the routing rule — this passage is
their reference; it is not a second home (live-spec-base rule 5, SPEC INV-69).

**The routing rule (SPEC INV-69) picks the tier — propose the cheapest tier that can pass the brief, the
senior may overrule it aloud:** the proposal reads the STEP and kind of the work, beyond the row's size
alone — a judgment step (spec, prove, architecture, matrix-level calls, findings triage, any taste call)
proposes the senior and is never routed down, a mechanical step proposes a worker at the tier above. The
economy rung moves the threshold (at `lean` an airtight brief rides one tier cheaper, at `tight` the
cheapest sufficient tier is always the proposal). And the proposal is ADVISORY — the senior may override
per wish, the override logged as one line on the checkpoint and the delivery report, proposed tier → chosen
tier → why.

**The brief is self-contained (the BMAD story-file lesson):** delegated work ships as one document
embedding the EXACT spec sentences it serves, the exact edit strings or commands, the checks to run, and
the checkpoint path — the worker never hunts context, never interprets the spec, never decides. If writing
the brief means deciding something first, that decision is the senior's and happens BEFORE delegation —
"explaining it would take longer than doing it" is how delegation silently dies.

**The brief's birth has three laws (SPEC INV-53/54/55):** a brief that edits existing files is born from
READING them in full — three recorded lines per file (current state · what changes · what must survive),
every step back-referencing its spec sentence, every technical claim citing a source (a file:line, a
command's output), never memory of a file. The brief carries the closed HALT list — ambiguous requirement
· two consecutive unexplained failures of one command · missing config/dependency · acceptance impossible
as briefed — stop WITH evidence, otherwise run to completion (the senior's escalation ladder is a separate
move, after a failed acceptance). And the brief is SIZED — its text within ~300 lines, at most ~8 files to
edit [default], the work splitting above either — passing PATHS, never inlined file bodies. See the private
playbook repo's PLAYBOOK.md.

**The worker contract (SPEC ACT-3):** the brief NAMES the files the worker may write — its session's
write-ownership narrowed to exactly those, reads free, writes fenced. Same-session sibling-worker files
are fence-benign (the concurrent-edit fence alarms on foreign sessions, staying quiet on your own briefed
hands — the senior who briefed both owns the seams between briefs). Owning those seams is a brief-time
act: before spawning another concurrent writer, the senior confirms its brief's write-set is disjoint
from every already-running writer's brief, or gives it an isolated worktree (SPEC INV-105) — because
the fence stays silent between same-session siblings, this disjointness is settled when the briefs are
written, ahead of the new worker's first write. The session's live setting lines ride
into the brief verbatim — a worker never resolves the settings ladder itself, it cannot hear the human's
spoken word.

**The brief carries the register laws, so the worker's own text obeys them (SPEC INV-221, INV-173).** The
brief states the register laws the worker's report and any agent-to-agent message must hold — the
no-scissors law (no naming a thing by denying its neighbour, SPEC INV-173) and the no-dramatization law
(grading the size of a change, up or down, is the reader's act, SPEC INV-221). A worker writes text a
human reads, and the chat and document judges [INV-203] never read its report, so the brief is where the
laws reach it. The worked instance: workers reporting to this pack opened "Excellent work" and named a
premise wrong "in an important way", both graded-size sentences the worker had no brief telling it to
drop (the owner's count, 2026-07-17).

The brief ARMS the worker for the workshop — it carries the host's problem-ledger path
(`.live-spec/PROBLEMS.md`) with the WATCHED-line duty: workshop noise the worker hits (a flaky harness, a
missing dependency, a tool misbehaving) goes into its checkpoint as a ledger line — signature, date, one
line of context, logged every time — and the senior carries the lines into the ledger at verify (SPEC
INV-23). And it carries the CLOCK — the date and time read at briefing — so the worker stamps its
checkpoint and any dated output from the brief's clock, never an invented hour (SPEC INV-24; a worker WITH
a shell re-reads the machine clock itself — the brief's line is the floor for one without, and elapsed
time is never guessed). And a result failing its brief's acceptance escalates exactly ONE tier every time,
with a logged line covering the move — one rung up, in order, always logged.

**Every delegation reports its saving:** the
delivery report carries one line — what went to the worker and roughly how much senior work it saved.
The line is what keeps the habit alive; a session that never writes it is a session that quietly
stopped delegating. The line lives in the row's delivery report, which the closing commit moves to the archive with the
row, and a suite check reads it from the archive: a delivered row without the line goes red
(SPEC INV-103, INV-276, forward from 2026-07-12).
 The same accounting also names the reads dispatched beside the work delegated, so a session that filled its own context with a read it should have dispatched shows that in the report (SPEC INV-137). The duty binds the
orchestrator seat regardless of model, whatever tier leads the seat.
