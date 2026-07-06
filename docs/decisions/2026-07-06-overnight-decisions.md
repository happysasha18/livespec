# live-spec — overnight decisions page (2026-07-06 night, session 22)

**NEEDS YOUR WORD — in the morning, nothing burns: 1 decision below.** Everything else tonight is
just updates (chat carries them); no action needed there. The interactive version of this page (pick
an option, add your word, save the JSON) is the .html twin opened in your browser — this .md is the
repo record.

Kill-list of this artifact (his review rounds, INV-42):
- Round 1 (~23:38): the first before/after sample — KILLED, both halves «непонятно ни до ни после»;
  the bar he set: tone of voice of the most qualified persona who owns that stage (a strong product
  manager for product sections, a strong engineering lead for process sections). Never resurface the
  round-1 phrasing.
- Round 1b (~23:40, on his quotes): **pack coinages as reader-facing words — KILLED** («the wish being
  built»: a human text says task, feature, work in progress; internal nicknames stay internal) and
  **filler openers — KILLED** («Here is exactly what happens» is noise; a rule starts with the rule).
  Both applied to round 2 below.

---

## Decision 1 — the spec-readability rewrite (row 148, mockup-first entry)

Your word (~23:24): specs should read as if a qualified human wrote them. Below is round 2 of the
sample — two real SPEC sections rewritten in the voice you named. If it fits, the whole document gets
this treatment section by section (rule content and anchors held identical, full prover re-check
after). If not — say what to change; your correction becomes the bar.

### Sample A — a product rule, written by a strong product manager

**NOW IN THE SPEC (v0.15.42):**

> **An approved look lives in its artifact — the clause that encodes it points there, and the build looks
> at it.** Text cannot carry a feel: a spec clause born of an approved visual prototype was once rebuilt
> from its own prose and shipped a cheap look-alike — 75 tests green, because tests derived from a misread
> spec prove the misreading (tlvphoto's door and gallery, 2026-07-05). So when the human approves a sketch
> as the look, the prototype becomes the **norm** for look and feel, and one law with four arms guards it.
> The clause CITES its artifact — a `norm: <path>` pointer at the clause's line end beside its anchors,
> the prose carrying the laws while the artifact keeps the look (spec-author owns the pointer's format). …

**PROPOSED (round 2):**

> **Approved prototypes are binding design references**
>
> When you approve a prototype ("this is the door"), that prototype — not the text describing it —
> becomes the reference for how the feature must look and feel.
>
> 1. **The spec links to the reference.** Any requirement born from an approved prototype ends with a
>    pointer to the file: `norm: docs/norms/door.html`.
> 2. **Approval freezes a copy.** The approved file is copied into `docs/norms/` with a short note:
>    what it is, when it was approved, which sketch it came from. Requirements point only at this
>    frozen copy — never at a working sketch, which may still change or be deleted.
> 3. **Builders open the reference before building.** Whoever implements such a requirement opens the
>    prototype first and records one line: how the plan differs from it. Work that skipped this is
>    rejected at review, and the final check judges look and feel against the same reference.
> 4. **"Show me a mockup first" is a recorded requirement.** It is written into the task itself, and
>    only you can cancel it — by saying so explicitly. A general "go ahead and build" does not cancel
>    it.
>
> Why this exists: a gallery was once rebuilt from its text description alone, without opening the
> approved prototype. All 75 tests passed — they had been derived from the same misread text. What
> shipped looked nothing like what was approved. (tlvphoto, 2026-07-05) [INV-43]

### Sample B — a process rule, written by a strong engineering lead

**NOW IN THE SPEC:**

> A bug may interrupt the wish in-work. The interrupted wish moves to **parked**: a checkpoint is written
> (failing test names if red, hypothesis, touched files — nothing red is ever committed), the bug takes the
> lane, and the parked wish resumes as the immediate next landing — ahead of ANY queued wish, a quick win
> included: a bubble [T-11] jumps only fresh queued wishes, never a resume. …

**PROPOSED (round 2):**

> **When a bug interrupts: the fixed sequence**
>
> 1. The feature being built is parked. Before parking, its checkpoint is written: which tests fail
>    (if any), the current hypothesis, which files were touched. Unfinished red work is never
>    committed.
> 2. The bug takes the lane and runs to completion. Nothing interrupts a bug — a newly arriving bug
>    waits, whatever its priority.
> 3. While one bug runs, others queue: critical ones first (among themselves — by arrival), the rest
>    by arrival.
> 4. When no bug is waiting, parked features resume — ahead of everything in the regular queue.
>    Nothing jumps ahead of a resume, including quick wins.
>
> At most one feature is parked per lane. If several lanes were running, a bug parks them all, each at
> its own checkpoint; they resume in the order they were due to land. [T-9, T-11, T-18]

### What the rewrite would change — and what it never touches

Changes: each section written in the voice of the person who owns that craft (product rules — a
product manager; process rules — an engineering lead); numbered rules where one sentence carried four;
the incident that justifies a rule told at the end, in two plain sentences. Never touched: the rules
themselves, the anchor set (checked mechanically before/after), trailing codes, English.

**Your call:** (a) round-2 voice fits — run the whole-doc pass (recommended); (b) adjust — name what;
(c) leave the spec as is, close row 148.

---

*(Nothing else needs your word yet. Landed tonight without needing it: the prototype-norm law, the
fresh-shopfront-at-every-push law, the reach-map push gate, the pytest-from-root fix — defaults named
in their landing reports in chat.)*
