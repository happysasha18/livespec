# Guardrails — the pack's gates as git hooks

Two git hooks turn the rules the pack already lives by into things that actually stop you,
instead of things you have to remember.

## What each gate catches

**`pre-push`** — blocks a push unless five things are all true:

- **a. Fresh review.** A prover record dated today exists under `docs/prover/` and is
  committed. This is the push gate every push of live-spec must pass (SPEC anchor `M-6`):
  no push without a same-day whole-spec re-check on file.
- **b. Tests green.** `python3 -m unittest discover tests` exits clean.
- **c. Every spec anchor has exactly one owner.** In this repo that's already asserted
  inside the test suite itself (`tests/test_traceability.py`), so gate (b) passing means
  gate (c) passed too — there's no separate check to run.
- **d. The test matrix's coverage checklist is fully walked.** `TEST_MATRIX.md` ends with a
  "Coverage validation" section of checkboxes; any box left unchecked (`- [ ]`) blocks
  the push until it's ticked or the row it belongs to is explicitly retired.
- **e. The prototype fence holds.** A prototype lives in a fenced home (a `prototype/`
  folder — SPEC `INV-17`); a PROD file referencing anything inside that home is RED.
  This gate catches STRUCTURAL wiring — a prod file naming or loading a fenced file
  (a script src, an import, a link target) — not narrative mentions: `docs/`, `attic/`,
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

The five-gate shape (fresh review · green tests · ownership · full coverage · prototype
fence) is the part worth copying as-is. What changes per host:

- **Test command.** Swap `python3 -m unittest discover tests` in `check-tests.sh` for
  whatever the host runs (`pytest`, `npm test`, …).
- **Review cadence.** Not every host proves the whole spec before every push — a host may
  only require a full prover pass before a major version, checking something lighter
  (or nothing) in between. That cadence is a host setting, not a pack default; state it in
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
neighbours' CLI lesson, ROADMAP row 114):

1. **A blocking red carries one typed line.** Beside its human lines, a BLOCKING gate that fails
   emits exactly one parseable JSON object — `{"severity": "...", "code": "...", "message": "...",
   "fix": "..."}` — where `fix` is the same sentence a person reads. Agents parse the line; humans
   read the prose; both see one truth. (First gate under the contract: `check-prototype-fence.sh`.)
2. **Every check declares blocking or advisory.** A header comment names it; an advisory check
   prints its findings and never flips the exit code.
3. **All-or-nothing writes.** A script that rebuilds artifacts validates every output before writing any — no half-written artifact ever lands on disk.

Exempt by name: `check-push-reach.sh` — its exit code is a VERDICT (which checks the diff can
reach), not a defect; it is a decider, not a blocking gate.
