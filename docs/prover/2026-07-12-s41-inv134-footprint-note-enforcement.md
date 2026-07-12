# Prover record — INV-134 (footprint-note enforcement) — 2026-07-12 s41

Prover skill version at this pass: product-prover 1.0.6. Mode: CROSS-LINK short form (SPEC INV-61 — small
delta, infra kind, no new user-facing surface; the new law's homes are the spec clause, the ROADMAP
template, and a suite check).

## The delta

One invariant, INV-134: a landed feature-or-refactor row carries its `footprint:` note, and a suite check
reads the queue (ROADMAP.md) and reddens a landed feature-or-refactor row that omits it. This is the
mechanical floor under the footprint read INV-128 states, built to the same shape the delegation-accounting
check [INV-103] gives the routing rule [INV-69]. It binds forward from the footprint read's own landing
(2026-07-12 ~17:01, when INV-128 landed), rows landed before it staying as they landed. Homes: the
enforcement clause after INV-128 + Formal index; the ROADMAP row template's footprint field; the capture
echo (already carrying the field from INV-128); the suite check `tests/test_footprint_note.py`. Owning node:
build-pipeline (owns-list + M-275).

## Previous record's unfolded rows

`2026-07-12-s40-inv133-critical-preempt-bound.md` — 0 must-fix, clean. No carry.

## Findings

**0 must-fix.** Cross-link checks walked:

- Index density, owning node, matrix-row-under-owner all hold: the Formal-index row INV-134 is present; the
  build-pipeline node's owns-list carries INV-134 beside INV-128 (the read it enforces) and INV-103 (the
  sibling mechanical check); matrix row M-275 sits under the recent-method block and cites INV-134.
- Composition against every neighbour named. INV-128 (the footprint read) is the read this holds; the new
  clause adds no new footprint semantics, only the mechanical floor INV-128 explicitly deferred to a
  follow-on row — no contradiction, a promised completion. INV-103 (the delegation-accounting check) is the
  structural template: same queue-scan shape, same forward-binding idea, same "prose states it, a check
  holds it" division; the two checks are independent (different notes, different homes) and do not overlap.
  INV-16 (the door law) is untouched — the check is scoped to the door verdict (feature/refactor) the row
  already carries; it reads the door, never sets it, so it cannot demote or promote a door.
- Forward-binding boundary examined for a false-red / false-green. INV-103 could bind from the bare date
  because delegation lines predated their check; INV-128 landed only mid-session-40, so a bare-date bind
  would false-red ~39 rows that legitimately predate the footprint concept. The cut is INV-128's own
  landing moment (~17:01 that day): rows at/after it owe the note, earlier rows stay. The single-day
  time-granularity carve is bounded — 2026-07-12 does not recur, and every later date owes the note whole,
  so the only place the ~HH:MM stamp matters is the one cutoff day. No forward feature/refactor row can
  evade on a future date.
- False-green closed: the check matches the `footprint:` note itself (colon plus one of the three values),
  not the bare word "footprint", which prose uses freely (row 259's own status reads "footprint HELD"). An
  early red-proof was foiled by exactly that looseness until the match was tightened, so the tooth is real,
  demonstrated by stripping row 259's note and watching the scan go red.
- Scope: the check covers feature/refactor doors (the Done-when's scope), leaving docs-only/skip/bug rows
  out — consistent with the footprint read mattering most where steps run and reach is sized.

## Verdict

CROSS-LINK clean, 0 must-fix. The delta is the mechanical completion INV-128 deferred; it introduces no new
footprint semantics, only enforcement, and composes cleanly with INV-128/INV-103/INV-16. Suite green at 553.
