# History Continuity

## Purpose

Verification of a single receipt is not sufficient.

A trusted system must also verify continuity between receipts.

## Current State

MIRA verifies:

- receipt integrity
- receipt semantics
- policy compliance

## Missing Layer

MIRA does not yet verify chronological continuity.

## Target Model

Receipt N
→ references Receipt N-1

Receipt N+1
→ references Receipt N

## Required Future Fields

```json
{
  "receipt_id": "<current>",
  "previous_receipt_id": "<previous>"
}
