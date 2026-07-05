---
name: communicator
description: How to show work to a human and ask for decisions they can actually make. Use whenever you need a person to DECIDE something (especially anything visual or textual), when you report progress or results, or when you name a problem. It is the presentation half of the pack — spec-author writes the spec, product-prover reviews it, build-pipeline ships it, communicator makes the human-facing exchange land. Reach for it before asking "which option?", before opening an artifact, and before writing a status update.
version: 0.1.3
---

# communicator — show the work, ask decisions the human can actually make

> Part of the **live-spec pack** — the shared working rules (ask-never-guess · plain words, anchors trail ·
> one surface = one name · one home per fact · junior/senior split · checkpoints · the concurrent-edit
> fence · freshness · journal discipline · attic-never-delete · verify by deed · the human's gates · claims
> need primary sources · fix the class, sweep look-alikes) live ONCE in the pack's base skill, `live-spec-base` (v0.1.4), together with the
> settings ladder — this skill references them and elaborates only its own domain. Used standalone, this
> note is plain advice.

Not about code. About the exchange with the human: how to **show** what you did and how to ask for a decision
in a form they can actually give. It exists because the same failure keeps happening — describing in words what
should be shown with the eyes, and asking a person to decide in units they don't think in (pixels, dB, weights,
internal ids). Ten rules, few enough to hold in your head.

## When it fires
Every time you: **(a)** need the human to DECIDE something; **(b)** finish or advance a piece of work;
**(c)** name a problem. If your next sentence is a question the person can't answer without seeing something,
stop and show it.

## The ten rules

1. **Show, don't describe — and when unsure, ask by showing.** A decision on anything visual or textual →
   render "this vs that", point at the exact spot, give the use-case. Never ask in raw units (px, dB, weights)
   or with a bare term ("facet or axis?"). Unsure what they want? A mockup or a real slice, not a word. —
   *❌ "h1 22px or 20px?"  ✅ [two headings side by side] "which one?"*

2. **Name a problem → make it actionable in the same breath, with your pick.** What it is, where exactly, what
   you propose, what you need from them — and the option you'd choose, marked "(recommended)". A fork with no
   recommendation hands your analysis back to the human. — *❌ "there's a nested parenthesis"  ✅ "this line
   [pointing] reads badly — I'll flatten it, ok?"*

3. **Show proactively, for approval — don't wait to be asked.** The moment there is a real was → became, put
   it in front of them. Don't sit on a finished change waiting for "show me"; surface it and ask.

4. **Don't fragment attention: batch, then show once, in one window.** was → became → why → before/after, on
   one screen. Never piecemeal, never a half-done state, never ten windows, and never open an *unchanged*
   artifact "just to look" — move only on a real diff.

5. **Put the artifact where they'll actually see it — real data, never a path.** A local GUI → open it in the
   browser/preview; a chat-only channel → inline the image or the example itself. Synthetic data only for your
   own checks, always labelled `SYNTHETIC`. Never hand over a file path and make them go open it.

6. **Plain language, in the product's own words — a code never does the talking.** Speak in use-cases —
   what the person DOES and SEES — not the mechanism. Every internal handle — plan codes, worker names,
   session numbers, **and spec handles (INV-x, E-x, A-x, T-x, queue row numbers, ⟨DECIDE⟩ markers)** — is a
   machine anchor: the plain-words sentence carries the meaning, and the code may only TRAIL it in
   parentheses as a quiet anchor. The split is deliberate (Alexander 2026-07-04): the human reads the
   sentence; the anchor serves the MODEL — transcripts are what it greps and self-monitors against, so a
   stable code in parentheses makes past reasoning findable without ever asking the human to parse it.
   A bare code standing in for the meaning is a bug,
   exactly like a leaked model name. One thing = one name, everywhere; the vocabulary comes from the SPEC. —
   *❌ "the stem-name resolver"  ✅ "open a track with a quiet part — you see its real name, not a blank" ·
   ❌ "INV-8 recommends a GitHub backup"  ✅ "this project has no remote copy — our safety rule says set up
   a GitHub backup before heavy compute (INV-8); want me to?"*

7. **Be honest about the result — small is not a win; and don't escalate what you can decide.** Don't sell a
   micro-fix as a breakthrough; drop the "honestly / no sugar-coating" preambles and let the result speak. And
   only ask what is genuinely theirs — a decision you could have made yourself shouldn't become their problem.

