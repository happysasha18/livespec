# Commit and push gates

This page explains what stands between a finished change and the remote: the done-gate a gated file
passes before any commit, the rule that decides when a commit happens, the law that moves accepted
work to the remote, how a delegated run's verdict is read, and the tighter gates a host may add.
Each rule's normative home is linked; this page explains and points, and the homes decide.

## The done-gate before a commit

`scripts/spec-done-gate.py` is the single definition of "done" for a gated prose file
(the design lives in `docs/prose-quality-gate-design.md`). The script runs a conjunction of
checks and prints green only when all of them hold. Exit 0 means green; exit 1 means red, and a
red gate blocks the commit. The conditions are:

- `spec-style-lint.py --gate` reports zero errors on the file. In gate mode the two advisory
  signals (caps-shout, second-person) become blocking errors, and a dated waiver file can move a
  still-unfixed finding into a counted debt bucket. A waiver is a recorded, visible debt; a silent
  pass never happens.
- `spec-redundancy-precheck.py` reports zero open findings; each finding is either resolved or
  waived.
- The prose judge, a language-model check, has passed its self-test and left zero surviving
  definite or likely findings.
  The judge's output file is required; without it the gate is red with "judge pending".
- The anchor multiset of the file is unchanged against a given git baseline. An anchor is a
  trailing code in brackets, such as `[INV-82]`; the multiset check proves a prose restyle moved
  no normative pointer.

Suite green is a separate leg of the same commit bar. The test suite, the needle tests, waiver
hygiene, and the debt ratchet run as pytest classes under `tests/`. A commit waits for both legs:
the done-gate on the gated files and a green suite.

## The commit rule

A change is committed when it leaves the tree the same or better. Green with no regression is
enough; the pipeline never parks finished work while waiting for perfect
(`skills/build-pipeline/SKILL.md`, step 9). Before the commit, every check the diff can reach has
run: a prose-only diff reaches the prose gates, a code diff reaches the suite (SPEC INV-45).

## The push law

Accepted work reaches the project's remote by rule (SPEC INV-82; the normative text lives in
`PRODUCT_SPEC.md`). "Accepted" means the change is same or better and every gate the diff reaches
ran and passed. The law has four parts:

- **Push by rule.** Where the host has a remote, accepted work is pushed. Parking it locally
  while waiting for a perfect state breaks the law.
- **Discover the remote first.** The remote is read from the tree; `git remote -v` already
  answers the question, so the agent never asks it.
- **One question when no remote exists.** A host with no remote gets a single contextual question
  at the first push moment: create a remote (and where — GitHub, GitLab, whatever the human
  names) or stay local. The answer is recorded in the host profile and the question never
  repeats.
- **Re-walk the README at every push.** Every push checks the README against the pushed truth:
  claims, counts, commands, and version homes still match, and a stale claim is fixed before the
  push. This is the shopfront law at every-push cadence (SPEC INV-44).

A push that changes what a public reader sees also passes the publish-quality gate first: the
publication owes its reader what the artifact's kind owes, such as fresh screenshots for a visual
product or real runs for a tool (`skills/publish/SKILL.md`). The publish gate prepares the
deposit; it never turns into a push authorization on its own.

## Reading a delegated run's verdict

A wrapper's exit code reports the wrapper, so for a background or delegated run it is never the
verdict. A background job can exit 0 while the suite inside it failed. The gate therefore reads
the suite log's own tail line — the "N/N green" line the suite itself prints — and that line is
the verdict (SPEC INV-80). A foreground gate reading the exit code of its own direct child stays
legal, because there the exit code is the suite's own.

## Host-level tighter gates

The rules above are the package floor. A host or a human may tighten them; loosening a gate takes
a recorded profile entry, never a silent skip (`skills/live-spec-base/SKILL.md`, the settings
ladder).

- **A tighter prover cadence.** The `prover.cadence` setting defaults to a full prover pass
  before every minor version bump. A project may tighten it to a full prover re-check before
  every push, recorded in its host profile; the live-spec project itself runs at that cadence.
- **A human's named release.** A milestone gate the human named in person — for example a version
  bump released on their explicit word — waits for that word. The push law moves routine accepted
  work only and never overrides a gate the human reserved by name (SPEC INV-82).
