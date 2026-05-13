# Sentinel Roadmap

Status: Draft

## Phase 0 — Specification
- Define Sentinel purpose
- Define ALLOW / DENY
- Define operation types
- Define non-bypass rule

Status: Done

## Phase 1 — Gatekeeper Skeleton
- Create minimal Sentinel entry point
- Accept operation type and payload
- Return ALLOW or DENY
- Default deny unknown operations

Status: Not started

## Phase 2 — MIRA Routing
- Route STATE_ONLY to MIRA
- Require MIRA receipt
- Deny if receipt is missing or invalid

Status: Not started

## Phase 3 — Diya Routing
- Route ACTION_ONLY to Diya
- Require Diya Verification Record
- Deny if action verification fails

Status: Not started

## Phase 4 — Composite Flow
- Enforce exact sequence:
  - Adopter → Sentinel
  - Sentinel → MIRA
  - MIRA → Diya
  - Diya → Executor
  - Executor → MIRA
  - MIRA → AFS
  - AFS → State Store
- Require pre-state validation before action
- Require Diya action verification before execution
- Require post-state validation before commit
- Bind proof references across the full flow
- Deny partial success

Status: Not started

Status: Not started

## Phase 5 — Adopter Dependency
- Require Adopter to call Sentinel
- Block direct access paths
- Prove fail-closed behavior

Status: Not started
