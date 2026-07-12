> Archived 2026-07-12 s40 — landed as ROADMAP row 281 (SPEC INV-124). The four-move class hunt lives in build-pipeline (bug entry), product-prover (class lens), base rule 14, and the F-bug spec clause.

# Wish: a caught bug triggers a class hunt — look-alikes, architecture, spec, and escalation — not a point fix

From: tlvphotos window · 2026-07-12 · Alexander's word, standing frustration

## The pain that raised it

Alexander's friends keep finding bugs clustered in roughly the SAME area of the product, visit after
visit. His read: each report gets its one instance fixed, and the siblings right next to it — the same
defect in a slightly different place — are left standing, so the next friend trips over the next one.
A point fix looks done and is not; the class is never swept.

His instruction, in his words: when ONE bug is caught, look for ALL the look-alikes, look at the
architecture, check the specs, and talk to the human (or whoever leads the project) when needed.

## What he wants the method to make routine

When a bug is confirmed, before it is called closed, the method should drive four moves, not one:

1. **Hunt the whole class of look-alikes.** Name the defect abstractly (what KIND of mistake is this —
   a scope too narrow, a missing guard, an assumption that holds in one place and not the neighbour),
   then actively SEARCH every surface where that same kind could live, and fix all of them together.
   This sharpens the standing "fix the class, not pointwise" rule from "fix the class you already see"
   to "go FIND the rest of the class you haven't seen yet."

2. **Check the architecture.** Ask whether the bug has a structural cause — a boundary the architecture
   drew wrong or left silent, a component owning something it shouldn't. If so, the architecture doc is
   updated, not just the code. A recurring cluster in one "district" is usually an architecture smell,
   not bad luck.

3. **Check the spec.** Ask whether the spec even describes the behavior that broke. If the prover could
   not have caught it because the spec is silent or under-describes the composition, the spec is the
   real defect — fix the spec first, let the prover flag it, then the code fix lands. (This is the
   spec-under-describes-composition lesson from the story×unfold bug, generalized to every bug.)

4. **Escalate to the human when needed.** Some class hunts need the project lead's read — which
   behaviors are one class, what the intended design was, whether a whole area needs a rethink. The
   method should say plainly when to stop and ask rather than guess the boundary of the class.

## A concrete case from today (the pattern, worked)

The exhibition had a reported bug: pinch-zoom on a phone broke the layout. The naive fix blocks pinch
and calls it done. Instead, naming the class — "browser zoom desyncs the JS scroll animator, and the
handlers guard only some of the surfaces/gestures where that can happen" — and sweeping it turned one
bug into five, all real and all live:
- pinch-zoom was blocked only over the photo, not the whole walk;
- double-tap-to-zoom was not blocked at all (iOS ignores the viewport meta), a different gesture, same
  desync;
- a pinch that releases back to one finger left the walk in native scroll — the fly-through the whole
  animator exists to prevent, reintroduced;
- the volume slider could not be dragged by touch (the swipe hijacked it);
- a Ctrl / trackpad-pinch wheel stepped a frame instead of being refused.

One report, one "district," five siblings. A point fix would have shipped four live bugs for the next
friend to find — exactly Alexander's complaint. The class hunt was an adversarial audit of the whole
touch/gesture/zoom surface against the architecture (who owns the viewport, the animator, the chrome)
and the spec (EX-PROTECT / EX-CHROME), then all five fixed together with the spec updated to match.

## Where this likely lands in the pack

- **build-pipeline**, at the bug entry (matrix step): a confirmed bug does not go straight to a red
  test on the one instance; it first runs a class hunt (name the defect abstractly → search all
  surfaces → list every sibling), an architecture check, and a spec check, and the red tests cover the
  whole swept class.
- **product-prover**: a "class lens" — given a found defect, does the same kind live elsewhere; does
  the architecture account for it; does the spec describe it.
- **live-spec-base**: sharpen the fix-the-class rule to fix-the-class-you-go-and-find, and add the
  when-to-escalate-to-the-human line.

Connects to: the "recurring problems get an owner" rule (a cluster in one district is a recurring
problem about the district, not the instance), the "prototype/real-device feel is his meter" boundary
(some classes only his device reveals), and the spec-under-describes-composition lesson.
