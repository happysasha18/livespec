# PENDING DRAFT — composition-walk fixes (must-fix + S1 + S2 + S3), drafted 2026-07-12 by the Opus auditor, NOT yet applied
# Next session: brief a sonnet applier from these blocks (the row-233 applier brief is the shape).
# Source audit: docs/audit/2026-07-12-composition-walk.md @ 8125b2c. Versions: read live values, +0.0.1 each (section V).
# NO INV/M RENUMBERING: this batch mints no new codes. It amends four existing clauses (M-6, INV-111,
# INV-112, INV-114) plus their index rows — a defect-and-composition batch riding the audit record.

Every old_string below was copied byte-exact from the live tree at 8125b2c and verified unique in its
file after whitespace-collapse. Apply order: tests first red-proven (section T, run pre-delta), then the
prose blocks, then versions, then green.

---

## FIX-M — M-6 gains the inbox-only carve-out (must-fix)

**Home decision.** M-6 in PRODUCT_SPEC.md is the normative home; the host profile line
(.live-spec/profile.md prover.cadence) already declares "M-6 is its normative home," so the profile gets a
pointer amendment and no second statement of the rule. Both edits below.

### M.1 — SPEC clause (PRODUCT_SPEC.md, the M-6 push-gate list, anchor verified unique)

**old_string**
```
  2. a fresh whole-spec re-check — a product-prover pass over PRODUCT_SPEC.md as it stands, with its record landing in docs/prover/ before the push.
```

**new_string**
```
  2. a fresh whole-spec re-check — a product-prover pass over PRODUCT_SPEC.md as it stands, with its record landing in docs/prover/ before the push.

  One carve-out, scoped by the diff: a push whose diff is exactly one new file under inbox/ — the remote deposit's shape [INV-112] — changes no spec-backed content, so it owes the fence and no re-check record; a diff carrying anything more rides the full gate.
```

### M.2 — Formal-index row (PRODUCT_SPEC.md:1841)

**old_string**
```
| M-6 | push gate: prover re-check before every push | Rhythm |
```

**new_string**
```
| M-6 | push gate: prover re-check before every push; one carve-out — a push whose diff is exactly one new inbox/ file (the remote deposit [INV-112]) owes the fence and no record | Rhythm |
```

### M.3 — Host profile pointer (.live-spec/profile.md, prover.cadence tail)

**old_string**
```
Alexander's explicit word, 2026-07-04. This line and the push gate [M-6] are one fact; M-6 is its
  normative home.
```

**new_string**
```
Alexander's explicit word, 2026-07-04. This line and the push gate [M-6] are one fact; M-6 is its
  normative home, and M-6 names the one carve-out: a push whose diff is exactly one new inbox/ file
  (the remote deposit, SPEC INV-112) owes the fence and no re-check record.
```

---

## FIX-S1 — INV-111 states the suite check and its relationship to INV-114

The relationship sentence lives in the INV-111 clause: the vehicle is the surface a host actually reads
when it runs a layout pass, so the routing sentence reads most naturally there. INV-114's own clause
gains its half through FIX-S2. Build-pipeline's INV-111 copy is an abbreviated pointer (SKILL.md:60) and
stays as it is; PRODUCT_SPEC.md stays the one full home.

### S1.1 — SPEC clause (PRODUCT_SPEC.md:1198, full-paragraph replace)

**old_string**
```
**A same-version docs-layout pass rides one sanctioned light vehicle.** The routing sends an adopted host's ask to its own queue when the ask restructures the host's own documents with no package-version delta [INV-110]. That pass runs one named shape. The owner's decisions are locked in a checkpoint before any file moves [INV-107]. The work builds on a clean pushed base, so one command restores the pre-pass tree. The pass proves content survived by a word-token multiset check AND a punctuation multiset check, since word-token identity alone passes a reflow that dropped or moved punctuation. The pass lands one journal chapter naming what moved and why. A host never improvises a layout pass; it cites this vehicle. [INV-111]
```

**new_string**
```
**A same-version docs-layout pass rides one sanctioned light vehicle.** The routing sends an adopted host's ask to its own queue when the ask restructures the host's own documents with no package-version delta [INV-110]. That pass runs one named shape. The owner's decisions are locked in a checkpoint before any file moves [INV-107]. The work builds on a clean pushed base, so one command restores the pre-pass tree. The pass proves content survived by a word-token multiset check AND a punctuation multiset check, since word-token identity alone passes a reflow that dropped or moved punctuation. The pass also reads the full suite green on the restructured tree, from the log's own line [INV-39], since a reflow can break a suite-owned doc check that no multiset reads. The pass lands one journal chapter naming what moved and why. A pass that rides a branch back to main closes through the restructure merge gate [INV-114], where this vehicle's multiset proof serves as the gate's first part; a pass landing directly on main owes its green suite on its own. A host never improvises a layout pass; it cites this vehicle. [INV-111]
```

