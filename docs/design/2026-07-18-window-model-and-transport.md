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
- **Self-hosted channels — RESOLVED 2026-07-18 (research, sourced):** a self-made local MCP server CAN
  act as a channel in development mode via `claude --dangerously-load-development-channels server:<name>`
  (a full-screen warning shows at launch). Alexander is a Pro/Max individual with no org gate, so nothing
  blocks the dev-mode path. The server declares `capabilities.experimental["claude/channel"]` and emits
  `notifications/claude/channel` events; a session started with the flag surfaces them and acts on its
  next turn, including when it was sitting idle at the prompt. A closed session still cannot be reached.
  PERMANENT clean use without the dev flag needs the plugin on the Anthropic allowlist or an enterprise
  `allowedChannelPlugins` setting — Alexander has neither, so permanent use stays blocked; the dev-mode
  path carries a proof-of-concept. Sources: code.claude.com/docs/en/channels.md and channels-reference.md.

## Decision status

- The window model above is Alexander's stated model; adopting it as a pack rule is his call (ROADMAP row 421).
- A proof-of-concept broker is now buildable (dev-mode channels, resolved above). It would prove live
  push between two OPEN windows. It stays a lab setup (dev flag, warning dialog) until a permanent
  allowlist path exists. Files remain the base transport for today's workflow, where the human drives each
  window himself; the broker earns its keep when windows must coordinate without him. Whether to build the
  POC now is Alexander's call.
