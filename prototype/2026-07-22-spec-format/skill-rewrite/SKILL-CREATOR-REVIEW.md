# Skill-creator review — eleven pack skills (pre-push, 2026-07-23)

Frame: skill-creator's review method (trigger-description quality, sibling boundaries, structure/size,
register spot-check). Reviewed against the pack's own law (register rewrite tonight + spec-author content
update + new text-audit). Read: all eleven `skills/*/SKILL.md` in full. All cited script/guardrail/template/
doc paths were checked on disk.

Severity key: BLOCKER (wrong/broken, fix before push) · RECOMMEND (queue row) · NOTE.

---

## BLOCKER list (verbatim)

**B1 — live-spec-base still says "nine working skills" and omits text-audit from every enumeration, while its
own footer includes it (internal contradiction in the normative rulebook).**
The pack now has ten working skills beside the base (spec-author, product-prover, design-reviewer,
build-pipeline, test-author, communicator, feedback-intake, feedback-collector, publish, text-audit). The
base was not updated when text-audit landed tonight:
- line 8 title: `# live-spec-base — one rulebook, nine working skills` — should be "ten".
- description (line 3): `Load it whenever a pack skill (spec-author, product-prover, design-reviewer,
  build-pipeline, test-author, communicator, feedback-intake, feedback-collector, publish) is in use` — nine
  members, text-audit missing.
- intro (line 11): the same nine-member list, text-audit missing.
- but the footer roster (line 553) DOES list text-audit.
So the single normative file that names the pack's membership both undercounts it and contradicts itself.
This is base rule 9 (docs travel with the change) broken on the base by the change that added text-audit.
Fix: change "nine"→"ten" and add `text-audit` to the two enumerations (description + intro).

(No other BLOCKERs found.)

---

## Per-skill verdicts (one line each)

- **live-spec-base** — SHIP AFTER B1. Rulebook is coherent and the footer is correct; only the header/
  description/intro miscount (B1). Large (553 lines, 34 rules) but that is its job as the single home.
- **spec-author** — SHIP with a queue row. Trigger + boundaries excellent; largest body (676 lines) and its
  comprehension-gate section now duplicates text-audit's cold-reader loop instead of pointing at it (R1).
- **product-prover** — SHIP with a queue row. Trigger clean; the three-review boundary is well-drawn toward
  design-reviewer but the "When NOT to use" prose/readability hand-off never names text-audit (R1).
- **design-reviewer** — SHIP. Trigger and the prover boundary are the sharpest in the pack; every finding is
  a recommendation/question by construction, so it can never mis-gate. No defect found.
- **build-pipeline** — SHIP. Strong orchestration description; body invokes design-reviewer at step 2 but the
  description's orchestration list omits it (N1). References used well (7 tables pushed to references/).
- **test-author** — SHIP. Trigger correctly routes bare "write tests for X" to build-pipeline first; kind-
  abstract ladder is clean. No defect.
- **communicator** — SHIP with a queue row. Trigger has a thoughtful "NOT a reason to LOAD it" clause; its
  pre-report clean-reader step now duplicates text-audit's loop rather than referencing it (R1).
- **feedback-intake** — SHIP. Clean in/out boundary vs communicator and vs feedback-collector; routing table
  is gap-free. Roster-merge question with feedback-collector noted below.
- **feedback-collector** — SHIP. Deliberately narrow, off-by-default, consent-gated; boundary vs
  feedback-intake explicit. Roster-merge question noted below.
- **publish** — SHIP. Trigger enumerates every edge-crossing case; boundary vs communicator (leave-machine vs
  in-session) clean. Kind checklist is a single-home table. No defect.
- **text-audit** — SHIP with a queue row. Internally excellent and register-clean; but it is wired into the
  pack one-directionally — no sibling body hands off to it (R1), and the base omits it (B1).

---

## RECOMMEND

