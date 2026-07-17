# Which standing habits should become blocking gates — the audit

ROADMAP row 420. Alexander asked for this walk in person (his ~18:27 word, 2026-07-17):
beyond the skill-creator review, reconsider what else makes sense to turn from a reminder
into a gate. He gave the test in the same breath: a habit that is forgotten and is
mechanically checkable is a gate candidate, and a taste call stays a habit. Row 419 —
the skill-creator-review gate, gate s, INV-208 — is the first member this walk found, and it
landed ahead of the audit so the audit generalises it.

This document is the analysis only. It produces a ranked list of promotions with the reasoning
for each; the gates themselves get built afterward, one ROADMAP row per promotion.

## The test, restated

A reminder relies on the agent remembering. A gate does not. Three questions decide each candidate:

1. Is the habit FORGOTTEN — does it recur as a failure rather than hold on its own?
2. Is it MECHANICALLY CHECKABLE — can a script inspect a file, a diff, a process list, or a
   transcript and reach a yes/no verdict without judgment?
3. Is it a TASTE call — a fact no artifact holds (a design branch, a feel, a policy)? A taste
   call is never a gate, however often it is missed.

A candidate that answers yes, yes, no is a promotion. Anything else stays a reminder, and the
reason it stays is stated so the line is not re-walked from scratch next time.

## The existing gate chain, so nothing already held is proposed again

The push gate (`guardrails/pre-push`) runs gates a through s. In plain terms they already hold:
a fresh prover record (a), a green test suite scoped to the diff (b, which also carries the
traceability check c), matrix coverage (d), prototype fence (e), skill loadability (f), pin
drift (g), the four host checks (h), shipped-language cleanliness (i), no broad browser-kill (j),
compaction freeze (k), muted browser launch (l), config health — installed hooks match their
source (m), the earned inbox message (n), the cleanup notice (o), touchpoint kind (p), the
waiting board (q), the authority anchor (r), and the skill-creator review (s).

The commit gate (`guardrails/pre-commit`) holds the concurrent-edit fence, no future-dated
stamps, the deferral-marker net, and the staged-plus-unstaged overlap catch.

The session hooks hold the rest at the chat surface, where a push gate cannot reach: the clock
line and the chat laws on UserPromptSubmit; the scissors, inflation, and validation scan plus the
register judge on Stop.

Everything below is measured against that chain. Where a habit is already held, it is marked
ALREADY-GATED and not re-proposed.

## The candidates, ranked by value (most-forgotten times most-checkable first)

### 1. The CI mirror must carry every gate the local push gate carries — PROMOTE

**The habit and where it lives.** `SPEC M-5` (ROADMAP row 14) says CI runs the same checks as
the local pre-push hook, one source of truth. `.github/workflows/gates.yml` is a hand-maintained
mirror: it names each gate as its own step. A hand-maintained mirror drifts the moment a gate is
added locally and the CI file is not touched.

**It has already drifted.** The local `pre-push` runs gates a through s. `gates.yml` runs a, b, d,
e, f, g, i, j, l, o, p, q, r, s. Three gates are missing from CI right now: gate h (the four host
checks), gate k (the compaction freeze), and gate n (the earned inbox message). Gate c is folded
into the test suite so it is covered; gate m (config health) is skipped in CI by design, because a
CI checkout installs no local hooks. So h, k, and n are genuine drift — a push that a green CI
would wave through can fail the local gate, and a machine that only had CI would never run those
three.

**Mechanically checkable.** Yes, cleanly. The check reads the gate letters that `pre-push` invokes
and the gate letters that `gates.yml` invokes, and reds if the CI set is missing any letter the
local set has (minus the by-design CI carve-outs c and m, which the check names explicitly). This
is the same class as gate m itself — gate m already proves the installed hook matches its source;
this proves the CI mirror matches the source too.

**Taste call?** No. It is a set comparison.

**Recommendation: PROMOTE-TO-GATE.** Most-checkable and proven-drifted, so it ranks first. One
line of reasoning: a mirror that is maintained by hand drifts by hand, and this one has, so a
machine should compare the two lists.

**Gate sketch and hook point.** A new `guardrails/check-ci-mirror.sh`, added to `pre-push` (and so
run in the suite too). It greps the `-- gate X` markers from `pre-push` and the `gate X` step names
from `gates.yml`, subtracts the named carve-outs, and reds on any letter in the local set but not
the CI set, naming the missing gate and the one fix (add the step to `gates.yml`). Rough size:
small, forty to sixty lines, the shape of `check-config-health.sh`.

### 2. The chat judges must stay wired — settings.json still lists the Stop and UserPromptSubmit hooks — PROMOTE

**The habit and where it lives.** The prose judges live at the chat surface: `scissors-scan.py`
and `register-judge-collect.sh` on Stop, the register report and chat laws on UserPromptSubmit,
all listed in `~/.claude/settings.json`. Gate m (`check-config-health.sh`) proves the installed
hook FILE exists and matches its source. Its own docstring names the residual and hands it to this
audit by name: it does not yet prove `settings.json` still LISTS the judge entries, because
settings.json is personal-layer, and that check is left for the row 420 gate audit.

