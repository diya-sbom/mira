# Policy Templates

Policy templates define reusable approval requirements for Veridian enforcement.

## default_policy.json

The baseline fail-closed policy template.

Rules:
- only `ALLOW` decisions are accepted
- required fields must exist
- unsupported receipt versions are blocked
- verification failures are blocked

## Purpose

Policy templates separate:

- receipt verification
from
- environment approval rules
