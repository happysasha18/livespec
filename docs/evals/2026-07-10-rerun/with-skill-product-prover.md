# With-skill run — product-prover scenario (2026-07-10 rerun, model = sonnet worker, arm = with-skill, FULL mode, product-prover 0.1.15)

Read skills/product-prover/SKILL.md directly (Read tool, not the Skill tool); 1 tool use.

Verbatim output:

---

Running in **FULL** mode (product-prover, whole-document review — every phase, no scope narrowing).

## Phase 0 — Triage

**TRIAGE: PROCEED** — this is a short feature spec with clear entities (player, stems, views, export job), states (play/pause, mute/unmute, view, render), and transitions; enough operational content to model and stress-test.

## Opening assessment

This describes a browser-based stem player: master playback and volume, four independently mutable stems, a persisted mute state, a two-density view toggle, and a background WAV export. The core interaction loop (play, mute a stem, switch views) is simple and well-scoped, and naming the four stems concretely (drums, bass, vocals, other) instead of leaving "stems" abstract is a good, buildable choice. The two things needing attention before this is ready: the export flow has no defined behavior for failure, concurrency, or "what exactly gets captured," and the persistence promise is written for only one of several pieces of state that a reload naturally raises questions about. Neither is a redesign — both are a handful of sentences the author can add. Overall: needs another iteration, mainly around the export path and the reload/persistence story.

## Phase 1 — The model

**Entities and relationships:**
- Track: the audio content being played; one active track assumed (spec never mentions loading, switching, or multiple tracks).
- Player: holds transport state (playing/paused) and master volume.
- Stem: one of exactly 4 (drums, bass, vocals, other), each with an independent mute flag; belongs to the current Track.
- View: Simple or Detailed; a display mode over the same underlying Player + Stem state, not a separate entity with its own data.
- Export job: created by the "Export mix" action; produces a WAV artifact and a download link.
- Persisted record: the stem mute flags, written to and read from localStorage.

**States of Player:**
1. Paused — entered on load (assumed) or via pause; exits to Playing (play).
2. Playing — entered via play; exits to Paused (pause).

**States of Stem (per stem, independently):**
1. Unmuted — default (assumed); exits to Muted (mute action).
2. Muted — exits to Unmuted (unmute action).

**States of View:**
1. Simple — entered by default (assumed) or by switching; exits to Detailed (switch action).
2. Detailed — exits to Simple (switch action).

**States of Export job:**
1. Idle — entered on load, or after a completed export (assumed); exits to Rendering (click "Export mix").
2. Rendering — exits to Ready (render completes). No stated exit for failure.
3. Ready — download link shown; no stated further transition (can the user export again? not stated).

**Actor-action assignments:**
- "Play / pause" — user.
- "Adjust volume" — user.
- "Mute / unmute a stem" — user.
- "Switch view" — user.
- "Click Export mix" — user.
- "Render mix to WAV" — the app (automated, background).

**Composition:** Player, Stem set, and View are tightly coupled (View is a lens over the same shared state, not a separate store); Export job reads from that shared state to produce an artifact. The only persistence boundary is stem mutes to localStorage.

**What I assumed:**
- A track is already loaded before any of this begins — the spec has no load/upload/select-track flow, so I treated track acquisition as out of scope rather than a gap.
- Default states before any user action: Player starts Paused, all stems start Unmuted, view starts Simple, export starts Idle. None of these defaults are stated; I inferred the "obvious" ones.
- Volume is a single master volume, not per-stem (only mute is per-stem) — the spec says "a volume slider," singular, alongside per-stem mute only.
- "Instant" view switching means no loading state or animation is needed for the switch itself, not a promise about audio continuity.

## Phase 2 — Structural issues in the model

F1 — No initial/no-track state is modeled, so "Play" has no stated precondition

> "The player plays a track with play/pause and a volume slider."

The spec opens as if a track is already present and playable, but never says how one gets there or what Play does before that's true. If a build team treats this literally, a user opening the app before a track is loaded (or after a track fails to load) hits a Play control with undefined behavior — nothing happens, an error, or a crash, depending on what the implementer guesses.

Add one sentence stating the precondition: either "a track is always provided before this screen is reachable" (making load explicitly out of scope, and say so), or describe the no-track state and what Play does then.

`should-clarify · missing-prerequisite (precondition)`

F2 — Simple view can silently play a mix altered by mutes it never shows, with no way to see or undo them there

> "Simple (play/pause and volume only)" ... "Detailed (adds the 4 stems with mute buttons)"

A user who muted drums and vocals in Detailed, then switched to Simple to just listen, hears a sparse mix with no indicator anywhere in Simple that anything is muted, and no control in Simple to fix it. They're left thinking the track itself sounds wrong, or that Simple is broken, with no path back except remembering to reopen Detailed.

