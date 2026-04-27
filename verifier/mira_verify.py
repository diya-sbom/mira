import hashlib
import json
from datetime import datetime


def hash_receipt(receipt_data):
    canonical = json.dumps(receipt_data, sort_keys=True)
    return hashlib.sha256(canonical.encode()).hexdigest()


def hash_state(state_data):
    canonical = json.dumps(state_data, sort_keys=True)
    return hashlib.sha256(canonical.encode()).hexdigest()


def verify_transition(prev_state, new_state, proof):

    # 🔑 Genesis case
    if prev_state is None:
        if new_state["version"] != 1:
            return "FAIL", "First state must have version 1"
        return "PASS", "Genesis state accepted"

    # 🔒 Normal validation (only runs if NOT genesis)

    expected_prev_hash = hash_state(prev_state["data"])
    if proof["prev_state_hash"] != expected_prev_hash:
        return "FAIL", "Previous state hash mismatch"

    expected_new_hash = hash_state(new_state["data"])
    if proof["new_state_hash"] != expected_new_hash:
        return "FAIL", "New state hash mismatch"

    if new_state["version"] != prev_state["version"] + 1:
        return "FAIL", "Invalid version increment"

    
     

    required_fields = ["operation", "actor", "timestamp"]
    for field in required_fields:
        if field not in proof:
            return "FAIL", f"Missing proof field: {field}"

    return "PASS", "Valid state transition"


def generate_receipt(prev_state, new_state, decision, reason, prev_receipt_hash=None):
    receipt = {
        "receipt_id": hashlib.sha256(
            (str(datetime.utcnow()) + new_state["hash"]).encode()
        ).hexdigest(),
        "prev_state_hash": prev_state["hash"],
        "new_state_hash": new_state["hash"],
        "prev_receipt_hash": prev_receipt_hash,
        "decision": decision,
        "timestamp": datetime.utcnow().isoformat(),
        "reason": reason,
        "verifier": "MIRA_v0"
    }

    receipt["receipt_hash"] = hash_receipt(receipt)

    return receipt
