# Veridian Demo Script (5 Minutes)

## 1. Problem

Autonomous systems can execute actions and persist state without deterministic verification.

This creates governance, security, and compliance risk.

## 2. Solution

Veridian verifies:

1. Actions before execution
2. State transitions before persistence

If verification fails, execution halts and no state is committed.

## 3. Architecture

External System
    ↓
Adapters
    ↓
Sentinel
    ↓
MIRA
    ↓
Diya
    ↓
Executor
    ↓
AFS
    ↓
State Store

## 4. Canonical Tests

Run:

```bash
python3 run_canonical_examples.py
