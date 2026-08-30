# Simulation Syndicate 01

Week-one simulation of the syndicate-genesis protocol. **Disposable test repo** - dummy identities, dummy research, real mechanics.

What is being rehearsed here:
- Git-native attribution (commits and reviews as the contribution record)
- PR-executed consortium agreement (approving review = signature)
- Continuous OpenTimestamps anchoring (weekly Bitcoin priority proofs)

Status: Phase 0 - template assembly.

## Layout

- `syndicate.yaml` - the manifest: members, gates, attribution weights
- `agreements/` - consortium agreement and execution log
- `vault/` - Obsidian vault (literature, notes, drafts, decisions)
- `tools/` - ingest and anchor tooling
- `.github/workflows/` - ingest and anchor automation

## Licensing

- Code (`tools/`, `.github/`, `bootstrap.sh`): MIT - see `LICENSE`.
- Templates and documents (`agreements/`, `README.md`, `vault/_templates/`): CC BY 4.0 - see `LICENSE-CONTENT.md`.
- Everything a syndicate commits to `vault/`, `ledger/`, or `agreements/EXECUTION-LOG.md` is governed exclusively by that syndicate's executed Consortium Agreement.
