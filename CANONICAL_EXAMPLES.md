# MIRA Canonical Examples

## Version
MIRA Core v1.0 (Frozen)

---

## Canonical PASS Example

File:
examples/canonical/pass.json

Meaning:
A valid state transition with correct structure and proof.

Expected result:
Decision: PASS  
Reason: Genesis state accepted

---

## Canonical FAIL Example

File:
examples/canonical/fail.json

Meaning:
An invalid state transition with broken proof linkage.

Expected result:
Decision: FAIL  
Reason: Previous state hash mismatch

---

## Command

From an external agent environment:

python3 examples/canonical/run_canonical.py

---

## Result

MIRA accepts the valid transition and rejects the invalid transition.

---

## Purpose

These two examples form the canonical reference pair for MIRA Core v1.0.

They define the minimum demonstrable difference between:
- accepted state transition
- rejected state transition

---

## Rule

Do not change the meaning of these examples without versioning.
