# Wish: a product spec is written for all users, in impersonal voice — no personal attributions

**The item.** A product's spec and shipped docs are read by everyone — contributors, auditors, future
users. They should state each requirement impersonally, as a rule and its reason: "the user needs X
because Y", "a stem matters only when Z". They should NOT carry personal attributions — "Alexander
decided X", "his call", "he wants Y", "APPROVED — <name> <date>". The person's name and taste do not
belong in the artifact that speaks for the product to all of its readers; the decision and its rationale
do. Today (2026-07-12) track-coach's SPEC.md carried ~138 such attributions (TEST_MATRIX ~23, a few in
README/SKILL) — the whole design doc read in one person's voice.

**Why it matters.** The spec is the audit surface — the place a reader checks what the product promises
and why. A personal voice narrows it to "one person's project" when it is meant to be everyone's reference.
The rationale is the load-bearing part and must survive; only the attribution is dropped. The owner grants
standing legitimation for the agent to make these impersonal-phrasing calls itself, in every product, from
now on.

**The rule proposed.** Shipped product docs (spec, matrix, README, skill card) state requirements
impersonally: the rule, the actor as a role ("the user", "the producer", "the target user"), and the
reason. A dated decision keeps the date as a plain anchor and drops the name. Attribution and candid
process voice live only in local-only diaries (JOURNAL / NEXT_STEPS), never in the shipped artifact. This
belongs in the publish gate and the spec-author guidance as a standing check for every product.

**Who throws it.** The track-coach Mac window, 2026-07-12 ~08:54, on Alexander's explicit word
(«спека она для всех, для аудирования … не надо личных таких вещей … это должно быть во всех продуктах
так», with standing legitimation to apply it).
