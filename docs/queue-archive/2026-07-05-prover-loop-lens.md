> ARCHIVED 2026-07-07, session 22 — landing as ROADMAP row 150 (SPEC INV-50, M-148): the entry-symmetry lens in product-prover 0.1.12, the face-law in SPEC + spec-author's journey lens.

# Wish: product-prover gains a loop/symmetry lens (faces, not just states)

From: the tlvphoto session (Fable), 2026-07-05 ~21:20, on Alexander's direct catch the same evening.
This file is the one allowed cross-project write (a new inbox file); the inbox/ folder was created with
it — live-spec had none yet (mirroring pack E-1, as the live-spec session did for tlvphoto's inbox).

## What happened

tlvphoto specced a threshold face ("the door": a cold visitor picks one of 5 photos, the pick seeds the
gallery; a stored walk skips the door on return). product-prover ran a CROSS-LINK pass over the new
surface's seams and found 6 real holes (bake seam, persistence seam, lock, void law, affordance leak,
rotation determinism) — but MISSED the biggest one, which Alexander caught by eye in one read:

**The door was a one-way face.** Enterable exactly once (cold arrival), never re-reachable — the walk had
no path back to the threshold. A dead-end in reverse: not a state with no exit, but a face with no
re-entry. His words: "всегда в автомате должен быть луп — если есть гет, есть сет" (every state machine
needs its loop; if there is a get there is a set), and "тебя никто не учил балансу?"

Why the prover missed it: the dead-end/liveness lens tests STATES for exits. The door and the gallery are
FACES of one surface (one URL, one entity in the model), so no "state without exit" fired — the gallery
has exits, the model looked live. The asymmetry lived one level up: in the reachability of the faces
themselves over the visit's lifetime.

## The wish

Add a **loop/symmetry lens** to Phase 3e (or 3b): for every FACE, MODE, or PANEL a user can enter —
especially one shown conditionally (first visit only, empty-state only, onboarding, a one-time banner) —
ask: **can the user deliberately return to it? If not, is the impossibility STATED as a decision?** A
face reachable only once is the finding; wordings like "shows only on first visit" are the trigger
pattern. Sibling class to sweep: any "only on first run / until dismissed / one-time" clause in a spec.

Suggested one-line home in the lens list: "**Entry symmetry** — when a face or mode is entered under a
condition (first visit, empty state, onboarding), what deliberate path re-enters it later? A get with no
set is a finding unless the spec states the one-way as a decision."

tlvphoto folded the instance same session (SPEC INV-31: the door↔gallery loop — a quiet exit re-opens the
door as a fresh quiz; skip returns to the walk untouched; a pick replaces the arc). The class belongs to
the pack.
