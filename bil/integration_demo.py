import json
from pathlib import Path

LEDGER = Path("bil/bil_ledger.jsonl")

def append_record(record):
    LEDGER.parent.mkdir(exist_ok=True)
    with open(LEDGER, "a") as f:
        f.write(json.dumps(record) + "\n")

append_record({
    "type": "INTENT_RECORD",
    "action": "write_state",
    "decision": "PASS"
})

append_record({
    "type": "STATE_RECORD",
    "status": "approved",
    "decision": "PASS"
})

append_record({
    "type": "COMMIT_RECORD",
    "commit": "state_store",
    "decision": "PASS"
})

print("BIL_CHAIN_WRITTEN")