**R1 — text-audit is integrated one-directionally; its siblings neither hand off to it nor stop restating its
loop.** text-audit was extracted tonight to be the one home of the cold-reader comprehension loop, and it
correctly points at product-prover and communicator. The reverse links are missing:
- product-prover "When NOT to use" sends "style or wording critique / grading finished prose" nowhere; it
  should name text-audit as the home for "will a stranger understand this," the mirror of text-audit's own
  boundary sentence. (product-prover contains zero mentions of text-audit.)
- spec-author's comprehension-gate section (mechanical lints → fresh cold readers → two-consecutive-clean)
  and communicator's pre-report clean-reader step both fully RESTATE the loop text-audit now packages. By the
  base's own opening ("a second full statement of a shared rule inside a working skill is drift, a defect to
  fold at the next milestone") these should become pointers to text-audit. The base defers duplication-fold
  to a milestone, so this is a queue row rather than a blocker — but it is the exact drift the base warns of,
  introduced by tonight's new skill. Repoint both, and add the product-prover hand-off, in the same landing
  that fixes B1 so text-audit's boundaries are gap-free from both sides.

**R2 — size: spec-author (676 lines) is the one body meaningfully over the ~500-line ideal with everything
inline.** build-pipeline (545) and base (553) run long too but push tables to references/ and read as single
coherent methods. spec-author could move the facet sweep or the compose-across-axes section to references/
the way build-pipeline moved its tables. Low priority; not blocking.

---

## NOTE

**N1 — build-pipeline's description orchestration list `(spec-author, product-prover, test-author)` omits
design-reviewer,** which the body invokes at step 2. Add it for completeness of the example list.

**N2 — `docs/deltas/` directory does not exist** though spec-author cites it as the home for per-delivery
delta records and `guardrails/check-delta-record.py` exists. This is an output dir created on first use, not
skill infrastructure, so not a defect — noted only so it is not mistaken for a dead pointer.

