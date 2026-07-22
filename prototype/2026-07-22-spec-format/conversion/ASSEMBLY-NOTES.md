# Assembly worklist — cross-unit items found during conversion and panels (2026-07-22)

Items the per-unit loops could not settle; each is owed at the assembly step.

1. **Source mis-anchor, E-12 vs E-20** (found by the build-loop-c converter): source line ~885 cites `[E-12]` for "the publish skill owns the per-kind checklist" while the Formal index homes that fact at `E-20`. The converted R47.1 carries `[E-12]` verbatim. At assembly: correct the anchor to `E-20` as a declared sharpen, recorded in the delta.
2. **One name: "spec-delta" vs "delta"** (build-loop-a defines "spec-delta"; when-something-breaks defines "delta" for the same thing). At assembly: pick "spec-delta" as the one name, rename in when-something-breaks, keep one pooled-glossary entry.
3. **"milestone" has no defining entry anywhere** — three units name it as carried (when-something-breaks, rules, part C) and part A points to the rhythm stretch, but no unit's glossary defines it. At assembly: the pooled glossary gets one entry, sourced from the rhythm requirements (part C's body).
4. **Rename note from part A converter**: source's "harness task list" rendered as "harness task panel" (the "task list" alias is registered to the queue in the one-name gate); "landing report" mapped to the carried "delivery report". Keep both renames consistent across the assembled document; record as declared sharpens.
5. **Carried-terms sentences diverge per unit** (each names a slightly different list). At assembly they collapse into the document preamble + one pooled glossary; the per-unit sentences disappear.
6. **Lane-open trigger reconciliation** (part B, reader finding): Req 44's spoken senior word vs Req 55's automatic graph verdict — the fixer resolves it per source; verify at assembly that the reconciled wording survived and matches INV-49's sharpened clause.
7. **Part C round-2 note**: Req 19's context says one member's net is the assertion shape while the criterion names three such members — align the count at assembly (non-blocking, caught by reader).
8. **Feature tags** (`[feature: F-...]`) carry no Formal-index rows; the generated code→location index must still resolve them (they map to scenario headings).