### S1.2 — Formal-index row (PRODUCT_SPEC.md:1768)

**old_string**
```
| INV-111 | a same-version docs-layout pass rides one sanctioned light vehicle: a host restructuring its own documents with no package-version delta [INV-110] runs one named shape; the owner's decisions are locked in a checkpoint before any file moves [INV-107], the work builds on a clean pushed base with a one-command restore, content is proven by a word-token multiset check AND a punctuation multiset check (word-token identity alone passes a reflow that moved punctuation), and one journal chapter lands; a host never improvises a layout pass and cites this vehicle; born of the track-coach s63 audited pass (2026-07-10) | Catch-up |
```

**new_string**
```
| INV-111 | a same-version docs-layout pass rides one sanctioned light vehicle: a host restructuring its own documents with no package-version delta [INV-110] runs one named shape; the owner's decisions are locked in a checkpoint before any file moves [INV-107], the work builds on a clean pushed base with a one-command restore, content is proven by a word-token multiset check AND a punctuation multiset check (word-token identity alone passes a reflow that moved punctuation), the full suite reads green on the restructured tree [INV-39], and one journal chapter lands; a branch-riding pass closes through the merge gate [INV-114]; a host never improvises a layout pass and cites this vehicle; born of the track-coach s63 audited pass (2026-07-10) | Catch-up |
```

---

## FIX-S2 — INV-114's token-identity gate scopes to content-preserving restructures

The clause lives as a full statement in three homes (spec + product-prover + build-pipeline), so the scope
sentence lands in all three, keeping the copies aligned [INV-13]. Canonical sentence pair (identical
after whitespace-collapse, citation style per home):

> The token-identity part scopes to a content-preserving restructure. A deliberate redesign changes
> content by intent, so it routes by the architecture-redesign law [INV-113], and its merge stands on the
> green suite and the delta-scoped prover pass, with no token-identity demand over text the redesign
> meant to change.

### S2.1 — SPEC clause (PRODUCT_SPEC.md:1200, insert before the born-of parenthesis)

**old_string**
```
And a session that sharpens a human's spoken bar beyond his words says the sharpened form back and marks it as its own interpretation. (Born of a strictly-improving restructure merge parked on the old side's pre-existing clarity debts because a spoken «prover finds nothing both sides» was over-sharpened into «any finding parks the merge», corrected live 2026-07-12.) [INV-114]
```

**new_string**
```
And a session that sharpens a human's spoken bar beyond his words says the sharpened form back and marks it as its own interpretation. The token-identity part scopes to a content-preserving restructure. A deliberate redesign changes content by intent, so it routes by the architecture-redesign law [INV-113], and its merge stands on the green suite and the delta-scoped prover pass, with no token-identity demand over text the redesign meant to change. (Born of a strictly-improving restructure merge parked on the old side's pre-existing clarity debts because a spoken «prover finds nothing both sides» was over-sharpened into «any finding parks the merge», corrected live 2026-07-12.) [INV-114]
```

### S2.2 — product-prover home (skills/product-prover/SKILL.md:169, append at the paragraph's tail)

**old_string**
```
The pass reads both the old tree and the merged tree; a finding present on both is pre-existing, a finding new to the merged side is delta-scoped and blocks.
```

**new_string**
```
The pass reads both the old tree and the merged tree; a finding present on both is pre-existing, a finding new to the merged side is delta-scoped and blocks. The token-identity part scopes to a content-preserving restructure. A deliberate redesign changes content by intent, so it routes by the architecture-redesign law (SPEC INV-113), and its merge stands on the green suite and the delta-scoped prover pass, with no token-identity demand over text the redesign meant to change.
```

### S2.3 — build-pipeline home (skills/build-pipeline/SKILL.md:103, insert before the born-of parenthesis)

**old_string**
```
says the sharpened form back and marks it as its own interpretation. (Born of a strictly-improving merge parked on the old side's pre-existing debts, corrected live 2026-07-12.)
```

**new_string**
```
says the sharpened form back and marks it as its own interpretation. The token-identity part scopes to a content-preserving restructure. A deliberate redesign changes content by intent, so it routes by the architecture-redesign law (SPEC INV-113), and its merge stands on the green suite and the delta-scoped prover pass, with no token-identity demand over text the redesign meant to change. (Born of a strictly-improving merge parked on the old side's pre-existing debts, corrected live 2026-07-12.)
```

### S2.4 — Formal-index row (PRODUCT_SPEC.md:1854; the row keeps "delta" and its trailing `| Catch-up |`)

