# Audit pass 3 of 3 — architecture lens + surface composition (0.8.0 milestone)

Date: 2026-07-05 night · Reviewer: product-prover (architecture lens) · Docs in view: ARCHITECTURE.md
(v0.1), SPEC.md (v0.14.0), all five skill SKILL.md, guardrails/, ADOPT.md, ROADMAP.md + queue archive,
matrix, decision pages, checkpoints, installed skills at `~/.claude/skills/`.

**Outcome: FOLDED (same sitting)**

This pass also discharges the deferred re-prove of the NEW `design-sync [target]` node (a structure change
whose architecture-lens re-prove ARCHITECTURE.md/row 84 explicitly parked on tonight's milestone audit).

---

## Verdict

The architecture holds. Anchor ownership is mechanically clean — every Formal-index anchor is owned by
exactly one node, no node stands without spec backing (`test_architecture_owns_every_anchor_once`, 35/35
green). The doors / facets / fences / intake-trio / founding ownership assignments (T-12..T-15,
INV-16..INV-21, B-2 → their nodes) are each under the RIGHT owner. The new `design-sync` node is rightly
SEPARATE from guardrails and snapshot. Installed skills match the repo exactly. The queue-archive split is
essentially complete and INV-1 is preserved.

Six findings, all `should-clarify` or below — no `must-fix`. The two that most deserve action this
milestone: the design-sync node ships with **no seam named** (F-A1), and E-18 is **[target] in the
architecture but BUILT in the matrix** (F-C1). Nothing blocks the milestone; these are consistency and
hygiene items a compaction pass closes.

---

## design-sync node — the deferred structure re-prove

**Rightly separate? YES.** design-sync's responsibility (optional · human-gated · publishes declared
components to an external team-review channel · SUPPLEMENTS the in-session render, never gates it) is
distinct from snapshot (saves a baseline and diffs declared scope to BLOCK an undeclared landing) and from
guardrails (mechanical RED/GREEN pre-push checks that BLOCK). They share only the declared-scope INPUT, not
a responsibility. Folding design-sync into either would conflate an external publish with a red/green
landing gate — one-name-one-responsibility keeps them apart. Keep the node.

**Seam missing? YES — see F-A1.** The other two [target] nodes each carry a [target] seam; design-sync
carries none.

**The two crossings the task flagged:**
- *host profile* — design-sync's on/off switch is just a setting; it resolves through the EXISTING
  `ladder resolution` seam (host-contract · base-rulebook). No NEW seam needed at [target] stage; a
  one-line note that the switch rides that seam would remove the doubt.
- *communicator's show rule* — the sync publishes rendered cards to a review channel that supplements
  what communicator shows in-session. Whether it flows THROUGH communicator is a genuine design question
  that can wait for the wiring row (93). Not required at [target] stage.
- *the crossing that IS required now* — design-sync ↔ the human: the per-sync publish gate crosses an
  irreversibility / publish boundary (base rule 17 + ACT-1). That is the seam to name today.

---

## Findings

| ID | Severity | Category | Headline |
|---|---|---|---|
| F-A1 | should-clarify | boundary-issue (composition) | design-sync node has no seam named, unlike the other two [target] nodes |
| F-C1 | should-clarify | internal-conflict (consistency) | E-18 is [target] in ARCHITECTURE but marked BUILT in matrix M-080, while the parallel [target] machine E-6 is TODO |
| F-A2 | worth-considering | hard-to-monitor (observability) | ARCHITECTURE header says "current through SPEC v0.10.0" but SPEC is v0.14.0 |
| F-A3 | worth-considering | hard-to-operate (ops-ux) | architecture pin line-caches drifted +7..+13 across most nodes tonight |
| F-A4 | worth-considering | unclear-owner (abstraction) | B-2 (founding questions) owned by attach while its sibling bootstrap fact B-1 sits in templates |
| F-C2 | worth-considering | persistence (state-space) | row 39 still in the ACTIVE queue with a status that reads terminal ("prototype landed") |

### F-A1 — design-sync node ships with no seam named

> "design-sync [target] | optional machine: declared components of a landing synced to the team's design
> project, human-gated" — ARCHITECTURE.md / Nodes; and the Seams table contains no design-sync row.

