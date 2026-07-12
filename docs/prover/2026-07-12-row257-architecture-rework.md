# Prover — row 257, the architecture redesign owes rework law (2026-07-12, short form per INV-61)

Small delta (kind: skill; architecture = new invariant, owner node build-pipeline).

- **Previous records:** 2026-07-12-row247-inbox-remote-arm.md clean (0 must-fix); no unfolded rows.
- **The delta in one line:** when structure is deliberately redesigned — layers restacked, a surface's
  ownership moved, nodes merged or split — the architecture document is re-shaped to the new form and
  re-proven with the architecture lens in the same movement; updating the pins alone is scoped to a
  boundary shift that leaves the document's shape standing, since after a real redesign the old shape
  itself lies and fresh pins on a stale shape are a defect — spec clause (INV-113 + index), the
  build-pipeline re-carve paragraph, the build-pipeline refactor line, M-252, two string tests plus
  the spec-anchor/index test, red-proven against the pre-delta tree. Composition read: no clash with
  the re-carve routing (INV-37, E-14) — that law carries a redesign as its own queue row; this states
  what the row owes the document once it lands. Born of the tlvphotos second-finger redesign
  (2026-07-11 ~23:11): a UI-layer rethink was ordered and the pack forced only a pins update, not a
  re-shaping.
- **Architecture gap caught, not drafted around:** the draft (257.7) stated ARCHITECTURE.md is not
  edited by this row. The traceability suite disagreed: every Formal-index anchor must be owned by
  exactly one ARCHITECTURE.md node, and INV-113's own matrix row sits in the `[node: build-pipeline]`
  block. The applier's first pass hit this as unpredicted red and STOPPED per house rule rather than
  silently expanding the write-set. The orchestrator's call: the draft omitted the owning-node edit;
  the row's own map already names build-pipeline as the owner ("Owner node = build-pipeline — it owns
  the architecture step and the refactor door"), and the fix is the precedented one-line addition
  (row 233 carried the same kind of ARCHITECTURE.md edit for INV-109) — INV-113 added to
  ARCHITECTURE.md:43's build-pipeline Owns column, pin `:215` (the re-carve paragraph) added alongside.
  Suite green after the addition: 418 passed.
- **Verdict:** ready to ship — 0 must-fix, 0 should-clarify.
