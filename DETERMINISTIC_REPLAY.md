# Deterministic Replay

## Purpose

Verification should be reproducible.

A verifier should produce the same decision when executed against the same receipt and ruleset.

## Replay Inputs

- receipt
- verifier version
- policy version

## Replay Output

- PASS
- FAIL
- identical evidence

## Invariant

Same inputs must produce the same decision.

## Fail Condition

Different decisions from identical inputs indicate verifier drift.

## Future Enforcement

Replay validation should be executable by independent operators.
