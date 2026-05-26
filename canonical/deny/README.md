# Canonical Deny Examples

These examples define negative-path policy behavior.

## deny_decision.json

A structurally present receipt with `decision: DENY`.

Expected policy result:

`POLICY_BLOCK`

## Rule

A denied receipt must never be accepted by policy enforcement.
