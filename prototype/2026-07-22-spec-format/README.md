# Prototype: one home per rule

This prototype shows a new Formal-index format for PRODUCT_SPEC.md, where each rule lives in one place instead of being stated three times. Today every rule appears as body scenario prose, as an accreted index anchor line, and as a one-sentence index Description; the worst anchor line wraps 1,653 bytes of dates, provenance, and cross-reference narrative around a 305-byte rule. The new index keeps one row per code carrying the Description sentence verbatim plus a bare `related:` list, and the anchor line's provenance moves to a journal export.

## File map

- **Index slice.** `before-index.md` is 12 contiguous index rows verbatim, including INV-128 (the worst accretion). `after-index.md` is those rows in the new format. `journal-export.md` is the provenance harvested out of their anchor lines, verbatim, under a heading per code.
- **Body slice.** `before-body.md` is the intake subsection verbatim. `after-body.md` is a phase-2 sample of the same subsection.
- **Numbers and proof.** `NUMBERS.md` holds the byte counts, the full-file projection, and the three verification results. `COMPARE.html` is a rendered side-by-side page.

## The two-phase migration

Phase 1 is mechanical and lossless: for every index row, keep the Description sentence byte-for-byte, harvest the cross-reference codes into a `related:` list, and move the rest of the anchor line into JOURNAL.md. Phase 2 is a judgment pass over body prose, run per section under the freeze equivalence check, that tightens each scenario by dropping sentences which only restate an index rule already carried by its code cite while keeping every behavioural fact and every code cite. Phase 1 alone projects the file from 783,678 to about 622,986 bytes, and phase 1 plus phase 2 to about 530,715 bytes. Phase 1 can land first because it changes no meaning, and phase 2 follows section by section behind the equivalence gate.
