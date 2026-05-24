# Canonical Receipt

## Purpose

A Veridian receipt is the primary proof artifact for a verified state transition.

It records:

- what was evaluated
- what decision was made
- when it occurred
- how the record can be independently verified

## Required Fields

```json
{
  "version": "1.0",
  "ts": 0,
  "state": {},
  "decision": "ALLOW",
  "record_hash": "<sha256>"
}
