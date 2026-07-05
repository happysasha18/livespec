# With-skill run — publish scenario (2026-07-05, Sonnet worker, read the SKILL.md first)

Note: this run used the skill's FIRST draft — before the same evening's fold that added the bare arm's
hygiene steps (secrets/history sweep, fixture copyright, dependency licenses, fresh-clone check, name
collision) to the floor and the GitHub-target steps.

Verbatim output:

---
1. **Name the kind and target** (SKILL.md "How it runs" §1): chordscan is a Python CLI → kind = **infra/tool**; target = **GitHub repo, public**.

2. **Walk the floor** (owed by every kind):
   - Write/update the README's first screen so it says, in the producer's language (not internal dev vocabulary): WHAT chordscan is, WHO it's for (music producers working with MIDI), HOW to start (install + first command).
   - Check every claim and example in the README is true of the code as it stands today — no stale flags, no described features that were cut.
   - State the license and attribution explicitly (pick/confirm a license file; credit any third-party chord-detection logic or MIDI libraries used).

3. **Walk the kind row for infra/tool**:
   - Capture at least one REAL run: an actual command against a real MIDI file and its real terminal output, pasted in — not a hypothetical example.
   - State the current version number.
   - State requirements/platform (Python version, OS, any dependencies like a MIDI parsing library).
   - Name the failure behaviour: what the user actually sees if they pass a bad/corrupt/non-MIDI file, or run it with no arguments.

4. **Walk the GitHub-repo target's own steps**:
   - README current at the repo root.
   - Re-shoot/re-verify any screenshots or sample output only if the host's rule calls for them; otherwise this step stands down (name it as stood-down, don't silently skip).
   - No tag/release is being cut yet, so release notes stand down for this pass.
   - Set the repo description and topics (e.g. "midi", "music", "chord-detection", "cli").
   - Confirm the host's own push gate still applies — this walk prepares the repo, it does not itself authorize the push.

5. **Fix anything that failed the walk** (README gaps, missing license, stale claims, missing real-run output) before involving the producer at all.

6. **Ask the producer only what only he can decide, once everything else is already fixed**:
   - Which license he wants on it (MIT/other), if he hasn't already stated a preference.
   - Confirm the exact GitHub repo name/visibility (public, as he said) and any org/account it should live under.
   - Anything he wants in the repo description/topics beyond the obvious.

7. **Hand him the publish gate** with the surface already worth approving: report that the README is current, a real run and its output are shown, requirements/failure behaviour are stated, license is set, description/topics are set — then ask: "push?"
---
