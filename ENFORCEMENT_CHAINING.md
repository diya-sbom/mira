# Enforcement Chaining

## Purpose

Enforcement chaining defines the ordered execution path for Veridian verification and policy enforcement.

## Current Chain

Receipt
→ Verifier
→ Policy Evaluation
→ Enforcement Decision
→ State Transition

## Current Components

### Receipt

Canonical proof artifact.

### Verifier

Validates:
- required fields
- decision semantics
- record hash integrity

### Policy Evaluation

Determines whether a verified receipt is acceptable for the target environment.

### Enforcement Decision

Returns:
- `POLICY_ALLOW`
- `POLICY_BLOCK`

### State Transition

Allowed only after successful verification and policy approval.

## Fail-Closed Rule

Failure at any stage must block downstream execution.

## Long-Term Direction

Future chains may include:

MIRA
→ Policy
→ Diya
→ Executor
→ AFS
→ State Store

## Invariant

No successful chain → no accepted transition.
