# Prover review — row 445 spec-format delta (INV-250..271), stage-1 design pass

A fresh-seat formal review of the row-445 spec-delta (prototype/2026-07-22-spec-format/delta/spec-delta.md,
six requirements, 56 criteria) and its gates plan, run before any format gate landed as code. The reviewed
documents sit under prototype/; PRODUCT_SPEC.md itself carries no format change yet — the delta's clauses
land at the conversion delivery per its own arming rule (INV-270). This record satisfies the push gate's
dated-record requirement for today and records the pass verbatim in its findings.

## Pass — formal review of the delta against the current spec's machinery

Verdict: LANDS WITH FIXES — all fixes applied the same hour (delta v2, commit d1beea3), none open.

Code-space check: highest existing code INV-249; INV-250..271 unused, no collision.

Blockers found and resolved in v2:
1. The generated index versus the description field's one-home rule (INV-239): the criteria and the
   glossary are now the stated authored home of every code's plain statement; the generated index carries
   locations only; check-description-field.py retires at the conversion delivery with that stated
   successor (INV-271).
2. The bytes-per-criterion ratchet was scoped to PRODUCT_SPEC.md only; the flat byte bound
   (check-doc-bound.py, INV-234) stays in force for ROADMAP.md, TEST_MATRIX.md, JOURNAL.md (INV-264).
3. Arming order was unstated against a spec still in the old format: the whole spec converts in one
   delivery and every format gate arms in that same delivery, never before (INV-270).

Should-fix cluster, all resolved in v2: text-diff normalization defined (whitespace collapsed, italic
markers stripped, case-fold outside anchors — INV-261); sharpen-survival check pinned to a normalized
full-sentence match on the sharpened code's own line (INV-262); growth accounting excludes sharpen and
glossary bytes and a 500-byte per-new-criterion cap seeded from the pilot's measured average (INV-263);
ratchet seed defined as the value measured at the conversion-end freeze (INV-264); ratchet numerator is
criterion-line bytes only (INV-264); panel liveness bound — four rounds with fresh blocking findings
escalates to the human as a named question (INV-267); the delta record rides the single-pen serialization
and re-diffs against the post-merge freeze baseline (INV-198 composition); test_traceability.py moved to
the rebuild list; the index gate carries the empty-input guard (INV-218); the ratchet bound's home named
(guardrails/spec-ratchet.json).

A parallel cold read of the delta found one blocking term (a banned coinage in the delta's own text,
replaced by the defined term) and four note-level items, all fixed in v2.

## Stage-1 code landing covered by this record

The seven format gates and the index builder landed UNARMED as new files only (guardrails/specformat.py +
eight check scripts + scripts/build-index.py + four data files), each proven red on a synthetic break and
green on the approved sample and the pilot section, 59 new tests, full suite 1797 passed. Four criterion
halves are undecidable by script and are assigned to the cold-reader panel by name in each script's header
(criterion atomicity, invented GAP answers, the domain-noun converse, novel two-name drift).
