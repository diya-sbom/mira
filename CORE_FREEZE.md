MIRA CORE FREEZE — v1.0

Decision:
PASS → state contains "proof"
FAIL → state missing "proof"

Behavior:
- PASS → execution allowed
- FAIL → execution halted

Verification Record:
- version
- ts
- state_hash
- decision
- record_hash

Ledger:
- append-only
- stores record_hash + state_hash + decision + ts

These semantics are fixed for v1.0.
Any changes must be versioned.
