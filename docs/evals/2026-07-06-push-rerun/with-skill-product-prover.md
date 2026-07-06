# With-skill run — product-prover scenario (2026-07-06 push-gate re-run, model = sonnet worker, arm = with-skill, product-prover 0.1.9)

Read skills/product-prover/SKILL.md + base first; 2 tool uses. Output preserved verbatim below
(long — the full FULL-mode walk). Highlights for the scorer: triage + mode named aloud; 11 findings,
all four-part with severity tags; model + five named assumptions; coverage tables + named
authorization skip; five paste-ready properties; found the persistence-version gap (F7), the
Simple-view observability hole (F9), and the export-view seam (F8) that the bare arm missed.

Verbatim output:

---

TRIAGE: PROCEED — this is a compact but genuine feature spec with entities, state, and transitions (player, stems, views, export); enough operational content to model. Running FULL mode per the product-prover skill (v0.1.9), against the live-spec-base rulebook (v0.1.13). This is a pre-build spec, not a claim about a shipped system, so no architecture-doc node pins are required before reviewing.

## Opening assessment

This spec describes a small, self-contained stem player: master transport (play/pause/volume), four persistent stem mutes, a two-tier view switch, and a background export-to-WAV. The two things working well: the view relationship is a clean superset (Detailed = Simple + stems, matching a monotonic view ladder), and every visible control name is already plain product language with no leaked internal terms. The two things that need attention before build: the export flow has no defined job semantics (what state it captures, what happens on a repeat click, what happens on failure), and the persistence rule for stem mutes names *that* it persists but not *what scope* it persists at (per track, or globally) or what happens to old data across a version change. Overall: needs another iteration — the core interaction is simple and buildable as-is, but export and persistence need explicit rules before code, or the implementer will silently pick answers that may not match intent.

## Phase 1 — The model

States of Player (transport):
1. Paused — entered on load (default not stated) or after Pause; exits to Playing (Play).
2. Playing — entered on Play; exits to Paused (Pause) or, at track end, to an undefined next state.

States of Stem (one per {drums, bass, vocals, other}):
1. Unmuted — entered by default (default not stated) or after un-mute; exits to Muted (mute button, Detailed view only).
2. Muted — entered by mute button; exits to Unmuted (mute button); persists to localStorage and restores as the entering state on reload.

States of View:
1. Simple — entered by default (default not stated) or by switching from Detailed; shows transport + volume only.
2. Detailed — entered by switching from Simple; shows transport + volume + 4 stem mute controls; switch is instant both ways.

States of Export:
1. Idle — entered by default, or after a prior export completes/fails (not stated); exits to Rendering (click "Export mix").
2. Rendering — entered on click; exits to Ready (render completes) — no Failed state is defined.
3. Ready — download link shown; no stated exit (can the user export again from here, and what happens to this link then?).

Entities and relationships:
- Track: the loaded audio; exact loading mechanism out of scope for this spec (assumed).
- Player: one transport (play/pause, volume) per Track.
- Stem: 4 fixed instances per Track (drums, bass, vocals, other), each with its own mute state.
- View: a display mode, not persisted data — controls which of the above are shown.
- Export job: a background process reading some snapshot of Player + Stem state, producing a WAV + link.
- Persisted record: stem mute states in localStorage, restored on reload.

Actor-action assignments:
- Play / Pause / adjust volume / toggle stem mute / switch view / click "Export mix" — the user.
- Render the WAV, write/read localStorage — the app (automated).

What I assumed:
- Every track always has exactly the same 4 stems; the spec doesn't address a track that lacks one.
- "The app" performing export is a single client-side process; no server, no accounts, no multi-user concerns — a single-user local tool.
- Track loading/selection is out of scope for this spec (the doc starts from "a track" already present).
- Out of scope: seeking/scrubbing, per-stem volume, formats other than WAV, undo, offline sync.
- I read "Switching views is instant" as a UI/perf guarantee only, not as a guarantee that playback or mute state is preserved across the switch — that guarantee is not actually stated (see F9).

## Phase 2 — Structural issues in the model

F1 — The 4-stem structure is assumed fixed for every track, with no accommodation for variation

> "mute any of 4 stems (drums, bass, vocals, other)" — the spec's stems clause

If a real track's stem separation produces fewer usable stems (e.g., no vocal content, or a source that only splits into 3), the model has no state for a missing stem — the implementer must guess whether to hide, disable, or fake that control. A user opens a track with no vocal content and sees a "vocals" mute button that does nothing, or the app crashes finding a stem file that doesn't exist.

State whether the 4 stems are guaranteed to always exist for every track, or add a per-stem `available` state distinct from `muted` that the UI reads before rendering that control.

`should-clarify · missing-scenario (state-space)`

F2 — Export's job semantics — what it captures, and what a repeat click does — are entirely unspecified

> "the app renders the current mix to a WAV in the background and shows a download link when ready" — the spec's export clause

