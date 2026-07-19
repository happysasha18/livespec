# Standing behaviors that fire only on a reminder — a conduct audit (2026-07-19)

Alexander asked for this audit on 2026-07-19, after noticing a pattern across the session: the seat
(the orchestrator agent running the live-spec pack) is capable of a behavior on paper, yet the behavior
only happens once he says the word.

## The finding

The pack (the shared skill library) and the personal profile state many standing behaviors as
default-on for the seat. A subset of them, however, only fire when Alexander reminds the seat in the
moment. In this session alone he had to remind the seat four times: to delegate work to cheaper
workers, to keep the seat's own context lean, to run independent work in parallel, and to drop graded
language from its replies.

The audit found a discriminator that sorts every standing behavior into one of two groups. A behavior
earns a machine when a machine can verify it by reading the turn's output text — the words the seat
actually sent in its reply. The register law, the scissors law (banning the contrast-by-denial frame),
the answer-first law, and the timestamp law are all held this way, each by a Stop-hook (a script the
harness runs when the seat finishes a turn, able to block the turn or force a rewrite) or a push gate (a
check that runs before a change reaches the shared repository). A behavior stays a reminder when it
concerns what the seat DID during the turn rather than what it said — an orchestration or process act,
such as choosing to delegate a piece of work, choosing to run two tasks at once, or choosing to write a
long document itself instead of dispatching it. No hook running today reads that action trace (the
record of which tools the seat called, in what order, during the turn), so nothing catches those
choices after the fact.

The pack already states the general principle behind this split. A quality a machine can verify is
enforced by a gate, held by no attention (base rule 30, SPEC INV-164). A behavioral rule that breaks
mid-turn twice earns a live channel (base rule 23, SPEC INV-108). The members in this audit that still
run as reminders simply have not yet broken twice into a live channel of their own.

## The class and its members

| Member | What it is | Where stated | Current holding (machine that fires by default / passive reminder line / once-read prose only) |
|---|---|---|---|
| Worker-routing | The lead orchestrates and briefs each unit of work, and each unit routes to the cheapest tier sufficient for it. | base rule 5 (SPEC INV-69) | passive reminder line only; named a standing failure and reminded roughly six times to date. |
| Lean-orchestrator | The seat authors nothing long itself and reads nothing past a glance inline, dispatching both the authoring and the deep read to workers. | profile proactivity.lean-orchestrator; base rule 25 (SPEC INV-137) | passive reminder line only; added and reminded in this same session. |
| Parallel isolated worktrees | Independent rows of the work queue run concurrently, each in its own isolated lane. | base rule 7; profile lanes.cap (3) | the lane mechanics run under a gate, but the decision to go parallel is a senior read that no gate settles. |
| Movement-end report | After every big movement, the seat refreshes NEXT_STEPS and reports without being asked. | profile report.movement-end | once-read prose only. |
| Pull unblocked work and never idle | After a landing, the seat walks the whole forward queue and does every item that needs no word from the human. | base rule 27 (SPEC INV-143); two memory entries | once-read prose only; reminded 2026-07-14 after idling for hours. |
| Plan-time question sweep | At plan time, the seat surfaces every genuine decision upfront. | profile proactivity.plan-time-question-sweep | once-read prose only. |
| How-to-ask | The seat asks only on a genuine fork, always with a recommendation attached, and notifies rather than asks when the matter is already decided. | profile proactivity.how-to-ask | once-read prose only. |
| No-only-say-hedge | The seat retires the hedge of offering to act only if asked, and instead does the reversible thing itself. | profile proactivity.no-only-say-hedge | once-read prose only; a recurring low-proactivity tell. |
| Classify the subtask | A mechanical subtask stays the seat's to do even when it sits under a heading the human owns. | profile proactivity.classify-the-subtask-not-its-heading | once-read prose only. |
| Full-run classifier | The seat states whether a change takes the full pipeline or a light road, together with the reason for that choice. | profile proactivity.full-run-is-a-classifier-with-a-recommendation | once-read prose only. |
| Loops are the seat's to propose and arm | The seat proposes and arms a recurring or self-paced loop itself, instead of leaving that step for the human to start. | profile proactivity.loops-are-mine-to-propose-and-arm | once-read prose only. |
| Recap unanswered | The seat closes a message with a one-line recap of any of the human's questions that went unanswered or got buried mid-work. | profile chat.recap-unanswered | once-read prose only. |
| Working narration | The seat narrates while it works, naming the task in hand and the current stage of the process. | profile chat.working-narration | passive reminder line; the outgoing chat reply cannot be blocked by a hook. |
| Self-install | The seat installs hooks, skill copies, and sync scripts by its own hand, without waiting for the human to run them. | profile trust.self-install | once-read prose only. |
| Search for a skill before reinventing | Before building something new, the seat scans installed skills for an existing fit. | base rule 20 (SPEC INV-65) | once-read prose only. |
| Problem-ledger second occurrence | Operational noise that recurs a second time gets an owner at that moment, recorded in the problem ledger. | base rule 19 | once-read prose only. |
| Fix the class and sweep look-alikes | On a found defect, the seat names the class the defect belongs to and sweeps every sibling in the same change. | base rule 14; base rule 27 (SPEC INV-143) | once-read prose only; a meaning read that no literal gate settles. |
| Human prose by a clean writer | Durable human-facing prose is briefed out to a fresh writer instead of authored by the seat that has been marinating in the project's own jargon. | base rule 21 (SPEC INV-84) | once-read prose only for the authorship step. |
| Deep independent audit by default and adversarial certification by a fresh seat | The whole-spec-and-architecture adversarial pass runs as a quality move by default, and the seat that authored the work never certifies that work itself. | profile proactivity.quality-over-budget; base rule 28; base rule 33 (SPEC INV-237) | the push gate checks that a review record exists but not that the deep pass ran by default; the cadence itself has no gate. |

