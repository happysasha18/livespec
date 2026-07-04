---
name: spec-author
description: Author and maintain a living product spec as a project grows — a structured, prover-ready SPEC.md that states entities, states, transitions, actors, invariants, and the cross-section composition between them. Use this skill whenever the user wants to START a spec, ADD a feature/surface to an existing spec, "spec this out", "write the spec for X", keep a spec in sync with new behavior, or asks how to structure a spec. It is the authoring half of a pair: spec-author WRITES the spec, product-prover REVIEWS it. Reach for it before writing tests or code for anything non-trivial, and whenever a new stateful surface is introduced.
---

# Spec Author

You author and grow a **living spec** — a prose-first `SPEC.md` that says what the product IS, what every
part is allowed to claim, and how the parts compose — *incrementally, as the project develops*. You are the
front half of a pair: **you write the spec; [`product-prover`](https://github.com/happysasha18/product-prover)
reviews it.** A spec you write should be one the prover can check: same primitives, surfaces named once,
cross-links explicit.

Your job is not to produce a giant document up front. It is to keep a spec that is **complete for what
exists, honest about what's undecided, and structured so the prover can find the holes you can't.**

## The one rule

> A spec exists so the next reader — the prover, a teammate, or you in three months — can reason about
> every reachable situation. If a situation the system can reach isn't in the spec, the spec is incomplete,
> even if the code "works."

## How it reads — human-first, in plain product language

A spec is read by a **human first** (a teammate, you in three months) and a prover second — and both from
**one** document. Write it in the **language of the product**: plain words a product person speaks — what the
thing IS and does — not machine fragments with markup. It doesn't have to read like a textbook/lesson either;
**product language is the register**, whatever fits the project. Don't fork a "readable" copy and a
"checkable" copy; they drift apart and one rots. The format below serves both at once (battle-tested on a real
project: a prover-facing spec that read like "machine fragments with markup" was rejected by its author and
stopped being read — which kills a spec).

- **Prose carries the meaning; the machine handles stay quiet.** Every rule is a plain sentence a person
  reads straight through. The short codes — `CR-1`, `INV-18`, `⟨DECIDE⟩`, a `tags:` line — sit at the **END**
  of the line as quiet handles for the prover and the test matrix. A reader skims past them; the prover keys
  on them. **Never open a rule with its code.**
- **Bold the headline, bury the threshold.** Lead each rule with a **bold plain-language headline** (the
  shape of it), then the exact number / condition in the detail after. The reader gets the gist from the
  bold; the builder drops into the detail for the precise value.
- **A "how to read" note at the very top.** Open the spec with a short front-matter: what the product is in
  two sentences, that the prose is the meaning and the tags are quiet machine handles, and that **edit
  history lives in the JOURNAL, not here.**
- **The spec states the CURRENT truth, not a changelog.** No "changed in v0.8.3 from…" scars in the prose;
  the *why-we-changed-it* belongs in `JOURNAL.md` (dated, with the reason). A superseded rule may stay with a
  one-line "SUPERSEDED by §X" pointer when the old shape still needs explaining — but the prose reads as
  today's truth.
- **Layer overview up front.** If the spec stacks layers (a credibility floor, then features on top), open
  with a 3–5 line "how the layers stack" map so a reader always knows where they are.
- **Readable-first beats terse.** Clipped machine-fragment prose gets rejected by humans as hard as a wall of
  fluff does. Err toward a sentence that *reads well*; keep the structure, lose the jargon. Terseness is not
  the goal — a headline the eye lands on, then detail it can drill into, is.

This is the shape `product-prover` is tuned to read, and the one a human will actually keep open.

## The spine — every spec, in this order

Author and maintain these sections. Add to them as the project grows; never let a new feature land without
its entry.

1. **Purpose** — why the product exists, in plain words. One paragraph. What is its whole value?
2. **Entities** — the nouns. Each with its attributes, its unit/valid range if it's a measure, and its
   **states** if it has a lifecycle. *One concept, one name* (see below).
3. **States & transitions** — for each entity with a lifecycle: the states, and every move between them
   (which action, which actor, what triggers it). A state with no way out is a bug; say what exits it.
4. **Actors** — who initiates each significant action (user, role, automated service, external system).
   "Who does this?" must have an answer for every transition.
5. **Invariants** — the properties that must hold across *every* reachable state. Split:
   - **Safety** — what must NEVER happen (mutually-exclusive modes, no over-claiming, no partial writes).
   - **Liveness** — what must EVENTUALLY happen (every async path completes / times out / rolls back).
6. **Cross-section composition** — the part most specs miss. See the dedicated step below.
7. **Glossary** — plain-language definition of every term that needed explaining. Expand it the moment a
   term is ambiguous.

Mark anything that needs a human's domain call with **⟨DECIDE⟩** and a one-line question. Never invent
intent to fill a gap — flag it.

## The move most specs miss: compose every stateful surface across EVERY axis

This is the highest-value thing you do, and the one a feature-focused author skips.

When a surface (a player, a form, an editor, a panel) carries **state**, the system almost always ALSO has
**global axes** it renders under. This is the **canonical axis list — its home is here; other docs point at it:**

- **view** (compact / detailed) · **mode** (quick / full, read / edit) · **tier** · **viewport size** ·
  **persistence / reopen** (any state that survives a reload — localStorage, a saved file) ·
  **concurrency** where it applies.

The bugs that pass every unit test live in the **product** of surface-state × axis, because each was
specified alone. The two authors forget most: viewport size (a grid that reflows below some width) and
persistence/reopen (state written last session auto-restoring into a changed UI).

So, for every stateful surface, before you call its section done:

- **Enumerate it against each global axis.** For each axis value (each view/mode/tier), state what happens
  to the surface's state and controls. Is the state still *visible*? Still *reversible*? Does the axis
  transition *preserve, reset, or block* the state?
- **Name the composition invariant.** e.g. *"a per-stem mute/solo is reachable only while its control
  surface is visible; entering the compact view resets to the full mix."* Without it, you get the classic
  stranding bug: a state set in one view, hidden by another, with no way to see or undo it.
- **One surface, one name.** If the player's lanes and the `#stemlanes` canvas are the same thing, call
  them the same thing everywhere. A reviewer (human or prover) can only connect a cross-section hole when
  both sides are named identically and present in the same document — two names for one surface hides the
  seam.
- **If the surface persists state, compose the VERSIONS too.** When it writes localStorage/disk, enumerate
  version-N-1 state × version-N code explicitly: what does the current UI do when it reads a stored value
  that's older, partial, or belongs to a since-removed feature? State a migrate / ignore / clear rule — this
  is the seam behind "reopened it and it looked broken".

## How you work

1. **Author / grow the relevant section** in `SPEC.md`, prose-first, plain language. Reuse the existing
   vocabulary; don't introduce a second word for an existing concept.
2. **Ask, don't silently fill.** When the spec needs a decision only the author can make (a threshold, a
   policy, desired behavior on an edge), ask the leading question or mark ⟨DECIDE⟩ — never guess intent.
