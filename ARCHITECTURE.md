# Veridian Architecture


External Systems
        ↓
     Adopter
        ↓
     Sentinel
        ↓
       MIRA
        ↓
       Diya
        ↓
     Executor
        ↓
       MIRA
        ↓
        AFS
        ↓
    State Store



## Component Roles

### Adopter
Forces external systems to enter the Veridian control path.

### Sentinel
Prevents bypass and terminates invalid execution paths.

### MIRA
Verifies state transitions and produces tamper-evident receipts.

### Diya
Verifies intent and action integrity before execution.

### Executor
Runs approved actions in a controlled environment.

### AFS
Commits only verified state transitions atomically.

### State Store
Passive persistence layer that receives only validated state.

## Core Invariant

No valid receipt → no accepted state transition.

## Strategic Meaning

Veridian is a verification and control layer for AI systems.

It ensures that actions and memory updates are accepted only when they pass deterministic integrity checks.
