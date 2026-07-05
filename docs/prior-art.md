# Prior art — what we found before publishing (July 2026)

Two surveys, run before the first public push; raw notes in the two files beside this one.

**Verdicts (blunt):**
- Spec-before-code: everyone has it (BMAD, spec-kit, Kiro, OpenSpec, …). Not ours.
- Baseline snapshot-diffing: mature testing practice (Jest, Percy, Chromatic). Not ours.
- Declared-scope diff as an agent freelancing-catcher: EXISTS in part — [agent-guardrails](https://github.com/logi-cmd/agent-guardrails)
  does per-task declared-file scopes diffed at merge. Credit where due. Ours differs: scope derives from
  the living SPEC, checked at pre-push.
- Continuous wish-intake validated against a living spec: not found published.
- The dev process itself specced + formally reviewed by a prover skill: not found published
  (closest: Lean4Agent, academic; agentic-os phase gates, bash-level).
- Mid-flight adopt → proven SPEC → pipeline attached: partial, scattered (OpenSpec onboard,
  reverse-engineering-skill); no single pack.
- **The integration — the spec as single authority binding intake, scope, proof and adoption: found nowhere.
  That is live-spec's claim, and the only one we make.**

Know prior art we missed? Open an issue — genuinely welcome.
