# Prover record — ROADMAP 415: a decision recorded as the person's names its exchange (INV-207)

Date: 2026-07-17 · Doc version: v2.6.3 (unchanged; the version bumps once at the movement's MINOR gate) ·
Form: FULL (cross-cutting delta — a new cross-cutting law, a new guardrail gate, a new read-back surface,
and a tree-wide first sweep) · Mode: FULL over the new invariant with the architecture lens on the
owns-list edit, plus CROSS-LINK against INV-205 (the touchpoint frame the read-back rides) and INV-206
(the waiting-list surface it is kin to).

## Previous records clean

The prior record (docs/prover/2026-07-17-rows416-418-register-judge.md and the row-408 waiting-list
record) closed with zero unfolded must-fix rows after the adversarial-review corrections. No open finding
carried into this landing.

## The delta

INV-207, the writing rule on human authority, stated for any person and any host. Every claim in the
pack stands on a checkable artifact; a human's word is the one input with no artifact behind it, so the
one claim no agent, prover, or gate questions — and therefore the one slot a fabrication, once placed, is
never reached again. The row was born 2026-07-17 when a session recorded its own lane-ranking as the
person's decision and he recognised nothing on read-back. The rule: a sentence carrying human authority
names the exchange it came from (at minimum a date a reader can check); a sentence the pack reasoned out
is written in the pack's own voice and stays challengeable. An autonomy grant authorizes an agent to
DECIDE and the agent owns that judgment as its own. Two machines: the read-back surface `DECISIONS.md`
(the decision-set record, the read-back touchpoint the frame declares) shows the person what the pack
believes he decided so he strikes what he never said; the gate `guardrails/check-authority-anchor.py`
reads the decision set — in a declared `DECISION-RECORD` surface every live on-record entry carries its
date, a struck one skipped, an unanchored one reds.

## Phase checks (FULL)

- **Entities / states.** One new entity: the decision-set record (a `DECISION-RECORD` surface). Its two
  states per entry — on-record (must carry a date) and struck (retracted, skipped, kept with its note).
  The states are total: an entry is on-record or struck, and the struck marker (`STRUCK` / ~~…~~) is the
  only transition. No third state. PASS.

- **Transitions.** The one transition — the person striking a line — is his action on the shown surface;
  the machine maintains and shows the set, never strikes on its own. This matches the row's own boundary
  ("the 'he strikes' is his action; the machine maintains and shows the set"). PASS.

- **Invariants / safety.** The safety property is exact: no entry recorded as the person's stands without
  a checkable exchange. The gate enforces it structurally on the one surface where every entry is a
  decision claim by construction, so the property is total there and free of false positives. A struck
  entry is exempt because the person has already reached in and struck it — the retraction is itself the
  fix, so exempting it is not a hole. PASS.

- **The gate has teeth (not a check that looks at nothing).** The gate reds a real violation: the
  fabricated lane-ranking fixture reds (record-unanchored.md), a bare unanchored prose claim reds
  (prose-unanchored.txt). It is not a check that looks at nothing — red-first proof captured in
  docs/prover/red-proof-2026-07-17-row415.txt. PASS.

- **False-positive discipline (the row's explicit risk).** The first sweep exposed the real hazard: in
  free spec prose, "his word" / "the owner's word" are overwhelmingly the pack's own RULE language
  ("the owner's word decides", "blocked on his word") — the law's own challengeable side, correctly
  needing no anchor — while every genuine attribution already carries its date. So the STANDING scan is
  narrowed to the `DECISION-RECORD` surface, where context is fixed and the anchor rule is unambiguous;
  free prose gets the one-time sweep only. The abstract-role forms ("the human's", "the person's",
  "the reader's", "one") are exempted from detection entirely, since they never name a definite
  individual's recorded decision. The gate does not over-red a legitimate dated attribution (they carry
  their date and pass) and it does red the fabricated ranking. PASS.

## Cross-link checks

- **Rides the touchpoint frame, does not re-open it [INV-205].** The read-back surface declares
  `TOUCHPOINT-KIND: decision-readback`, added to the manifest as asynchronous and person-opened —
  the same kind as the waiting list. `check-touchpoint-kind.py` scans it green: it carries only the
  wait and teach markers a person-opened asynchronous point affords, and no interrupt. The read-back's
  cadence and surface ride the frame; the row states this and the manifest realizes it. PASS.

- **Kin of the waiting list [INV-206].** The row states "the list itself rides the waiting list". The
  read-back surface is a small file at the host root that the person opens on request and reads on his
  own clock, rendered through the same `scripts/render-doc.py` — structurally the waiting list's sibling.
  Both are asynchronous person-opened touchpoints. No conflict. PASS.

- **No collision with the impersonal-shipped-language law [INV-120].** DECISIONS.md is a host-local
  operational record (it names the host's own person), kin of NEXT_STEPS.md, so it is added to
  check-shipped-language's excluded set; the shipped TEMPLATE (templates/DECISIONS.template.md) is
  name-free. The gate's own code names no person — the roster lives in authority-anchor.json as data
  (the shipped-language allowlist's rule), and the gate + its config join the detector self-exclusion
  set. Shipped-language stays green. PASS.

- **Architecture lens (six checks) on the owns-list edit.** INV-207's anchor lands on exactly one node
  (guardrails), pinned to `check-authority-anchor.py:1`, `authority-anchor.json:1`, `DECISIONS.md:1`,
  and `templates/DECISIONS.template.md:1` (traceability suite green — every anchor owned once). No new
  node (the gate joins the existing guardrails family beside check-board and check-touchpoint-kind).
  No new seam (the gate reads a file, an internal read). No new quality budget (a boolean-presence
  check read by the suite). Placement: a build-time check on the author's machine plus a rendered file
  the person opens. PASS.

## The first sweep (the row's first act)

Ran the gate over the spec, the base rulebook, and the active roadmap. Findings: 31 (spec) + 4 (base
rulebook) + 84 (roadmap) sentence-level flags. Triage: every one is either the pack's own rule language
referencing the person's authority as a policy category (correctly the pack's own voice, no anchor
owed), a dated attribution whose date wraps to an adjacent physical line (already anchored — e.g. base
rulebook "the owner's decision (recorded 2026-07-16)"), or noun-sense noise ("landing order", "decision
page"). Every one of the 84 roadmap hit-rows carries a date somewhere in its row (0 rows without a
date), so every reference is row-anchored. ZERO genuine unanchored owner-attributions were found: every
specific-decision record in the tree already carries its date. Nothing to fix, nothing unresolved to
list. The sweep confirms the tree is clean of the incident's defect, whose only durable home — the
decision-set record — is now guarded.

## Red-first proof

Captured in docs/prover/red-proof-2026-07-17-row415.txt: all 20 tests red against the pre-delta tree
(gate + config + surface + template absent; spec/index/architecture/matrix carry no INV-207; pre-push
unwired), green after. The three named red-proofs: the fabricated lane-ranking reds unanchored, passes
once struck; a genuine dated attribution passes; the pack's own rule language passes.

## Verdict

HOLDS. Zero must-fix. The law composes with INV-205 (rides the frame) and INV-206 (kin of the waiting
list); the gate has teeth; the false-positive risk the row named is met by scoping the standing gate to
the decision-record surface and exempting abstract-role rule language. Open ⟨DECIDE⟩ touched by the
change: none.

## Note for the orchestrator (out of this row's narrow scope)

The CI mirror `.github/workflows/gates.yml` is behind the local pre-push: it lists gates through o
(cleanup-notice) but not p (touchpoint-kind) or q (waiting-list) from the prior two rows. This landing
added gate r there beside gate o for its own completeness; the missing p/q are a pre-existing mirror gap,
flagged here rather than fixed, to keep this commit's diff to row 415's delta.
