from verifier.canonical import hash_state


def verify_transition(prev_state, new_state, proof):

    # Genesis
    if prev_state is None:
        if new_state["version"] != 1:
            return "FAIL", "First state must have version 1"

        expected_new_hash = hash_state(new_state["data"])
        if proof["new_state_hash"] != expected_new_hash:
            return "FAIL", "Genesis state hash mismatch"

        return "PASS", "Genesis state accepted"

    # Hash checks
    expected_prev_hash = hash_state(prev_state["data"])
    if proof["prev_state_hash"] != expected_prev_hash:
        return "FAIL", "Previous state hash mismatch"

    expected_new_hash = hash_state(new_state["data"])
    if proof["new_state_hash"] != expected_new_hash:
        return "FAIL", "New state hash mismatch"

    # Version continuity
    if new_state["version"] != prev_state["version"] + 1:
        return "FAIL", "Invalid version increment"

    # Required fields
    for field in ["operation", "actor", "timestamp"]:
        if field not in proof:
            return "FAIL", f"Missing proof field: {field}"

    return "PASS", "Valid state transition"
