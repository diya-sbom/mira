# Attack Simulations

## Purpose

This document records deterministic adversarial simulations against Veridian receipt verification and policy enforcement.

The goal is not to claim perfect security.

The goal is to show expected fail-closed behavior under specific attack conditions.

---

## ATTACK-001 — Missing Required Fields

### Attack

A receipt is submitted without one or more required fields.

Examples:

- `version`
- `decision`
- `record_hash`

### Expected Result

`MISSING_FIELD`

### Enforcement Result

BLOCK

### Protected Invariant

No structurally incomplete receipt may be accepted.

---

## ATTACK-002 — Invalid Decision Injection

### Attack

A receipt uses an unsupported decision value.

Example:

`ALLOW_ALL`

### Expected Result

`INVALID_DECISION`

### Enforcement Result

BLOCK

### Protected Invariant

Only explicitly defined decisions may control execution.

---

## ATTACK-003 — Record Hash Tampering

### Attack

The receipt body is changed after `record_hash` is created.

### Expected Result

`HASH_MISMATCH`

### Enforcement Result

BLOCK

### Protected Invariant

Receipt contents must match the committed cryptographic digest.

---

## ATTACK-004 — Receipt Substitution

### Attack

A different receipt is substituted into the verification path.

### Expected Result

Verification or policy mismatch.

### Enforcement Result

BLOCK

### Protected Invariant

Only the expected canonical receipt path may authorize transition.

---

## ATTACK-005 — Partial Receipt Truncation

### Attack

A receipt is cut off, malformed, or missing required structure.

### Expected Result

Verification failure.

### Enforcement Result

BLOCK

### Protected Invariant

Malformed proof artifacts cannot authorize execution.

---

## Core Rule

If verification or policy cannot prove approval, execution must not proceed.
