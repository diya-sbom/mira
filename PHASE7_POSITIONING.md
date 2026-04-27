# MIRA — Phase 7

MIRA is not a logging system.

MIRA is a runtime dependency.

If MIRA is removed:
→ execution stops

If MIRA is present:
→ execution proceeds

## Core

MIRA enforces:

Memory is not accepted because it exists.

Memory is accepted only if:
- lineage is valid
- proof is valid
- invariants hold

## System

Agent
→ MIRA Adapter
→ MIRA Core
→ Memory Store

## Direction

The goal is not visibility.

The goal is dependency.

Systems should not be able to operate safely without MIRA.
