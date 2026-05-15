import json
import hashlib
import os
from datetime import datetime, timezone

STATE_FILE = "afs/current_state.json"
RECORD_FILE = "afs/verification_record.json"

def canonical_hash(data):
    encoded = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def atomic_write(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)
    os.replace(tmp, path)

def verify_and_commit(proposal_path):
    current = load_json(STATE_FILE)
    proposal = load_json(proposal_path)

    current_hash = canonical_hash(current)

    if proposal.get("parent_hash") != current_hash:
        record = {
            "decision": "FAIL",
            "reason": "parent_hash_mismatch",
            "expected_parent_hash": current_hash,
            "received_parent_hash": proposal.get("parent_hash"),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        atomic_write(RECORD_FILE, record)
        return record

    new_state = proposal["proposed_state"]
    new_hash = canonical_hash(new_state)

    atomic_write(STATE_FILE, new_state)

    record = {
        "decision": "PASS",
        "reason": "state_committed",
        "parent_hash": current_hash,
        "new_hash": new_hash,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    atomic_write(RECORD_FILE, record)
    return record

if __name__ == "__main__":
    result = verify_and_commit("afs/proposal.json")
    print(json.dumps(result, indent=2))
