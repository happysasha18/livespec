# Wish: the design review must name and check the same-kind PARITY class

**The item.** When a spec ships a gesture or a motion that opens/closes a layer (a zoom, an
inspect view, a lift), the design review should treat three parity groups as same-kind and check
behaviour equality across each, by construction:

1. **Entry mirrors exit.** If a layer opens by a scaling flight from the source, it must close by
   the reverse of that same flight — not a different animation, not a fade, not the entry played
   backwards where backwards looks wrong. The way out is the way in, reversed.
2. **All object TYPES behave identically.** Every kind of picture the gesture can act on (in this
   project: a gallery frame, a polaroid print, a door window, a series-room work) opens and closes
   the same way — and each returns to ITS OWN on-screen rectangle (its own size and place), which a
   true per-element FLIP does by reading the source rect, so differing sizes are handled by
   construction, never by a per-type special case.
3. **All POSITIONS behave identically.** The same gesture on the same type in different slots (in
   this project: the top / middle / bottom picture on the door) must behave the same. A difference
   between the bottom and the middle is a defect the review should predict before a device ever
   sees it.

**Why.** tlvphotos shipped the pinch entry/exit-symmetry feature (INV-82/INV-83, v1.3.2). The
review caught only part of group 1 — the bare fact "entry and exit are same-kind, so they should
mirror" — and did not name groups 2 or 3 at all. On real devices Alexander then found: the desktop
pinch entry does not mirror the (good) exit; on phone a full pinch-out shrinks but will not fly the
picture back to its place and close without the × button; and the door pinch-out behaves differently
for the bottom picture than for the middle. He expected the prover / design review to surface these
as same-kind parity gaps before the ship. The design-reviewer skill answers "do same-kind things
behave alike, and what groupings did the text never declare" — motion entry↔exit, object-type, and
position are exactly such undeclared groupings, and a gesture/overlay spec should trigger this check
as a standing lens.

**Primary source.** Alexander, 2026-07-15 ~23:20, on the live tlvphotos pinch: the bugs above, and
the direct word that the prover should have told me these must all behave the same, and that I should
have asked or caught it. He said to drop it here.

**Who threw it.** The tlvphotos window (a host adopt run of the live-spec pack), 2026-07-15.