The pack's own practice is that a [target] node still names its seams before it is code: snapshot carries
`baseline → checks [target]` and guardrails carries `checks → push [target]`. design-sync carries none,
though E-18 states three crossings — the switch home in package defaults, the recorded host-profile line,
and (most important) a human-gated publish OUTSIDE the machine. A publish that crosses an
irreversibility/publish boundary with no seam is the one place a composition bug hides unnamed: at the
wiring landing (row 93) nobody has a named place that says who owns the render format sent out and who
holds the gate.

Add one seam row now, matching snapshot/guardrails: `sync → design project [target]` · between
`design-sync · human` · what crosses = the declared-component render cards + the per-sync human gate ·
format owner = design-sync. Optionally a one-liner noting the on/off switch rides the existing
`ladder resolution` seam so the host-profile crossing is not read as unhandled.

`should-clarify · boundary-issue (composition)`

### F-C1 — E-18 is [target] in the architecture but BUILT in the matrix

> "| M-080 | Design-sync: optional machine … human-gated publish … | E-18 | string | machine lands at
> row 93; clause presence: `test_spec_states_founding_and_designsync` | BUILT |" — TEST_MATRIX.md

E-18 is [target] in ARCHITECTURE (pin `—`, "not yet code") and [target] in SPEC, yet its matrix row is
**BUILT**. It is BUILT only in the sense that its string-level clause-presence test exists — but the
parallel [target] machines are marked differently: E-6 host-facing guardrails is **TODO** at M-060 ("first
slice BUILT … host-facing await"), ACT-3 router is **TODO** at M-010. A milestone reader scanning matrix
statuses sees design-sync = BUILT the same evening the node was added and can read the machine as shipped.
This is a cross-surface inconsistency in how "done" is represented for [target] machines.

Mark M-080 **TODO** with "clause present; machine lands row 93" in the notes, matching M-060 / M-010 — or
adopt ONE explicit convention across the matrix for [target]-machine rows whose only test today is clause
presence (e.g. a `TODO (clause BUILT)` marker). One convention, applied to every [target] row.

`should-clarify · internal-conflict (consistency)`

### F-A2 — architecture header carries a stale version label

> "Kept current through SPEC v0.10.0 by assignment (…the doors landing…; the facet-sweep landing…; the
> fences landing…; the intake-trio landing…; the founding/design-sync landing 2026-07-05 night…)" —
> ARCHITECTURE.md, opening paragraph.

The prose lists the v0.11–v0.14 landings by name, but the version LABEL still reads v0.10.0 while SPEC is
v0.14.0. A reader trusting the label thinks the doc trails four spec versions when it is in fact current.

Change "through SPEC v0.10.0" to "through SPEC v0.14.0" (the landings it already enumerates).

`worth-considering · hard-to-monitor (observability)`

### F-A3 — pin line-caches drifted across most nodes tonight

Spot-checking ~23 pins by opening the pinned file:line: the named thing every pin points at still resolves,
but the cached `:line` has drifted after tonight's insertions —

- spec-author: all 5 pins +7 (spine 75→82 · [target] 100→107 · axes 112→119 · fences 144→151 ·
  facet-list 159→170)
- base-rulebook: ladder 114→127 · defaults 141→154 (the new rule 17 "Irreversible means gone" pushed them
  ~13 lines)
- communicator: ten-rules 27→33 · build-pipeline: steps 58→67 · ADOPT: unbacked-verdict 100→106 · attic
  110→117 · attach-record 148→159

Every drift is within the pin-drift gate's ±25 window, so `check-pin-drift.sh` passes even in `--strict`
(all 23 named things resolve) — the gate is NOT broken, and per E-14 the `:line` is an explicitly-tolerated
cache. But a milestone (M-1: "the derived docs' headers re-pinned … then proven") is exactly when the
caches are refreshed; this is precisely the "7 of 17 pins drifted in one session" pattern row 90 built the
gate to notice.

Batch-refresh the `:line` caches this milestone (re-grep each named thing). No ownership change — hygiene.

`worth-considering · hard-to-operate (ops-ux)`

### F-A4 — the two bootstrap facts split across two nodes with no rationale note

> "B-2 → attach" (ARCHITECTURE Nodes / attach owns) vs "B-1 → templates" (templates owns); both index-homed
> in "Bootstrap."