**old_string**
```
| INV-114 | a restructure or migration merge gate judges the delta: three parts — load-bearing token identity old-versus-new modulo the per-chunk named deltas plus the punctuation-multiset check [INV-111], the full suite green on the merged tree [INV-39], and a full prover pass on both sides whose blocking set is delta-scoped (an unmatched token, a red suite, a new-side finding absent on the old side, an unnamed meaning change); pre-existing findings equal on both sides route to queue rows in the same landing and never block; and a session that sharpens a human's spoken bar beyond his words says the sharpened form back and marks it as its own interpretation; homes: the spec clause + product-prover's restructure-merge gate + build-pipeline's restructure door; born of a strictly-improving merge parked on the old side's pre-existing debts, corrected live (2026-07-12) | Catch-up |
```

**new_string**
```
| INV-114 | a restructure or migration merge gate judges the delta: three parts — load-bearing token identity old-versus-new modulo the per-chunk named deltas plus the punctuation-multiset check [INV-111], the full suite green on the merged tree [INV-39], and a full prover pass on both sides whose blocking set is delta-scoped (an unmatched token, a red suite, a new-side finding absent on the old side, an unnamed meaning change); pre-existing findings equal on both sides route to queue rows in the same landing and never block; the token-identity part scopes to content-preserving restructures, and a content-changing redesign routes by INV-113; and a session that sharpens a human's spoken bar beyond his words says the sharpened form back and marks it as its own interpretation; homes: the spec clause + product-prover's restructure-merge gate + build-pipeline's restructure door; born of a strictly-improving merge parked on the old side's pre-existing debts, corrected live (2026-07-12) | Catch-up |
```

---

## FIX-S3 — INV-112's deposit push and INV-82's live-session stand-down

The sentence lands in the spec clause only: inbox/README.md and adopt/ADOPT.md carry the remote arm in
abbreviated pointer form (verified — neither carries the fence-composition sentence), so the spec stays
the one full home and the copies stay compatible.

### S3.1 — SPEC clause (PRODUCT_SPEC.md:1598, insert after the benign-case sentence)

**old_string**
```
The deposit composes with the peer fence by its shape: a remote seat cannot see which sessions are live, and one fresh inbox/ file is the fence's expected benign case [INV-11].
```

**new_string**
```
The deposit composes with the peer fence by its shape: a remote seat cannot see which sessions are live, and one fresh inbox/ file is the fence's expected benign case [INV-11]. The live-session stand-down [INV-82] holds no bar over the deposit either: the one new inbox/ file is additive and races nothing, so the deposit push proceeds, while any push beyond that one file still stands down.
```

### S3.2 — Formal-index row (PRODUCT_SPEC.md:1730; the row keeps "remote arm" and "grant")

**old_string**
```
| INV-112 | the inbox door's remote arm: a seat that reaches a repo only through git deposits one new file in inbox/, commits it touching inbox/ only with the source named, and pushes it, under a per-repo grant recorded in the host profile like the push grant [INV-82] (the owner links the Claude environment to GitHub once, grants each repo once); a seat with no grant fails honestly — it names the grant it lacks and hands the owner the one action, the honest failure of a window that never opened [INV-67], never silent, never a guessed workaround; born of the owner thinking the cloud seat through (2026-07-10) | Package repo |
```

**new_string**
```
| INV-112 | the inbox door's remote arm: a seat that reaches a repo only through git deposits one new file in inbox/, commits it touching inbox/ only with the source named, and pushes it, under a per-repo grant recorded in the host profile like the push grant [INV-82] (the owner links the Claude environment to GitHub once, grants each repo once); the deposit push is exempt from the live-session stand-down [INV-82] by its additive one-file shape, anything beyond the one file still standing down; a seat with no grant fails honestly — it names the grant it lacks and hands the owner the one action, the honest failure of a window that never opened [INV-67], never silent, never a guessed workaround; born of the owner thinking the cloud seat through (2026-07-10) | Package repo |
```

---

## T — Test extensions (apply FIRST against the pre-delta tree; the three new asserts must fail red, then the prose blocks land, then green)

The amended clauses are spec-backed literals, so the docs and the test land in the same session
[INV-104]. No new test file and no new matrix row: each assert extends the law's existing test, and the
matrix rows M-249/M-251/M-253 keep their names.

### T.1 — tests/test_restructure_merge_gate.py (the S2 needle, all three homes)

**old_string**
```
            self.assertIn("merge gate judges the delta", body, home)
            self.assertIn("blocking set is delta-scoped", body, home)
```

**new_string**
```
            self.assertIn("merge gate judges the delta", body, home)
            self.assertIn("blocking set is delta-scoped", body, home)
            self.assertIn(
                "scopes to a content-preserving restructure", body, home
            )
```

### T.2 — tests/test_docs_layout_vehicle.py (the S1 suite-green needle, spec)

**old_string**
```
        self.assertIn("builds on a clean pushed base", spec)
        self.assertIn("lands one journal chapter", spec)
```