**Why it matters — this movement hit it.** A judge that is not listed goes dark silently while
every other gate stays green. This is the failure Alexander named for this walk: a landing that
claims a machine works when it was never wired live, the judge delivering no verdict. The file can
be present and correct on disk and still never run, because the run comes from the settings entry,
not the file.

**Mechanically checkable.** Yes. The check parses `~/.claude/settings.json` and asserts that the
Stop array references `scissors-scan` and `register-judge-collect`, and the UserPromptSubmit array
references `clock-hook`, `chat-law-hook`, and the register report. A referenced hook whose entry is
missing reds. The hook set to require is read from `hooks/` in the repo, so the list stays honest
as hooks are added, the same self-widening shape gate m already uses for the file check.

**Taste call?** No. It is a presence check over a JSON array.

**Recommendation: PROMOTE-TO-GATE.** It is the direct fix for a failure this very movement hit, and
config-health already handed it here, so it ranks second only because the CI-mirror drift is even
cheaper to check.

**Gate sketch and hook point.** Extend `check-config-health.sh` (gate m) with a second arm, or add a
sibling `check-judge-listed.py`, run in `pre-push`. It reads each source hook's basename from
`hooks/`, decides which surface each belongs to, and reds if `settings.json`'s Stop or
UserPromptSubmit array does not reference it. Rough size: small, thirty to fifty lines. Caveat: it
reads a personal-layer file, so on a host with no such settings.json it stands down by name rather
than reds, exactly as gate m skips in CI.

### 3. Every gate must be able to fail — each check carries a known-red fixture — PROMOTE

**The habit and where it lives.** No single doc states it, which is part of why it is forgotten.
This movement proved the cost: the authority-anchor gate was hollow — it reported green without
reaching the surfaces it claimed to inspect, and the fix (commit 8a0209f) had to feed it the
read-back, reach the surfaces, and strike the live fabrication. The same shape is the worker that
left a false "zero violations" claim: a check that cannot fail reports success and protects
nothing.

**Mechanically checkable.** Yes. For every `guardrails/check-*.{sh,py}` there must exist a fixture
or a test that drives the check with input it MUST red on, and the suite asserts the check actually
reds. A check with no red fixture is itself the finding. Most gates already ship fixtures
(`authority-anchor-fixtures/`, `board-fixtures/`, `touchpoint-fixtures/`); the gate makes the
fixture mandatory rather than a matter of the author remembering.

**Taste call?** No. The presence of a red fixture and a test that consumes it is a file-and-exit-code
fact.

**Recommendation: PROMOTE-TO-GATE.** This is the meta-gate — it guards the guards. It ranks third
because defining "the check reds on this fixture" for every existing check is more work than the two
list-comparisons above, though the principle is the sharpest lesson of this movement.

**Gate sketch and hook point.** A `guardrails/check-gates-can-fail.sh` (or a `tests/test_gates_red.py`
that the suite runs, so it rides gate b). It enumerates `guardrails/check-*`, and for each one
requires a registered red fixture — a file under a `*-fixtures/red/` convention, or a named test —
that the check exits non-zero on. A check with no such fixture reds the gate. Rough size: medium; the
enumerator is small, but back-filling a red fixture for each existing check that lacks one is the
bulk of the work and can be staged.

### 4. A finished worker leaves no runaway child — PROMOTE

**The habit and where it lives.** The memory note "Worker completion can orphan a runaway child"
(2026-07-17): a finished worker left a difflib process burning one core for forty-six minutes, and
the frozen status line masked it. The note's own fix is to check ps for children and reap the scoped
group. It recurs because it depends on the agent remembering to look after a worker reports done.

**Mechanically checkable.** Partly. A session Stop hook can scan for processes in the session's own
process group that are still alive and consuming CPU after a worker reported completion, and warn or
reap. This reads a live process list rather than the repo, so it belongs at the Stop surface, not the
push gate — a push gate runs long after the runaway would have burned its cores.

**Taste call?** No, but the trigger is fuzzier than the list checks: "which processes belong to a
finished worker" needs the process-group scoping the note already describes, and a too-broad scan
risks the browser-kill class of mistake (INV-162). The scoping must be precise.

**Recommendation: PROMOTE-TO-GATE**, at the Stop-hook surface, built carefully. It ranks fourth
because the value is real and recurring, but the check lives in process space where a coarse
implementation can do harm, so it needs the same care the cleanup-scoping gates already carry.

**Gate sketch and hook point.** A Stop-hook arm (beside the scissors and register-judge Stop hooks)
that lists processes in the session's process group, filters to alive-and-CPU-bearing children not
owned by the lead, and reports them by name — the cleanup-notice discipline (gate o) applied to its
own reaping. Reaping automatically is the riskier step; the first version reports, a later version
reaps within the proven scope. Rough size: medium.

