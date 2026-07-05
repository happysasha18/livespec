# Wish: bless "surface registry as an EXECUTABLE GATE" as the preferred E-10 form

## The wish (plain words)
E-10 / ADOPT Phase 2 prescribe a `SURFACE_REGISTRY.md` document. Where the host has a test harness,
the stronger form is a registry that is CODE: a declared map of every user-facing surface (id →
render-condition → owning gate test) inside a completeness-gate test, so that (a) a surface that
renders but isn't registered turns the suite RED automatically, and (b) a registered surface that
comes out empty in a real render turns it RED too. The .md registry rots silently when someone adds a
panel and forgets the doc; the executable one cannot — the mismatch IS a failing test. Suggest the
pack: keep the .md as the fallback for doc-only hosts, name the executable form as preferred, and
have ADOPT Phase 2 say "lift the inventory into the gate test if a harness exists (or seed one)".

## Why (what broke / what was missing)
Nothing broke — the opposite: during track-coach's adoption pass (2026-07-05) the walk found it has no
SURFACE_REGISTRY.md, and creating one would have been a step BACKWARDS: its registry already lives as
`USER_SURFACES` in `tests/test_completeness_gate.py` (INV-46), where a scan of the real rendered
widget cross-checks every id both directions (rendered-but-unregistered = red; registered-but-empty =
red). That mechanism has caught real silent-empty-surface regressions. The adoption checklist should
recognise this form as satisfying E-10 — and recommend it — rather than reading "no registry file" as
a gap.

## Who threw it
The track-coach session, live-spec adoption pass, 2026-07-05.
