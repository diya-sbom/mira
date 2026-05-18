# Why Veridian Exists

AI systems can execute actions, modify files, and persist memory.

Most systems assume these operations are trustworthy once they are requested.

Veridian changes that assumption.

Veridian requires every action and every state transition to pass independent verification before it is accepted.

If verification fails, execution halts and no state is committed.

This creates a fail-closed control layer for AI systems.

## Core Principle

No valid proof → no accepted state.

## Architecture

Adapters force external frameworks into the verification path.

Sentinel prevents bypass.

Diya verifies actions before execution.

MIRA verifies state transitions before persistence.

AFS commits only verified state.

## Why It Matters

As AI systems become more autonomous, the cost of unverified execution increases.

Veridian provides a deterministic control layer that allows organizations to enforce integrity, traceability, and tamper-evident history.

## In One Sentence

Veridian is a cryptographic control plane for autonomous systems.