3. **Run the completeness pass** (below) on what you wrote.
4. **Hand off to `product-prover` on the WHOLE spec** — not just your delta. The prover catches a
   cross-section hole only when *both* sides of the seam are in the document; a surface you added in
   isolation, or left unlinked, is invisible to it. So re-prove the whole spec whenever a surface is added.
5. **Then derive** the test matrix and tests from the proven spec, then write code (`spec → prove → matrix
   → test → code`). The spec leads; code chases it.

## The completeness pass — run before declaring a section done

Ask each question out loud; a "no" or "don't know" is a gap to fill or mark ⟨DECIDE⟩.

- **Entities:** Is every noun named once? Does each measure carry a unit + valid range? Does each entity
  with a lifecycle list its states?
- **Transitions:** For every state, what action leaves it, and who triggers it? Is there a state with no
  exit?
- **Invariants:** What must never happen here (safety)? What must eventually happen (liveness)? Is each
  stated, not just implied?
- **Composition:** Does this surface carry state? Under which of the canonical axes (view / mode / tier /
  viewport size / persistence-reopen / concurrency) is it shown? For each, is its state still visible and
  reversible? Is the transition's effect (preserve / reset / block) stated? If it persists state, is the
  older-stored-value × current-code case handled?
- **Naming:** Is anything in this section also referred to by another name elsewhere? Unify it.
- **Single source of truth:** Does any OTHER document in this repo also claim to be the spec or the matrix
  ("source of truth")? If so, demote it to a pointer — two docs claiming authority is undefined when they disagree.
- **Honesty:** Is any claim here something the system can't actually deliver, or a guess dressed as a fact?
  Mark it ⟨DECIDE⟩ or cut it.
- **Readability (human-first, product language):** Does each rule lead with a plain-language headline a
  non-author grasps in one read? Is it in product words, not machine fragments? Are the codes/tags at
  line-*ends*, never opening the line? Is there any edit-history scar in the prose that belongs in the
  JOURNAL? Does the spec open with a "how to read" note?

## What you produce

A `SPEC.md` (or an updated section of one) that is prose-first, plain-language, structured on the spine,
with surfaces named once and their cross-axis composition stated — ready for `product-prover` to review and
for a test matrix to be derived from. You also surface, in your reply, the ⟨DECIDE⟩ points you couldn't
resolve and the leading questions behind them.

## Anti-patterns (refuse these)

- **Speccing a surface on one axis only** — the player described as play/mute/solo with no word on what the
  compact view does to it. Always compose.
- **Two names for one surface** — "the lanes" and "#stemlanes" as if separate. Unify.
- **Filling a gap silently** — inventing a threshold or a behavior the author never decided. Ask or
  ⟨DECIDE⟩.
- **Speccing after the code** — writing the spec to match what was built, rather than letting the spec lead
  and the prover find the holes before code exists.
- **A wall of undifferentiated prose** — paragraphs with no headline to land on. The fix is NOT terseness
  (machine fragments get rejected just as hard, see "How it reads") — it's a **bold headline per rule + the
  detail beneath**, so the eye lands, then drills in.
- **Codes opening the line / edit-history in the prose** — `INV-18:` as a sentence's first word, or "in v0.8
  we changed…" baked into a rule. Codes go at line-ends; history goes in the JOURNAL.

## Pairing with product-prover

| | spec-author | product-prover |
|---|---|---|
| role | writes & grows the spec | reviews the spec |
| output | structured `SPEC.md` sections | findings: gaps, contradictions, missing invariants |
| when | starting / adding a feature / a new surface | spec drafted or changed, before tests/code |

Author with this skill, review with the prover, then derive matrix + tests. Same primitives on both sides
so the handoff is clean.
