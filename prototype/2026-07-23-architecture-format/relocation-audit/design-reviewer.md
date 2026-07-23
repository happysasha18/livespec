# Relocation audit — node `design-reviewer` (owns-field prose)

Input: `prototype/2026-07-23-architecture-format/out/ARCHITECTURE.converted.md`, `### [node: design-reviewer]`.
Spec checked: `PRODUCT_SPEC.md` (anchors trail criteria as bracket codes; glossary consulted).

Note on the field. In the draft conversion the literal **owns** field (line 205) is bare — six
anchor codes, `INV-141, INV-142, INV-154, INV-156, INV-165, INV-169`, no trailing prose. Every
ownership-describing fragment for this node still sits in the **responsibility** field (line 202),
which the new format wants reduced to one sentence with the ownership notes carried onto the owned
anchors in the owns field. The fragments below are that ownership prose — the material the
relocation must place onto the owns anchors or drop for a spec citation. Each is attached to the one
anchor it describes.

| fragment (quoted; … past 40 words) | anchor | class | evidence |
|---|---|---|---|
| "reads a proven spec after the prover and judges the design behind it — builds its own element inventory, proposes the same-kind groupings no clause declared, checks behaviour parity within each group …" | INV-141 | DUPLICATE | SPEC R61.1 (l.1454): "the system *shall* have the design review read the same spec, build its own transient inventory of every element a person acts on that a spec sentence names"; parity in R61.2 (l.1455): "propose elements whose sentences match as a same-kind group, check each group for the same gestures, transitions, and affordances". |
| "every finding a recommendation or an ask, never a defect" | INV-142 | DUPLICATE | SPEC R69.1 (l.1605): "write a confident finding as a recommendation that queues and never blocks"; R69.2 (l.1606): "write a likely finding as one question to the human"; R61.3 (l.1459): "produce no blocking defects". |
| "owns the prover/design-review loop's round-count and cap — it counts its own progressing rounds, stops at three by default, and rests in one of three named ways (converge / wait / stand-down) …" | INV-154 | DUPLICATE | SPEC R70.4 (l.1635): "cap the loop at three progressing rounds by default, let a host set its own cap, and count progressing rounds on the design-review pass alone, resetting when a fresh pass opens"; three rests in R70.3 (l.1631): "it converges when … it waits when … and it stands down when …". |
| "owns the review-record class declaration — every review pass … writes a dated record of one shared shape, the verify-by-deed audit the one difference, landing its verdict in the landing record, keeping no dated file of the class" | INV-156 | DUPLICATE | SPEC R67.1 (l.1585): "have the prover, the design review, and the periodic audit each write a dated file of one shared shape under its own home"; R67.3 (l.1590): "land the verify-by-deed audit's verdict and its per-landing skill-creator review in the landing record, since verify is a per-landing gate and keeps no dated file of this class"; skill-creator walk in R (l.2820). |
| "(ROADMAP row 323)" | INV-156 | KEEP | ROADMAP-row pointer — stays in the architecture. |
| "this node holds the class because it reached the one-class reading from the record-sibling seam it already owns (design review → record), the class declared once here and cited by product-prover and build-pipeline without restatement" | INV-156 | KEEP | Ownership note (why the anchor sits at this node) plus a wiring note (product-prover and build-pipeline cite it without restatement); no spec rule restated. |
| "(added session 55, ROADMAP row 310 — node add re-proven, record `docs/prover/2026-07-14-design-review.md`)" | INV-141 (node add) | KEEP | Carries a ROADMAP-row pointer (row 310). The session number and record path are provenance the no-history law relocates to the journal, not architecture content. |

## Pins provenance

Pins field: `` `skills/design-reviewer/SKILL.md:1` `` (frontmatter + when it fires), and "the
similarity-lens, confidence-read, echo-channel, and record-discipline sections in the same file".

Pin labels carrying a date, a session number, or a landed-row provenance note: **none**. Both pins
are clean `file:line` (or in-file section) pointers with descriptive labels only.
