# With-skill run — product-prover scenario (2026-07-05, Sonnet worker, read the SKILL.md first, FULL mode)

Scorer's summary: the run walked the full method — TRIAGE: PROCEED → opening assessment ("needs
another iteration") → Phase 1 model (states of Player/Stem-mute/View/Export + entities + actor
assignments + five named assumptions) → Phases 2–4 with ELEVEN findings, each four-part
(headline · quoted pin · operational consequence · concrete action) and severity-tagged → CRUD +
invariants-per-state coverage tables + a NAMED authorization/security skip → Phase 5 closing: top-3,
five paste-ready properties, three open questions for the author. Substance beyond the bare run: found
the end-of-track dead-end (F5, must-fix · stuck-state) the bare run missed.

Findings register (verbatim headlines + tags):

---
F1 — No default/initial state named for view, mute, or volume — `should-clarify · missing-scenario (state-space)`
F2 — Stem-mute effect not defined across the view/export boundary — `must-fix · boundary-issue (composition)`
F3 — Fixed enumeration of 4 stems may not survive real tracks — `worth-considering · abstraction`
F4 — No snapshot guarantee for what Export actually renders — `must-fix · partial-success-risk (atomicity)`
F5 — No defined transition at end of track — `must-fix · stuck-state (liveness)`
F6 — No failure or timeout path for the export render — `must-fix · no-exit (dead-end)`
F7 — Duplicate "Export mix" clicks are unhandled — `must-fix · partial-success-risk (atomicity)`
F8 — No fallback if localStorage is unavailable — `should-clarify · hard-to-monitor (observability)`
F9 — No schema/version rule for the persisted mute state — `worth-considering · missing-rule (invariant)`
F10 — No progress indicator specified for the Rendering state — `must-fix · hard-to-monitor (observability)`
F11 — No stated ceiling on track length for export — `worth-considering · missing-rule (invariant)`
---

Paste-ready properties it closed with (verbatim):

---
- "Export mix captures stem-mute state and volume as a snapshot at the moment of the click; changes made afterward do not affect the in-flight render."
- "Only one export may be in flight at a time; a second Export mix click while Rendering is a no-op."
- "On reaching the end of the track, the player transitions to Paused with position reset to 0, and the UI reflects this immediately."
- "If a stem is muted in Detailed, that mute stays in effect after switching to Simple, and Export always uses the current mute state regardless of which view is active."
- "The default state on first load (no stored preference) is: Simple view, all stems unmuted, volume at [default value]."
---
