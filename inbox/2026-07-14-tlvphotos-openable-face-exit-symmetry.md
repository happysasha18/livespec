# Wish — make "openable faces" a standing same-kind group in the design review, checked for enter/exit symmetry

## The wish (method change)

The design review should carry a standing same-kind group: **every surface a visitor opens into an
over-everything face and later closes** — a zoom layer, a side room, a lifted print, a card, the door.
For that group it should always check one parity: **does the way OUT mirror the way IN** — both the set of
close affordances and the visual treatment of the transition. When ONE member states a mirror principle in
so many words, every sibling is measured against that same principle by name.

## The exact case that slipped through

Project: tlvphotos. Spec: `/Users/sashaabramovich/tlvphotos/SPEC.md`.

Two members of that group behave unlike each other, and the difference is plain in the text:

- **The series side room** declares the principle outright: "the way OUT mirrors the way IN — the close
  plays the same veil crossing as the open, reversed" (SPEC:1091-1092). It opens through the door's black
  crossing (SPEC:1083-1084) and closes three ways, one of them the browser's Back (SPEC:1089-1091).
- **The zoom layer (pinch to inspect)** opens by a two-finger scale-up under the finger (SPEC:1220-1222) but
  has no reversed pinch that closes it: a pinch back toward 1× recentres the image and holds the layer open
  (SPEC:1240); closing falls to a × control, a tap on the dark backdrop, or Esc (SPEC:1222-1223). Its enter
  is a finger-tracked scale-up; its exit is a fade of the whole layer (SPEC:1249), a different treatment at
  the two ends of one face. It also omits the browser-Back close its sibling faces carry, though it is
  declared a face under the same freeze-and-restore law.

The clean mirror already in the family, for contrast, is the lifted print: one tap lifts it, one tap sets it
down (SPEC:1243-1244) — same gesture in and out.

## Why this matters (what broke)

The morning design-review pass on this spec (record `tlvphotos/docs/prover/SPEC-design-review-2026-07-14.md`)
did not draw the zoom-and-room grouping, so the asymmetry went unnamed. The owner caught it himself on a
phone: he pinches to open, then has to reach for the × to close, and the size arrives and leaves with a jump
rather than continuously. He asked why the review had not caught a thing like this.

A blind design-review run today, given only "the family of surfaces a visitor opens into a face and closes"
and NO hint about pinch or the specific finding, DID surface it — it reported the zoom's missing
pinch-to-close against the room's stated mirror (its F1), the enter-scale versus exit-fade treatment (F4),
and the missing Back close (F2), plus the one-directional door crossing the room copies (F3). So the
capability is there. The miss was that the standing pass never drew this same-kind group, so the parity was
never asked. Making the group and the enter/exit parity standing is what closes the hole.

## Primary source

Owner report, tlvphotos session, 2026-07-14 ~19:20–20:53: the two pinch wishes (a full pinch-out should
return to the previous layer without a tap on ×; the size should move continuously at both ends), and the
direct question "why was the enter/exit symmetry not found by the review." The blind-review findings above
back it.

## Who threw it

The tlvphotos session (this conversation), acting from its own window through this inbox.
