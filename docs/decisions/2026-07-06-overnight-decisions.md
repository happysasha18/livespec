# Overnight decisions page — 2026-07-06 night, session 22 (for Alexander's morning)

Questions only yours, accumulated by the overnight loop. Each one: context, the options, my
recommendation. Nothing here blocks the queue — where a default was takeable, it was taken and told.

---

## Decision 1 — the spec-readability sample (row 148's entry deed: mockup first, then the rewrite)

Your word (~23:24): specs should read as if a human — a product person, an architect — wrote or at
least edited them. Row 148 is queued with a mockup-first entry condition; this is the mockup. Two real
sections of the pack's SPEC, before → after. If the voice fits, the whole-doc pass runs section by
section (anchor sets held identical, full prover re-check after). If not — name what to change and the
pass takes your correction as the bar.

### Sample A — the prototype-norm law (landed tonight, row 109)

**BEFORE (as it stands in SPEC v0.15.42):**

> **An approved look lives in its artifact — the clause that encodes it points there, and the build looks
> at it.** Text cannot carry a feel: a spec clause born of an approved visual prototype was once rebuilt
> from its own prose and shipped a cheap look-alike — 75 tests green, because tests derived from a misread
> spec prove the misreading (tlvphoto's door and gallery, 2026-07-05). So when the human approves a sketch
> as the look, the prototype becomes the **norm** for look and feel, and one law with four arms guards it.
> The clause CITES its artifact — a `norm: <path>` pointer at the clause's line end beside its anchors,
> the prose carrying the laws while the artifact keeps the look (spec-author owns the pointer's format).
> Approval FREEZES the artifact into the project's records: a copy lands in `docs/norms/` with a dated
> provenance line (what, approved when, from which sketch), and the pointer cites the frozen copy — a
> norm pointer never reaches into a live prototype home, so the one-way fence stays absolute and the
> sketch stays free to die [E-17, INV-17]. Building a surface whose clauses carry a norm-pointer OPENS
> the artifact before the code step, and the landing records a one-line plan-vs-prototype diff — a
> missing diff line is a defect at review (build-pipeline's code step); the verify step's feel bar reads
> the same pointer [INV-30]. A story's declared mockup-first entry condition — "show me first, then
> build" — is WRITTEN in the wish's queue row at intake ("entry: mockup-first") and is cancelled only by
> the human naming it; a general "go build" moves priority, never that condition (the door step). …

**AFTER (the proposed voice):**

> **An approved look lives in its artifact — the clause points there, and the build looks at it.**
>
> Text can't carry a feel. We learned this the hard way: a clause born from an approved prototype was
> rebuilt from its own prose, and what shipped was a cheap look-alike — with 75 green tests, because
> tests derived from a misread spec faithfully prove the misreading (tlvphoto, 2026-07-05).
>
> So approval now does something concrete. When you approve a sketch as *the look*, that prototype
> becomes the norm:
>
> - The spec clause **cites it** — a `norm: <path>` pointer at the end of the line, next to the
>   anchors. The prose keeps the rules; the artifact keeps the look.
> - Approval **freezes a copy** into `docs/norms/`, with one line saying what it is, when it was
>   approved, and which sketch it came from. The pointer cites the frozen copy, never a live sketch —
>   the prototype fence stays absolute, and the sketch stays free to die. [E-17, INV-17]
> - The build **opens it**. Before building a norm-pointered surface, open the artifact and write one
>   line: how the plan differs from the prototype. A missing line is a review defect; verify reads the
>   same pointer for its feel check. [INV-30]
> - "Show me first, then build" **is written down** — in the wish's queue row ("entry: mockup-first") —
>   and only you cancel it, by naming it. A general "go build" moves priority, never this condition.
>
> The prover reads visual clauses with the same lens: a prototype-born clause without a pointer, or
> text contradicting its own artifact, is a finding. The law binds forward — a clause owes its pointer
> at the first landing that touches it; a pointer names only what you actually approved. [INV-43]

### Sample B — when a bug cuts the line

**BEFORE:**

> A bug may interrupt the wish in-work. The interrupted wish moves to **parked**: a checkpoint is written
> (failing test names if red, hypothesis, touched files — nothing red is ever committed), the bug takes the
> lane, and the parked wish resumes as the immediate next landing — ahead of ANY queued wish, a quick win
> included: a bubble [T-11] jumps only fresh queued wishes, never a resume. Should more bugs arrive while
> one holds the lane, **critical** bugs head the waiting line (among themselves by arrival), the rest
> follow by arrival; the parked wishes resume only once no bug waits. A bug already in the lane is never
> itself interrupted — an arriving bug, critical included, joins the line, so at most one wish is ever
> parked PER LANE: when several trains were rolling [T-18], the bug parks them all — each at its own
> checkpoint — and they resume in their landing order. [T-9]

**AFTER:**

> A bug may interrupt the wish being built. Here is exactly what happens.
>
> The interrupted wish **parks**. Its checkpoint is written first — the failing test names if anything
> is red, the current hypothesis, the files touched. Nothing red is ever committed. Then the bug takes
> the lane.
>
> The parked wish **resumes next** — ahead of any queued wish. Even a quick win only jumps fresh queued
> wishes; it never jumps a resume. [T-11]
>
> More bugs while one holds the lane? They **wait in line**: critical ones at the head (among
> themselves — by arrival), the rest by arrival. Parked wishes resume only when no bug is waiting. And
> a bug in the lane is never itself interrupted — an arriving bug joins the line, critical or not.
>
> So at most **one wish is parked per lane**. If several trains were rolling, the bug parks them all,
> each at its own checkpoint, and they resume in their landing order. [T-18, T-9]

### What the rewrite changes — and what it never touches

Changes: sentence length (one idea per sentence), paragraphs that breathe, bullets where one sentence
carried four rules, bold on the beats a skimmer needs, incidents told as short stories. Never touched:
the anchor set (identical before/after, checked mechanically), the rules themselves, the trailing-code
convention, English.

**Your call:** (a) voice fits — run the whole-doc pass (my recommendation); (b) adjust — name what;
(c) leave the spec as is, close row 148.

---

*(Nothing else accumulated yet — rows 109, 146, 147, 106 landed without needing your word; defaults
taken are named in their landing reports.)*
