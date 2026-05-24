# Current Status

## Completed

- Canonical ALLOW and DENY examples pass
- API verification tests pass
- Ledger verifier works with legacy support
- GitHub Actions runs `verify-output`
- Branch protection requires `verify-output`
- Bypass is disabled
- Verification contract is frozen
- Independent curl verification example exists

## Enforcement Meaning

The repository now depends on verification output.

A protected branch update requires the `verify-output` check to pass.

## Current Control Path

Code change
→ GitHub Actions
→ Canonical verification
→ API verification
→ `verify-output`
→ Protected branch enforcement

## Remaining Work

- Receipt schema validation
- Adapter automated tests
- Exception workflow
- Operational metrics
- Independent external pilot