Some members of this same class already carry a machine, and stand as the pattern to replicate. The
no-inflation law runs through a Stop-hook reading scissors-personal.json. The no-scissors and
no-validation laws run through scissors-scan.py. The answer-first law runs through
answer-first-scan.py. The deferral-must-justify-itself law runs through check-deferral-marker.py. The
timestamp law runs through clock-hook.sh. The register law on shown documents runs through
preshow-register-lint.py and the register judge (a model reading a document's text against the
register rule, SPEC INV-203). The register judge just gained two more classes in the 2.8.2 release,
which is a concrete sign that a model reading a turn's text is a mechanism the pack already runs in
production today.

## The recommended mechanism

One primary mechanism, with two supporting ones, covers the gap this audit found.

1. A conduct judge that reads the turn's action trace. This generalizes the register judge (SPEC
   INV-203) from reading the turn's output text to reading what the seat did during the turn: which
   tools it called, whether it dispatched a worker for a long authored artifact or a deep read, whether
   it refreshed NEXT_STEPS at a landing, whether it kept pulling unblocked work or idled. A model reads
   the trace against the standing orchestration laws and reds a violation after the fact, in the same
   way the register judge reds a register violation today. This is the mechanism for the judgment
   members that a deterministic gate cannot settle.
2. Deterministic gate extensions for the members that are already machine-verifiable facts: a check
   that a landing commit refreshed NEXT_STEPS (movement-end report), and a config-health extension that
   reds an un-synced installed hook or skill copy (self-install). These read a checkable fact and owe
   no model call.
3. The plan-time members form the lightest bucket. Some of them can run as the plan-time arm of the
   same conduct judge; others stay a passive reminder line where a dedicated judge pass would be more
   machinery than the behavior earns.

Assigning every member from the table to one of the three buckets:

- **Conduct judge, action trace (bucket 1):** worker-routing, lean-orchestrator, parallel isolated
  worktrees, pull unblocked work and never idle, classify the subtask, search for a skill before
  reinventing, problem-ledger second occurrence, fix the class and sweep look-alikes, human prose by a
  clean writer, deep independent audit by default and adversarial certification by a fresh seat.
- **Deterministic gate extension (bucket 2):** movement-end report, self-install, no-only-say-hedge (its
  hedge phrasing is a literal string in the reply's own text, so it can take a scissors-style pattern
  check with no model owed).
- **Lightest bucket, plan-time arm or stays a reminder (bucket 3):** plan-time question sweep,
  how-to-ask, full-run classifier, loops are the seat's to propose and arm, recap unanswered, working
  narration (its own current-holding entry already notes the outgoing reply cannot be blocked by a
  hook, so a passive reminder is the working answer here).

## Forks for Alexander

1. Whether a conduct judge runs on every turn's action trace, which costs one model call per turn.
   The recommendation is on. The profile's quality-over-budget setting already treats token cost as a
   non-reason on the current plan. The open fork here is the policy question alone.
2. How this couples with the dynamic parameters registry and the onboarding movement (ROADMAP 427),
   where the lean-orchestrator setting is already slated to live. The recommendation is that the judge
   mechanism lands inside this audit's own movement, while the per-person strictness setting stays the
   registry's entry. Keeping the two apart means the two movements do not compete for one home.
3. Which members are worth a dedicated machine and which are fine to keep as a reminder, since a
   low-frequency behavior may not repay a dedicated net. The recommendation is to mechanize the members
   with a reminder-history of two or more first — worker-routing, lean-orchestrator, pull unblocked
   work and never idle, no-only-say-hedge, classify the subtask, and deep independent audit by default —
   and to leave the single-occurrence members as reminders until they recur, which is what base rule 23
   already prescribes.
