import json
import sys
from datetime import datetime

from verifier.mira_verify import hash_state
from gate.mira_gate import apply_memory_transition
from store.memory_store import load_store


def load_input(path):
    with open(path, "r") as f:
        return json.load(f)


def get_previous_state():
    store = load_store()

    if not store:
        genesis_state = {
            "state_id": "0",
            "version": 0,
            "data": {},
            "hash": hash_state({})
        }
        return genesis_state

    return store[-1]["state"]


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 apply_transition.py examples/pass.json")
        sys.exit(1)

    input_path = sys.argv[1]
    payload = load_input(input_path)

    prev_state = get_previous_state()
    new_state = payload["new_state"]
    proof = payload["proof"]

    new_state["hash"] = hash_state(new_state["data"])

    proof["prev_state_hash"] = prev_state["hash"]
    proof["new_state_hash"] = new_state["hash"]

    if proof.get("timestamp") in [None, "AUTO"]:
        proof["timestamp"] = datetime.utcnow().isoformat()

    receipt = apply_memory_transition(prev_state, new_state, proof)

    print("Stored successfully")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
