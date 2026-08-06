# Full Chain Proof

## Purpose

This document defines the narrow Veridian full-chain proof target.

No UI.  
No dashboard.  
No plugins.  
No scaling.  
No extra features.

Only one enforced path.

## Clean Chain

External System
→ Adopter
→ Sentinel
→ Agent Runtime proposes action + intended state delta
→ Diya verifies action intent BEFORE execution
→ Executor / Sandbox runs action
→ MIRA verifies actual state AFTER execution
→ AFS commit gate
→ State Store

## Key Rules

Diya = intent/action verification before execution.

MIRA = actual state verification after execution.

AFS = commit only verified state.

Sentinel = prevents bypass.

Adopter = forces entry.

## Narrow Proof Path

external input
→ adopter
→ sentinel
→ Diya pre-exec gate
→ executor sandbox
→ MIRA post-exec state verification
→ AFS commit
→ state store

## Success Conditions

If Diya fails, executor does not run.

If MIRA fails, AFS does not commit.

If Sentinel is bypassed, flow fails closed.

Final state changes only after a verified commit.

## Core Invariant

No verified intent
→ no execution.

No verified state
→ no commit.

No Sentinel path
→ fail closed.
