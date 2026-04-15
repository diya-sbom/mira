import json
from verifier.mira_verify import hash_state
from store.memory_store import load_store


def verify_store_integrity():
    store = load_store()
    results = []

    for i, entry in enumerate(store):
        state = entry["state"]
        receipt = entry["receipt"]

        actual_state_hash = hash_state(state["data"])

        if state["hash"] != actual_state_hash:
            results.append({
                "index": i,
                "decision": "FAIL",
                "reason": "State hash mismatch"
            })
            continue

        if receipt["new_state_hash"] != state["hash"]:
            results.append({
                "index": i,
                "decision": "FAIL",
                "reason": "Receipt does not match stored state"
            })
            continue

        results.append({
            "index": i,
            "decision": "PASS",
            "reason": "Entry verified"
        })

    return results


if __name__ == "__main__":
    results = verify_store_integrity()
    print(json.dumps(results, indent=2))