B-2 (founding questions) lands in `attach` while its sibling bootstrap fact B-1 (templates → gate → first
wish) lands in `templates`, and there is no bootstrap node. The assignment is DEFENSIBLE — B-2 is a process
rule shared with adoption (A-1 owes the same questions at orient), and templates owns document SHAPES not
processes — so co-locating B-2 with the adoption node that already references it is sound. But a reader
hunting the founding-questions owner won't look under "attach," and the split has no note (unlike the
explicit T-1..T-7 split note the doc already carries).

Add one line to the Nodes preamble's split rationale: bootstrap facts split B-1 → templates (the shape) /
B-2 → attach (the founding-questions process, shared with adoption A-1). No reassignment.

`worth-considering · unclear-owner (abstraction)`

### F-C2 — a straggler terminal row in the active queue

> "| 39 | Interactive decision page … | surface · quick win | prototype landed 2026-07-05 | … Mechanism
> folded into communicator … landed 2026-07-05 |" — ROADMAP.md (ACTIVE table)

The archive split is otherwise clean: 63 rows moved verbatim to `docs/queue-archive/2026-07-05.md`, the
active header states it holds only the active queue, INV-1 preserved. Row 39 is the lone active row whose
status reads terminal ("prototype landed … landed 2026-07-05"). Either the wish landed and the row should
have archived with its siblings, or the full feature beyond the prototype is still open and the status
should say so. (Rows 55/57/63/64 flagged by a word-grep are false positives — all "queued".)

Confirm row 39's exit: if landed, move it to the archive; if the non-prototype work remains, restate the
status so it does not read as landed.

`worth-considering · persistence (state-space)`

---

## Verified clean (no finding)

- **Anchor ownership** — every index anchor owned by exactly one node, no orphan nodes; mechanically green
  (`test_architecture_owns_every_anchor_once`). The one deliberate split (T-1..T-7 across build-pipeline +
  communicator) is named in both the doc and the matrix.
- **Ownership assignments under the right owner** — T-12/INV-16 → build-pipeline (door is a classify step)·
  E-17 → base-rulebook (prototype = shared discipline) · INV-17 → guardrails (the fence MACHINE) · A-10 →
  attach (adoption verdict) · T-13/INV-18 + T-14/INV-19 + INV-20/INV-21 → spec-author (all authoring:
  facet sweep, fence-authoring, the delta's closing sentences) · T-15 → build-pipeline (appetite = intake
  rider) · E-18 → design-sync. All correct.
- **Installed vs repo skills** — exact match: live-spec-base 0.1.7, spec-author 0.1.7, product-prover
  0.1.6, build-pipeline 0.2.6, communicator 0.1.7; all four working skills' installed copies pin base
  v0.1.7. Tonight's "installed copy synced" discipline held — no stale-boot hole. (Standing fragility, not
  a tonight-hole: the repo ↔ `~/.claude/skills/` sync is manual with no guardrail asserting the two homes
  agree; the sync command is owned by row 51, package-is-source per D-4.)
- **Two sessions / lane token** — INV-2 + INV-11 hold; `test_roadmap_single_in_work` passes (≤1 in-work).
- **Decision pages** — `docs/decisions/` holds the archived round-trip JSONs (2026-07-05-decisions.json,
  -2.json); provenance intact (communicator owns the format).
- **[default] tag** — 4 occurrences, all descriptive of the mechanism (the pack's own spec DECIDED every
  facet, so no real taken-default); grep-ability is spec'd but simply unexercised on the dogfood spec.
  Expected, no finding.

---

## Actions this outcome implies

1. After folding F-A1/F-C1 (and optionally F-A2/F-A3/F-A4/F-C2), add a Prover-record row for the
   design-sync structure re-prove (this pass) — the doc's own rule requires it once the node ADD is proven.
2. F-A3 pin refresh + F-A2 header bump are pure hygiene; fold in the same compaction pass.

All six findings folded same sitting by the senior: F-A1 seam row added; F-C1 M-080 -> TODO (E-6 convention); F-A2 header re-versioned; F-A3 full milestone re-pin (16 pins refreshed, drift gate green); F-A4 B-1/B-2 split noted in the header; F-C2 row 39 archived. Design-sync structure re-prove recorded in the architecture doc's Prover record table.
