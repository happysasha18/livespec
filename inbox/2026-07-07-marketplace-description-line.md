# Wish (from promoter window) — one line: marketplace.json description

`claude plugin validate .` passes but warns: `.claude-plugin/marketplace.json` has no
`description` field, and directory submission runs the same check. One line fixes it, e.g.:

```json
{ "name": "live-spec", "owner": { "name": "Community" },
  "description": "Living-spec methodology pack: spec-author, product-prover, build-pipeline, communicator and their shared rulebook.",
  "plugins": [ { "name": "live-spec", "source": "./", "strict": false } ] }
```

(Second warning — `icon` field in plugin.json unknown to the validator — is explicitly safe to
keep, no action.) Raised 2026-07-07 morning; the two directory submissions are otherwise
unblocked and queued on the owner.
