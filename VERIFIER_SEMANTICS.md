# Verifier Semantics

## Purpose

Verifier semantics define how MIRA determines whether a receipt is valid.

The verifier does not approve execution.

The verifier only determines receipt validity.

Policy decides whether a valid receipt is acceptable.

## Required Fields

A valid receipt must contain:

- `version`
- `ts`
- `state`
- `decision`
- `record_hash`

## Valid Decisions

The only valid receipt decisions are:

- `ALLOW`
- `DENY`

## Hash Rule

`record_hash` must equal the SHA-256 hash of the canonical JSON representation of the receipt excluding `record_hash`.

Canonical JSON uses:

- sorted keys
- compact separators
- UTF-8 encoding

## Failure Outputs

The verifier must fail closed with deterministic outputs:

- `MISSING_FIELD: <field>`
- `INVALID_DECISION`
- `HASH_MISMATCH`
- parser error / malformed receipt failure

## Success Output

A valid receipt returns:

`RECEIPT_VALID`

## Stability Rule

Future verifier versions may add new checks.

They must not redefine the meaning of existing verifier outputs.

## Core Invariant

No valid receipt → no accepted state transition.
