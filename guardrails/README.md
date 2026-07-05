# Guardrails — the pack's gates as git hooks

Two git hooks turn the rules the pack already lives by into things that actually stop you,
instead of things you have to remember.

## What each gate catches

**`pre-push`** — blocks a push unless four things are all true:

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

Each check lives in its own small script (`check-prover-record.sh`, `check-tests.sh`,
`check-matrix-coverage.sh`) so it can be run and tested on its own, pointed at a scratch
file instead of the real repo.

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

The four-gate shape (fresh review · green tests · ownership · full coverage) is the part
worth copying as-is. What changes per host:

- **Test command.** Swap `python3 -m unittest discover tests` in `check-tests.sh` for
  whatever the host runs (`pytest`, `npm test`, …).
- **Review cadence.** Not every host proves the whole spec before every push — a host may
  only require a full prover pass before a major version, checking something lighter
  (or nothing) in between. That cadence is a host setting, not a pack default; state it in
  the host's own profile and adjust `check-prover-record.sh`'s expectations (or drop gate a
  entirely) to match.
- **File names/paths.** If the host's matrix or prover folder lives somewhere else, pass
  it as the script's argument, or edit the default.

Everything else — the fence being opt-in, the plain-English failure messages, hooks
living in a version-controlled `guardrails/` folder rather than only inside `.git/hooks/`
so they travel with the repo — is meant to hold for any host.
