# Signed Receipts

## Purpose

Signed receipts bind a verification result to a trusted issuer.

Hashing proves receipt integrity.

Signing proves receipt origin.

## Current State

MIRA currently supports deterministic receipt verification using:

- canonical JSON
- SHA-256 record hash
- fail-closed verifier behavior

## Next Layer

Signed receipts add identity and trust.

A signed receipt should prove:

- who issued the receipt
- what was verified
- when it was verified
- whether the receipt was altered after signing

## Required Future Fields

```json
{
  "version": "1.0",
  "ts": 0,
  "state": {},
  "decision": "ALLOW",
  "record_hash": "<sha256>",
  "issuer": "<issuer-id>",
  "signature": "<signature>"
}
