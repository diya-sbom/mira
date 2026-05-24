# Verifier Compatibility Policy

## Purpose

This policy defines long-term verifier compatibility guarantees.

## Core Rule

A verifier that supports receipt version `1.x` must continue validating all blessed `1.x` receipts indefinitely.

## Stability Guarantee

Existing field meanings must never change.

The following fields are permanently stable for `1.x` receipts:

- `version`
- `ts`
- `state`
- `decision`
- `record_hash`

## Decision Stability

The meaning of:

- `ALLOW`
- `DENY`

must never change for `1.x`.

## Hash Stability

The canonicalization rules for `1.x` receipts must never change.

This includes:

- sorted keys
- compact separators
- UTF-8 encoding
- SHA-256 hashing

## Allowed Future Changes

Future versions may:

- add optional fields
- add new receipt versions
- add additional verifier outputs

Future versions must not:

- redefine existing fields
- redefine existing decisions
- invalidate blessed receipts
- silently alter canonicalization rules

## Blessed Receipt Rule

All blessed receipts are permanent compatibility artifacts.

Every future verifier release must validate them successfully.

## Invariant

Once dependency exists, semantic stability becomes mandatory.
