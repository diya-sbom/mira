# Cross-Repo Enforcement

## Purpose

Cross-repo enforcement means an external repository cannot proceed unless Veridian verification and policy checks pass.

## Current Proof

Veridian currently has:

- canonical receipt verification
- fail-closed receipt validation
- policy semantics
- policy templates
- external dependent consumer
- external policy enforcer
- CI-based policy enforcement

## Target Enforcement Model

External Repo
→ Veridian Receipt
→ Independent Verifier
→ Policy Enforcer
→ CI Required Check
→ Merge / Deploy Allowed or Blocked

## Required Behavior

If verification fails, the external repo must block.

If policy fails, the external repo must block.

If required proof is missing, the external repo must block.

## Invariant

No valid verification + policy approval → no external execution.