**new_string**
```
        self.assertIn("builds on a clean pushed base", spec)
        self.assertIn("full suite green on the restructured tree", spec)
        self.assertIn("lands one journal chapter", spec)
```

### T.3 — tests/test_inbox_remote_arm.py (the S3 stand-down needle + the M-6 carve-out needle, spec)

**old_string**
```
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-112]", spec)
```

**new_string**
```
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-112]", spec)
        self.assertIn("holds no bar over the deposit", spec)
        self.assertIn("owes the fence and no re-check record", spec)
```

---

## V — Version bump note (one for the whole batch: read live values at apply time, +0.0.1 each; never hardcode a target)

- `VERSION` (pack) — +0.0.1 (reads 1.0.32 now).
- `PRODUCT_SPEC.md` header line 1 — +0.0.1 on the spec's own number (reads `v1.0.24, 2026-07-12` now; the date stays today's clock).
- `skills/product-prover/SKILL.md` frontmatter `version:` — +0.0.1 (reads 1.0.2 now; S2.2 touches the skill).
- `skills/build-pipeline/SKILL.md` frontmatter `version:` — +0.0.1 (reads 1.0.9 now; S2.3 touches the skill).
- `.live-spec/profile.md` carries no version line; no bump.
- Base rulebook untouched: the working skills' `live-spec-base` header pins do NOT move.

---

## D — Disposition of the audit's four notes (recorded, routed — no clause edits tonight)

- **N1 (partially-shipped checkpoint under INV-107)** — recorded, routed: lives in docs/audit/2026-07-12-composition-walk.md; a queue row at the next bookkeeping sweep.
- **N2 (INV-111's decision-lock record under INV-107's closing test)** — recorded, routed: same home, same sweep.
- **N3 (fire-and-forget remote seat and INV-106's read-the-verdict duty)** — recorded, routed: same home; kin of the mechanical-arm row below, sequence the two together.
- **N4 (INV-112's unbounded push retry)** — recorded, routed: same home, same sweep.
- **Mechanical arm of FIX-M (found while drafting, named here so it is never lost [INV-1])**: the CI mirror (.github/workflows/gates.yml) runs guardrails/check-prover-record.sh on every push to main, so the first remote inbox deposit on a day with no committed prover record reds the CI even after the prose carve-out lands. The script's matching diff-scoped carve-out is an infra change owing its own red-first test, beyond tonight's prose batch — routed as a queue row beside N3.

## A — Audit-doc addendum (the applier appends this block to docs/audit/2026-07-12-composition-walk.md at landing, filling the commit)

```
---

**Addendum (landing).** The must-fix and S1-S3 landed in commit `<commit>` via
.live-spec/checkpoints/pending-draft-composition-fixes.md: M-6 carve-out (clause + index + profile
pointer), INV-111 suite-green + merge-gate relationship (clause + index), INV-114 content-preserving
scope in all three homes (clauses + index), INV-112 stand-down sentence (clause + index), three test
extensions red-proven then green. The four notes and the CI mechanical-arm row stay routed per the
draft's disposition section.
```

---

## Self-verify (drafter's own walk)

- **Needle compatibility checked against**: tests/test_restructure_merge_gate.py (all four pinned needles kept in all three homes; index row keeps "delta" and still ends `| Catch-up |`), tests/test_docs_layout_vehicle.py (all five pinned needles kept; index row keeps "vehicle"), tests/test_inbox_remote_arm.py (all six pinned needles kept in all three prose homes; index row keeps "remote arm" and "grant"), tests/test_guardrails.py (scripts untouched tonight), tests/test_onboarding_card.py (pins "before every push" in the onboarding card html — untouched), tests/test_traceability.py (no new Formal-index anchor is minted, so node ownership stands; ARCHITECTURE.md untouched).
- Every old_string copied byte-exact from the tree at 8125b2c and grep-verified unique in its file (M.1 anchor: 1 hit; M.3 anchor "normative home.": 1 hit; full-paragraph anchors unique by construction).
- New-sentence needles appear where their asserts look: "scopes to a content-preserving restructure" in S2.1/S2.2/S2.3 (all three homes); "full suite green on the restructured tree" in S1.1 (spec); "holds no bar over the deposit" in S3.1 (spec); "owes the fence and no re-check record" in M.1 (spec).
- Register: plain SVO; every prohibition its own sentence; no "X — not Y" frame (the em-dashes wrap appositives).
- Dates only from the clauses' own records (2026-07-04/10/11/12) or today's clock.
- No new INV/M codes; no renumbering; ROADMAP untouched tonight (the routed rows open at the next bookkeeping sweep, per the coordinator's word).

APPLIED + CLOSED at landing 2026-07-12 (bump-worker.md).
