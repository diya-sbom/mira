# MIRA

Veridian is a cryptographic control plane for autonomous systems.

It verifies actions before execution and state transitions before persistence.

If verification fails, execution halts and no state is committed.

MIRA is the state verification layer within Veridian.

It ensures:
- only valid state changes are accepted
- every accepted change produces a verifiable receipt
- history is tamper-evident---

## Verification Contract

MIRA’s current verification semantics are defined in:

- `VERIFICATION_CONTRACT.md`
- `CORE_FREEZE.md`
- `canonical_examples/PASS_RECEIPT.json`
- `canonical_examples/FAIL_RECEIPT.json`

Core invariant:

No valid MIRA receipt → no accepted output.

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


## CI Enforcement

GitHub Actions runs the `verify-output` job on push and pull request.

The repository now depends on the verification result: canonical examples and API tests must pass before the protected workflow is considered valid.

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
