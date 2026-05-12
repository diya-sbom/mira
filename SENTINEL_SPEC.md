# SENTINEL_SPEC.md

# Sentinel Specification v1.0

Status: Draft
Scope: Architecture and protocol definition
Implementation Status: Not Started

---

## 1. Purpose

Sentinel is the deterministic control plane that ensures no state transition or external action can occur unless all required verification gates approve it.

Sentinel coordinates the integrity engines but does not replace them.

---

## 2. Core Principle

Nothing changes unless Sentinel returns ALLOW.

If Sentinel returns DENY, the operation must stop immediately.

---

## 3. Responsibilities

Sentinel performs five functions:

1. Classify the requested operation
2. Route the request to the required verification engines
3. Enforce the required sequence
4. Return a final decision
5. Release or block execution

---

## 4. Non-Responsibilities

Sentinel does not:

- Verify state integrity (MIRA does this)
- Verify action integrity (Diya does this)
- Execute actions
- Store memory
- Commit state
- Modify verification results

---

## 5. Operation Types

Sentinel supports three operation types:

### STATE_ONLY
Operations that affect state or memory only.

### ACTION_ONLY
Operations that affect external systems only.

### STATE_ACTION_COMPOSITE
Operations that modify state and execute actions in one sequence.

---

## 6. Decision Contract

Sentinel returns one of two decisions:

### ALLOW
The operation may proceed.

### DENY
The operation is blocked.

Optional future decision:
- REQUIRE_APPROVAL

---

## 7. Component Relationships

### MIRA
Verifies state integrity and issues receipts.

### Diya
Verifies action integrity and issues Verification Records.

### AFS
Controls state transitions and commits accepted state.

### Adopter
Integrates external systems and forces them through Sentinel.

---

## 8. Routing Rules

### STATE_ONLY
Sentinel → MIRA → AFS

### ACTION_ONLY
Sentinel → Diya → Executor

### STATE_ACTION_COMPOSITE
Sentinel → MIRA → Diya → Executor → MIRA → AFS

---

## 9. Composite Sequence

1. Validate proposed state using MIRA
2. Validate action using Diya
3. Execute the action
4. Validate resulting state using MIRA
5. Commit state using AFS
6. Return ALLOW

If any step fails, Sentinel returns DENY.

---

## 10. Default Deny

Sentinel denies the operation when:

- Operation type is unknown
- Required proof is missing
- Any verification step fails
- Execution fails
- State commit conditions are not met

---

## 11. Proof References

Sentinel may return references to proof artifacts, including:

- pre_state_receipt
- diya_verification_record
- post_state_receipt

Sentinel does not generate these artifacts; it only binds their references.

---

## 12. Non-Bypass Requirement

All Adopters must use Sentinel as the mandatory entry point.

Direct access to:

- Memory stores
- Executors
- State commit interfaces

must be blocked.

---

## 13. Determinism

For the same inputs and verification results, Sentinel must return the same decision.

Sentinel must not rely on probabilistic or non-deterministic behavior.

---

## 14. Fail-Closed Behavior

If Sentinel cannot reach a required verification engine, the operation must be denied.

No partial success is allowed.

---

## 15. Minimal Interface

sentinel_gatekeeper(operation_type, payload) -> Decision

---

## 16. Invariants

- No state without valid MIRA receipt
- No action without valid Diya Verification Record
- No commit without successful post-state validation
- No operation without Sentinel ALLOW

---

## 17. Architectural Position

Adopter
    ↓
Sentinel
   ↙   ↘
MIRA   Diya
  ↓      ↓
AFS   Executor

---

## 18. One-Line Summary

Sentinel is the final yes-or-no control plane that determines whether state and action are allowed to exist.
