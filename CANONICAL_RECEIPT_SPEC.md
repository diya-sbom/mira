# Canonical Receipt Specification

## Purpose

The canonical receipt is the stable proof artifact for Veridian verification.

It records the evaluated state, the verification decision, and the cryptographic hash used for independent verification.

## Required Fields

```json
{
  "version": "1.0",
  "ts": 0,
  "state": {},
  "decision": "ALLOW",
  "record_hash": "<sha256>"
}