**N3 — register spot-check is clean for the bar that applies.** Three sampled reader-facing sections
(text-audit "The register it holds a text to", product-prover "Communication principles", communicator rule
6) read positive and plain with no marketing voice, no significance inflation, no leftover contrast-by-denial
frames. Skill BODIES use pervasive ALL-CAPS emphasis and compressed "X, never Y" phrasing, but that is
agent-instruction register (product-prover states it explicitly: "these instructions use caps for emphasis to
YOU; do not echo that style"), not the shipped-prose bar the scissors linter enforces. No register leftovers
to flag.

**N4 — all cited paths resolve.** Every guardrail/script/template/doc referenced across the eleven skills
exists on disk (spot-checked ~30 paths: the guardrails suite, scripts/preshow-*.py, spec-*.py,
build-index.py, templates/*.template.md + headless_harness.py, docs/lenses.md, docs/spec-format.md,
docs/spec-style.md, docs/prose-quality-gate-design.md, tests/test_interface_coverage.py,
tests/test_derived_doc_header_policy.py). Frontmatter versions all 4.0.0, matching VERSION and the base.

---

## Roster verdict — is eleven the right cut?

**Yes, eleven is essentially right; nothing is begging to split.** The three-way document-review split
(product-prover "does it hold together" · design-reviewer "is the design right" · text-audit "will a stranger
understand it") is genuinely three different failures on one page, each cross-referenced, and each earns its
seat. build-pipeline/spec-author/base run long but are single coherent methods, not merge-or-split
candidates.

**The one real roster question is feedback-intake + feedback-collector.** They are the two smallest bodies
(98 and 137 lines), both about feedback, opposite directions. A reasonable person could fold them into one
"feedback" skill with an inbound arm and an outbound arm. Recommendation: **keep them split.** Their TRIGGERS
are genuinely different — intake fires on anything handed in (always on); collector fires only on an
unmistakable strong reaction AND a host flag (off by default). Collector is a consent-gated outbound move
about a real person; isolating it from the always-on inbound router keeps that gate from ever leaking into
routine intake. The split costs two small files and a triggering surface that must disambiguate
"received-from-the-person" vs "observed-strong-moment," and both descriptions already draw that line cleanly.
The cost is worth the isolation. Flagging it because the owner asked explicitly, not because it needs
changing.

**text-audit earns its place** provided R1 lands — otherwise it is a fourth statement of a loop that already
lives in spec-author and communicator, rather than their shared home.

---

## Fix landing — B1, R1, N1 applied (2026-07-23)

Write set: `skills/live-spec-base/SKILL.md`, `skills/spec-author/SKILL.md`, `skills/communicator/SKILL.md`,
`skills/product-prover/SKILL.md`, `skills/build-pipeline/SKILL.md` (frontmatter only). No commits, no test edits.

**Per-fix one-liners:**

- **B1 (live-spec-base)** — title line 8 "nine working skills" → "ten working skills"; added `text-audit`
  before `publish` in both member enumerations (description line 3, intro line 11), matching the footer roster.
- **R1(a) (spec-author comprehension gate)** — kept the gate's normative statement (it is spec law, every
  changed section runs it, closes on two consecutive clean reads) and the "per changed section the gate is
  cheap" line and the `[GAP: ...]` paragraph (spec-author's own); repointed the HOW — the mechanical-lint list
  and the cold-reader-loop restatement — to one pointer sentence naming text-audit as the carrier of the loop's
  method and reader-prompt. True duplication only was trimmed.
- **R1(b) (communicator pre-report clean-reader step)** — added one pointer sentence to the clean-reader
  paragraph naming text-audit as the home of the clean-reader loop and reader-prompt; inserted inline (no new
  physical line) so the body stays at 499 lines, under the row-280 <500 ceiling.
- **R1(c) (product-prover boundary)** — added the hand-off sentence in "When NOT to use": reader-comprehension
  ("can a stranger read the prose") routes to text-audit, the mirror of the prover's pass.
- **N1 (build-pipeline frontmatter)** — orchestration list `(spec-author, product-prover, test-author)` →
  `(spec-author, product-prover, design-reviewer, test-author)`.

**Pins touched: none.** Grepped `tests/` and `guardrails/` for every sentence changed or removed (the "nine
working skills" title, both enumerations, the comprehension-gate lint list + cold-reader paragraph, the
communicator clean-reader lines, the product-prover boundary lines, the build-pipeline orchestration list).
No pinning test or guardrail asserts any changed or removed sentence, and none of the five new phrases is
pinned. `test_communicator_body_thinned` (<500-line ceiling) and `test_communicator_register_extracted`
(body must not contain "Cold-reader check") both stay satisfied.

**Lints:** `preshow-register-lint` clean (exit 0) on live-spec-base, spec-author, product-prover,
build-pipeline. `spec-style-lint` errors=0 on all five (spec-author fully clean, 0 warnings; the others carry
only pre-existing soft caps-shout warnings — agent-instruction register per N3). communicator's
`preshow-register-lint`/`spec-style-lint` errors are pre-existing and self-referential (flagged lines
211/220/221/297/459/460 quote banned patterns as examples of what to avoid); none fall in the edited region
(lines 471–472), so the edits added zero new lint findings.

**Tests:** Ran the 14 test files that read these five skills. All pass except 11 pre-existing reds in
`test_traceability.py`, every one asserting a missing needle in `PRODUCT_SPEC.md`/`ROADMAP.md` (files outside
this write-set, several annotated in the test source as "CANDIDATE REAL DEFECT — genuinely dropped, left red").
Isolation proof: reversing all five edits to the WIP baseline yields the identical `test_traceability`
result (11 failed, 160 passed), so the edits changed zero test outcomes. The tree is a large uncommitted
work-in-progress (~200 files modified vs HEAD); the 11 reds belong to that WIP, not to this landing.
