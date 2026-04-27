# MIRA Specification v1.0 (Frozen)

## 1. Purpose

MIRA enforces valid state transitions and produces a verifiable receipt.  
No state change is valid without MIRA verification.

---

## 2. Input

A verification request MUST contain:
- prev_state (object or null)
- new_state (object)
- proof (object)

### new_state REQUIRED fields:
- state_id (string)
- version (integer)
- data (object)

### proof REQUIRED fields:
- operation (string)
- actor (string)
- timestamp (string)

---

## 3. Rules

### 3.1 Genesis Rule

If prev_state is null:
- new_state.version MUST equal 1

Otherwise → FAIL

---

### 3.2 Hash Integrity

- hash(prev_state.data) MUST equal proof.prev_state_hash
- hash(new_state.data) MUST equal proof.new_state_hash

Otherwise → FAIL

---

### 3.3 Version Continuity

- new_state.version MUST equal prev_state.version + 1

Otherwise → FAIL

---

### 3.4 Required Proof Fields

- operation MUST exist
- actor MUST exist
- timestamp MUST exist

Otherwise → FAIL

---

## 4. Decision

MUST return only:
- PASS
- FAIL

No intermediate states.

---

## 5. Receipt (on PASS)

MUST include:
- receipt_id
- decision
- timestamp
- prev_receipt_hash (null for genesis)
- receipt_hash
- new_state_hash

---

## 6. Enforcement

If decision != PASS:
- state MUST NOT be written
- ledger MUST NOT append
- execution MUST halt

---

## 7. Ledger

- Each PASS MUST append a receipt
- Ledger MUST be append-only
- Each receipt MUST reference previous via prev_receipt_hash

---

## 8. Failure Behavior

Any validation failure MUST halt execution.  
No fallback or bypass allowed.

---

## 9. Determinism

Same input MUST produce same decision.

---

## 10. Versioning

This specification is frozen as v1.0.  
Behavior MUST NOT change.  
Future changes require new versions.
## 11. Formal Invariants (v1.0)

### State Transition

S_{t+1} = f(S_t, A)

A transition is valid **iff**:

MIRA_VERIFY(S_t, A) = PASS

Otherwise:
- S_{t+1} MUST NOT be written
- No ledger entry is appended
- Execution MUST halt

---

### Proof Requirement

Proof(S_t, A) MUST include:
- prev_state_hash
- new_state_hash
- operation, actor, timestamp

Hash rules:
- hash(S_t.data) == prev_state_hash
- hash(S_{t+1}.data) == new_state_hash

---

### Determinism

Given identical inputs (S_t, A, Proof):
- decision MUST be identical
- receipt_hash MUST be identical

---

### Ledger Invariant

For every PASS:
- exactly one receipt is appended
- receipt.prev_receipt_hash links to prior receipt

No mutation, no deletion.

---

### Enforcement

If any invariant fails:
- decision = FAIL
- state write is blocked
- ledger append is blocked
