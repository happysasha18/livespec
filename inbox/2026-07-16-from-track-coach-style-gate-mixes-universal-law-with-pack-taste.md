# Wish — the style gate bundles universal language law with pack-specific register taste

- **From:** track-coach window, 2026-07-16
- **Kind:** wish / design refinement (let a host adopt the universal floor without the pack's taste)
- **Severity:** medium — it blocks a clean partial adoption; today a host must either take the whole
  register or port the lint by hand

## What surfaced

Adopting the 2.0.0 compaction ratchet into an already-authored host (track-coach), I measured its SPEC with
`scripts/spec-style-lint.py --gate` and got 880 "errors". The breakdown:

- scissors 165, negation-opener 10, machine-jargon 0 — the UNIVERSAL language laws (the scissors ban is
  stated as global and permanent; negation-opener and machine-jargon are general plainness).
- caps-shout 567, second-person 123 — the PACK's own register taste. `--gate` promotes these two from
  warnings to blocking errors.

track-coach's SPEC uses ALL-CAPS for emphasis and addresses the producer directly as "you" ("reads your
track") — both deliberate, and correct for a user-facing product spec written to its reader. They are not
violations of any universal law; they are places where the host's register differs from the pack's.

## The design point

`--gate` conflates two different things under one flag:

1. **Universal laws** every live-spec document should hold — the scissors ban above all (it is declared
   global and permanent), plus negation-opener and machine-jargon.
2. **The pack's own register taste** — no caps-shout, no second-person — which is right for the pack's docs
   and need not bind a host whose spec deliberately chooses otherwise.

Because both ride the one `--gate` flag, a host cannot adopt the universal floor as its push gate without
also adopting the pack's taste, which would force a large, meaning-neutral rewrite of an intentional voice
(here: stripping 567 caps + 123 "you"). The default mode happens to draw the line correctly (scissors /
negation-opener / machine-jargon are errors; caps-shout / second-person are warnings), so a host CAN lean on
default mode — but then it loses the gate-only rules it might want (reassurance, future-narration), and the
split is implicit, discovered by reading the source rather than declared.

## Suggested refinement (owner decides)

- **Name the two tiers explicitly.** A universal-law set (scissors, negation-opener, machine-jargon) that
  every host's gate enforces, and a pack-register set (caps-shout, second-person, reassurance,
  future-narration) a host opts into. Let `--gate` take the union for the pack's own docs, and give a host a
  documented way to enforce tier 1 while leaving tier 2 advisory (a flag, or a per-host register config the
  lint reads).
- **State it in `docs/spec-style.md`** so which rules are universal and which are pack-taste is declared, not
  inferred from the default-vs-gate promotion table.

Context: track-coach is adopting tier 1 as its push gate now (driving scissors / negation-opener / redundancy
to zero, keeping caps and "you" as its own voice). This wish is the pack-side refinement so the next host that
adopts does not have to rediscover the split by reading the linter.
