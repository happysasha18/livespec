# Whole-document prover pass — SPEC.md v0.15.61 (2026-07-08, session 26)

**Mode:** FULL — the whole document, read end to end (959 lines), after the humanize movement closed all
18 scenario sections and after today's two decision edits. Run to certify the register consolidation and to
clear the M-6 pre-push prover-record gate.

**TRIAGE: PROCEED** — a mature, shipped-and-target product spec with a full Formal index and an owning
architecture doc; analyzable, and its facts are pinned (ARCHITECTURE.md node table + M-7 version homes).

## Opening assessment

SPEC.md describes the live-spec pack: a wish walks one proven pipeline from intake to a tested landing,
with the human pulled in only for the calls that are genuinely theirs. After the humanize movement the whole
document now reads in one technical-writer voice — scenarios lead, short codes trail as quiet anchors, the
Formal index closes it. The two things I came to check both hold: today's decision edits are clean, and the
consolidation introduced no structural drift. This was a register movement over a document already proven
section by section (per-section cross-links under docs/prover/), so this pass is a whole-document
composition and consistency check, not a from-scratch re-derivation of the model — I say that plainly rather
than imply a fresh proof. One worth-considering item stands, and it is a known open field leg, not a hole.
Confidence: ready to build / ready to push once the gate is green.

## The two decision edits — validated

**DEC-1 — the feature-map bold lead (SPEC L309).** The old lead carried a scissors construction
("transparency is a command, not archaeology") and the Russian trigger «покажи все фичи» in the prose. His
decision was the full English gate. The lead now reads:

> "Ask \"show all features\" and a single answer hands you the whole product map, current as of that moment." — Section: Asking what the product does

