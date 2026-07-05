# skill-creator evaluation — live-spec pack skills

**Date:** 2026-07-05 · **Auditor:** Opus worker (roadmap row 5, rides the 0.5.0 night block)
**Scope:** the four pack working skills (spec-author, product-prover, build-pipeline, communicator) in
BOTH copies (repo `~/live-spec/skills/<name>/` + installed `~/.claude/skills/<name>/`), plus a light pass
on the shared base (live-spec-base). **This is an EVALUATION — no files were edited; fixes are the
senior's to fold later.**

## Method (per skill-creator/SKILL.md)

skill-creator's own runnable tooling and how it was applied here:

- **`scripts/quick_validate.py`** — the static frontmatter validator. Could not run as-is: `import yaml`
  fails (`ModuleNotFoundError: No module named 'yaml'` on system python 3.9). Its checks were **replicated
  inline** (no yaml dependency) — faithful to the script's logic (ALLOWED_PROPERTIES set, description
  length/angle-bracket rules, kebab-case name rule). Raw results below.
- **`scripts/run_loop.py` / `run_eval.py` / `improve_description.py`** (description-triggering optimizer) —
  **NOT run.** They shell out to `claude -p` (model budget) AND write a new description back into the skill.
  Both are out of bounds for an eval-only pass. Triggering was assessed **manually** per skill-creator's
  "How skill triggering works" guidance (substantive multi-step queries trigger; near-miss negatives are
  the real test).
- **The full eval loop** (spawn with-skill vs baseline subagents, grade, benchmark, viewer) is skill-creator's
  method for *iterating a skill against a user*, not for a static audit of finished skills. Not applicable to
  a no-edit evaluation pass; the structural + triggering + consistency lenses below are the audit-appropriate
  subset.

### Raw: drift (repo vs installed)

`diff -rq ~/live-spec/skills/<name> ~/.claude/skills/<name>` returned **empty for all five skills** — repo
and installed copies are **byte-identical. No drift.** (Every skill dir holds exactly LICENSE, README.md,
SKILL.md — no scripts/references/assets/templates subdirs.)

### Raw: replicated quick_validate + measurements

| Skill | SKILL.md lines | frontmatter keys | name kebab | desc chars (≤1024) | validator verdict |
|---|---|---|---|---|---|
| spec-author | 216 | name, description, **version** | ok | 768 | FAIL — `version` not in ALLOWED set |
| product-prover | 363 | name, description, **version** | ok | 552 | FAIL — `version` not in ALLOWED set |
| build-pipeline | 159 | name, description, **version** | ok | 650 | FAIL — `version` not in ALLOWED set |
| communicator | 124 | name, description, **version** | ok | 512 | FAIL — `version` not in ALLOWED set |
| live-spec-base | 136 | name, description, **version** | ok | 745 | FAIL — `version` not in ALLOWED set |

(An earlier automated flag of "angle brackets in build-pipeline description" was a **false positive** from my
extraction catching the YAML folded-scalar `>` indicator, not literal `<`/`>` in the text. `yaml.safe_load`
resolves the block scalar correctly; the description content is clean. Discarded.)

---

## Cross-skill findings (the classes — fix once, sweeps all)

### X1 — `version:` is a top-level frontmatter key, which skill-creator's validator rejects — MUST-FIX (class, all 5)
skill-creator's `quick_validate.py:42` defines `ALLOWED_PROPERTIES = {name, description, license,
allowed-tools, metadata, compatibility}`. A top-level `version:` (spec-author:4, product-prover:4,
communicator:4, live-spec-base:4, build-pipeline:10) is **not** in that set, so the validator returns
`FAIL: Unexpected key(s) ... version` for every pack skill — and `package_skill.py` would inherit that gate.
The sanctioned home is **`metadata.version`** (`metadata` IS allowed). Remedy per skill:
```yaml
metadata:
  version: 0.1.3
