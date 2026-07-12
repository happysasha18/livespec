# PENDING DRAFT — row 260, examined 2026-07-12 by an Opus drafter — STOP, not drafted
# LANDING ORDER for the batch was 257 → 258 → 260. Rows 257 and 258 are drafted (their files).
# Row 260 hits the STOP rule (bundle). No edits are proposed here; a split is recommended below.

---

# DELTA — Row 260 — STOP (bundle of two independent stories)

Row 260 ("Compaction is a scheduled station for code as well as docs, **and** an abstraction proves
itself by three questions") trips the STOP rule on the one-feature-one-story law (SPEC T-17), so I did
not draft it. Its headline joins two claims with "and", and they are two independently-shippable stories
with different primary homes, different triggers, and each its own likely invariant:

1. **The abstraction-fitness test — the three questions (P7).** Its home is build-pipeline's architecture
   step (the test a new or carved node passes before it lands) plus product-prover (which flags a node
   that fails it). It fires at **every node birth**, not only during a compaction pass — so it is not
   acceptance of the compaction story, it is its own behaviour with its own trigger.
2. **Compaction widened to code, as a scheduled station with a second trigger (P11).** Its home is the
   milestone-rhythm gate (SPEC line 699 doc-compaction clause + build-pipeline's "before a MINOR bump"
   gate). It states that duplicates merge, dead weight leaves with its listing (INV-109, reused), and the
   station now covers code, fired by the MINOR audit and by base rule 19's second occurrence.

The architect draft the row itself cites as working material
(`.live-spec/checkpoints/pending-design-principles-architect-draft.md`) already split exactly these into
**R4 (P7, abstraction fitness at the architecture step)** and **R6 (P11+P12, the scheduled compaction
station and its lock)** — two rows, in its own deep authorized pass. Row 260 re-bundles them under one
"small" size and one code. Two distinct new laws, two homes, two invariants: the split is owed.

P12 (the lock) mints no code either way — it is INV-98 / base rule 22 plus rows 216-218, cited never
restated (the row text already says "the convergence law, base rule from row 218, cited never restated;
row 217's audit covers the lock").

## Recommended split (so the orchestrator loses nothing)

- **Row 260a — abstraction fitness at the architecture step (P7).** Door: feature. Kind: skill. Homes:
  build-pipeline's architecture step (the three questions as the gate a new or carved node passes) +
  product-prover (extends the speculative-node flag: a node with one caller and no promised second is
  flagged). New invariant. **Code: INV-115 / M-254** (the codes this batch reserved for row 260 pass to
  its first-landing half). Land this FIRST — the compaction station's extraction gate cites it.
- **Row 260b — compaction is a scheduled station for code, with its second trigger (P11).** Door: feature.
  Kind: skill. Homes: the milestone-rhythm doc-compaction clause (SPEC line 699, widened to code) +
  build-pipeline's "before a MINOR bump" gate. Reuses INV-109 (removal listing) and cites P7's fitness
  test (now INV-115) as the extraction gate and INV-98/rows 216-218 as the lock. New invariant. **Code:
  the next free INV-116 / M-255** (verify free at its landing).

Both are `small`, both collide on the spec/matrix/version chain, so they run as one more drafter-applier
train after 257/258, landing order 260a → 260b.

## Why not fold (the judgment, said plainly)

The say-the-bar-back rider in row 258 folded into one law because it is the same incident's lesson about
the same gate's bar. Row 260 is the opposite case: the fitness test governs every architecture step
whether or not a compaction pass is running, so it has an independent life the compaction station does
not contain. Folding them would put four homes (spec milestone clause + build-pipeline MINOR gate +
build-pipeline architecture step + product-prover) under one "small" row and one code — which is what a
bundle looks like. The one-feature-one-story law splits it.

## Trigger, in one line

STOP: bundle. Row 260 carries two independent stories (abstraction fitness P7 · code compaction P11) that
the architect draft already split into R4 and R6; each owns a distinct home, trigger, and invariant.

---

## Numbering consequence

Because row 260 stops as one row and splits into two, INV-115/M-254 attach to the FITNESS half (260a) and
INV-116/M-255 (verify free at landing) to the COMPACTION half (260b). If the orchestrator instead keeps
row 260 whole and overrides this STOP, INV-115/M-254 is the single code and the four homes above are the
draft target — say the word and I draft it as one law, flagging the four-home reach.

---

SPLIT ACCEPTED + CLOSED 2026-07-12 (rows 260a/260b queued). ROADMAP row 260 replaced with two rows —
260a (abstraction fitness, P7, lands first) and 260b (code compaction with its second trigger, P11,
lands second, citing 260a's fitness test as its extraction gate) — exactly per the recommended split
above, five-cell format matching neighbors, both status `queued 2026-07-12`, both born-of pointing to
the six-principle wish and this architect draft. Anticipated codes (INV-115/M-254 for 260a,
INV-116/M-255 for 260b) carried in prose only, not minted — verified free at each row's own future
landing, per the row-231 reservation-lift precedent (codes consume in landing order). Pure bookkeeping,
no version bump (precedent: commit 30a62f9).
