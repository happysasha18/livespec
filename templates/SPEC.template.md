# [Project Name] Spec

> How to read: the prose is the meaning; the short codes (INV-x, CR-x, ⟨DECIDE⟩) are quiet machine handles at line-ends for the prover and test matrix. Edit history lives in JOURNAL.md, not here. This spec states today's truth.

---

## 1. Purpose

Why the product exists, in plain words. One paragraph. What is its whole value to the person using it?

---

## 2. Entities

The nouns. Each with its attributes, its unit/valid range if it's a measure, and its states if it has a lifecycle.

**[Entity name]** — description. Attributes: [attr: type, valid range]. States: [if lifecycle — see section 3].

*One concept, one name everywhere. If two sections use different words for the same thing, unify them.*

---

## 3. States and transitions

For each entity with a lifecycle: the states, and every move between them (which action, which actor, what triggers it). A state with no way out is a bug; say what exits it.

**[Entity]:**
- State A → State B: [action], triggered by [actor] when [condition]
- State B → State C: [action], triggered by [actor] when [condition]

---

## 4. Actors

Who initiates each significant action.

- **[Actor]** — [what they do and which transitions they initiate]

Every transition in section 3 must name an actor from this list.

---

## 5. Invariants

Properties that must hold across every reachable state.

**Safety** — what must NEVER happen:
- [INV-1] Plain-language headline — exact condition. `tags: safety`

**Liveness** — what must EVENTUALLY happen:
- [INV-2] Plain-language headline — async path completes / times out / rolls back within [bound]. `tags: liveness`

---

## 6. Cross-section composition

For every stateful surface, composed across the canonical axis list: **view · mode · tier · viewport size · persistence/reopen · concurrency**.

**[Surface name]** — [what state it carries]:
- view (compact / detailed): [what happens to the surface's state and controls]
- mode (quick / full): [preserve / reset / block — and what triggers it]
- viewport size: [reflow behaviour below [width]px]
- persistence/reopen: [what the surface writes to disk/localStorage; what happens when an older stored value meets the current UI]
- concurrency (if applicable): [concurrent access behaviour]

*Composition invariant: "[plain sentence stating what must hold across axes]."*

---

## 7. Glossary

Plain-language definition of every term that needed explaining. Expand whenever a term is ambiguous.

- **[Term]** — [definition]

---

*Authored via spec-author. Review with product-prover before deriving the test matrix or writing code.*
