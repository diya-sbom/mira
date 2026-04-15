# MIRA Canonical Examples

## Version
MIRA Core v0.1

## Canonical PASS Example
File:
`examples/pass.json`

Meaning:
A valid state transition with correct previous state hash, correct new state hash, correct version increment, and required proof fields.

Expected result:
`Decision: PASS`

## Canonical FAIL Example
File:
`examples/fail.json`

Meaning:
An invalid state transition with broken proof linkage.

Expected result:
`Decision: FAIL`

## Purpose
These two examples are the canonical reference pair for MIRA Core v0.1.

They define the minimum demonstrable difference between:
- accepted memory transition
- rejected memory transition

## Rule
Do not silently change the meaning of these examples without versioning.
