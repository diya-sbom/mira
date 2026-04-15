# MIRA Core Freeze

## Version
MIRA Core v0.1

## Frozen Doctrine
Memory_n = State_n + Proof(State_(n-1) -> State_n)

No valid proof -> no accepted memory

## Frozen Architecture
Agent -> MIRA -> Memory Store

Store is passive.
All writes go through MIRA.
FAIL halts execution.
Tampering must be detectable.

## Frozen Decision Semantics
PASS = the proposed state transition was verified and accepted
FAIL = the proposed state transition was rejected

## Frozen Verification Semantics
A transition is valid only if:
1. proof.prev_state_hash matches the hash of the previous state's data
2. proof.new_state_hash matches the hash of the new state's data
3. new_state.version = prev_state.version + 1
4. proof contains:
   - operation
   - actor
   - timestamp

## Frozen Receipt Semantics
A receipt contains:
- receipt_id
- prev_state_hash
- new_state_hash
- prev_receipt_hash
- decision
- timestamp
- reason
- verifier
- receipt_hash

## Frozen Chain Semantics
Each accepted receipt links to the previous accepted receipt by prev_receipt_hash.

If receipt linkage is broken, history integrity fails.

## Steward Rule
Do not change the meaning of an existing receipt after others may depend on it.

Allowed:
- add optional fields
- add new versions
- add new verification modes

Not allowed:
- silently change PASS / FAIL meaning
- silently change receipt semantics
- reinterpret old receipts without versioning
