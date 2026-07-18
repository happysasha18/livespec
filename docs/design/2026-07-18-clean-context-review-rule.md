# Adversarial review runs from a clean context — rule to land (2026-07-18)

Alexander's demand, 2026-07-18, after a fresh web review caught self-referential defects that the
in-context 2.7.0 release prover missed. To land as a MINOR through the method, reviewed from a clean
context itself.

## The failure it fixes
The 2.7.0 release prover ran its adversarial passes in the same context that authored the new lenses, so
it never turned a brand-new lens onto the skill's own body. A fresh review immediately found: Phase 5 said
"four blocks" over five items (the skill's own count-vs-contents lens), and two bullets packed three or
four rules each (the skill's own reading-load lens). The authoring seat is blind to its own new blind spot.

## The rule to state in the pack
1. **Clean-context adversarial review.** Every adversarial or high-stakes review runs from a clean
   context — a fresh agent with no authoring marination. The authoring seat drafts and accepts; it does not
   adversarially certify its own work. A release's adversarial pass is authored by a fresh seat.
2. **Self-application of new rules.** A newly added lens or rule is run against the very document that
   introduces it before release; the release record names the result.

## Scope
A new invariant (next free INV-237), a base-rulebook rule, referenced by build-pipeline (the verify/review
station) and product-prover (release self-application). MINOR bump. A release gate can require a dated
clean-context review record authored by a seat other than the release's; whether the review was truly
clean-context stays a process fact the gate cannot fully see, so the gate checks the record exists, is
dated to the release, and is authored by a different seat.

## Evidence this works
Tonight's three clean-context adversarial passes on product-prover caught a regression the same session
introduced (a broken lenses.md pointer created while splitting a dense bullet). Clean context found what
the authoring context could not.