Three related questions have no answer, and they're the same underlying gap (no defined snapshot/job boundary), so grouping them as one class: (a) does "current mix" freeze mute/volume state at the instant of the click, or does a mute toggled mid-render affect the file being written; (b) if the user clicks "Export mix" again while one render is in progress, does it queue, replace, run in parallel, or is the button disabled; (c) once a second export finishes, does the first download link stay valid, get replaced, or become orphaned. A user who mutes vocals right after clicking Export, expecting the file to reflect that, may get a mix with vocals still present — or the opposite — with no way to tell which happened from the UI.

Add one explicit rule per sub-case: (a) state the snapshot instant (recommend: capture at click time, later changes don't affect the in-flight render); (b) pick one of disable-button / queue / replace-in-progress-job for a repeat click (recommend: disable until Ready or Failed, simplest to build and reason about); (c) state whether a new export invalidates the previous link (recommend: yes, only the latest link is shown).

`must-fix · missing-rule (atomicity)`

F3 — No failure or rollback path for the export render

> "renders the current mix to a WAV in the background and shows a download link when ready" — the spec's export clause

Only a success path is described. If the render fails (decode error, out of memory on a long track, tab backgrounded/killed by the OS mid-render), the state machine has no Failed state — the spec doesn't say the user sees an error, can retry, or that Rendering ever resolves. A user who clicks Export on a long track and gets nothing back has no way to know whether it's still working or silently died, and no retry action is defined.

Add a Failed state reachable from Rendering, with a user-visible error and a retry action (re-click Export mix from Idle/Failed).

`must-fix · unclear-recovery (rollback)`

F4 — Playback behavior at the end of a track is unspecified

> "The player plays a track with play/pause" — the spec's playback clause

Play/pause and their toggle are named, but there's no third case: what happens when playback reaches the end of the track. Stop-and-return-to-start, hold on the last frame, loop, or something else are all consistent with the stated text. A user reaches the end of a track and the transport UI is left showing "Playing" indefinitely with no audio, or the track silently loops when the user expected it to stop.

State the end-of-track transition explicitly (recommend: stop and return to Paused at position zero, matching typical player expectations; loop only if the product intends a loop feature, which isn't mentioned).

`should-clarify · no-exit (liveness)`

F5 — No default/initial state for play/pause, volume, or view on first load

> "The player plays a track with play/pause and a volume slider." / "two views: Simple ... and Detailed" — the spec's playback and views clauses

Neither clause states what the transport shows before the user takes any action: paused or already playing, what starting volume, and which of Simple/Detailed is the default view. This differs from stem mutes, which the spec does pin down (persisted, restored). Two users opening the app for the first time could see genuinely different starting states depending on what the implementer assumed, with no way to tell which is "correct."

State the initial values: recommend Paused, a fixed default volume (e.g., a clearly stated level, not silence), and Simple as the default view (Detailed being the "expert" tier).

`should-clarify · missing-prerequisite (precondition)`

F6 — Persistence is stated for stem mutes only, and with no key scope, leaving both "what persists" and "persists for what" undefined

> "mute states persist in localStorage and restore on reload" — the spec's stems clause

Two related gaps in the same persisted-state design: first, volume and play/pause aren't named as persisted or as reset-per-session, so it's unstated whether reload restores everything or only mutes; second, the persistence key isn't scoped to a track — if the user mutes vocals on Track A, opens Track B, the model as written gives no basis for whether Track B shows vocals muted too (shared key) or unmuted (per-track key, not yet stored). A user who intentionally muted drums on one track then opens a different track and hears it unexpectedly drums-muted (or the reverse expectation) has no documented behavior to point to as a bug or a feature.

State that stem mutes persist keyed by track id (recommend), defaulting to Unmuted for a track with no stored record, and explicitly state that volume/play-state are session-only (reset on reload) or also persisted — pick one and say so.

`must-fix · missing-rule (invariant)`

F7 — No migration/compatibility rule for the persisted mute data across a future shape change

> "mute states persist in localStorage and restore on reload" — the spec's stems clause

If a later version changes the stem set (renames "other," adds a 5th stem, changes the storage key format), the spec gives no rule for what happens when older stored data meets the newer UI — read-and-ignore unknown keys, clear on mismatch, or attempt a migration. This is exactly the class of bug where a user reopens the player after an update and either sees stale/partial mute state or a broken control bound to a stem that no longer exists.

Add one line: on version/shape mismatch, ignore unrecognized stored keys and fall back to default-unmuted for any stem missing a stored value (simplest, no migration code needed) — or, if a stricter guarantee is wanted, version the storage key and clear on mismatch.

`should-clarify · persistence-and-versions`

F8 — Which view "Export mix" is available from is not stated

> "Export: the user clicks "Export mix"" — the spec's export clause

The export action is described independently of the two-view model, so it's unclear whether the button exists in Simple, Detailed, or both. Since Detailed ⊇ Simple in every other respect (F1a of the view ladder), this is the one place the spec breaks that pattern by not saying. A user who only ever uses Simple view may not have an export path at all, or the implementer places it inconsistently across the two views.

State that "Export mix" is visible in both views (consistent with the ladder: Simple keeps Detailed's core actions available), or explicitly restrict it to one view with a reason.

`should-clarify · undefined-path (transitions)`

## Phase 3 — Property analysis

F9 — A user in Simple view has no way to see or explain why muted stems (restored from a prior session) make playback partially or fully silent

> "Simple (play/pause and volume only)" — the spec's views clause

Because stem mutes persist and restore silently (per the stems clause), a user can reopen the player, land in Simple view by default, hit Play, and hear less than expected — or nothing at all if all 4 stems are muted from a prior session — with no indicator in Simple view that any stem is muted and no control there to fix it. The user has to guess to switch to Detailed to find out why, which most won't do on their own.

Add a visible indicator in Simple view when one or more stems are muted (e.g., a small "3 of 4 stems audible" note or icon), even without exposing the individual mute controls there.

`should-clarify · hard-to-monitor (observability)`

Coverage tables:

| Entity | Create | Read | Update | Delete | Notes |
|---|---|---|---|---|---|
| Stem mute (per stem) | implicit, first toggle | covered (restore on reload) | covered (toggle) | missing | no "reset all mutes" action stated |
| Export / WAV | covered (render on click) | covered (download link) | n/a | missing | no rule for what happens to a prior link when a new export runs (F2) |
| Player transport (play/pause, volume) | missing (no stated default, F5) | covered | covered | n/a | not stated as persisted or session-only (F6) |

Invariants per state:

| State | Invariants stated | Invariants missing |
|---|---|---|
| Playing | none named | must define what happens at track end (F4); must reflect live stem mutes regardless of active view (implied, not stated) |
| Paused | none named | default state on load (F5) |
| Stem: Muted | persists across reload | scope of persistence — per-track vs global (F6); behavior on shape/version mismatch (F7) |
| Export: Rendering | produces a WAV and shows a link when ready | snapshot boundary (F2); no Failed state (F3); no repeat-click rule (F2) |

Authorization: not applicable — this is a single-user local player with no accounts, roles, or shared data described anywhere in the spec.

## Phase 3.5 — Acknowledged gaps

No explicit Open Items or TBDs in the document.

## Phase 4 — Human and operational factors

F10 — No stated duration budget or progress feedback for the export render

> "renders the current mix to a WAV in the background and shows a download link when ready" — the spec's export clause

There's no stated ceiling on track length/duration the export needs to handle, and no progress indicator between click and "ready" — only a binary Rendering → Ready. On a long track, a user watching an unchanging "Export mix" state with no progress cue has no way to distinguish "still working" from "stuck," and may click again (feeding directly into F2's undefined repeat-click behavior) or abandon the export assuming it failed.

State an assumed ceiling for supported track length (e.g., the longest track the product expects to handle) and add a progress indicator or at minimum an elapsed-time/spinner state distinct from Idle.

`worth-considering · hard-to-operate (ops-ux)`

F11 — localStorage write failure or unavailability isn't addressed

> "mute states persist in localStorage and restore on reload" — the spec's stems clause

Private/incognito browsing, storage quota limits, or a user clearing site data can all make the localStorage write silently fail or wipe prior state. The spec doesn't say whether mute toggling still works in-session when persistence fails (degraded but functional) or whether the user should see any indication that their mutes won't survive a reload.

State that mute toggling always works for the current session regardless of persistence success, and that a persistence failure is silent to the user (acceptable for a single-user local tool) rather than surfaced — or surface it, if silent data loss across reloads is considered worth flagging.

`worth-considering · dependency reality`

Security/privacy: out of scope by nature of the product (single-user local tool, no accounts, no network transmission described) — named here as an explicit skip, not an oversight.

Domain language: every user-facing string in the spec (Play/Pause, volume, mute, Simple, Detailed, Export mix) is already plain product language; nothing to flag.

## Phase 5 — Closing summary

Top 3 to fix before development:
1. F2 — define Export's snapshot boundary, repeat-click behavior, and link-replacement rule.
2. F3 — define the export Failed state and retry path.
3. F6 — define whether stem mutes are scoped per-track and what persists vs. resets each session.

Properties that should be stated explicitly in the doc:
- "Clicking Export mix freezes the current stem-mute pattern (and volume level, if included in the export — state which) at that instant; changes made after the click do not affect the render already in progress."
- "Only one export renders at a time; clicking Export mix while a render is in progress is disabled until the current render reaches Ready or Failed."
- "Every Rendering state reaches either Ready or Failed; there is no Rendering state that never resolves."
- "When playback reaches the end of the track, the player stops and returns to Paused at the start position."
- "Stem mute state is stored keyed by track id; a track with no stored record defaults every stem to Unmuted."

Open questions where only the author can decide:
- Should "Export mix" be reachable from Simple view, Detailed view, or both?
- Is the exported WAV rendered at the current master volume level, or always at a fixed unity gain regardless of the slider?
- Is stem-mute state meant to be shared across all tracks (one set of 4 toggles) or private to each track?

Overall readiness: needs another iteration — the transport/mute/view core is simple and close to buildable as stated, but the export flow and the persistence scope need explicit rules before code, or an implementer will silently pick answers on both that may not match intent.
