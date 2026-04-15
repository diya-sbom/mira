import hashlib
import json
from datetime import datetime


def hash_state(state_data):
    """
    Create deterministic hash of state data
    """
    canonical = json.dumps(state_data, sort_keys=True)
    return hashlib.sha256(canonical.encode()).hexdigest()


def verify_transition(prev_state, new_state, proof):
    """
    Core MIRA verification logic
    """

    # 1. Check previous state hash
    expected_prev_hash = hash_state(prev_state["data"])
    if proof["prev_state_hash"] != expected_prev_hash:
        return "FAIL", "Previous state hash mismatch"

    # 2. Check new state hash
    expected_new_hash = hash_state(new_state["data"])
    if proof["new_state_hash"] != expected_new_hash:
        return "FAIL", "New state hash mismatch"

    # 3. Check version increment
    if new_state["version"] != prev_state["version"] + 1:
        return "FAIL", "Invalid version increment"

    # 4. Basic proof fields check
    required_fields = ["operation", "actor", "timestamp"]
    for field in required_fields:
        if field not in proof:
            return "FAIL", f"Missing proof field: {field}"

    return "PASS", "Valid state transition"


def generate_receipt(prev_state, new_state, decision, reason):
    """
    Create receipt after verification
    """
    receipt = {
        "receipt_id": hashlib.sha256(
            (str(datetime.utcnow()) + new_state["hash"]).encode()
        ).hexdigest(),
        "prev_state_hash": prev_state["hash"],
        "new_state_hash": new_state["hash"],
        "decision": decision,
        "timestamp": datetime.utcnow().isoformat(),
        "reason": reason,
        "verifier": "MIRA_v0"
    }

    return receipt


if __name__ == "__main__":
    # Example test
    prev_state = {
        "state_id": "1",
        "version": 1,
        "data": {"value": "A"},
        "hash": ""
    }
    prev_state["hash"] = hash_state(prev_state["data"])

    new_state = {
        "state_id": "2",
        "version": 2,
        "data": {"value": "B"},
        "hash": ""
    }
    new_state["hash"] = hash_state(new_state["data"])

    proof = {
        "prev_state_hash": prev_state["hash"],
        "new_state_hash": new_state["hash"],
        "operation": "update",
        "actor": "agent_1",
        "timestamp": datetime.utcnow().isoformat()
    }

    decision, reason = verify_transition(prev_state, new_state, proof)
    receipt = generate_receipt(prev_state, new_state, decision, reason)

    print("Decision:", decision)
    print("Reason:", reason)
    print("Receipt:", json.dumps(receipt, indent=2))
