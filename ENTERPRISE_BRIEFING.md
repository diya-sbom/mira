# Veridian Enterprise Briefing

## Executive Summary

Veridian is a cryptographic control plane for autonomous systems.

It verifies every action before execution and every state transition before persistence.

If verification fails, execution halts and no state is committed.

## Core Architecture

External Frameworks (LangChain, AutoGen, CrewAI)
        ↓
Adapters
        ↓
Sentinel
        ↓
MIRA (state verification)
        ↓
Diya (action verification)
        ↓
Executor
        ↓
MIRA (post-state verification)
        ↓
AFS (atomic commit)
        ↓
State Store

## Key Properties

- Fail-closed enforcement
- Non-bypassable verification
- Tamper-evident history
- Framework-agnostic integration
- External dependency proof

## External Applications

- veridian-first-dependent
- veridian-compliance-reviewer
- veridian-contract-reviewer
- veridian-audit-evidence-verifier

## Enterprise Use Cases

- AI governance
- Compliance automation
- Audit evidence verification
- Contract review
- Memory integrity

## Strategic Position

Veridian creates a mandatory decision layer for autonomous systems.

Applications cannot act or persist state without approval.

## One-Line Summary

Veridian is a cryptographic control plane for autonomous systems.
