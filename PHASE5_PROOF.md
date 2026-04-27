# Phase 5 — External Dependency Proof

## Objective

Demonstrate that the system cannot produce an answer without external, verified evidence.

---

## Architecture

READ:
Retriever → Evidence Bundle → MIRA Adapter → MIRA Core → Verified Context → LLM

OUTPUT:
LLM proposed answer → MIRA Output Gate → Final Answer or HALT

WRITE (optional):
Agent → MIRA Adapter → MIRA Core → Store / Ledger

---

## Enforcement Rules

- Evidence MUST originate from an external source
- Evidence MUST be non-empty
- Evidence MUST include a valid hash
- Unsupported answers MUST be blocked
- Missing evidence MUST halt execution

---

## Test Cases

### 1. Valid External Evidence

Condition:
External knowledge file contains valid data.

Command:
python3 phase5_rag_mira/agent.py

Result:
- PASS
- Final answer produced
- Receipt generated

---

### 2. Missing External Evidence

Condition:
External knowledge file is empty.

Command:
python3 phase5_rag_mira/agent.py

Result:
MIRA READ HALT: no external evidence found

---

### 3. Unsupported Answer

Condition:
Proposed answer not grounded in retrieved evidence.

Result:
MIRA OUTPUT HALT: answer not supported by verified context

---

## Conclusion

The system enforces external dependency at runtime.

Removing or bypassing external evidence results in immediate failure.

The agent cannot produce an answer without:
1. External retrieval
2. Verified evidence
3. MIRA PASS decision

---

## Final Statement

External knowledge is no longer optional.

It is a required dependency for execution.
