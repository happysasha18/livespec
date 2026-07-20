# Skill review — spec-author (the INV-244 axes-from-kind clause)

`SKILL-REVIEW`

Skill: spec-author
Date: 2026-07-20
Reviewer: skill-creator (Anthropic) — run from a clean context per INV-237/INV-208

Verdict: passes — the added clause matches spec-author's register and structure, points to its
homes in the architecture rather than duplicating them, cites only anchors that resolve, states
what INV-244 and the architecture actually claim, and leaves the description frontmatter unchanged
so no triggering surface moved. Body reviewed; description reviewed.

## What changed

The v3.2.0 landing (commit a46f76c) makes one additive edit to `skills/spec-author/SKILL.md` and
bumps two version stamps. The added clause sits in the facet-sweep section and tells the author to
read a surface's composition axes from the project kind before composing, beyond the kind-independent
C-1 floor, homing the per-kind axis set in the axis table in ARCHITECTURE.md and on the host
profile's `project.axes` line. It reads as the third of three parallel bold-led paragraphs: the
declared-layers read (INV-135), the declared-design-principles read (INV-136), and now the
declared-axes read (INV-244). The two stamps — the metadata version 3.1.0 to 3.2.0 and the
base-skill reference v3.1.0 to v3.2.0 in the pack note — are the machine-written frontmatter that
`scripts/stamp-versions.py` owns and that INV-208 carves out of the review duty.

## How this review was run

Run from a clean context, a fresh reviewer forming its own read of the diff, the surrounding
facet-sweep section, spec INV-244 in both its body and formal-index forms, the C-1 canonical-axes
formal row, and the axis table in ARCHITECTURE.md. The read was adversarial: the hunt was for a
dropped or overreaching claim, a citation that dangles, a duplicated fact that should have been a
pointer, and a moved trigger. This dogfoods the clean-context review rule the skill-review gate
enforces (INV-237, INV-208).

## Findings

- **Register and structure fit (clean).** The clause opens "Read the surface's composition axes from
  the kind too (SPEC INV-244)", the same bold-imperative shape as its two neighbours — INV-135's
  "Read the project's declared layers, do not assume code" and INV-136's "Read the kind's declared
  design principles too". It reuses their framing, reading the axes from the kind "the same way it
  reads the declared layers", so the three paragraphs read as one family. Plain words, anchors
  trailing. The fit holds.

- **One home per fact — points rather than duplicates (clean).** The clause carries the authoring
  duty and points to the two homes — the per-kind axis table in ARCHITECTURE.md and the host
  profile's `project.axes` line — rather than restating the axis lists. The full model lives in spec
  INV-244 and the architecture table; the skill body cites them and copies no axis-table content,
  mirroring how the INV-135 and INV-136 paragraphs beside it point to their own tables.

- **Claims match the spec and the architecture (accurate).** "A project kind owes every surface a
  further axis set beyond the kind-independent C-1 floor" matches INV-244 ("a surface's composition
  axes are the C-1 floor plus the further axes its project's kind owes"). "The composition axes a
  surface answers because its kind renders under them" reproduces the architecture's axis-section
  sentence almost word for word. "Reads these declared axes from the kind before folding the facet
  sweep below, the same way it reads the declared layers" matches the architecture's "reads its axes
  from the kind the way it already reads the declared layers". The mandatory-declaration-with-an-empty-escape
  shape matches INV-244's "a kind may name none beyond the floor as an explicit stated decision".

- **Anchors resolve (all real).** SPEC INV-244 is present in PRODUCT_SPEC.md, both as a body clause
  and as a formal-index row. The C-1 floor is the canonical-axes formal row and the kind-independent
  floor the architecture names. The per-kind axis table is the "Composition axes by project.kind"
  section of ARCHITECTURE.md, heading plus a project.kind table. The host profile's `project.axes`
  line is the field the architecture names as the declaration site and reds when absent. No citation
  dangles.

- **Trigger surface unchanged — no trigger moved (clean).** The diff touches only the metadata
  version line, the base-skill version reference in the pack note, and the added clause. The
  `description:` frontmatter is byte-for-byte identical to the pre-change file, so the triggering
  surface did not move and no eval drift is expected.

- **Empty-case scope — a precision note (accepted, non-blocking).** The clause attaches the
  legitimate "none beyond the C-1 floor" answer to "a kind with no visitor-facing surface". INV-244
  legitimises the empty declaration in the same terms ("the empty case ... legitimises for a kind
  with no visual surface"), so the clause is faithful to the spec's own sentence. The spec carries a
  deeper point the skill body leaves out: the non-visual backend kind owes a load, version, and
  tenant axis set of its own, so an empty answer is substantively wrong for that particular kind even
  while an explicit "none" stays a permitted declaration form. The clause points to INV-244 and the
  table where that fuller model lives, so an author following the pointer reaches it, and carrying the
  whole disproof into the skill body would duplicate the spec. Accepted as within the clause's
  altitude.

- **Additive only, no neighbour disturbed (clean).** The hunk is a pure insertion between the INV-136
  paragraph and the viewport-bands bullet. No adjacent sentence changed, so no prior fact was silently
  reworded under cover of the addition.

- **Version stamps (exempt).** The 3.1.0 to 3.2.0 metadata bump and the v3.1.0 to v3.2.0 base
  reference are the stamp carve-out INV-208 names; they carry no review duty and rode along with the
  clause.
