# MIRA Verification Contract

MIRA produces a decision for protected execution and state acceptance.

## Decisions

PASS means:
- required proof is present
- verification succeeded
- execution or state acceptance may continue

FAIL means:
- required proof is missing or invalid
- verification failed
- execution or state acceptance must stop

## Required Evidence

A valid accepted output must include:

- decision
- record_hash
- receipt
- protected output

## Canonical Examples

Canonical PASS receipt:

`canonical_examples/PASS_RECEIPT.json`

Canonical FAIL receipt:

`canonical_examples/FAIL_RECEIPT.json`

## Invariant

No valid MIRA receipt → no accepted output.