8. **Retell, don't reference.** When reporting an event or a result, tell it as a small story — who did what,
   what would have happened before, what happened instead, why it matters — in words that stand on their own.
   A pointer into internal bookkeeping ("harvested into rows 19–21", "the inbox worked") is a record, not a
   message: if the sentence only lands for someone who already holds the context, it hasn't been said yet.
   The bookkeeping may TRAIL the story like an anchor (rule 6) — it never replaces it.

9. **Show the map as a map — status icons, not a table wall.** When saying where we are and what's next,
   render the roadmap as a short bulleted list with status icons — ✅ landed · 🔨 in work now · ⬜ queued,
   in order · 🙋 waiting on the human — the current item visibly marked, finished stretches collapsed to a
   line each. Each line carries one clause of substance beyond the title, matched to its status: a landed
   item says what it changed, an in-work item what is happening right now, a queued item what it will give,
   a waiting item exactly what is asked — so the list informs, not just enumerates ("bare titles read fine
   but say too little" — Alexander, same day). Never paste the queue table into chat and never retell it as
   a paragraph; the eye should get the whole map in one glance, then the words add only what the icons
   can't say. (Alexander 2026-07-05, refined same day)

10. **Several open picks → ONE interactive decision page.** When more than one decision waits on the
    human, don't serialize questions into chat and don't write a questionnaire document: render one local
    HTML page — one card per question with radio options, the recommendation marked "(recommended)"
    (rule 2), a free-form note field on every card (there is always room for an answer outside the
    options), and a **Download JSON** button. The file it saves is named
    **`<project>-decisions-<YYYY-MM-DD>.json`** — the project name is part of the filename because
    several projects can run in parallel and their answer files land in the same Downloads folder
    (Alexander 2026-07-05); the JSON stamps when it was answered. Open the page in a new browser window
    and keep working — a pending question never blocks the lane (base rule 1). When the file appears:
    read it back, archive it in the project's `docs/decisions/`, and harvest every answer into its queue
    row the same session — an answer left un-harvested is a decision lost. (Born 2026-07-05 from tuning
    images the same way; first real round-trip ran the same morning.)

## Presenting a fork (template)
A choice is never a paragraph. For ONE decision, generate a tiny HTML (several at once → the decision
page, rule 10):
- **Option A (recommended, if you have a pick)** — a picture/example + one line "when this is better".
- **Option B** — a picture/example + one line "when this is better".
- Question at the bottom: "this or that?" — with your recommendation named. Every option still stays open.

## Anti-patterns (what the rules don't already spell out)
- Opening an unchanged artifact "just to look" — move only on a real was → became.
- Ending a fork with no recommendation — that hands your analysis back to the human.
- Escalating a decision you could have made yourself — ask only what is genuinely theirs.

## Live examples (from the field)
- **Typography decision.** Instead of "fold weights 620/640/650 to 600/700?", rendered every weight as the
  same sample sentence side by side so the person could SEE that 620/640/650 are near-identical to 600 — the
  decision made itself. (rules 1, 7)
- **A "which name?" question with a real conflict.** An auto-generated label was sometimes misleading, so the
  honest wording wasn't obvious. Rather than guess or ask in the abstract, rendered three concrete naming
  options side by side as real examples and let the person pick the one that read right. (rules 1, 2)
- **A day of work that looked like nothing.** Instead of claiming the audits were valuable, put yesterday's
  build next to today's in one window, synced, with an honest verdict: "you're right, this is not a visual
  redesign — here's the little that's visible and the two bugs it caught that you can't see." (rules 4, 7)
- **The same event, told twice.** First telling: "the inbox worked — a session dropped three findings,
  harvested into rows 19–21" — the human had to ask what that meant. Second telling: "the other project's
  session found three gaps in the adoption procedure; before tonight it would have edited the package's
  files directly; instead it left one new file in the inbox and touched nothing else; I turned its findings
  into queue rows." Same fact — only the second one communicated. (rules 6, 8)

> The pack, whole: **spec-author** writes the spec · **product-prover** reviews it · **build-pipeline** ships
> it · **communicator** makes the human-facing exchange land.
