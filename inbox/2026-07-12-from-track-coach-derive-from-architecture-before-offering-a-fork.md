# Wish: derive a requirement from the existing architecture before offering the human a fork

**The item.** When a session must state or fix a requirement and the answer is already
determined by a first-class project artifact (the architecture, the spec, the invariants), the
method today gives no step that makes the session derive it from that artifact first. Tonight
(2026-07-12, track-coach) that gap produced a needless design fork. Asked to fix the catalog's
staleness rule — the rule that decides when a deposited widget is out of date and must be
re-rendered — the orchestrator presented Alexander two options (a hand-maintained analysis
version, or a content fingerprint) and asked him to choose. But `ARCHITECTURE.md` already draws
the exact line the rule needs: eight layers, where the content-producing layers (signal
analysis, project parsing, credibility, reference) sit apart from the widget-render layer, which
sits apart from the infrastructure layers. The requirement falls straight out of that split — a
widget is stale when a content layer changed since it was built; a render-only or infrastructure
change never stales it. Alexander corrected it (~01:34): read the architecture, derive the
requirement, stop handing me forks.

**Why this slipped.** Ask-never-guess covers information that is genuinely missing. Here the
information sat in a first-class artifact and the miss was not consulting it before speaking. The
two situations face opposite ways — one asks the human, one reads the doc — and the method names
only the first, so "I lack this, ask" quietly absorbs the case that should have been "the artifact
settles this, derive it."

**The law proposed.** Before surfacing a design choice to the human, a session checks whether an
existing proven artifact already determines the answer. When it does, the session derives the
requirement from that artifact and states it back with the section cited as its ground, and does
not offer a fork. A fork reaches the human only for what the artifacts leave genuinely open — a
taste call, or a real trade-off with no artifact-grounded winner. This is the read-the-doc twin
of ask-never-guess, and it belongs beside it in the base rules.

**Who throws it.** The track-coach Mac window, 2026-07-12 ~01:37, on Alexander's explicit word
(«покажи в инбокс лайвспеку … что не сошлось почему ты это вообще предложил»).
