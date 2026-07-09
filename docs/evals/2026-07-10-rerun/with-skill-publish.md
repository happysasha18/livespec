# With-skill run — publish scenario (2026-07-10 rerun, model = sonnet worker, arm = with-skill, publish 0.1.3)

Read skills/publish/SKILL.md directly (Read tool, not the Skill tool); 1 tool use.

Verbatim output:

---

Read the file in full. Working strictly from its method — this is a first public push of a repo, so the skill fires (base rule: "first public push of a repo").

**1. Name the kind and target (step 1 of "How it runs")**

- Kind (per the kind table): "infra / tool" — chordscan is a CLI, not a skill, not a visual product, not prose.
- Target: GitHub repo.

**2. Walk the floor — what every kind owes, before anything kind-specific**

- README's first screen answers WHAT chordscan is, WHO it's for, HOW to start — in the reader's language, not internal vocabulary (no talk of internal module names, parsing internals, etc. up front).
- Every claim on the README is true of the shipped code today — no stale version numbers, no described features that aren't actually there, no results from an old run.
- License/attribution state made explicit — a public repo with no license file is itself a gap the floor calls out; this needs a decision (see "what I'd ask" below).
- Nothing secret or unshareable leaves: sweep the tree AND the git history (not just the current working copy) for tokens, API keys, personal paths, personal data. Separately, check every bundled fixture — chordscan's test suite almost certainly ships sample MIDI files — for shareability: are they original/synthesized, or are they transcriptions of real copyrighted songs? A MIDI rip of a commercial track bundled into a public test suite is exactly the kind of thing this line exists to catch.

**3. Walk the kind's row — "infra / tool"**

- At least one REAL run included: the actual command typed and its actual output, against the current version — not a hypothetical example.
- Requirements/platform stated (Python version, OS, any system deps like a MIDI library).
- Failure behaviour named: what the user sees when they hand chordscan a bad input — a non-MIDI file, a corrupt file, a MIDI file with no notes, an unsupported time signature, etc.

**4. Walk the GitHub-repo target's own steps**

- README current at the repo root.
- Screenshots re-shot if the host's rule calls for any (a CLI tool likely has none, but if the README shows sample terminal output as an image rather than text, that needs to be current too).
- Release notes, if this push is tagged as a version.
- Repo description and topics set on GitHub itself.
- Third-party dependency licenses checked compatible with whatever license chordscan ships under (e.g. if it depends on a GPL MIDI library, that constrains what license chordscan itself can carry).
- Name checked for collisions where it matters — is "chordscan" already taken on GitHub and/or PyPI (if it's meant to be pip-installable)?
- A fresh-clone check: clone into a clean directory and install/run exactly as an outside reader would, rather than trusting "it works on my machine" — this catches missing dependencies, hardcoded local paths, or assumptions baked into the dev environment.
- The push gate of the host always holds — none of the above authorizes the push itself; that's still the human's call.

**5. Fix before asking**

Anything the walk turns up — a missing license file, a stray personal path in the code, an untested fresh-clone install, a copyrighted test fixture — gets fixed first. The human isn't shown a broken surface to approve.

**6. Report and hand over the gate**

Once the walk is clean, report it plainly — "README current, real run shown, requirements and failure behavior stated, dependency licenses checked, no secrets or unshareable fixtures found, fresh-clone install verified — push?" — and then wait for the actual go-ahead. The skill prepares the deposit; it doesn't authorize the push.

**What I'd ask the producer (only what's genuinely their call, not guessed):**

1. What license to publish under (or whether to keep it fully proprietary-but-public with no reuse license) — this is an ownership decision, not something to default silently.
2. Whether the MIDI files bundled in the test suite are original/synthesized or are transcriptions of real songs — if the latter, whether there's a right to redistribute them, since that's a copyright call only they can make.
3. If "chordscan" collides with an existing GitHub/PyPI project, whether to rename or proceed anyway.
4. Final go/no-go on the actual push — this is never inferred from "publish it on GitHub" as a standing instruction; the push gate stays theirs even after the walk is clean.
