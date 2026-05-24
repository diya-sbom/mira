# Frozen Verifier Baseline

## Tag

`verifier-v1-frozen`

## Purpose

This tag marks the first frozen verifier baseline for Veridian receipt validation.

## Guarantees

The verifier at this tag validates:

- canonical receipt structure
- required receipt fields
- ALLOW / DENY decision semantics
- SHA-256 record hash consistency
- blessed v1 receipt compatibility

## Compatibility Rule

Future verifier versions must continue validating blessed v1 receipts.

## Strategic Meaning

This tag creates a stable protocol reference point for downstream consumers.
