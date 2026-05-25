# Architecture Overview

## Core Flow

Code / State Change
→ Canonical Receipt
→ Verifier
→ GitHub Actions
→ Required `verify-output`
→ Protected `main`

## External Dependency Flow

External Consumer
→ Independent Verifier
→ Blessed Receipt
→ Frozen Verifier Semantics
→ ALLOW / DENY

## Invariant

No valid receipt → no accepted state transition.

## Current Proofs

- Canonical receipt validation
- Fail-closed proof
- Protected branch enforcement
- Independent verifier
- External dependent consumer

## Strategic Meaning

Veridian is not only a tool. It is an enforcement layer where downstream systems can depend on verified receipts.
