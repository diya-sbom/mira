import json
from pathlib import Path

LEDGER = Path("bil/bil_ledger.jsonl")


def append_record(record):
    LEDGER.parent.mkdir(exist_ok=True)

    with open(LEDGER, "a") as f:
        f.write(json.dumps(record) + "\n")


if __name__ == "__main__":
    append_record({
        "type": "INTENT_RECORD",
        "action": "write_state",
        "decision": "PASS"
    })

    append_record({
        "type": "STATE_RECORD",
        "state": {
            "status": "approved"
        },
        "decision": "PASS"
    })

    append_record({
        "type": "COMMIT_RECORD",
        "commit": "ALLOWED",
        "decision": "PASS"
    })

    print("BIL_RECORD_WRITTEN")
