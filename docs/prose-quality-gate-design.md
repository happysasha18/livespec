# Durable prose-quality DONE-GATE — design (2026-07-08)

Origin: after a full restyle round the same prose defects recurred (scissors, redundancy, second person).
Root cause: "0 lint errors" was treated as done, but the done-set was smaller than the set of known defect
classes; caps-shout + second-person were non-blocking warnings that accumulated, redundancy had no rule, and
parking left defects in place (broken-windows). This design is the output of a deep-research pass
(run wf_d5338e62-3bd) + a fresh clean-context design pass. Memory [[prose-quality-gate-must-block-not-park]].

## The one idea
A single fixed machine-checkable DONE-GATE that (a) makes every known mechanical defect blocking, (b) adds the
one semantic check regex cannot do (redundancy), (c) turns "not fixed yet" into explicit dated debt
instead of a silent warning, and (d) is the same definition a "humanize" and a "restyle" pass must both satisfy — which
ends the oscillation, because a warm/second-person pass can no longer pass.

Gate scope: the product spec files only (SPEC.md and section files), never meta-docs (spec-style.md, journals,
READMEs, which legitimately use CAPS/second person). The gate takes an explicit file list.

## 1. Rule set + severities (all blocking after promotion)
- Global (never legitimate, no exemption): `scissors`, `machine-jargon`, `caps-shout`.
- Normative-only (exempt inside marked informative regions): `second-person`, `negation-opener`, new
  `reassurance` (lexicon: don't worry / simply / of course / feel free / you can ignore / …), new
  `future-narration` (will/shall + verb), optional `open-conditional` (conditional with no "otherwise").
- Exemption regions (normative-only rules skip these; global rules always run):
  (a) `**User story:**` lead → block to next blank line; (b) `>` blockquote → per line; (c)
  `NOTE (informative)` lead → block to next blank line. Guard: a pytest asserts no `[INV-…]` anchor sits
  inside a `>` region in gated files (a normative rule may not hide in the informative lane).
- Needle collision: promoting second-person collides with pinned phrases (e.g. heading "…what you know to
  ask"). Resolution: rewrite to register-clean + re-point the needle in the SAME commit (e.g. "what the
  author knows to ask"); or exempt only if genuinely informative; never leave it. `TestNeedleRegisterClean`
  lints every needle string and asserts 0 errors — closes the "re-point to a new defect" loophole.

## 2. Mechanical redundancy pre-check (no LLM) — scripts/spec-redundancy-precheck.py
Segment into sentence/bullet units; normalize (reuse linter scrub, lowercase, stoplist) → content tokens T +
3-gram shingles S. Candidate pair if min(|T_a|,|T_b|) ≥ 6 and (jaccard(S) ≥ 0.60 or containment(T) ≥ 0.85).
False-positive controls: min length; parallel-sibling-bullet bucket separated from redundancy; anchor-only
units dropped. Emits both spans + line numbers + score. Gate: open == 0 (resolved or waived). Catches lexical
/ near-verbatim / reordered dup; CANNOT catch paraphrase with disjoint vocab (that goes to the LLM judge).

## 3. LLM-judge redundancy+register — scripts/spec-judge.py + scripts/judge-rubric.md (hash-pinned)
This is a harness: the judgment is a FRESH spawned agent (Opus max, pack NOT loaded), whole document in one
context (≈45K tokens — one mind over the whole doc, catches cross-section dup). Flow: --emit-prompt (locked
rubric + line-numbered doc + appended seeded self-test region) → fresh agent writes JSON → --verify (schema,
verbatim-quote check, self-test check, strip seeds). Rubric hash-pinned (sha256 asserted before every run).
Output schema: findings[] each with criterion, severity (definite/likely/nit), verbatim `quote`,
`duplicate_of`, why. Verify discards any finding whose quote is not found verbatim (hallucination guard).
Self-test: appended region has 3 planted defects at known lines; verify asserts all 3 are caught, else the run
is INVALID (not green). Reliability: no holistic score trusted, only verbatim-verified per-span findings;
union of 2 temp-0 runs (bias to recall); calibration examples in the rubric. Gate: self-test passed AND zero
surviving definite+likely (or waived); nits advisory.

## 4. No-park waiver — scripts/spec-waivers.json + scripts/spec-debt-cap.json
Waiver = dated auditable debt that still counts and self-destructs. Fields (all required): id, rule, file,
snippet, reason, owner, date, expiry. Snippet-based match (line numbers drift; snippet self-invalidates when
the text is fixed → stale waiver flagged for removal). Each checker: active waiver → move finding to `waived`
bucket (always printed + counted, never changes exit code); expired waiver → does NOT suppress, stays hard
ERROR (forgotten debt breaks the gate); stale waiver → warning to remove. Forcing functions (pytests): waived
always visible; expiry ≤ date+30d; expired reverts to error (time-travel fixture test); monotonic ratchet cap
(spec-debt-cap.json counts can only be lowered).

## 5. Unified DONE-GATE — scripts/spec-done-gate.py (+ tests/test_done_gate.py)
GREEN iff ALL hold: (1) style-lint 0 errors with all promoted rules; (2) redundancy pre-check open == 0;
(3) LLM-judge self-test passed + 0 surviving definite/likely; (4) anchor multiset unchanged vs baseline;
(5) traceability needles green + TestNeedleRegisterClean; (6) full suite green minus pinned skips; (7) waiver
hygiene (no expired-in-use, TestWaivers + TestDebtRatchet green); (8) whole-doc-rewrite path: fresh-checker
fact-preservation artifact recorded. Prints GREEN + debt summary or RED + failing condition. Commit only GREEN.

## Build order
1. Waiver + ratchet (prereq for landing the 317 accumulated findings as dated debt instead of a silent park).
2. Promote warnings + new mechanical rules + exemptions + needle fix (highest ROI).
3. Mechanical redundancy pre-check.
4. LLM-judge protocol (most complex, least reliable → last, behind its mitigation stack).
5. Unified done-gate wiring + 8 pytest classes.

## Honest limits
Mechanical layers (1–3) are drift-proof but blind to semantics; the LLM layer (4) sees semantics but is
probabilistic — the self-test canary converts it to "trust only on a run where it demonstrably worked", which
is the strongest guarantee without a labeled gold corpus. None of this judges positive elegance/flow (the
exemplars + a human's single sample read own that). The gate enforces the FLOOR across the whole doc without a
tired human — the stated goal.