```
Honest severity note: the skills still LOAD in Claude Code (they appear in `available_skills`), so the
practical impact is **packaging/validation-time, not runtime**. But this pass is *by skill-creator's method*,
and its canonical validator fails all five — so it is the top mechanical fix. One edit pattern, five files.

### X2 — dangling template pointers: skills tell the reader to copy a file that isn't there — MUST-FIX (class, 2 skills)
- spec-author:77 and spec-author:140 — "Copy `templates/SPEC.template.md`".
- build-pipeline:65-66 — "(template: `ARCHITECTURE.template.md`)".

The templates **exist**, but at the **repo root** `~/live-spec/templates/` (SPEC/ARCHITECTURE/ROADMAP/
JOURNAL/NEXT_STEPS/TEST_MATRIX.template.md) — **not** inside the skill. Resolved against the skill's own
directory (`ls ~/.claude/skills/spec-author/templates/` → *No such file or directory*), the bare relative
pointer resolves to nothing. This directly breaks each skill's own header promise ("Used standalone, this
note is plain advice") — a public install of spec-author or build-pipeline (both marked Public) ships with
**no template at all**. Remedy options: (a) bundle the templates under the skill's `assets/` or `templates/`
(skill-creator's anatomy puts output templates in `assets/`); or (b) qualify the pointer ("the pack's
`templates/` at the live-spec repo root") so it's not read as skill-relative. (a) is the portable fix.

### X3 — the base version `v0.1.4` is hand-pinned in four sibling headers — SHOULD-FIX (drift risk, class)
Every working skill's opening blockquote hardcodes "the pack's base skill, `live-spec-base` (v0.1.4)"
(spec-author:12, product-prover:12, build-pipeline:18, communicator:12). Base **is** 0.1.4 today, so it's
consistent **now** — but this is the base's version pinned in four places, which is exactly base rule 4
("one canonical home per fact") turned against the pack itself: the next base MINOR bump silently staledates
four headers. Consider dropping the parenthetical version from the prose pointer (name the skill, not its
number) and letting freshness re-resolve it, or accept it as a known milestone-sweep item.

### X4 — the 14-rule blockquote header is repeated verbatim across the 4 working skills — NOTE
The "shared working rules (ask-never-guess · plain words … · fix the class)" name-list is present once in
each working skill (grep confirms 1 occurrence each) and fully stated in base. As a **named index** (it
lists rule *names*, doesn't restate their bodies) it stays on the right side of base's own rule 1 ("a second
full statement of a shared rule inside a working skill is drift"). But it's a ~7-line list duplicated 4×; if
base renames a rule, four headers drift. Low priority — it's a pointer, not a restatement — but worth a
milestone glance.

---

## Per-skill sections

### spec-author (216 lines, desc 768) — verdict: STRONG, one portability break

- **Triggering — strong.** Description carries all "when to use", with concrete pushy triggers ("START a
  spec", "spec this out", "write the spec for X", "keep a spec in sync", "asks how to structure a spec") and
  a clean role split from the prover. No obvious false-trigger surface. skill-creator-compliant: all when-to
  info in the description, slightly pushy.
- **Structure & size — good.** 216 lines, well under the <500 ideal; bold-headline-then-detail throughout;
  clear anti-patterns + completeness-pass sections. No content is crying out for a reference file.
- **Consistency — good.** Canonical axis list (view/mode/tier/viewport/persistence/concurrency) matches the
  same list in build-pipeline and CLAUDE.md; base-version pointer correct.
- **Findings:** MUST-FIX X2 (dangling `templates/SPEC.template.md`, ×2). MUST-FIX X1 (version key). Note X3.

### product-prover (363 lines, desc 552) — verdict: STRONG, largest file, glossary is reference-shaped

- **Triggering — strong.** Good verb spread ("review, critique, stress-test, lint, find gaps", "poke holes
  in this", "is this spec ready / what did I miss") plus the explicit name mention. Well-bounded.
- **Structure & size — acceptable, watch the ceiling.** 363 lines is the pack's largest SKILL.md — still
  under skill-creator's <500 ideal, but it's the one approaching it. Two blocks read like reference material
  that skill-creator would push down a level: the **category table** (lines 95-116, 18 rows of
  plain-label/formal-term/meaning) and the **Glossary mode definitions** (lines 342-362, 18 term
  definitions). Moving either to `references/categories.md` / `references/glossary.md` (loaded on demand)
  would lighten the always-in-context body. SHOULD-FIX / low.
- **Consistency — good.** Four-part finding format, severity set (`must-fix`/`should-clarify`/
  `worth-considering`), and FULL vs CROSS-LINK modes all align with how build-pipeline step 2/4 invoke it.
  The persist-to-`docs/prover/YYYY-MM-DD.md` instruction (line 329) matches build-pipeline:59. No internal
  contradiction found.
- **Findings:** SHOULD-FIX: extract category table + glossary to reference files. MUST-FIX X1 (version key).

### build-pipeline (159 lines, desc 650) — verdict: STRONG, one dangling ref + a style outlier

- **Triggering — strong, best-bounded of the pack.** It's the only description with an explicit **negative**
  boundary ("NOT for tiny reversible edits … or pure research/fact-gathering"), which is exactly
  skill-creator's guidance on making near-miss negatives fail. Good positive triggers too.
- **Style outlier — NOTE.** It's the only skill using a YAML **folded block scalar** (`description: >`,
  line 3); the other four use an inline single-line description. Both are valid YAML and validate fine — but
  it's a within-pack inconsistency; unify on one style at a milestone.
- **Structure & size — good.** 159 lines; the 9 steps + the "Guardrails — the pipeline's TEETH" section are
  the substantive core and earn their place.
- **Consistency — good.** Step order matches CLAUDE.md and spec-author's handoff exactly; SPEC anchors
  (E-14/E-15/INV-15, base rules 13/14) are used as trailing anchors, not as the talking. `docs/prover/`
  discipline matches product-prover.
- **Findings:** MUST-FIX X2 (`ARCHITECTURE.template.md` dangling ref, line 65). MUST-FIX X1 (version key).
  NOTE: block-scalar style outlier. Note X3.

### communicator (124 lines, desc 512) — verdict: SOLID, but the description has no OFF-switch

- **Triggering — the pack's one over-trigger risk.** The description fires on "**when you report progress or
  results**" and "when you name a problem" — i.e. very nearly every assistant turn. Unlike build-pipeline,
  it carries **no negative boundary** at all. skill-creator warns to make descriptions pushy against
  *under*-triggering, but this one sits at the opposite edge: it reads as always-on. For this user that may
  be the intent (a near-standing "how to talk to Alexander" skill), so it's a **judgment call for the
  senior**, not a mechanical defect — but it should be a *decided* over-trigger, not an accidental one. If
  narrowing is wanted, add a "NOT for routine one-line acknowledgements" style carve-out. SHOULD-FIX (needs
  a human decision on intent).
- **Structure & size — good.** 124 lines, the tightest working skill; ten numbered rules + templates +
  field examples. Clean.
- **Consistency — good.** Rule 6 (plain words, code trails) is the concrete face of base rule 2; rule 10's
  decision-page filename convention (`<project>-decisions-<YYYY-MM-DD>.json`) is self-consistent and dated.
- **Findings:** SHOULD-FIX: decide + (if narrowing) bound the "report progress" trigger. MUST-FIX X1
  (version key). Note X3.

### live-spec-base (136 lines, desc 745) — noted, not deep-eval'd

Frontmatter is well-formed except the same X1 version-key issue. Description triggers sensibly ("Load it
whenever a pack skill is in use … when two skills seem to state one rule differently"). 14 rules + the
four-scope settings ladder are stated once and cleanly; it is genuinely the single home skill-creator's
progressive-disclosure model would want. Only cross-cutting fix that touches it is **X1**.

---

## Closing table

| Skill | Verdict | Top fix |
|---|---|---|
| spec-author | STRONG | X2 — bundle/qualify `templates/SPEC.template.md` (dangling ×2) |
| product-prover | STRONG | Extract category table + glossary to `references/` (largest body) |
| build-pipeline | STRONG | X2 — `ARCHITECTURE.template.md` dangling ref |
| communicator | SOLID | Decide the "report progress" over-trigger; bound it if narrowing |
| live-spec-base | SOUND | X1 — move `version` under `metadata` |
| **PACK-WIDE** | **healthy, no drift** | **X1 — `version:` → `metadata.version` in all 5 (fails skill-creator's validator)** |

**Single most important fix:** **X1** — every pack skill puts `version` at the top level of frontmatter,
which skill-creator's own `quick_validate.py` rejects (and `package_skill.py` would inherit); move it under
`metadata.version`. It's the one defect that fails the canonical tool, spans all five skills, and is a
one-line mechanical edit each.

**Runner-up (breadth of user impact):** **X2** — spec-author and build-pipeline tell the reader to copy
template files that don't resolve from the skill directory (they live at the repo root), so a standalone
install ships those skills template-less, contradicting each skill's own "used standalone, still stands"
promise.
