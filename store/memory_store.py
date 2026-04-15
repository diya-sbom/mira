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
    store = load_store()

    entry = {
        "state": new_state,
        "receipt": receipt
    }

    store.append(entry)
    save_store(store)
