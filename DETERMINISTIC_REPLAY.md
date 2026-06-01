# Deterministic Replay

## Purpose

Verification should be reproducible.

A verifier should produce the same decision when executed against the same receipt and ruleset.

## Replay Inputs

- receipt
- verifier version
- policy version
- canonical JSON rules
- hash algorithm

## Replay Output

Replay must produce:

- the same verifier decision
- the same failure reason
- the same evidence result

## Core Rule

Same inputs must produce the same decision.

## Fail Condition

If identical inputs produce different decisions, verifier drift has occurred.

## Future Enforcement

Replay validation should be executable by independent operators.

## Invariant

No deterministic replay → no trusted historical verification.
