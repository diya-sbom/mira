import json
import sys
from datetime import datetime

from verifier.mira_verify import hash_state, verify_transition, generate_receipt


def load_example(path):
    with open(path, "r") as f:
        return json.load(f)


def prepare_example(example):
    prev_state = example["prev_state"]
    new_state = example["new_state"]
    proof = example["proof"]

    prev_state["hash"] = hash_state(prev_state["data"])
    new_state["hash"] = hash_state(new_state["data"])

    if proof.get("prev_state_hash") in [None, "AUTO"]:
        proof["prev_state_hash"] = prev_state["hash"]

    if proof.get("new_state_hash") in [None, "AUTO"]:
        proof["new_state_hash"] = new_state["hash"]

    if proof.get("timestamp") in [None, "AUTO"]:
        proof["timestamp"] = datetime.utcnow().isoformat()

    return prev_state, new_state, proof


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 run_mira_demo.py examples/pass.json")
        sys.exit(1)

    example_path = sys.argv[1]
    example = load_example(example_path)

    prev_state, new_state, proof = prepare_example(example)

    decision, reason = verify_transition(prev_state, new_state, proof)
    receipt = generate_receipt(prev_state, new_state, decision, reason)

    print("Decision:", decision)
    print("Reason:", reason)
    print("Receipt:")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
