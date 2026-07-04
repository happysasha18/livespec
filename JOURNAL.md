# livespec Journal

Edit history lives here — the WHY behind every change. The spec and README state current truth; this file explains how we got there.

---

## 2026-07-04 — Package born

**What:** Created the livespec skeleton repo — directory structure, four bundled skills, templates, adopt procedure, guardrails outline, install script.

**Why:** The method (spec → prove → reconcile → matrix → test → code → verify → commit) has been running in production on track-coach for over a year and is proven. It lives scattered: CLAUDE.md rules, four skill repos, a playbook, and a habit. The goal of livespec is to make the whole thing one attachable package — clone it, run `./install.sh`, and the skills land in `~/.claude/skills/` ready for any project. One home, not four.

**Why "livespec":** Alexander's coinage (2026-07-04). Working name; a better name may emerge (queued in ROADMAP).

**Status:** Skeleton only. Skills are read-only copies (source repos unchanged). No SPEC authored yet — that waits for Alexander's signal to publish, so spec-author runs on the full intended scope, not a moving target. Unpublished; local only.

**Decided:** Local-only for now. No GitHub creation, no push. When Alexander says publish, that is ROADMAP item 1 — create the repo, push, wire the skill install to the real source.

## 2026-07-04 — SPEC v0.1: the first self-application run
Alexander caught a real hole in ADOPT (it inventoried code but not existing DOCUMENTS) and added two more
wishes (attic-not-delete; version-control gate). Instead of patching ADOPT.md pointwise, livespec was run
on itself: three wishes → queue rows 8-10 → SPEC.md v0.1 authored covering the whole package (wish
lifecycle, both entry modes, actors, milestones, self-application invariant M-4). ADOPT.md and README will
be updated AFTER the prover pass (row 7) — spec before docs, by the book.

## 2026-07-04 — prover pass (row 7) + the honesty correction
FULL product-prover pass over SPEC v0.1: 11 findings (wish exit states; preemption path; surface-registry
entity; current-vs-target marking; profile owner+trust rule; provenance reconcile transition; baseline
advance timing; INV homes; human-gate re-listing; skill-version drift; checkpoint home). All folded → v0.2.
Alexander then challenged the "pioneers / no prior art" claim as possible people-pleasing. He is partly
right: artifact-baseline diffing is MATURE prior art in testing tooling (Jest snapshots, Percy, Chromatic
visual regression). Our narrower true claim: declared-scope diff as an agent pre-push guardrail + the
continuous-intake combination. README rewritten to credit lineage and link BMAD; long-tail search of the
skill ecosystem launched before publish.

## 2026-07-04 — first REAL adopt run (tlvphoto) + dogfood fix to ADOPT.md (row 4)
The adopt procedure ran end-to-end on a live host for the first time. The run's own story lives where it
belongs — in the HOST's journal (tlvphoto JOURNAL.md, entry "2026-07-04 — livespec adopt"); this entry keeps
only what changed LIVESPEC. (Trimmed 2026-07-04 late: the host story was originally written here too —
that duplication is exactly what the write-ownership rule now forbids.)

**Why this changed livespec itself:** the run proved `adopt/ADOPT.md` was STALE vs SPEC (it still had the old
inventory→reverse-spec→snapshot order, missing orient/attic/VCS-gate). Rewrote ADOPT.md to the SPEC A-0…A-7
sequence. One genuine refinement the run surfaced and I folded: the **version-control gate belongs FIRST**
(before orient touches anything) so the whole run is reversible — annotated SPEC A-0/A-5 (codes name
meanings, not a frozen order). A re-prove of the adopt section is due at the next milestone (minor reorder,
not blocking). Closes ROADMAP row 4; completes the "update ADOPT.md to the proven spec" tail of row 7.
Note: livespec repo was concurrently edited by another session (publish + rows 12-15) — this entry touched
only ADOPT.md, SPEC A-0/A-5, ROADMAP row 4, and this journal.

## 2026-07-04 — parallel-session protection (row 16) + codes-never-speak (row 17)
Two sessions edited this repo the same evening: one publishing (rows 1, 12–15), one running the tlvphoto
adopt (row 4) — the adopt session edited ADOPT.md/SPEC/ROADMAP/JOURNAL directly and avoided a collision only
by NOTICING the foreign commits and being surgical. Alexander: that must be mechanics, not luck — and a host
run's story belongs in the HOST's docs, not here.

Landed (SPEC v0.3): **INV-10 write-ownership** — only a session the human assigned to livespec itself writes
this repo; every other session is read-only except creating one new `inbox/` file. **INV-11 concurrent-edit
fence** — re-check HEAD/`git status` before every write and every commit; foreign changes ⇒ stop, re-read,
proceed surgically or back off; never push while another session is live (push coordination is the human's);
applies to host repos too. **E-11/T-10 inbox/** — one new file per outside wish; file-creation cannot collide,
so no-wish-is-lost holds without outsiders touching shared files. ADOPT.md now states the host-session
read-only rule. The row-4 entry above stays (it documents a real livespec change); under the new rule that
change would have arrived as an inbox wish.

Same evening, second leak of the same class (row 17): a session told Alexander "INV-8 рекомендует
GitHub-бэкап" — a spec handle spoken to the human. communicator rule 6 hardened from a soft "translate
internal ids" to a hard gate: spec handles (INV-x, E-x, A-x, T-x, row numbers, ⟨DECIDE⟩) are machine anchors
that never appear in a sentence addressed to the human; the leak itself is the rule's ❌ example now.

## 2026-07-04 — late refinements: anchors-in-parens, journal cleanup, push gate + its first run
Three refinements from Alexander the same night, all landed before the v0.3 push:
1. **Anchors in parentheses are allowed — with the WHY recorded** (row 17 refined): the plain sentence
   carries the meaning for the human; the trailing code serves the MODEL — transcripts are what it greps
   and self-monitors against, so a stable anchor makes past reasoning findable. Rule 6 rewritten from
   "codes never appear" to "a code never does the talking"; installed copy synced.
2. **Journal cleanup by the new ownership rule:** the row-4 entry held the tlvphoto run's full story — a
   HOST's story in the package's journal, the exact duplication the write-ownership rule forbids. Trimmed
   to the livespec-only part with a pointer to tlvphoto's JOURNAL (verified present there first).
3. **Push gate (M-6, row 18):** Alexander — livespec specifically gets a fresh whole-spec re-check before
   EVERY push. Spec'd and enforced immediately: prover pass docs/prover/2026-07-04-v03-push.md over v0.3
   found 7 findings in the new seams — the gate could regress on itself (fold→re-prove forever), an
   outsider's uncommitted inbox file would trip the very fence built to receive it, an inbox wish could
   wait durably-recorded but invisible, plus name-collision/record-naming/standing-routine edges. Six
   folded into SPEC same session (gate no-regress rule; outsider commits its inbox file + fence treats
   inbox files as benign; sessions sweep inbox first + milestone lists unharvested files; `-2` counter;
   dated record naming; standing routines count as assignment). Seventh recorded onto row 3's scope
   (guardrails scaffold also mechanizes the fence and the push gate). First push of v0.3 follows this entry.
