# live-spec — Architecture (v0.1, 2026-07-05)

How the pack is BUILT: the named nodes the spec's facts live in. Written from the proven SPEC v0.7
(record `docs/prover/2026-07-05-lost-layers.md`; the matrix cites v0.7.1 — the same proven spec after
two already-decided questions were reworded to their decided state, no rule delta), proven itself
with the architecture lens before the
test matrix was derived (record: see Prover record below). One node = one name = one responsibility —
the one-surface-one-name rule applied to structure. Kept current through SPEC v0.9.1 by assignment
(E-16 → host-contract; 2026-07-05 audit folds — no anchor delta); last full architecture-lens prove:
v0.1, 2026-07-05. [E-14]

**What "pin" means here.** live-spec is a documentation-and-skills product: its shipped artifact IS the
text. A pin therefore points to the file:line where the node's responsibility is normatively stated or
carried — every pin below comes from a grep/read actually run on 2026-07-05, none from memory. Two nodes
are [target] (spec'd, not yet code); the template allows their pin cells to start empty.

**When this doc changes:** a large or surface-class wish updates it BEFORE the matrix is touched; a bug
or small wish only cites the existing node it lands in — or assigns an orphan fact to a fitting node
(recorded here; an assignment alone triggers no re-prove). Re-proven when structure changes, not on
every landing.

---

## Nodes

Every spec fact (anchor in SPEC.md's Formal index) is OWNED by exactly one node. The one deliberate
split: the wish walk `T-1..T-7` is one index row but two responsibilities — the walk itself (T-1..T-6,
build-pipeline) and the report step (T-7, communicator); both sides are named here and in the matrix.

| Node | Responsibility (one line) | Owns spec facts (anchors) | Pinned to (file:line) |
|---|---|---|---|
| base-rulebook | shared working rules stated once + package defaults + the settings ladder | E-12, E-13, INV-5, INV-9, INV-11, INV-13, INV-14, ACT-1, ACT-2, ACT-3, M-2, M-7 | `skills/live-spec-base/SKILL.md:17` (rules), `:49` (fence), `:92` (ladder), `:101` (defaults) |
| spec-author | authoring method for a living, use-case-first, prover-ready SPEC.md | E-4, C-1 | `skills/spec-author/SKILL.md:74` (spine), `:103` (axes composition) |
| product-prover | formal review of spec and architecture; executes the push-gate re-check | M-6 | `skills/product-prover/SKILL.md:148` (review modes), `.live-spec/profile.md:6` (gate cadence instance) |
| build-pipeline | the wish lifecycle: intake → classify → spec → prove → architecture → matrix → test → code → land | E-2, T-1..T-6, T-8, T-9, T-11, INV-1, INV-2, INV-3, INV-4, INV-12, E-14, E-15, INV-15, M-1 | `skills/build-pipeline/SKILL.md:45` (steps), `:30` (entry map), `:128` (gates) |
| communicator | the human-facing exchange: reports, batched questions, decision pages | T-7 (the report step; the walk before it is build-pipeline's) | `skills/communicator/SKILL.md:26` (ten rules) |
| templates | the document shapes a host copies at bootstrap; the matrix's coverage checklist | E-3, E-5, INV-6, B-1 | `templates/TEST_MATRIX.template.md:43` (checklist), `templates/ROADMAP.template.md:1`, `templates/SPEC.template.md:58` (index) |
| attach | attaching the pack to a host: adoption phases, VCS gate, attic, skill install + version record | E-1, E-9, INV-7, INV-8, A-0, A-1, A-2, A-3, A-4, A-5, A-7, A-8, A-9 | `adopt/ADOPT.md:16` (VCS gate first), `:103` (attic), `:141` (attach record), `install.sh:2` |
| inbox | parallel-safe intake door for wishes born outside a live-spec session | E-11, T-10, INV-10 | `inbox/README.md:3` (write rule), `:9` (file format), `:14` (commit rule) |
| host-contract | the recorded settings instances: this host's profile, the human's personal profile, and the thin loader that boots the personal layer | E-8, E-16 | `.live-spec/profile.md:1` (host), personal: `~/.claude/live-spec/profile.md` (symlink → playbook repo `personal/profile.md`, its git home — row 38 landed 2026-07-05), loader: `~/.claude/CLAUDE.md:1` (thin loader live — row 52 landed 2026-07-05) |
| package-docs | live-spec's own host instance (dogfood): spec, queue, journal, resume file, version, records | S-0, M-3, M-4, D-1, D-2, D-3, D-4, D-5 | `SPEC.md:1`, `ROADMAP.md:8` (queue table), `JOURNAL.md:1`, `VERSION:1` |
| guardrails [target] | mechanical pre-push checks + surface registry + CI mirror; first slice LIVE (the pack's own gates + opt-in fence, hooks installed), host-facing checks + registry + CI still [target] (ROADMAP rows 14, 55) | E-6, E-10, M-5 | `guardrails/pre-push:1` (gates), `guardrails/pre-commit:1` (fence), `guardrails/install.sh:1`, `tests/test_guardrails.py:1`; registry/CI: — |
| snapshot [target] | saved baseline of the last accepted run; declared-scope diff (ROADMAP row 55) | E-7, A-6 | — (spec'd, not yet code) |

## Seams

The places two nodes meet — named, because that is where composition bugs live. Each seam states what
crosses it and which side owns the format.

| Seam | Between | What crosses | Format owner |
|---|---|---|---|
| spec → prove | package-docs · product-prover | SPEC.md, whole document | spec-author (the shape both sides speak) |
| prove → record | product-prover · package-docs | prover record `docs/prover/YYYY-MM-DD[-suffix].md`, folded/rejected column | product-prover |
| pipeline → shapes | build-pipeline · templates | the document shapes the steps produce, incl. the coverage checklist | templates |
| outside wish → queue | inbox · package-docs | one wish file, harvested into a ROADMAP row at sweep | inbox (file naming law) |
| attach → host state | attach · host-contract | `.live-spec/` (profile, installed versions, checkpoints home) | attach |
| base → working skills | base-rulebook · the four working skills | the inherit pin (base name + version each skill opens with) | base-rulebook |
| ladder resolution | host-contract · base-rulebook | the resolved working contract communicator reads before every exchange | base-rulebook (ladder rule); host-contract (the lines) |
| report → human | communicator · the human | plain-language report · decision page + `<project>-decisions-<date>.json` | communicator |
| checks → push [target] | guardrails · build-pipeline | pre-push verdict (red blocks the push) | guardrails |
| baseline → checks [target] | snapshot · guardrails | declared-scope diff vs baseline | snapshot |

## Prover record

| Date | Doc version proven | Record |
|---|---|---|
| 2026-07-05 | v0.1 | `docs/prover/2026-07-05-architecture.md` |

---

*Coverage rule (walked at matrix derivation): every spec anchor appears in some node's "owns" column —
an orphan fact means a missing node or a missing assignment; a node owning nothing traces to no spec
backing and is itself a finding. Mechanized in `tests/test_traceability.py`.*
