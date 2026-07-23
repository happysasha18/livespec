# Shared brief — rebuild an ARCHITECTURE node section under the new format (row 456 stage 2)

You are rebuilding one or more `### [node: <name>]` sections of the converted architecture document into
the new architecture format. This is a mechanical-with-care edit governed by an audit that already
classified every fragment. Do NOT invent, paraphrase, or summarize surviving text — keep it VERBATIM.
Halt and report if anything is ambiguous rather than guessing.

## Inputs you read

- The converted doc: `prototype/2026-07-23-architecture-format/out/ARCHITECTURE.converted.md` — find your
  assigned `### [node: <name>]` section(s). Each has three fields: **responsibility**, **owns**, **pins**.
- The per-node audit: `prototype/2026-07-23-architecture-format/relocation-audit/<node>.md` (the guardrails
  node has TWO: `guardrails-a.md` and `guardrails-b.md` — read both). The audit table classifies each
  owns-field fragment as KEEP, DUPLICATE, PARTIAL, or ABSENT, with the anchor it belongs to and evidence.
- The PARTIAL/ABSENT decisions: `prototype/2026-07-23-architecture-format/apply-decisions.md` — for any
  PARTIAL or ABSENT fragment in your node, do exactly what its row says.

## The transform, per node

The **owns** field is a sequence of anchors (`E-1`, `INV-227`, `INV-250..INV-265`, …), some trailing a
`(parenthetical)`. Rebuild it so:

1. **Every anchor stays**, in its original order. The anchor SET must not change (the suite checks it).
2. For each anchor, look at its parenthetical clauses and classify each by the audit:
   - **KEEP** clause → survives VERBATIM. Attach the single most load-bearing KEEP clause to the anchor as
     its one parenthetical: `INV-227 (…verbatim KEEP text…)`. INV-279 allows **at most one parenthetical
     per anchor**.
   - If an anchor has MORE THAN ONE KEEP clause, keep the primary one as the parenthetical and move the
     rest VERBATIM into the node's **notes** field (see below), each still naming its anchor, e.g.
     "INV-213: the browser-kill lesson of row 334." Never drop a KEEP word; never merge two KEEP clauses
     into a paraphrase.
   - **DUPLICATE** clause → REMOVE it. Its words live at the spec clause the audit's evidence cites; it is
     a named delta. Record it (see Output).
   - **PARTIAL / ABSENT** clause → do what `apply-decisions.md` says for that exact fragment:
     `RULE→spec` = remove it from owns and record it as a named delta (it moves to the spec, done by the
     lead — you only remove and record); `NOTE→arch` = keep it verbatim (as the parenthetical or in notes);
     `NOTE→pin` = move it into the **pins** field as a pin label; `DROP` = remove and record as a delta.
3. A bare anchor with no parenthetical, or one whose only clauses were all removed, is emitted bare:
   `INV-89, INV-90`.

The **responsibility** field: if it is one sentence naming what the node is for, keep it. If it carries
extra ownership/wiring prose beyond that one sentence (some nodes do), TRIM it to the one naming sentence
and move the extra VERBATIM into **notes**. A dated/historical phrase in responsibility is DROPPED and
recorded as a delta.

The **pins** field: keep every pin. DROP only a pin-LABEL's dated / session-number / landed-row provenance
phrase where the audit's pins-provenance list names it (record each as a delta); the `path:line` and the
functional label stay. Add any `NOTE→pin` fragment from step 2 as a new pin label.

The **notes** field is NEW and OPTIONAL: emit `**notes** — …` only if step 2 or the responsibility trim
gave it overflow. Keep overflow text verbatim.

## Output — return, per node, exactly two blocks

**REBUILT SECTION** — the full `### [node: <name>]` section markdown (heading, responsibility, owns, pins,
and notes if any), ready to paste. Keep the `[target]` mark on the heading if the original had it.

**NAMED DELTAS** — one line per removed fragment (every DUPLICATE, every DROP, every RULE→spec), quoted
VERBATIM and complete (do NOT truncate — copy the whole clause from the converted cell, not the audit's
40-word-truncated quote). Prefix each with its anchor and class, e.g.
`INV-245 DUPLICATE: "a core spec names no foreign project and tells no dated incident"`. These are the
words that legitimately leave the node; the lead's content-preservation proof adds them back and checks the
converted node content is reproduced exactly, so completeness and verbatim accuracy here are load-bearing.

Do not edit any file. Return the two blocks per node as your final message.
