---
name: livespec-base
description: The livespec pack's shared rulebook and default settings — the rules every pack skill works by (ask-never-guess, plain words with trailing anchors, one name per surface, one home per fact, checkpoint discipline, the concurrent-edit fence, freshness checks) stated ONCE, plus the three-step settings ladder (package defaults → personal profile → host profile). Load it whenever a pack skill (spec-author, product-prover, build-pipeline, communicator) is in use, when resolving how the pack should behave for a given human or host (language, proactivity, prover cadence), or when two skills seem to state one rule differently — this file is the normative home; the working skills only reference and elaborate.
version: 0.1.0
---

# livespec-base — one rulebook, five skills

The pack's shared working rules live HERE, once. A working skill (spec-author, product-prover,
build-pipeline, communicator) opens by naming this base and the version it was written against, references
these rules, and elaborates only its own domain — communicator teaches HOW to speak plainly; THAT we speak
plainly is this file's sentence. A second full statement of a shared rule inside a working skill is drift —
a defect to fold at the next milestone, not a convenience (SPEC INV-13). Used standalone, outside the pack,
a working skill still stands: its pointer here reads as plain advice.

## The shared rules

1. **Ask, never guess.** A gap only the human can fill — a threshold, a policy, a taste call — is asked or
   marked `⟨DECIDE⟩` with a one-line question and a recommended pick. Never invent intent; and never ask
   what you can decide or verify yourself — a pending question rides in its row while the lane keeps moving
   on the recommendation (SPEC INV-4, INV-5, INV-12).

2. **Plain words carry the meaning; the code trails, quietly.** Every human-facing sentence stands on its
   own in the product's language; internal handles (INV-x, row numbers, worker names, model names) never do
   the talking. One convention, two faces: in **chat**, the anchor may trail the sentence in parentheses —
   "no remote copy exists (INV-8)"; in **documents**, anchors sit at line ends in square brackets — `[INV-8]`.
   Never open a line with a code.

3. **One surface = one name, everywhere.** The moment one thing answers to two names, every cross-check
   silently loses the seam between them. The vocabulary comes from the host's SPEC.

4. **One canonical home per fact.** Everything else that mentions the fact is a pointer, and pointers are
   kept live — a doc superseded or moved gets every inbound reference repointed the same session. Two
   documents claiming authority over one fact is undefined behaviour when they disagree.

5. **Mechanical work goes to a junior; judgment stays senior.** If the steps can be written precisely
   (known edit strings, a known command, fan-out fact-gathering), a cheaper worker runs them — the cheapest
   tier that can (one-shot → haiku; multi-step mechanical → sonnet; judgment/design → senior). The junior
   pastes RAW output (command + exit code + failing lines) as it works; raw output is evidence, the
   junior's prose is only a lead, and the senior spot-checks by re-running.

6. **Every long or delegated piece of work keeps a persistent checkpoint.** A file on disk (host home:
   `.livespec/checkpoints/`, gitignored — never a system temp dir) holding done / in-progress / next,
   updated AS the work runs — so a cut-off RESUMES from disk instead of restarting. Red at a pause is never
   committed; the failing test name + hypothesis becomes the top NEXT_STEPS item — the checkpoint IS the
   red test.

7. **The concurrent-edit fence, before every write and every commit.** Re-check `git status` + HEAD against
   what you last read; if HEAD moved or the tree holds changes you did not make — STOP, re-read, then
   proceed surgically or back off. A repo you were not assigned to is read-only (one exception: a new wish
   file in its inbox). Applies to ANY skill that writes shared files, not just adoption (SPEC INV-10, INV-11).

8. **Freshness: versions are re-checked at every safe breakpoint.** Re-stat the installed skills, the pack,
   and the profiles; on any version change re-read the changed file before continuing — never coast on the
   in-memory copy — and journal one line naming old → new (SPEC A-7, M-7).

9. **History lives in the JOURNAL; docs travel with the change.** The dated WHY of every movement goes to
   JOURNAL.md the same session; SPEC / NEXT_STEPS / ROADMAP prose states only current truth. A shipped
   change updates its README / CHANGELOG / SKILL.md before the session ends.

10. **Nothing is silently deleted.** A superseded host file moves to the attic with a manifest line; a
    removed feature leaves a dated tombstone in the spec and RETIRED matrix rows; only clearly-regenerable
    junk may be deleted, listed and human-OK'd first (SPEC INV-7, A-4, A-9).

11. **Verify by deed; show the real thing.** "Works" is said only after running it and seeing the result;
    otherwise it is labelled an assumption. What the human sees is real data in its real render — synthetic
    only for your own checks, always labelled SYNTHETIC; never a bare file path.

12. **The human's gates are the human's.** Irreversible moves, authored-content moves, publishing, pushes
    where the host says so, taste and domain wording — proposed with a recommendation, executed on their
    word. And only what is genuinely theirs is asked; everything else proceeds and is reported.

## The settings ladder

How the pack behaves is a **named setting** resolved up a three-step ladder — **host profile beats personal
profile beats package default** (SPEC E-13):

| Step | Home | Holds settings about |
|---|---|---|
| package defaults | the table below, in this file | the pack out of the box |
| personal profile | `~/.claude/livespec/profile.md` (SPEC D-5) | the HUMAN — follows them across every project |
| host profile | `<host>/.livespec/profile.md` | THIS project |

An override exists only as a written line in its profile file, and setting one leaves a dated journal note
in the home it governs — never a silent divergence (SPEC INV-14). Proactivity mode and trust are written
only on the human's word — the agent may propose, never set (SPEC INV-9). Profiles are re-read at the same
freshness points as skills (rule 8). A profile line the current pack does not recognize is ignored ALOUD —
named once in the session's next report — never silently dropped, never an error.

### Package defaults

| Setting | Default | A profile may say |
|---|---|---|
| `language.docs` | English — docs, commits, code, artifacts | another docs language |
| `language.chat` | mirror the human's language | pin one (e.g. Russian) |
| `proactivity.mode` | ask-at-max — surface forks, wait on taste calls | max-proactive: proceed on recommendations, batch questions |
| `trust` | low — human word before outward moves | raised only by the human (INV-9) |
| `prover.cadence` | FULL pass before every MINOR bump; CROSS-LINK on every surface add | tighter (e.g. livespec itself: before every push) or looser, recorded |
| `worker.tiering` | router proposes the cheapest sufficient tier; senior may override, logged | fixed tier per size class (SPEC D-2) |
| `checkpoints.home` | `<host>/.livespec/checkpoints/`, gitignored | another host path |

A profile file is plain markdown: one `setting: value` line per override, each with a trailing date and,
when it narrows the defaults, one line of WHY. Settings not listed above may be proposed as wishes — the
table grows through the queue like everything else.

> The pack, whole: **livespec-base** holds the shared rules and defaults · **spec-author** writes the spec ·
> **product-prover** reviews it · **build-pipeline** ships the change · **communicator** makes the human
> exchange land.
