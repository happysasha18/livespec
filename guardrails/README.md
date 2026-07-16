# Guardrails — the pack's gates as git hooks

Two git hooks turn the rules the pack already lives by into things that actually stop you,
instead of things you have to remember.

## What each gate catches

**`pre-push`** — blocks a push unless five things are all true:

- **a. Fresh review.** A prover record dated today exists under `docs/prover/` and is
  committed. This is the push gate every push of live-spec must pass (SPEC anchor `M-6`):
  no push without a same-day whole-spec re-check on file.
- **b. Tests green.** `python3 -m pytest -q tests` exits clean — the SAME runner the CI mirror
  runs, so the local net and the second net can never disagree on what "the suite" is.
- **c. Every spec anchor has exactly one owner.** In this repo that's already asserted
  inside the test suite itself (`tests/test_traceability.py`), so gate (b) passing means
  gate (c) passed too — there's no separate check to run.
- **d. The test matrix's coverage checklist is fully walked.** `TEST_MATRIX.md` ends with a
  "Coverage validation" section of checkboxes; any box left unchecked (`- [ ]`) blocks
  the push until it's ticked or the row it belongs to is explicitly retired.
- **e. The prototype fence holds.** A prototype lives in a fenced home (a `prototype/`
  folder — SPEC `INV-17`); a PROD file referencing anything inside that home is RED.
  This gate catches STRUCTURAL wiring — a prod file naming or loading a fenced file
  (a script src, an import, a link target). Narrative mentions stay clear of the gate: `docs/`, `attic/`,
  `inbox/`, `JOURNAL.md`, `ROADMAP.md`, `NEXT_STEPS.md`, any `README.md` under
  `guardrails/`, and `.live-spec/` are excluded, so a journal can talk *about* a
  prototype without tripping the gate. If no `prototype/` directory exists (or it's
  empty), the gate passes — there's nothing fenced yet. A host that names its fence
  home something else passes that name as the script's second argument
  (`check-prototype-fence.sh <repo-root> <fence-dir-name>`).

Each check lives in its own small script (`check-prover-record.sh`, `check-tests.sh`,
`check-matrix-coverage.sh`, `check-prototype-fence.sh`) so it can be run and tested on
its own, pointed at a scratch file instead of the real repo.

**`pre-commit`** — the concurrent-edit fence. It protects against two sessions writing the
same repo at once. It is **off by default**: if no `.live-spec-fence` file exists at the
repo root, the hook does nothing. A session opts in by running `guardrails/fence-refresh.sh`,
which records the commit it started from. From then on, if the commit at the repo's tip ever
moves without that session's knowledge (another writer got there first), the next commit is
blocked with a message explaining what to review and how to re-arm the fence.

`pre-commit` also runs two content gates. It rejects a staged line stamped with a future time
(`check-future-times.sh`, SPEC `INV-24`), and it runs the **deferral-marker gate**
(`check-deferral-marker.py`, SPEC `INV-152`): a work item in `NEXT_STEPS.md` or a
`docs/decisions/*.md` page that parks for the human's word — "his to correct", "reserved for
his", "still his", "row N reserved" — must name its human-only fact (taste, policy,
irreversible, or device-feel), or drop the marker and do the item. A marker that names no
reason reds the commit with the file, line, and text. A negated mention ("NOT owner-reserved")
and a quoted narration of an old marker are both left alone. This is the mechanical net for the
same rule the chat-law hook delivers at the ask moment — the two arms of base rule 29.

## How to install

From the repo root:

```
./guardrails/install.sh
```

This copies `pre-commit` and `pre-push` into `.git/hooks/` and makes them executable.
Safe to re-run any time — it just overwrites with whatever is currently in `guardrails/`.
It does **not** create `.live-spec-fence`; the fence stays opt-in until you run
`guardrails/fence-refresh.sh` yourself.

## How a host project adapts the pattern

**The ratchet gates (style lint · redundancy · freeze) install themselves in one pass:** run
`bash <pack>/adopt/install-ratchet.sh` from the host root (SPEC INV-172). It vendors the scripts
with a source-pin manifest, seeds the host's debt caps at the sizes measured that moment — green
at once, shrinking-only from then on — and generates the guard test. The section below covers the
structural gates, which are adapted by hand.

The five-gate shape (fresh review · green tests · ownership · full coverage · prototype
fence) is the part worth copying as-is. What changes per host:

- **Test command.** Swap `python3 -m pytest -q tests` in `check-tests.sh` for whatever the host
  runs (`npm test`, `go test`, …) — and set the CI mirror to the SAME command, so the local net
  never under-runs what CI runs (a runner that collects fewer tests than CI false-greens locally).
- **Review cadence.** Not every host proves the whole spec before every push — a host may
  only require a full prover pass before a major version, checking something lighter
  (or nothing) in between. That cadence is a host setting; state it in
  the host's own profile and adjust `check-prover-record.sh`'s expectations (or drop gate a
  entirely) to match.
- **File names/paths.** If the host's matrix or prover folder lives somewhere else, pass
  it as the script's argument, or edit the default.
- **Fence home name.** If the host calls its prototype home something other than
  `prototype/` (say `sketches/` or `labs/`), pass that name as
  `check-prototype-fence.sh`'s second argument instead of renaming the script.

Everything else — the fence being opt-in, the plain-English failure messages, hooks
living in a version-controlled `guardrails/` folder rather than only inside `.git/hooks/`
so they travel with the repo — is meant to hold for any host.

## The gate contract (SPEC INV-47)

Every gate script authored or next touched in this directory obeys three conventions (the
neighbours' CLI lesson, adopted from OpenSpec's gate contract — provenance and the full
borrowings inventory: docs/research/2026-07-10-originality-audit.md; the adopting row rests in
the queue archive):

1. **A blocking red carries one typed line.** Beside its human lines, a BLOCKING gate that fails
   emits exactly one parseable JSON object — `{"severity": "...", "code": "...", "message": "...",
   "fix": "..."}` — where `fix` is the same sentence a person reads. Agents parse the line; humans
   read the prose; both see one truth. (First gate under the contract: `check-prototype-fence.sh`.)
2. **Every check declares blocking or advisory.** A header comment names it; an advisory check
   prints its findings and never flips the exit code.
3. **All-or-nothing writes.** A script that rebuilds artifacts validates every output before writing any — no half-written artifact ever lands on disk.

Exempt by name: `check-push-reach.sh` — its exit code is a VERDICT (which checks the diff can
reach) rather than a defect; it is a decider, informational rather than a blocking gate.

## The CI mirror (SPEC M-5, ROADMAP row 14)

The gates' native home is the LOCAL pre-push hook — CI is the second net, never the first. Three
rules: **same checks, one source of truth** — CI invokes the same scripts in this directory
and never redefines a check; **the full set, always** — the reach map (SPEC INV-45) is a local latency
optimization, the second net stays conservative; **a plain workflow a host copies** — swap the test
command for your own, keep the script calls. The worked example is this repo's own
`.github/workflows/gates.yml` (note its `fetch-depth: 0` — the prover-record freshness rule reads
history — and its `TZ` pin, so "today" is measured in the author's own timezone, distinct from UTC).

## The kill-list scanner (SPEC E-26)

A host with taste-reviewed artifacts keeps a kill-list beside them (template:
`templates/KILL_LIST.template.md` — the human's cuts as dated literals, appended, never removed) and
wires a SCANNER: a test that reads the kill-list table and greps the artifact's surfaces for each
literal — a killed phrase reappearing turns the suite red. Same shape as every gate here: the list is the
declared truth, the test re-walks it every run.
