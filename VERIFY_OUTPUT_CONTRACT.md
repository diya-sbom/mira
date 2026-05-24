# Verify Output Contract

## Purpose

`verify_output.py` is the enforcement verifier for the canonical receipt.

It validates that the canonical receipt is structurally complete and cryptographically consistent.

## Canonical Input

`canonical/pass.json`

## Required Fields

The canonical receipt must contain:

- `version`
- `ts`
- `state`
- `decision`
- `record_hash`

## Valid Decisions

Only the following decisions are valid:

- `ALLOW`
- `DENY`

## Hash Rule

`record_hash` must equal the SHA-256 hash of the canonical JSON representation of the receipt excluding the `record_hash` field.

The canonical JSON representation uses:

- sorted keys
- compact separators
- UTF-8 encoding

## Fail-Closed Behavior

If any required field is missing, verification fails.

If the decision is invalid, verification fails.

If the hash does not match, verification fails.

## Success Output

```text
RECEIPT_VALID


## Failure Outputs

```text
MISSING_FIELD: <field>
INVALID_DECISION
HASH_MISMATCH
```
