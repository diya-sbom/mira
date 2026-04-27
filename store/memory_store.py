import json
import os

STORE_FILE = "store/memory.json"


def load_store():
    if not os.path.exists(STORE_FILE):
        return []
    with open(STORE_FILE, "r") as f:
        return json.load(f)


def save_store(data):
    with open(STORE_FILE, "w") as f:
        json.dump(data, f, indent=2)

def append_state(new_state, receipt):
    # 1. Require receipt
    if not receipt:
        raise Exception("Write blocked: missing receipt")

    # 2. Require PASS decision
    if receipt.get("decision") != "PASS":
        raise Exception("Write blocked: invalid receipt decision")

    # 3. Require receipt hash
    if not receipt.get("receipt_hash"):
        raise Exception("Write blocked: missing receipt hash")

    store = load_store()

    # 4. Enforce chain linkage
    if store:
        last_receipt = store[-1]["receipt"]
        expected_prev = last_receipt.get("receipt_hash")

        if receipt.get("prev_receipt_hash") != expected_prev:
            raise Exception("Write blocked: receipt chain mismatch")

    entry = {
        "state": new_state,
        "receipt": receipt
    }

    store.append(entry)
    save_store(store)

    print("Write enforced through MIRA")
 


def get_last_receipt_hash():
    store = load_store()
    if not store:
        return None
    last_receipt = store[-1]["receipt"]
    return last_receipt.get("receipt_hash")
