# Wish: fold the tlvphoto/exhibition-engine week's escaped bugs back into the test method

**From:** Alexander, 2026-07-09 evening, live-spec window (tlvphoto is audit-only here — this wish
changes the PACK, never that project). His verdict, paraphrased: elementary bugs keep passing that
project's suites; he ordered a full test review there and questioned what the tests verify at all. The
evidence below is from tlvphoto/exhibition-engine commits of 2026-07-08/09, gathered read-only.

## The escaped bugs, clustered — each cluster is a method gap, not a project patch

1. **Real-device behaviour a headless desktop browser cannot see.** One momentum swipe flew through
   several works on his iPhone (iOS ignores `scroll-snap-stop:always`; tlvphoto `b7f6042`); a
   backgrounded phone throttled a 2.5 s JS failsafe into a black screen (`50b86de`). The harness had no
   touch emulation until the fix added it, and even with it, iOS momentum physics stays out of reach.
   **Method delta (test-author):** the level ladder tops out at browser-computed/pixel on desktop
   Chromium; it must NAME the device-fidelity boundary honestly — behaviours that live in touch physics,
   scroll snapping, and background throttling get a "real-device walk" row the suite cannot green, owed
   before ship, kin of the motion-feel gate (his standing rule: feel is his call, never ship off green).

2. **Geometry asserted as absolute values instead of viewport-relative — and drift that accumulates.**
   His report tonight: image centering is computed by shifting an absolute amount that differs from the
   screen size, so each next image lands further off-center. A test that asserts one swipe at one
   viewport passes forever. **Method delta (test-author):** a centering/positioning fact is asserted as
   RELATIVE geometry (|center(work) − center(viewport)| ≤ ε), at ≥2 viewport sizes, and after N
   consecutive steps so cumulative drift shows — one-step assertions hide it by construction.

3. **Donor-instance assumptions leaking into the generic engine, tested only on donor-shaped data.**
   The engine's id validator kept tlvphoto's digits-only regex and rejected the engine's own slug ids —
   every `/api/story` call 400'd (`178740c`); the door wordmark stayed hardcoded (`8d40209`).
   **Method delta (test-author + spec-author):** when a generic engine is extracted from an instance,
   the engine's suite runs on the ENGINE's own generic fixtures, never only on the donor's data; every
   donor-specific constant the extraction finds becomes a named content-contract entry with a test that
   the engine works without it.

4. **Unmodeled state compositions.** The finale kept the previous work's caption; the quiz chip lingered
   after answering; the door re-faded on an aspect-ratio change (`50b86de`, `7c41d8a`). The composition
   law already names exactly this (spec-author's axes; the finale case is literally its example), and a
   prover lesson was already filed from the field (live-spec `2a0944a`). **Method delta:** verify the
   prover's stateful-surface sweep actually fires on ADOPTED specs (the engine's SPEC.md was authored
   fresh, 844 lines, and the compositions still slipped) — this is enforcement, the law exists.

5. **The suite's own plumbing lied.** A `skip()` NameError hid on the no-Pillow path (`62cb70b`); a
   missing shim re-export kept a suite silently red; a worker's "green" was the wrapper's exit code.
   The gate-on-suite-LOG rule exists (his word); **method delta (test-author):** a pinned-skip-set
   check that also FAILS on a skip path that cannot execute (import the skip helper at module load),
   and the engine/instance shim owes a re-export completeness test.

## Also from the field, same evening (communicator, enforcement not new law)

The tlvphoto session asked him to decide a client-asset sync, phrased in jargon he could not parse — a
sync the agent could have just done. The rules already ban both (ask in plain words; never ask what you
can decide). The failure is enforcement in live chat, where no gate runs — kin of the standing note that
chat cannot be machine-gated; the pre-ask self-scan must cover QUESTIONS, not only reports.

## Boundaries

- All deltas land in the pack's skills/templates/tests; tlvphoto and exhibition-engine fix their own
  trees in their own windows (both already ship red-first tests for bugs 3–4 of their list).
- Each delta is one story through the pipeline; this file is the intake material, never the spec.
