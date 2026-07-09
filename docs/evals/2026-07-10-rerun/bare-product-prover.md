# Bare run — product-prover scenario (2026-07-10 rerun, model = sonnet worker, arm = bare)

No skill file read; zero tool uses.

Verbatim output:

---

Reviewed as if this were a real PRD headed into build — here's what holds up and what needs answers before code gets written.

**What's solid**
The core entities are named cleanly (Player, 4 Stems, View, Export job) and the two views map onto a clear subset relationship (Simple ⊆ Detailed controls), which is good — it means there's one underlying state model with two windows onto it, not two divergent code paths. Persistence requirement for mute state is explicit, which is the right thing to call out since it's the one piece of state that outlives a session.

**Gaps that will bite during implementation**

1. **"Current mix" for export is undefined.** Does the exported WAV reflect the stems currently muted in the UI, or does it always render the full unmuted mix? This is the single biggest ambiguity in the spec — export is the one feature where "what does the button actually produce" has real, divergent, plausible interpretations. Needs one sentence: e.g. "Export renders exactly the stems that are currently unmuted, at the current master volume" (or explicitly the opposite, if volume is meant to be a monitoring-only control that shouldn't be baked into the file — that's a real convention in mixing tools and worth deciding on purpose, not by default).

2. **Export snapshot timing isn't specified.** If the user mutes another stem or drags the volume slider while a render is in flight, does the in-progress render use the state from the moment they clicked, or does it pick up the change? Needs an explicit invariant: "Export snapshots stem/volume state at click time; changes after that don't affect the pending render."

3. **No behavior defined for a second click of "Export mix" while one is already running.** Queue it, block the button, cancel-and-restart, or run two jobs with two links? Silence here reads as "didn't think about it" rather than "any behavior is fine."

4. **No failure or interrupt path for export.** What does the user see if the render errors out? What happens to the job if they reload or navigate away mid-render — is it silently lost, and does the user get any signal that it's gone versus still cooking?

5. **Persistence scope is stated for mutes only.** Reload restores mute state — does it also restore volume level, or does volume reset to a default? Does it restore which view (Simple/Detailed) was last open, or always start on one of them? Right now only one of three plausible "sticky" pieces of state is actually specified as sticky; the other two are silent, and silence reads differently to different engineers.

6. **Default state on first-ever load isn't stated.** Before localStorage has anything in it, are all 4 stems unmuted? Almost certainly yes, but "obviously yes" is exactly the kind of thing that should be one written sentence rather than an assumption three people make three different ways.

7. **"Switching views is instant" has no invariant attached to what it must NOT do.** The important claim isn't the speed, it's that switching views is purely a visibility change on controls — playback continues uninterrupted, position doesn't reset, mute/volume state is untouched. As written, someone could "correctly" implement a view switch that pauses and reloads the player and still claim they met the letter of the spec. Say explicitly: view switching changes which controls are shown, never the underlying player/stem state.

8. **Track scope for mute persistence is implicit.** The spec talks about "a track" (singular), so this is probably a non-issue, but if there's ever more than one track loaded into this player over its lifetime, is mute state keyed per-track or global to the player? Worth one line to close this off explicitly rather than leaving it to be discovered later.

9. **All-muted playback isn't addressed** — presumably allowed (play continues silently), just confirm that's intended and not meant to be blocked or flagged to the user.

**Recommended before you build:** resolve #1 and #2 first — they change what the export code path actually does, not just its edge cases. #5 and #7 are one-sentence additions each and prevent divergent behavior between whoever builds the view toggle and whoever builds persistence. The rest (#3, #4, #6, #8, #9) are the kind of thing that's fine to answer with a quick default ("no queueing, button disables while a render is in flight," "unmuted by default," etc.) as long as it's a stated decision rather than an accidental one.
