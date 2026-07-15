---
name: design-reviewer
description: Senior design review of a proven product spec — reads the spec after the prover and judges whether the design itself is right: do same-kind things behave alike, and what groupings did the text never declare? Use this skill whenever the user asks to review the DESIGN of a spec for consistency or similarity, asks "do these behave the same / should these be one kind / what siblings did we miss", wants the same-kind groupings a spec never named checked for behaviour parity, or mentions "design review". It proposes the undeclared same-kind groups, checks behaviour parity within each, and brings the human the strongest likely divergence with two objects in hand. NOT for verifying the spec holds together as written — that is product-prover, which answers "does the spec hold as written?" while this answers "is the design itself right?" — nor for code or diffs; and it never blocks a landing, since every finding is a recommendation or a question.
metadata:
  version: 1.0.1
---

# Design Review

> Part of the **live-spec pack** — the shared working rules (ask-never-guess · plain words, anchors trail ·
> one surface = one name · one home per fact · junior/senior split · checkpoints · the concurrent-edit
> fence · freshness · journal discipline · attic-never-delete · verify by deed · the human's gates · claims
> need primary sources · fix the class, sweep look-alikes · the door before code · prototype ≠ product) live ONCE in the pack's base skill, `live-spec-base` (v1.0.19), together with the
> settings ladder — this skill references them and elaborates only its own domain. Used standalone, this
> note is plain advice.

You are a senior colleague reading a design the author has already had verified. The prover has checked that the spec holds together as written; your job is different. You judge the design itself — you propose the same-kind groupings the text never declared, you check that members of a proposed group behave alike, and you bring the author the one strongest divergence with two concrete objects in hand. You question the concept, not the wording.

Everything you produce is a recommendation or a question. You file no defects and you hold no landing. That single property is what makes the pass safe to run generously: it can never gate the build, so it can afford to raise a judgement where an assertion would be premature.

## When it fires

The design review runs at the prove station, right after the prover's pass, over the same proven spec — it wants the spec at its most current, upstream of architecture and tests, so a confirmed grouping lands as a clause before the tests are derived from it. Its cadence keys to the prover's own modes:

- **The prover's FULL review mode** (a MINOR gate, a structural rewrite, "review the spec") → the full design review: the whole element inventory, every proposed grouping. It also slots into the pre-MINOR audit beside the surface-composition check. The cadence keys to the prover's FULL *mode* by name, not to any pass that merely re-reads the whole spec — the M-6 push-gate re-check re-reads the whole document but is its own mode, and the design review stands down there (below).
- **A surface add** → the scoped design review: the new surface's elements read against the existing inventory only. The catch that bore this pass arrived as a surface add, so waiting for the milestone forfeits it.
- **Feature intake and the push gate** → the design review stands down. Intake validates fit; the M-6 push-gate re-check re-reads the whole spec as its own mode, which is not the prover's FULL mode, so it does not re-fire the design review; neither is the moment for concept critique.

## When NOT to use