State explicitly whether Simple shows a lightweight indicator when any stem is muted (e.g., a small "2 muted" badge linking to Detailed), or whether Simple is deliberately a pure playback-only reduction and that's an accepted tradeoff — either is fine, but it needs to be a decision, not silence.

`should-clarify · confusing-for-users (cognitive-load)`

F3 — No default mute state is defined for the very first run, before any localStorage entry exists

> "mute states persist in localStorage and restore on reload"

The spec covers restoring a mute state that already exists, but not what a stem's mute flag reads as before one has ever been written — first install, cleared browser storage, or a new device. If the read code doesn't special-case "no record yet," it could throw, or arbitrarily default to muted rather than unmuted.

State the default explicitly: "absent a stored value, all four stems start unmuted."

`should-clarify · missing-prerequisite (precondition)`

## Phase 3 — Property analysis

**3a/3b/3c — safety, liveness, enforceability**

F4 — Export doesn't say whether it captures a snapshot at click-time or reads live state during the async render

> "the app renders the current mix to a WAV in the background and shows a download link when ready"

A user clicks Export mix, then — while the render is still running in the background — mutes another stem or nudges the volume. Whether the resulting WAV reflects the mix as it stood at the click, or picks up that later change mid-render, is unstated. Either answer is defensible, but as written the output could correspond to neither the mix the user heard before clicking nor the mix they set afterward — a file nobody actually asked for.

State that "current mix" means a snapshot of stem-mute and volume state taken at the moment Export mix is clicked; later changes affect live playback and any future export only.

`must-fix · partial-success-risk (atomicity)`

F5 — No failure, timeout, or retry path for the background render

> "renders the current mix to a WAV in the background and shows a download link when ready"

If the render stalls or errors (resource limit, backgrounded tab, unexpected input), there is no defined Failed state. The user is left watching a screen with no download link and no error message, with no way to tell whether it's still working or dead.

Add an explicit Failed state: a shown error message, a retry action, and a maximum render duration after which a non-completing job is marked failed rather than left pending indefinitely.

`must-fix · stuck-state (liveness)`

**3e — generative stress-testing**

F6 — Concurrency: a second "Export mix" click while one render is already in progress is undefined

> "the user clicks \"Export mix\""

Nothing says what happens if the user clicks Export mix again before the first render finishes — most likely out of impatience on a longer track. Whether this starts a second concurrent render, queues, is silently ignored, or races the first job for the same output slot is unstated.

Define the button's busy state while a render is running (disabled or visibly "Rendering…"), and state that a repeat click while busy is a no-op, unless an explicit cancel-and-restart is intended.

`should-clarify · undefined-path (transitions)`

F7 — Persistence and versions (sibling-instance sweep): the reload question is answered for stem mutes but left open for every other piece of session state

> "mute states persist in localStorage and restore on reload"

This is a class, not a single point: the same "what survives reload?" question applies to at least three other pieces of state the spec never addresses. Master volume — reset to a default, or persisted? Play/pause and playback position — does the track resume where it left off, or reset to the start, paused? Active view (Simple vs. Detailed) — does it stay on whichever was open, or always reopen to Simple? A user who sets a custom volume, is mid-track, and is in Detailed, then reloads, has one guarantee (their mutes survive) and three unknowns — likely landing on a jarring mix of "the thing I set stayed" and "the things I set reset," which won't feel like a coherent "restore" experience.

For each of {volume, play/pause + position, active view}, state explicitly whether it persists across reload or resets to a named default. If the intent is that only mutes persist by design, say that as a decision, not as an omission the reader has to infer.

`must-fix · missing-rule (invariant)`

F8 — Dependency reality + reference integrity: where rendering happens and how long the download link lives are both unstated

> "renders the current mix to a WAV in the background" / "mute states persist in localStorage"

Two related unknowns: whether rendering runs client-side (e.g., in-browser audio processing) or is uploaded to a server, and how long the resulting download link remains valid. If it's client-side and produces something like a session-scoped blob URL, a user who reloads or navigates away right after the link appears — or while the render is still running — loses it with no stated way to get it back except starting over. Separately, if localStorage is unavailable (private browsing, quota, disabled), the mute-persistence promise in the same sentence-neighborhood fails silently, with no message telling the user their mutes won't survive a reload.

State where rendering happens (this also settles whether any audio ever leaves the device, worth naming explicitly even if the answer is "never"), how long the download link stays valid and what happens if the user reloads or navigates away before or during rendering, and what the user is told (if anything) when localStorage writes fail.

