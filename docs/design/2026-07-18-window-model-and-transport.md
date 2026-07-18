# Window model and inter-agent transport — findings (2026-07-18)

Captured from a design conversation with Alexander on 2026-07-18. This records facts and his stated
model; adopting the model as a pack rule stays his call (the open design question, ROADMAP row 421).

## The window model (Alexander's word, 2026-07-18)

- A window drives one **working set**. The set may be: (a) one project; (b) an engine plus one
  instance (the exhibition engine and one site); (c) an engine plus several instances (a promoter
  backbone and its promoters).
- The set is **fluid**: an instance can be pulled into its own window as it grows. Today he drives a
  family from one window; later he gives a grown instance its own window.
- Splitting a set across windows **costs nothing**, because agents coordinate through files (the inbox
  and the git store), which behave the same whether two trees share a window or sit in separate ones.
- This refines the "one window = one project" rule into **"one window = one working set the human is
  driving."** The stable atom is the project (its card, spec, queue, inbox); the window is a fluid lens
  the human composes over one or more projects.
- The human is the conductor. As the window count grows, the first thing needed is a **read-only board**
  that summarizes every window's state; agent-driven orchestration comes only after that.

## Transport findings (research 2026-07-18)

- **Files are the always-works store.** A receiver that is not running is reachable by nothing else, so
  the file store stays the base transport regardless of what fast path exists.
- **Waking an idle or closed window from outside needs harness support.** The harness carries the client
  half of a socket path, switched off, with no listener shipped; an idle session has no event loop that
  reacts to external I/O. This is Anthropic's to ship. A tripwire (INV-231) fires the day a listener appears.
- **Pushing into an OPEN window works today via Claude Code "channels."** An MCP server declaring the
  `claude/channel` capability pushes events into a session started with `--channels`; the session acts on
  its next turn. This is how sessions receive Telegram/Discord/webhook events while the human is away.
- **OPEN QUESTION that gates a custom broker:** channel plugins appear to require approved-vendor /
  allowlist status (Anthropic- or org-managed). Whether a self-hosted local plugin can declare
  `claude/channel` is unverified. If it can, a local broker gives near-real-time messaging between OPEN
  windows. If it cannot, files stay the transport until the harness ships the waking listener.

## Decision status

- The window model above is Alexander's stated model; adopting it as a pack rule is his call (ROADMAP row 421).
- Building a broker is premature today: files cover the current workflow, and a poll-only broker barely
  improves on files. The cheap next step is answering the approved-vendor question above, then building a
  broker only if that answer is green.
