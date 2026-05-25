# Veridian Policy Layer

## Purpose

The policy layer defines which verified receipts are acceptable.

Verification proves structure and integrity.

Policy decides whether the verified result is allowed for a specific environment.

## Initial Policy Rules

A receipt is accepted only if:

- `decision` is `ALLOW`
- `record_hash` is valid
- required fields are present
- receipt version is supported
- canonical verification passes

## Deny Conditions

A receipt is denied if:

- required fields are missing
- hash validation fails
- decision is not `ALLOW`
- receipt version is unsupported
- policy requirements are not satisfied

## Invariant

Verified does not always mean approved.

Policy approval is required before acceptance.