`should-clarify · unenforceable-promise (discharge)`

F9 — Bounds and edges: muting all 4 stems at once is never addressed

> "The user can mute any of 4 stems"

"Any of 4" technically allows all four at once, producing silence. Whether that's an accepted state (playback simply goes silent) or should be prevented (a floor rule requiring at least one unmuted stem) is unstated — and whether Export in that state should proceed to output a silent WAV, warn the user first, or block, is equally open.

State that all four may be muted simultaneously, playback goes silent as the natural result, and Export in that state produces a silent WAV as expected (or, if undesired, define a floor rule and what the user sees when they hit it).

`worth-considering · missing-rule (invariant)`

**Coverage tables**

| Entity | Create | Read | Update | Delete | Notes |
|---|---|---|---|---|---|
| Stem mute state | missing (F3) | covered (Detailed mute buttons) | covered (toggle) | missing (no reset-to-default action) | |
| Export job | covered (click) | partial (F10 — no progress state before Ready) | N/A | missing (no cancel, ties to F6) | |
| View | covered (default assumed) | covered | covered (switch) | N/A | |

| State | Invariants stated | Invariants missing |
|---|---|---|
| Playing / Paused | none | precondition: track loaded (F1) |
| Stem Muted / Unmuted | none | all-4-muted allowed? (F9); first-run default (F3) |
| Simple / Detailed view | switch is instant | mute-state visibility across views (F2) |
| Export Idle / Rendering / Ready | shows link when ready | no Failed state (F5); no concurrent-render rule (F6); snapshot timing (F4) |

Authorization: not applicable — single-user local player with no accounts, roles, or multi-tenant data in scope.

## Phase 3.5 — Acknowledged gaps

No explicit Open Items or TBDs in the document.

## Phase 4 — Human and operational factors

F10 — No progress indication between clicking Export and the link appearing

> "renders the current mix to a WAV in the background and shows a download link when ready"

A user clicks Export mix and the screen shows nothing different until the link appears. On a longer track this reads as the click not having registered, prompting a repeat click (compounding F6) or the user navigating away, assuming nothing happened.

Add a visible in-progress state — a "Rendering…" label or spinner that appears immediately on click and clears when the link is shown.

`should-clarify · hard-to-monitor (observability)`

F11 — No stated ceiling on track length or file size for export

> "renders the current mix to a WAV in the background"

There's no assumed limit on how long a track can be before rendering becomes slow or the output unreasonably large. Without a stated ceiling, render time and memory/storage use for a given export are unbounded.

State an assumed ceiling (e.g., tracks up to N minutes at a stated sample rate) and what happens above it — reject with a message, or explicitly "no limit, inputs are pre-constrained upstream."

`worth-considering · missing-rule (invariant)`

Domain language check: all user-facing terms in the spec (play, pause, volume, mute, stem names, "Export mix," "download link") are plain product words — no internal identifiers or mechanism names leak through. No finding here; noting it because it's done well.

Security/privacy: genuinely unclear rather than out of scope — see F8. Once the client-vs-server rendering question is answered, if it's server-side, a one-line privacy statement (does the track's audio ever leave the device) belongs in the spec; if client-side, this can be closed with "N/A, all processing stays on-device."

## Phase 5 — Closing summary

**Top 3 to fix before development:**
1. F4 — define whether Export captures a snapshot at click-time or live state during render.
2. F5 — add a Failed/timeout state for the background render; nothing currently defines what a stuck or errored export looks like to the user.
3. F7 — for volume, playback position, and active view, state explicitly whether each persists across reload or resets — right now only stem mutes have an answer.

**Properties to state explicitly in the doc (paste-ready):**
- "Export mix captures a snapshot of stem-mute and volume state at the moment it is clicked; changes made after clicking do not affect the in-progress render."
- "A render that does not complete within [N] reaches a Failed state with a shown error and a retry action."
- "On reload, mute state restores from localStorage; volume resets to [default] / persists; playback resets to the start, paused / persists position; the active view resets to Simple / persists — pick one behavior per item and state it."
- "All four stems may be muted simultaneously; this is expected and produces silent playback and a silent exported WAV."

**Open questions needing author input:**
- Is client-side vs. server-side rendering already decided elsewhere (an architecture doc), or does this spec need to make that call? (F8)
- Is Simple view meant to be pure playback with mute state fully hidden, or should it surface a lightweight "N stems muted" indicator? (F2) — this is a product-feel call, not one inspection can resolve.

**Overall readiness: needs another iteration** — the play/mute/view core is solid and buildable as-is; the export path (snapshot timing, failure handling, concurrency) and the reload/persistence story need a few explicit sentences before this is safe to build against.
