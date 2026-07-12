# communicator — worked examples from the field

The illustration bank for the rules in [`../SKILL.md`](../SKILL.md). Load it when you want a worked
example of a rule in action; the SKILL.md body keeps only the short inline examples a rule cannot be
read without. Nothing here is a new rule — every line illustrates a rule already stated in the body,
and the *(rule N)* tag on each says which.

## Narration and status in action *(rule 13)*

- **The detached-work cadence** — *✅ start: "suite running in the background, log at
  `.live-spec/logs/suite.log`, about six minutes" … beat: "suite past the render tests, two minutes
  left" … done: "suite landed: 351 green"*
- **The offline window** — *✅ "tests are running; I can manage about ten minutes without you, and
  when you're back I'll show what we closed" ✅ return-beat: "you're needed again: to look at the
  landing and give your word on the deploy"*
- **The leave-word** — *✅ "понял, довожу до безопасной точки — минуты три: останавливаю воркера,
  коммичу зелёное" … "можно выключать; продолжим со строки 216, всё в файле возобновления"*
- **Live status** — *✅ "now: fixing the feature map (stage — code); next: tests and push"*
- **A beat, not silence** — *❌ [forty minutes of silent tool calls, then a wall of report]
  ✅ "the spec is written, calling the prover to check the seams (station: spec done, prove next)"
  ✅ station-end: "tests finished: it is now covered that every station leaves a digest, and that
  silence past ten minutes is a debt (tests: the three teeth pinned)"*

## Plain words, one name *(rule 6)*

- **Own report coinages read as riddles.** *❌ "the rule is still on an open leg" ✅ "the rule is
  written, but not yet checked in a real session"* — a metaphor born in the pack's English docs ("open
  leg", "ladder rung") dropped raw into chat means nothing to the reader; a translation after the fact
  does not fix it.
- **One thing = one name, from the SPEC.** *❌ "the stem-name resolver" ✅ "open a track with a quiet
  part — you see its real name filled in" · ❌ "INV-8 recommends a GitHub backup" ✅ "this project has no
  remote copy — our safety rule says set up a GitHub backup before heavy compute (INV-8); want me to?"*

## Presenting a fork (template) *(rules 2, 10)*

A choice is never a paragraph. For ONE decision, generate a tiny HTML (several at once → the decision
page, rule 10):
- **Option A (recommended, if you have a pick)** — a picture/example + one line "when this is better".
- **Option B** — a picture/example + one line "when this is better".
- Question at the bottom: "this or that?" — with your recommendation named. Every option still stays open.

## Walking the evidence *(rule 11)*

*❌ "yes, the tests were done by the methodology" ✅ "verified: suite green — tonight's run, this commit;
done by pack 0.8.x / prover 0.1.8; asserted (not re-checked): the adoption record's coverage claim"*

## Live examples (from the field)

- **Typography decision.** *(rules 1, 7)* Instead of "fold weights 620/640/650 to 600/700?", rendered
  every weight as the same sample sentence side by side so the person could SEE that 620/640/650 are
  near-identical to 600 — the decision made itself.
- **A "which name?" question with a real conflict.** *(rules 1, 2)* An auto-generated label was
  sometimes misleading, so the honest wording wasn't obvious. Rather than guess or ask in the abstract,
  rendered three concrete naming options side by side as real examples and let the person pick the one
  that read right.
- **A day of work that looked like nothing.** *(rules 4, 7)* Instead of claiming the audits were
  valuable, put yesterday's build next to today's in one window, synced, with an honest verdict:
  "you're right, this is not a visual redesign — here's the little that's visible and the two bugs it
  caught that you can't see."
- **The first departures board, bounced by its reader.** *(rules 6, 8, 9; SPEC INV-28)* The night
  report led every line with the feature's coined nickname ("A Walk Through the Evidence", "The Clock
  Grows Teeth") plus a row number, and compressed a story to "seven times — twice the fence". The reader
  asked WHAT??? four times. Retold under the law: "ask me 'did you actually do X?' — I now answer by
  walking the artifacts, with the method version named from the record (row 101)" — the outcome first,
  every handle trailing.
- **The same event, told twice.** *(rules 6, 8)* First telling: "the inbox worked — a session dropped
  three findings, harvested into rows 19–21" — the human had to ask what that meant. Second telling:
  "the other project's session found three gaps in the adoption procedure; before tonight it would have
  edited the package's files directly; instead it left one new file in the inbox and touched nothing
  else; I turned its findings into queue rows." Same fact — only the second one communicated.
