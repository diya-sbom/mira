# Policy Semantics

## Purpose

Policy semantics define how verified receipts are accepted or rejected by Veridian policy enforcement.

Verification answers:

Is the receipt structurally and cryptographically valid?

Policy answers:

Is this valid receipt acceptable for this environment?

## Core Rule

Verified does not automatically mean approved.

A receipt must pass both:

1. receipt verification
2. policy approval

## Policy Decisions

### POLICY_ALLOW

The receipt is valid and satisfies policy requirements.

### POLICY_BLOCK

The receipt is invalid, denied, unsupported, or does not satisfy policy requirements.

## Initial Policy Requirements

A receipt is accepted only if:

- required fields are present
- `record_hash` is valid
- `decision` is `ALLOW`
- receipt version is supported
- canonical verification passes

## Deny Conditions

Policy must block if:

- `decision` is `DENY`
- `decision` is missing
- `record_hash` is missing
- receipt version is unsupported
- receipt verification fails

## Fail-Closed Rule

If policy cannot determine approval, it must block.

## Stability Rule

Future policy versions may add new requirements, but must not redefine the meaning of existing decisions.

## Invariant

No valid receipt + policy approval → no accepted state transition.
