# Bare run — product-prover scenario (2026-07-06 push-gate re-run, model = sonnet worker, arm = bare)

No skill file read; zero tool uses.

Verbatim output:

---

# Track Player — spec review

**What's solid:** The Simple/Detailed split is a clean view ladder (Detailed = Simple + stems, nothing removed), which is the right shape. Scope is tight — one track, four fixed stems, no playlist, no solo — that's appropriate for a first build.

**Gaps that will bite during build, in order of how much they'll cost later:**

**1. Mute persistence has no identity key.** "Mute states persist in localStorage and restore on reload" — restore *for which track*? If mutes are stored globally, loading a different track inherits the last track's mute pattern, which is almost certainly wrong. If they're meant to be per-track, the spec needs to say so and name what identifies a track (filename? hash? id?). This is a one-line spec fix now, a data-migration problem later if skipped.

**2. View switching and mute state — the relationship is implied, not stated.** When the user is in Simple view, the stem buttons are hidden, but do the underlying mute states still apply to what's playing? Almost certainly yes — but the spec never says "the view is presentational only; mute/play/volume state lives independent of which view is showing." Without that sentence, an implementer could plausibly reset or ignore mutes when hidden. Worth one explicit invariant.

**3. Export doesn't say what "current mix" is frozen against.** If the user changes a mute mid-render, does the in-flight export use the mix as of the click, or drift with later changes? Also unaddressed: what happens if they click "Export mix" again while one is already rendering — second job queued, rejected, or does it cancel the first? This is a real race condition, not a nice-to-have. Needs one sentence of resolution before code, since it changes the button's behavior (e.g., disable while rendering vs. allow overlapping jobs).

**4. Export does not say where the render happens or what "ready" means.** In-browser (WebAudio/offline render) vs. a server round trip are different architectures with different failure modes (browser tab closed mid-render vs. server job surviving it). The spec also has no failure state — if rendering errors out, what does the user see? At minimum needs an explicit "render fails → X" line.

**5. Volume vs. mute asymmetry is unexplained.** Mute state is explicitly persisted; volume is not mentioned either way. Is that a deliberate choice (volume resets to a default per session) or an oversight? State it either way so it isn't decided by accident in code.

**6. Playback position/state on reload is unstated.** The spec calls out that *mute* restores on reload but says nothing about play/pause or scrubbed position — presumably it doesn't resume playback and starts paused at 0, but "presumably" shouldn't be doing that work. One line closes this.

**7. All-four-stems-muted is a reachable state with no defined behavior.** Not necessarily a problem (silence is a valid mix), but worth a deliberate "yes, that's allowed" rather than leaving it to whoever writes the mute-toggle code to notice.

**8. Stem availability is assumed, not stated.** The spec assumes drums/bass/vocals/other are always ready to mute. If stem separation is itself a background job (as it is elsewhere in this codebase's audio tooling), the player needs a state for "stems not ready yet" before Detailed view can show working mute buttons. If stems are guaranteed pre-computed before the player ever loads, say that explicitly so it's a decision, not an assumption.

**Suggested invariants to add before this goes to build (short, plain-language form):**
- Mute state is keyed per track and survives reload for that track only.
- Which view is showing (Simple/Detailed) never changes play state, volume, or mute state — it only changes what's visible.
- Clicking "Export mix" captures the mix (mute pattern + volume) at that instant; changes made afterward don't affect that export.
- Only one export runs at a time — decide and state whether a second click queues, is blocked, or cancels the first.
- Export failure has a visible state, not just success.

None of this requires restructuring the spec — it's five to eight sentences of decisions that are currently left to whoever writes the code first. I'd resolve items 1–4 with you before building; 5–8 are smaller and could be decided inline while writing the spec's next draft.
