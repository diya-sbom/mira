# MIRA Core

## Definition
MIRA = Memory Integrity and Receipt Architecture

## Doctrine
Memory_n = State_n + Proof(State_(n-1) -> State_n)

## Acceptance Rule
No valid proof -> no accepted memory

## Architecture
Agent -> MIRA (verify + decide) -> Memory Store

## System Rules
1. Store is passive.
2. All writes go through MIRA.
3. FAIL halts execution.
4. Tampering must be detectable.
5. Any accepted state must have a receipt.
6. Any state without a valid receipt is invalid.

## Decision Semantics
PASS = verified and accepted
FAIL = rejected

## Core Objects
- State
- Previous State Reference
- Proof
- Receipt
