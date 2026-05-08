# BIL Freeze — v1.0

BIL is the append-only evidence ledger for accepted MIRA verification receipts.

## Entry Fields

Each BIL entry contains:

- timestamp
- decision
- record_hash
- previous_hash
- entry_hash

## Semantics

- `decision` records the MIRA verification result.
- `record_hash` links the ledger entry to the MIRA verification record.
- `previous_hash` links this entry to the previous accepted ledger entry.
- `entry_hash` is the deterministic hash of the current entry.

## Invariants

- No ledger entry without a MIRA receipt.
- No accepted history without valid hash-chain continuity.
- Any modified entry must break verification.
- Any removed entry must break continuity.

## v1.0 Rule

These fields and meanings are frozen for BIL v1.0.

Future changes must be versioned.
