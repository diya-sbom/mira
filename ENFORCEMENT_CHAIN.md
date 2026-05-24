# Enforcement Chain

## Current Protected Path

Code change
→ GitHub Actions
→ `verify-output`
→ `verify_output.py`
→ canonical receipt validation
→ protected `main` branch

## Enforcement Rule

The protected branch depends on the `verify-output` status check.

If canonical receipt verification fails, the protected path must not proceed.

## Current Canonical Artifact

`canonical/pass.json`

## Verifier

`verify_output.py`

## Invariant

No valid receipt → no accepted state transition.

## Strategic Meaning

The repository is no longer only storing verification code.

It now requires verification output as part of the protected development path.
