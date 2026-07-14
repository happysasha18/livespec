# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-14 — the cleanup movement is done, about to push)
**PACK v1.4.0, PROVER v1.1.4.** A MINOR bump under the Fable pre-MINOR gate. **Suite: 682 passed, 1
expected red** (`test_guardrails.py::TestGateA_ProverRecord::test_real_repo_passes`, red only because the
new prover record is not yet committed — it clears at the lead's commit; 683 green once landed). The tree
is left UNCOMMITTED for the lead's review; the lead commits and pushes, not this window. Read this, then
wipe memory once it pushes; every landing's full story lives in JOURNAL + ROADMAP.

## What the cleanup movement did (five pieces, rows 316-320)
Alexander's word 2026-07-14 ("позор, до победного"): the spec and skills carried rule/lens BIOGRAPHIES
inline that bloated what the model loads each call, INV-140's KIND block argued itself, and the quality
would have failed the skill-creator's own bar. A full-pass response — three fresh-eyes reviews → five
serial chunks → a Fable three-pass gate → 1.4.0:
- **Row 316 (chunks 1+5)** — 88 provenance biographies swept to `docs/lenses.md`; a new
  `provenance-narrative` lint (docs/spec-style.md **R15**) holds the class on every push.
- **Row 317 (chunk 2)** — INV-140's KIND collapsed to one rule: defect/recommendation is the sole verdict,
  the three-level **severity axis retired**.
- **Row 318 (chunk 3)** — the design review wired into the M-1 milestone gate (it was skipped silently
  before) + structural compaction (narrated lens cross-refs cut to bare anchors, base rule 7 split,
  one-home dedupe, INV-133 reworded).
- **Row 319 (chunk 4)** — two new base rules: **INV-143** the seat acts by default (max-agency, never parks
  derivable work), **INV-144** the spec is the definition of correct (a code/spec divergence defaults to a
  possible code error; silently rewriting the spec to match code is forbidden).
- **Row 320 (chunk 5)** — **INV-145** a periodic full audit (two layers: continuous lints for KNOWN drift +
  a full audit every ten landings for UNKNOWN drift), and "an audit is adversarial by nature" folded into
  INV-46 as a definition.

Three new invariants (143/144/145). Records: prover re-check `docs/prover/2026-07-14-cleanup-movement.md`
(Fable + product-prover 1.1.4, six defects folded, CLEAR to 1.4.0); the first M-1 design-review record
`docs/design-review/2026-07-14.md` (STOOD DOWN by INV-141 — live-spec is a skill pack with no acted-on
elements). Skill versions: base 1.0.16, product-prover 1.1.4, build-pipeline 1.0.28.

## ⟨DECIDE⟩ — two taste-call defaults I set (overturn either if you meant otherwise)
1. **Scoped design review at every surface add** (vs milestone-only). The born-of miss arrived as a
   surface add, and the scoped form (the new surface's elements against the existing inventory) is cheap
   by construction — so I default to running it on every surface add rather than deferring to the next
   MINOR gate. Overturnable to milestone-only.
2. **The v1 echo channel holds exactly ONE producer** (the same-kind divergence). The design memo framed
   two producers; the independent prove showed the second — a "likely-missed edge" the running product
   reaches — is the INV-72/138 blank-answer class the existing lenses already treat as BLOCKING, which
   would collide with the never-blocks promise. So I narrowed v1 to one producer; a later producer earns
   its own clause and wish row. Overturnable if you want the wider channel now.

## Queue (take at a queue-take — all QUEUED, none blocking)
- **Row 315** — the TEST_MATRIX provenance cells (18 "; born of …" cells outside the lint's scope): sweep
  them to docs/lenses.md and widen the gate test's scope, OR record the matrix as a stated boundary of R15.
- **Row 261** — GitHub Issues as the strangers' wish door: still a DECIDE, awaiting Alexander's word.
- The one real remote deposit still owes its live run.
- The tlvphotos impersonal-voice wish sits in its own inbox.

## OWNER-HELD (needs your hand — no autonomous move taken)
- **`~/.claude/CLAUDE.md` says "seven working skills"** — the pack now has EIGHT working skills + base
  (design-reviewer since row 310). This is a host-side file on your machine, outside this project's tree,
  so this window does NOT edit it — your one out-of-tree edit ("seven working skills" → "eight working
  skills").

## Standing habits (always-on)
- When a method skill changes, run a fresh-eyes adversarial pass (INV-46); a MILESTONE earns the deep
  Fable whole-spec + architecture pass. A full audit also runs on a landing-count cadence (INV-145).
  `date` before any stamp. Shipped docs stay impersonal (INV-118/120), provenance in docs/lenses.md +
  JOURNAL — never inline in the body (R15/INV-83). The seat decides and acts on derivable work and reports
  (INV-143); the spec is the definition of correct (INV-144). Delegation by base rule 5 → INV-69; the lead
  dispatches its discovery reads (base rule 25 → INV-137). Public READMEs edited ONLY via a fresh
  clean-context agent (bilingual safety).
- No self-certification (INV-94) · plain words, codes trail (INV-28) · say-what-it-is, no contrast frames
  · inbox swept first · one lane one commit · a delegated run's verdict is the suite log's tail (INV-80).
- Next free codes: read the live Formal index before minting (INV-145 consumed; codes consume in landing
  order, reservations dead).

## Memory
Once this movement pushes, memory can be wiped — its whole story lives in JOURNAL + ROADMAP + the two
records above.
