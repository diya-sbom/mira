import json
from verifier.mira_verify import hash_state, hash_receipt
from store.memory_store import load_store


def verify_store_integrity():
    store = load_store()
    results = []
    previous_receipt_hash = None

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

        if receipt.get("prev_receipt_hash") != previous_receipt_hash:
            results.append({
                "index": i,
                "decision": "FAIL",
                "reason": "Receipt chain broken"
            })
            continue

        receipt_copy = dict(receipt)
        stored_receipt_hash = receipt_copy.pop("receipt_hash", None)
        recomputed_receipt_hash = hash_receipt(receipt_copy)

        if stored_receipt_hash != recomputed_receipt_hash:
            results.append({
                "index": i,
                "decision": "FAIL",
                "reason": "Receipt hash mismatch"
            })
            continue

        previous_receipt_hash = stored_receipt_hash

        results.append({
            "index": i,
            "decision": "PASS",
            "reason": "Entry verified"
        })

    return results


if __name__ == "__main__":
    results = verify_store_integrity()
    print(json.dumps(results, indent=2))