Checked: the scissors is gone from all three functional homes (this prose, the tested needle in
`test_traceability.py`, the communicator echo at SKILL.md rule 14); the tested needle moved to a real
substring of the new lead ("hands you the whole product map"); «покажи все фичи» survives only where it is
his real trigger phrase (the skill's description/when-it-fires metadata) and in history/matrix. The rest of
the section (L310–313) and the Formal-index line INV-38 (L893) already describe the mechanics without the
old phrasing, so no cross-reference dangles. Consistent.

**DEC-2 — ARCHITECTURE.md assignment-history log.** Outside this SPEC pass (separate doc), but noted for the
record: the ~90-line inline log migrated verbatim to JOURNAL, the intro register-cleaned, 169 → 90 lines.
Verified before the cut that every ARCHITECTURE test reads only the Nodes/Seams sections, so the anchor set,
the pins, and pin-drift are unchanged.

## Composition & consistency scan (whole document)

- **Anchor ↔ index integrity:** every anchor cited in the prose resolves to a Formal-index row and an owning
  architecture node (mechanized by `test_architecture_owns_every_anchor_once`, green). No orphan, no
  double-owner surfaced by eye either.
- **One voice:** the 18 sections read as one register. The three "— not" occurrences (L199 "version
  comparison — not this time", L313 "per-feature history timeline — not this time", L572 "SUBSTANTIVE — not
  a stub") are non-goal labels and a definitional gloss, not the banned define-by-negation scissors. Clean.
- **Seam laws compose:** the passport (INV-51), away-stretch accumulation (INV-52), seat-matched channel
  (INV-67), and unmissable end (INV-57) form a consistent showing-cadence family with no contradiction —
  each names one home (communicator) and defers to the next by citation, not restatement.
- **No new dead-end / entry-symmetry / unbacked-surface gap** was introduced by the humanize; the
  register rewrites changed wording, not state or transition structure.

## Findings

Only one item rises above taste, and it is a known open leg rather than a defect.

**F1 — The seat-detection law states an active behaviour whose real-remote proof is still an open field leg.**

> "The session reads its seat from what it can actually reach — the platform, the display, whose filesystem — and names the channel it picked." — Section: Throwing a wish, INV-67

The clause states seat detection as settled law, and the build legs did land (INV-67, communicator rule 5,
`test_showing_seat`). But no run has yet exercised a real cloud-seated session, so whether a remote session
actually detects "I am remote" and picks the right channel is asserted, not observed. A remotely-seated
reader handed a local file path would meet exactly the defect the clause warns against, and nothing today
proves that cannot happen. This is not a spec hole — the law is correctly stated and its field leg is
tracked (ROADMAP row 168, sharpened today with the human's 2026-07-08 re-raise: "does a session actually
know it is remote, and how do we communicate then?"). Action: keep it as the open field leg it is; the first
real cloud-seated session is its proof, and no spec or code change is owed now.

`worth-considering · unenforceable-until-proven (discharge)`

## Coverage note

The three coverage tables (CRUD / invariants-per-state / authorization) are N/A as a block: live-spec is a
documentation-and-skills product with no user-mutated persistent entities and no multi-role authorization —
its "state" is the queue/spec/journal under the one-pen serialization law (INV-2/INV-11), already covered by
the suite. A table of N/A rows would be ritual noise.

## Folds applied by this pass

None — no must-fix or should-clarify finding surfaced that required a text change. The two edits under review
were applied before the pass (DEC-1/DEC-2, his decisions this session) and are validated above, not folds of
this pass. F1 is a worth-considering item already owned by ROADMAP row 168; it triggers no fold and stays
LOCAL (no wider re-trigger of the M-6 gate).

## Readiness

Ready to push once the gate is green. The document is internally consistent, reads in one voice, and carries
no unresolved must-fix. Suite context at this pass: 174/175, the single red being this very gate demanding a
today-dated record — which this file supplies.

---

## Short-form addendum — Open-decisions compaction (same session, INV-61 small-delta form)

A milestone prose-only delta after the pass above: the SPEC "Open decisions" section had four already-decided
items (D-2/D-3/D-4/D-5) collapsed to one-line resolved pointers, their dated rationale moved to JOURNAL. No
new surface, no structure change — three-line short-form record:

- **Previous records clean** — the whole-doc pass above found no must-fix; this delta touches only the
  Open-decisions section.
- **The delta** — D-2/D-3/D-4/D-5 verbose bullets → one-line pointers, each KEEPING its anchor (anchors are
  cited elsewhere and guarded by the anchor-set test); D-1 stays open; rationale preserved verbatim in the
  JOURNAL session-26 entry.
- **Verdict** — clean. Anchor set unchanged (test_architecture_owns + index tests green), the tested D-3
  close-needle "Decided 2026-07-07 (row 55)" and the D-2 forbidden-open-string constraints both hold. The
  fold stays LOCAL to the Open-decisions section, so it does not re-trigger the gate.

---

## Short-form addendum — INV-70 parameter-default law (row 172, CROSS-LINK)

A new invariant added after the milestone, from Alexander's tlvphoto conversation handed to the pack as a
general rule (2026-07-08). Small delta, no new node/seam (assigned to build-pipeline). Three-line record:

- **Previous records clean** — this delta adds one invariant and its elaboration; it touches the "Throwing
  a wish" scenario, the Formal index, ARCHITECTURE (assignment only), the matrix, and build-pipeline.
- **The delta** — INV-70: a tunable parameter (resolution, batch size, timeout, sampling rate) is set by the
  agent to a sensible default and TOLD with its `[default]` tag, never asked; carried to build-pipeline's
  landing-report step; the human tunes it later at most; and where the human GRANTS it, the agent pushes to
  prod on its own certification when sound.
- **Seams checked** — composes cleanly: it is the taste-told law [INV-31] extended to numeric/config knobs
  (same TELL, no new confirmation path), the same idea the economy ladder applies to cost [T-19], and rests
  on the ask-only-real-questions rule [INV-4]. The push-autonomy clause is framed as a TRUST the human
  grants and can withdraw [INV-9], resolving the same way live-spec's own push gate already does [M-6] — no
  contradiction with INV-9's "human owns the push gate" (the grant is the human's word). Verdict: clean,
  red-first test `test_parameter_default` (M-176) proven red on the missing skill elaboration then green.

---

## Short-form addendum — INV-28 pre-show lint arm (row 170, INV-61 small-delta form)

A prose-only delta: INV-28 gained a sentence naming its mechanical PRE-SHOW arm (`scripts/preshow-lint.py`),
its Formal-index line updated to match, plus the communicator pre-report walk's step 3 and matrix M-177.

- **Previous records clean** — this delta adds the mechanical arm of an EXISTING law (INV-28), no new
  invariant; it touches the INV-28 clause, its index line, communicator, and the matrix.
- **The delta** — the lint reads a human-facing artifact's prose and flags a line that OPENS with an
  internal handle (spec code / row / session number) before showing; a warning to clear, never a silent
  rewrite; scans the shown surface only, so the spec's own trailing anchors stay legal.
- **Verdict** — clean, and same shape as INV-24's clock hook (a mechanical arm enforcing a stated chat law,
  the skill staying the law's home). Red-first proven: `test_leading_handle_goes_red` flags real leaks,
  `test_outcome_led_and_trailing_anchor_pass` keeps clean text green. Stays LOCAL to INV-28.

---

## Short-form addendum — INV-71 live status in any seat (row 166, INV-61 small-delta form)

A new invariant, from Alexander's live board asks (2026-07-08): the harness task list/spinner is
local-only (absent in a browser) and intermittent (dark through long tool runs), so the live "where are we
now / what's next" cannot live there. Owned by communicator; small delta, no new node/seam.

- **Previous records clean** — adds one invariant + its rule; touches the "Throwing a wish" showing-cadence
  family, the index, ARCHITECTURE (assignment only), the matrix, and communicator's narration rule.
- **The delta** — INV-71: a short NOW (work in hand + station) and NEXT status kept current in the CHAT (the
  one surface every seat shows, INV-67), refreshed at each station change with a heartbeat on a long stretch
  (INV-35); the harness list is a courtesy kept plain-worded (INV-28), never the status's home; a rendered
  page is the local seat's optional view; binds for every project live-spec runs.
- **Seams checked** — composes with INV-35 (narration/heartbeat, now with an always-answerable NOW/NEXT),
  INV-67 (chat as the cross-seat surface), and rule 6's task-list-plain-words point (INV-28) with no
  contradiction — INV-71 says the task list is not the status's HOME, rule 6 says when shown it stays plain.
  Red-first test `test_live_status` (M-178). Clean, stays LOCAL to the showing-cadence family.
