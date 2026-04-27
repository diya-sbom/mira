# MIRA

MIRA is a verification gate for state transitions.

It ensures:
- only valid state changes are accepted
- every accepted change produces a verifiable receipt
- history is tamper-evident
---

## 2-Minute Proof

Start MIRA:

uvicorn api.api:app --reload

Run canonical examples:

python3 examples/canonical/run_canonical.py

Expected:

- pass.json → PASS
- fail.json → FAIL

MIRA accepts valid state transitions and rejects invalid ones.

No transition is valid without verification.
---

## Flow

Agent → MIRA → Store → Ledger

- MIRA verifies transitions
- Store accepts only PASS
- Ledger records proof

If MIRA is removed, the system stops.

---

## What’s included

- SPEC.md (frozen protocol)
- reference implementation
- examples (PASS / FAIL)

---

## What’s not included

The MIRA Core verification engine is not exposed as a public library.

It is accessed through the API boundary.

---

## Decision Model

MIRA returns only:
- PASS
- FAIL

No partial states.

---

## Enforcement

- FAIL → execution halts  
- no write  
- no ledger append  

---

## Status

Working. Enforced. Fail-closed.

---

## License

- Specification: Apache 2.0  
- Core: BSL 1.1