## Candidates judged and NOT promoted

These were walked and left as reminders. The reason each stays is recorded so the line is settled.

**Lead every reply with the timestamp** (profile `chat.timestamp`; memory "Timestamp every message"
notes a reliable always wants a hook). Mechanically checkable at the Stop surface — a hook can read
the last assistant turn and check it opens with `[HH:MM]`. Low harm when missed and low value, and
the clock hook already injects the time on every prompt. A borderline PROMOTE if a cheap Stop arm is
wanted later; KEEP-AS-REMINDER for now.

**Answer-first ordering** (profile `language.answer-first`). The reminder rides the chat-law hook;
the mechanical arm that reds a lead-less doc or report is already ROADMAP row 397. Whether a chat
reply led with its answer is semantic and cannot be gated at push. KEEP-AS-REMINDER; the doc arm is
already planned.

**No scissors, no inflation, no validation** (profile `language.no-scissors`, `no-inflation`,
`no-validation`). ALREADY-GATED — the register lint blocks any shown artifact (INV-83), the freeze
gate holds the docs, and the Stop-hook personal overlay carries the scissors, inflation, and
validation patterns for chat (installed 2026-07-17).

**Register and native-English on shown text** (profile `language.register`, `native-english`).
ALREADY-GATED — `scripts/preshow-register-lint.py` gates every artifact shown to a human, and the
register judge runs on Stop.

**Deferral must justify itself** (profile `proactivity.deferral-must-justify-itself`). ALREADY-GATED
— `check-deferral-marker.py` runs in pre-commit over NEXT_STEPS and the decision pages.

**Push only on the suite log's own green** (profile `trust.push`; memory "Gate commit on suite LOG
green"). Effectively ALREADY-GATED — the push gate's gate b re-runs the suite and reads its result
directly, so a bg job's misleading exit 0 cannot carry a push. The habit of not trusting a wrapper's
exit is a reminder; the gate re-runs regardless.

**Worker write-set disjoint from mine / narrow git add on a shared tree** (memory two notes). Partly
held — the pre-commit overlap check reds a file that is both staged and carrying unstaged edits, the
signature of a second writer, and the fence catches a moved HEAD. A full "the staged set matches the
session's declared write-set" gate has no declared write-set to compare against, so it is not
mechanically checkable today. KEEP-AS-REMINDER, with the pre-commit overlap catch as the partial arm.

**Delegate to the cheapest sufficient worker** (memory "Sonnet worker delegation", a standing
failure). NOT mechanically checkable — whether a subtask needed Opus or Sonnet is exactly the
judgment the routing rule asks for. A taste and difficulty call. KEEP-AS-REMINDER.

**Compaction every pass** (memory, INV-164). Partly held by the freeze gate on the guarded docs.
"Compaction ran this pass" has no clean mechanical trigger — pass boundaries are not marked in a way
a script reads. KEEP-AS-REMINDER; revisit if a pass marker is ever introduced.

**Never show a partial run; show real not synthetic; open artifacts in the browser; render docs not
Sublime; movement-end NEXT_STEPS; recap the unanswered** (profile show/report habits and the matching
memory notes). These live at the showing surface, which a push gate does not reach, and most turn on a
judgment ("is this run complete", "is this the milestone to show"). KEEP-AS-REMINDER.

**README never regresses on push** (memory). "Regressed" is a quality judgment on prose and
screenshots. A taste call. KEEP-AS-REMINDER.

## A note on the two remaining movement failures

Two failures this movement hit are addressed above: the judge that delivered no verdict maps to
candidate 2, and the hollow gate reporting a false green maps to candidate 3. A third — a prover
record naming the wrong file (commit 8f8eab4 corrected a record that named communicator instead of
build-pipeline) — is partly held already: gate s requires a skill-review record to name the changed
skill, and gate a ties the prover record's freshness to the actual document commits. The general
form, "a record must name a file that is actually in the diff it covers," is checkable and worth a
later, smaller row, but it is narrower than the top four and did not make this build order.

## Build order

Build these first, in this order:

1. **CI-mirror parity** (candidate 1). Cheapest to check, already drifted with gates h, k, and n
   missing from CI, so it pays for itself immediately. Small.
2. **Judges stay listed in settings.json** (candidate 2). The direct fix for the no-verdict failure
   this movement hit, and config-health already handed it here by name. Small, and it slots onto the
   existing gate m.
3. **Every gate carries a known-red fixture** (candidate 3). The meta-gate that would have caught the
   hollow authority-anchor gate. Medium; the enumerator is small and the red fixtures can be
   back-filled in stages.

Candidate 4 (no runaway worker child) is a real promotion but lives in process space at the Stop
surface, where a coarse implementation can do harm, so it is built fourth and carefully, after the
three repo-surface gates above are in.
