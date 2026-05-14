# AFS — Agentic File System

## Problem

Autonomous agents can propose changes to system state without a guaranteed, enforceable proof that the resulting state is valid.

AFS solves this by making every state change pass through lease control, isolated execution, verification, and atomic commit.

## Core Rule

No state change exists unless it passes AFS.

## Flow

Agent
↓
Request Lease
↓
AFS Gateway
↓
Ephemeral Sandbox
↓
Proposed State
↓
MIRA Verification
↓
Diya Verification
↓
Atomic Commit
↓
State Store

## Minimal Components

1. Lease Manager
2. Sandbox Manager
3. Commit Controller
4. Atomic Swap Engine
5. Verification Adapter
6. State Store Interface

## Success Criteria

- No direct writes to state
- Invalid proposals are rejected
- Valid proposals commit atomically
- Removal of AFS breaks the workflow
