# Veridian Due Diligence Checklist

## Technical Foundation
- MIRA Core implemented
- Sentinel enforcement implemented
- Real Diya API integrated
- Executor implemented
- AFS commit layer integrated

## Framework Integrations
- LangChain adapter
- AutoGen adapter
- CrewAI adapter

## External Dependency Proof
- veridian-first-dependent
- veridian-compliance-reviewer
- veridian-contract-reviewer
- veridian-audit-evidence-verifier

## Security Properties
- Fail-closed behavior
- Non-bypassable control path
- Deterministic verification
- Tamper-evident history

## Documentation
- README.md
- ARCHITECTURE.md
- WHY_VERIDIAN_EXISTS.md
- ENTERPRISE_BRIEFING.md

## Evaluation Questions
1. Does removing Veridian break dependent applications?
2. Are invalid actions blocked?
3. Are invalid state transitions rejected?
4. Can external frameworks be forced through the control path?
5. Is the architecture coherent and extensible?

## Summary
Veridian is a cryptographic control plane for autonomous systems with working code, external dependency proofs, and multi-framework integrations.
