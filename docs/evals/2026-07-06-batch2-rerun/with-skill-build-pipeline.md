# arm = with-skill, skill = build-pipeline, date 2026-07-06, Sonnet worker

## Scenario

> You maintain a small CLI project; the repo contains SPEC.md, ARCHITECTURE.md,
> TEST_MATRIX.md, a pytest suite in tests/, and the tool's source. A user reports:
> "mytool --export out/report.csv silently writes an EMPTY file when the out/
> directory doesn't exist." Describe EXACTLY what you would do to handle this
> report — step by step, in order, from the moment you read it to the moment
> you consider it done.

## Answer

### 0. Name the door, out loud, before any tool call

Intake line, stated before touching anything: size — small · priority — user-reported
correctness bug, moves ahead of backlog but not queue-jumping the door · door — **bug**
(no new user-visible surface, no new persistent state, no new interaction — `--export`
already exists; this is existing behaviour misbehaving) · work-kind — **product** (the
CLI's stdout/stderr/exit-code and the files it writes ARE what the user faces directly).
This is the intake line the human hears back as the capture echo before work starts.

### 1. Recurrence check, before taking the bug as a bug

Grep `JOURNAL.md` for the export/output-writing area's name (`export`, `--export`,
`csv`, `out/`, "output directory") and check dates. Two failures in the same area
inside ~30 days means the area is missing an invariant and the door re-fires to
**feature** (full pipeline from the spec step, spec the invariant, then fix under it).
If this is the first reported issue in that area, the bug door stands and I proceed
below. (If it turns out NOT to be the first, everything from step 2 on is replaced by
the full `spec → prove → architecture → prove architecture → matrix → test → code`
pipeline instead.)

### 2. Enter the pipeline at the matrix step, citing the existing architecture node

Bug lane skips spec/architecture rewriting and cites the existing node. I open
`ARCHITECTURE.md`, find the node that owns CSV export / output-writing, and re-verify
its `file:line` pin by actually reading that source location — never trust the doc's
own prose or memory for the pin (a claim needs its primary source). If the pin is
stale, I correct it in the same change; if the node genuinely doesn't exist yet
(export logic was never architected), that absence is itself the finding and gets a
one-line architecture fix before continuing — but I do not rewrite the whole document
for a bug.

### 3. Name the bug's CLASS, not just the instance, and sweep for siblings

The pattern behind this instance: "a code path opens a file for writing without
checking that its parent directory exists, and swallows the resulting failure instead
of surfacing it." I grep the whole repo for every other file-write call the tool makes
— other export/output flags, log files, cache files, config writes, any place a path
argument reaches `open(..., 'w')` or equivalent — and check each one's behaviour under
a missing parent directory. Every sibling that shares the pattern gets fixed in this
same change, not filed separately.

### 4. Resolve the one real policy call — ask, don't guess

There are two legitimate correct behaviours here: (a) auto-create the missing
directory and write the file, or (b) fail loudly with a clear, actionable error naming
the missing path. This is a taste/policy call, not something I can verify myself, so
it is marked `⟨DECIDE⟩` with a recommended pick — I recommend (b), fail loudly, because
silently creating directories a user never asked for is a surprise of its own, and a
clear error is cheap and unambiguous — and I proceed on that recommendation while the
question rides along in the batched report rather than blocking on a round-trip.
Silence is consent; it isn't re-asked.

### 5. Update SPEC.md's failure-behaviour sentence

Work-kind = product/infra hybrid for a CLI tool's own contract: the spec sentence for
`--export` should already state inputs → output → failure behaviour. If it's silent on
the missing-directory case (likely, since the bug shipped), I add the decided sentence
now, in the same change, at export's existing spec location — not a new section, since
this is the same surface, just closing a gap in its documented failure behaviour. Any
sibling surface fixed in step 3 gets its own sentence updated too.

### 6. Derive the matrix rows

Under the owning node's block in `TEST_MATRIX.md`, I add or correct the row(s) so each
states BOTH sides: what it DOES (rejects with a named, actionable error when the parent
directory is missing) and what it must NEVER do (produce a zero-byte / empty output
file, or exit 0 while having written nothing meaningful) — the never-side IS the
regression fence for this exact bug. Assertion level: this is observable file-system +
exit-code + stderr text, so string/DOM levels don't apply here — the row pins a level
that actually runs the binary and inspects real output (a "function/process-level"
level, per the infra row of the work-kind table: run the tool, assert real output).
Matching rows go in for every sibling surface fixed in step 3.

### 7. Write the test — and watch it fail first

In `tests/`, I add a test that invokes the real CLI (subprocess call, not a source-string
match) in a temp directory whose `out/` does not exist, with `--export out/report.csv`.
I run it against the CURRENT code first and confirm it goes red exactly the way the
report describes — a zero-length `report.csv` gets created and the process exits
success. That red run is the reproduction; only after seeing it fail do I move to code.
Sibling-surface tests get the same red-first treatment.

### 8. Implement the fix

Add a directory-existence check before any write in the owning function: on missing
parent directory, raise/print a clear error naming the exact path and exit non-zero,
without touching the filesystem — per the decided policy from step 4. Apply the
identical guard to every sibling call site found in step 3, in this same change, not a
follow-up. Keep the change itself minimal and mechanical enough that if it needs more
than a small, well-scoped edit per site it's the kind of work I'd hand to a junior
worker with the exact edit locations, the exact error-message text, and the checkpoint
path — but I keep the judgment call (which sites qualify, what the message says) senior.

### 9. Verify by deed

Run the guardrails (completeness / tests-present / bounds / conflicts) and the full
pytest suite — green means zero failures and the skip-set matches exactly the expected
pinned list, nothing more. Then, separately from the suite, I actually run
`mytool --export out/report.csv` by hand against a real missing `out/` directory and
read the real terminal output and file-system state with my own eyes — and run the
normal (directory-exists) case too, to confirm no regression there — and run every
sibling surface fixed in step 3 the same way. Only after seeing this do I call it
working; before that it's an assumption, not a fact.

### 10. Commit & show

Docs travel with the code in the same session: `CHANGELOG.md` gets a user-facing entry
in plain words with one concrete before/after example (old: silently wrote an empty
`report.csv`; new: `mytool --export out/report.csv` now prints
`error: output directory 'out/' does not exist` and exits non-zero) — no function
names or row IDs in that entry, those go to `JOURNAL.md` instead, dated, with the WHY
and the recurrence-check outcome from step 1. Version bumps PATCH (unasked, since
green with no regression). Before writing or committing, I re-check `git status` +
HEAD against what I last read (the concurrent-edit fence) to make sure nothing else
touched the tree meanwhile. I then show the human the real terminal run from step 9 —
both the fixed missing-directory case and the still-working normal case — in a new
window/pane; push happens only after they've seen that, per the host's push gate (a
push is not itself irreversible, but it still waits on their review here).

### 11. Done means every leg closed, not most of them

I consider the report closed only when ALL of the following hold at once, not as a
partial status: the recurrence check was run and logged · the class was swept and every
sibling site fixed in the same change · SPEC.md's failure-behaviour sentence is current
for export and any sibling surfaces · TEST_MATRIX.md rows exist with both sides for each
· the red-on-bug test(s) now pass and the full suite plus guardrails are green with the
expected skip-set · CHANGELOG and JOURNAL are updated · the human has seen the real run.
An open leg — say, a sibling site found but not yet fixed — keeps the whole row in-work,
never reported as done.

## Workshop noise

None.