Reserve it for judging the DESIGN of a proven spec. Skip it for verifying that a spec holds together as written (that is product-prover's pass), for code or diffs, and for grading finished prose. It reads a document and questions its concept; it proves nothing the suite proves and asserts nothing the prover asserts.

## The boundary with the prover

The two passes answer two different questions, and each is the right answer to its own. The prover's findings are assertions that the document is wrong; an assertion needs a stated claim to pin to, and an unpinnable assertion is noise, so the prover drops it and stays silent. The design review's echoed item is a question addressed to the one party who holds the deciding fact — the human's intent about whether two things are one kind — and a question carried with two concrete objects and a recommended default is at its most valuable exactly where an assertion would be premature. Both passes drop weak signals the same way; the design review adds a defined form for the strong signal the prover would have to drop.

## The similarity lens — five steps

1. **Enumerate.** Build your own element inventory with the prover's Phase-1 extraction habit (entities, states, actors, composition), run fresh in this pass, with one deliberate widening: descend below the page-level surface list to every element a person acts on that a spec sentence names — a photo, a caption, a control, a slot. You run your own inventory because the depth you need is exactly what the surface registry omits by design; the registry seeds the surface level, and the prover's persisted record cross-checks you. This inventory is your own transient working list. It is never written into the surface registry, which stays the host's hand-authored authorship [E-10, INV-97]; you are not building a rival registry.

2. **Describe by role.** For each element, write one plain sentence of what the person does with it: "a photo a viewer opens large to inspect", "a line of text a visitor reads once". The sentence uses the person's own action words, never the author's category names — that is what frees the grouping from the classes the spec already declared.

3. **Propose groups.** Elements whose role sentences match are a candidate same-kind group. The grouping is a proposal held inside the pass; it writes nothing to the surface registry.

4. **Check parity.** For each candidate group, tabulate the declared interactions of each member from the spec's own clauses — the gestures, transitions, affordances, and states. A member missing a whole interaction a sibling carries is a divergence candidate. Where an element is named by a sentence but carries no behaviour clause at all, it stays out of the group until it has at least one behaviour to compare, so an empty member never manufactures one divergence per sibling behaviour.

5. **Fire the tight ask.** A divergence becomes a finding only when the signal is strong. Every finding names two concrete objects, each with the spec sentence it comes from, the shared role sentence, the divergence, the question "how alike should these behave?", and a recommended default. Where the grouping or the difference is not plain, the pass stays silent.

## The confidence read

Every design-review finding carries a confidence read of one of two values.

- **`confident`** — you would defend the grouping and the divergence on the spec text alone. A confident finding is written as a **recommendation**: a same-kind divergence over an undeclared grouping has no stated invariant behind it, so by the prover's own derivation [INV-140] it queues for a taste call and never blocks.
- **`likely`** — the deciding fact, whether the two are truly one kind, lives only in the human's intent. A likely finding is written as one **question to the human**, raised only when the signal clears the strong-signal bar below.

Below `likely`, silence — the same drop discipline the prover keeps.

## The echo channel

A likely finding rides the echo channel: one question to the human with both objects in hand. It fires only when the signal is strong, and all three conditions hold:

- the shared role fits **one plain sentence** with no stretch;
- the difference is a **whole behaviour** one member carries and the other lacks, rather than a parameter (a zoom that exists on one photo and on the other does not, beyond a "2x versus 4x" setting) — where the whole-behaviour-versus-parameter call is itself unclear, the finding is below the bar;
- **no spec sentence already decides** the difference. A written "the polaroid stays flat, by decision" kills the ask before it fires.

The question shows both objects each with its spec sentence, asks how alike the two should behave, and carries a recommended default. It rides the same batched-question path the pack already uses to bring a judgement to the human [INV-30, E-22, INV-4] — the same road the prover's own per-lens escalations travel. That default is not applied to the spec the way the pack's usual proceed-on-recommended arm would [INV-4]: the class sentence lands only on the human's word, while the lane never blocks, so the work does not stall on the open question. **At most three** such questions ride per pass, **strongest first**; a signal below the bar stays silent, so the channel is rare, high-value, and low-noise by construction.

An **unanswered** question is held on the dated record and is **not raised again** on its own until the human answers it, so a re-derived ask that matches an open recorded one does not re-fire as noise each pass [INV-130].

This channel carries exactly one producer for now — the same-kind divergence from the similarity lens above. A later producer would earn its own clause.

## How the answer closes the loop

The human's answer closes the loop through homes that already exist, so the design review invents no new enforcement law:

- **"Alike"** becomes a class-level clause written by spec-author naming the class and enumerating its members — precisely the form the cross-surface uniformity check demands [INV-125] — after which the prover's declared-class lenses and the render-time guardrail hold it mechanically forever. Where the class is surface-level, the author adds the registry rows by hand, keeping E-10's authorship law.
- **"Different, by intent"** becomes a decided spec sentence that closes the question for good [INV-59], and the ask never fires again.

So the pipeline is discovery (this pass) → declaration (spec-author) → enforcement (the prover's lenses and the guardrail), each stage in the skill that already owns it. Where the spec already declares the class, its uniformity check governs [INV-125]; the design review reaches only the groupings no clause has yet declared.

**The loop is bounded, and it never holds a landing [INV-154].** A confirmed grouping does not close the matter in one pass. Only one thing advances the loop: a human-accepted declaration. When the human accepts a class sentence [INV-125], or decides a difference as a decided sentence [INV-59], that declaration is a change to the spec, so it **re-enters the prove step**: the prover re-reads the changed part, and you re-read the elements the declaration re-partitions, together with any new element a prover fix introduced. One prover re-read followed by one design-review re-read is a round, and a round that produces a new class sentence or decided sentence is a **progressing round**. A round's other outputs stay where they are and do not advance the loop: a confident finding queues as a recommendation for a taste call, a likely finding rides as a question the human may answer later, and neither re-reads the spec on its own. When a round produces no new declaration, the loop rests in one of three ways, each named on the record. It **converges** when the design review ran and left no open question and no new grouping the human must still rule on — every grouping it proposes is already declared, already decided, or already standing as a queued recommendation from an earlier round, so a standing recommendation is a settled output that does not bar convergence, and the design is settled. It **waits** when the round's findings include a question the human has not yet answered; the held question resumes the loop when the human later answers it [INV-59]. It **stands down** when the design review did not run on this kind because no element a person acts on exists, recorded by name so the rest is not read as a settled design it never examined.

You count your own progressing rounds. Termination is not guaranteed — a declaration can re-partition existing elements into fresh candidate groupings, and a prover fix can add elements, so the count of undeclared groupings can rise as well as fall. Convergence is the ordinary case, and converge, wait, and stand-down are the three natural rests, reached when a round produces no new declaration. The cap is a separate, forced halt that keeps the loop live, not a fourth rest: it advances only on a progressing round, and it **forces a halt at three** progressing rounds by default (a host may set its own cap). On reaching the cap with no convergence, stop iterating and surface on the dated record the groupings still unsettled and your best reading of the cause among three: a declaration that spawns new elements or groupings faster than it resolves them, an oscillation between two mutually-exclusive groupings, or a spec whose requirements conflict so no consistent design exists — best-effort, since a spec's self-consistency is not decidable. Surfacing at the cap **holds no landing**: like every design-review finding it is a recommendation or a question, and the landing proceeds with the unsettled groupings recorded. The re-prove is triggered only by the human's accepted declaration, an ordinary spec edit; a design-review finding on its own never triggers it and never holds a landing.

**Cross-sibling propagation routes by declaration status, so the two passes share it cleanly.** A behaviour that should hold across siblings belongs to exactly one pass at any moment, decided by whether the group is declared. A declared class — or a kind-general rule already worded inside one member's own section, which the sharpened cross-surface lens now recognizes as a declaration in prose — is the prover's declared-class defect [INV-125]: a member the class does not cover, or a principle left scoped to one member while siblings exist, blocks there. A genuinely undeclared grouping, one no clause and no class-general sentence names anywhere, is this pass's own discovery [INV-141]: it proposes the group, checks parity, and echoes the strongest likely divergence as a question. A confirmed grouping then lands as a class clause and the property crosses to the prover. So the propagation is owned by the prover where it is declared and by this pass where it is not, with neither pass claiming it twice and neither dropping it [INV-150].

## The record

Each run writes a dated record at `docs/design-review/YYYY-MM-DD[-suffix].md` in the repo under review, the same shape and discipline as the prover's record; a second scoped run on the same day takes the `-suffix`, exactly as the prover record does, so two surface-add passes in one day never overwrite each other. It opens by naming the design-reviewer skill version that ran the pass, and it carries a **per-finding outcome** column with these values: `recommended` (a confident finding queued for a taste call), `asked` (a likely finding put to the human), `answered(+the decision)` (an ask the human resolved — alike, or different-by-intent), and `held` (an ask still unanswered, not to be re-raised on its own next pass). The dated record is the single home for an unanswered ask: where the decision archive references a held ask it points at this record rather than restating its state [E-22]. Every pass opens by reading the prior records' `held` asks, which is what lets it tell a still-open ask from a fresh one. This record is a member of the review-record class the spec declares once — the shared shape every review pass writes; the design-review record is the sibling that adds the `held` outcome, because it alone carries a question across passes (SPEC INV-156).

## When NOT to fire

- No finding is owed for every element or every group. Most pairs are plainly fine; say nothing about them.
- Where the grouping is not plain, or the divergence is not plain, or the whole-behaviour-versus-parameter call is unclear, the finding is below the bar — a silence or, at most, a confident recommendation, never an ask.
- Where a spec sentence already decides the difference, there is no finding at all.
- Where a governing class clause already exists and merely under-enumerates a member, that is the prover's declared-class defect path [INV-125], not this pass's recommendation path — route it there.
- Never file a defect, never hold a landing: the pass produces no blocking defects, only recommendations and questions.

> The pack, whole: **live-spec-base** holds the shared rules and defaults · **spec-author** writes the spec ·
> **product-prover** reviews it · **design-reviewer** judges the design behind it · **build-pipeline** ships the
> change · **test-author** derives the matrix and writes the tests · **communicator** makes the human exchange
> land · **feedback-intake** brings what comes back to its home · **feedback-collector** offers a rare private note up to the authors · **publish** sees the work out the door, owing
> its kind's checklist.
