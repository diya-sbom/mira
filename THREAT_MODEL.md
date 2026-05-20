# Veridian Threat Model

## Assets Protected

- Agent state
- Memory writes
- Action requests
- Verification receipts
- Ledger history
- Execution decisions

## Primary Threats

### 1. Invalid State Write

An agent attempts to persist corrupted or unauthorized state.

Control:
MIRA rejects state transitions without valid verification.

### 2. Unauthorized Action

An agent attempts to execute an unapproved action.

Control:
Diya verifies action integrity before execution.

### 3. Bypass Attempt

A system attempts to avoid the verification path.

Control:
Sentinel blocks execution paths that do not pass verification.

### 4. Receipt Tampering

A receipt is modified after creation.

Control:
Receipts are tamper-evident and linked to verification history.

### 5. Ledger Manipulation

Ledger entries are changed or removed.

Control:
Append-only ledger structure detects continuity breaks.

## Core Invariant

No valid receipt → no accepted state transition.

## Fail-Closed Rule

If verification is unavailable, incomplete, or invalid, execution must halt.
