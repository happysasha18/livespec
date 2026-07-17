# Prover — batch push re-check (2026-07-17, short form per INV-61)

A push re-check for a batch of seven unpushed commits. No product delta of its own; this record blesses a
stale compaction-freeze baseline and re-runs the full push gate so the batch can leave the machine.

## The batch

Seven commits stand ahead of origin/main (`git log --oneline origin/main..HEAD`):

- `1d6a5fa` Rows 416/418: fix six delivery/wiring defects an adversarial review found in the register judge
- `2bd6c97` Row 417 corrections: close four guard-inversion defects the adversarial review found
- `ce37e95` Row 413: every point of contact with the person has a kind, and the kind decides what may be said there
- `38d2488` Row 417: a cleanup says what it ended, and four name-list guards invert
- `ebe591d` Rows 416+418: the register judge holds the class a literal list cannot — one landing, both surfaces
- `472cf9b` Row 391: the pack-side net-liveness meter — every net keeps its own runs and fires
- `65d55db` ROADMAP: record three 2026-07-17 instructions — skill-review gate (419), habits-to-gates audit (420), 390/392 doc-rotation extension

## Suite

The full suite runs green under the push gate's reach classifier, which sends every one of these files to
the full run: 1185 passed in 152s, zero failures.

## The two high-stakes landings passed an adversarial review

Both hard landings in this batch went through a Fable adversarial review the same session, and both reviews
found real defects that are now fixed and red-proven. The details live in the two landing records'
"Corrections after adversarial review 2026-07-17" sections.

The register judge (rows 416/418, `docs/prover/2026-07-17-rows416-418-register-judge.md`): the review found
six defects, two of which defeated the landing's own claim. The chat judge had been delivering no verdict at
all because a wait-on-non-child race destroyed every one; the whole-turn gather read only the text after the
final tool call because every tool result is a `type:"user"` transcript record; quote validation was
substring-only in both directions; INV-94 still commanded per-catch list growth against INV-83's retraction;
a sourced hook missing from the install passed config-health as a green skip, so the judge could go dark with
every gate green; and the owner's personal register bank shipped verbatim in a public test. Each defect
carries a red-first test and is now green.

Row 417's guard inversions (`docs/prover/2026-07-17-row417-cleanup-notice-and-inversions.md`): the review
falsified the landing's claim that each of the four inverted guards kept its prior catch while widening to
the class. The broad-kill rewrite from a browser-word list to an owned-identity read had dropped three
browser-killing forms the old guard caught, and a shared-install-path exemption re-blessed a cross-run kill
the INV-162 spec forbids. Four confirmed defects, each red-proven against the committed tree first, then
fixed and greened; every newly caught form is now pinned in the committed probe corpus so a later change
cannot silently narrow it.

## Broad-kill safety spot-check

The founding-incident commands all red again. `pkill -f ~/.cache/puppeteer` and `pkill -f user-data-dir`
(the ROADMAP 335 cross-run kills), `/usr/bin/pkill chrome` (the full-path form), and `killall Safari` each
exit nonzero through `guardrails/check-broad-kill.sh`, while the safe owned-group forms `os.killpg(...)` and
`kill $MY_RECORDED_PID` pass quiet. The guard discriminates by ownership as INV-162 requires.

## Freeze re-blessing

The local `.spec-freeze/` baseline was frozen after the register judge landed and before the two correction
commits, so gate k read two intended deltas as drift. Both are legitimate and compact:

- **PRODUCT_SPEC.md, anchor INV-203 count 4 → 6.** The two new citations both belong to INV-94 (no line
  certifies its own sincerity), added by the corrections commit `1d6a5fa`. Before the correction INV-94's
  body said each caught phrase "joins the register lint's pattern family as its own class", the retracted
  per-catch growth doctrine; the fix rewords both of INV-94's homes — its prose statement and its
  Formal-index row — to say the register judge holds the class and a caught phrase informs the judge and the
  first pass, the list growing by nobody's duty. Each cite is INV-94's standard body-plus-index pair, the
  same shape every invariant carries. Neither is padding and neither duplicates the other.
- **TEST_MATRIX.md, path `/usr/bin/pkill` appeared.** Added by the row 417 corrections commit `2bd6c97` as
  an acceptance probe in M-311: a full-path `pkill` that must red. It closes broad-kill defect D1, where the
  guard's name-kill class excluded a leading `/` and let an absolute-path `pkill chrome` through. The probe
  is pinned in the committed corpus fixture and covered by `test_full_path_and_pipe_and_two_line_resolvers_red`.

The baseline was re-frozen with `python3 scripts/spec-freeze.py --freeze PRODUCT_SPEC.md ARCHITECTURE.md
TEST_MATRIX.md --compaction`. The cache is gitignored and local, so re-freezing writes nothing to the
tracked tree.

## Gate result

`guardrails/pre-push` exits 0: all gates green, push allowed. Gate k reads the guarded docs as matching
their re-blessed baseline.

## Verdict

The batch is push-ready.
