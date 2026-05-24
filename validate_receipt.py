import json
from pathlib import Path


REQUIRED_FIELDS = [
    "version",
    "ts",
    "state",
    "decision",
]

VALID_DECISIONS = {"ALLOW", "DENY"}


def validate_receipt(receipt):
    for field in REQUIRED_FIELDS:
        if field not in receipt:
            print(f"RECEIPT: MISSING_FIELD {field}")
            return False

    if receipt["decision"] not in VALID_DECISIONS:
        print(f"RECEIPT: INVALID_DECISION {receipt['decision']}")
        return False

    print("RECEIPT: VALID")
    return True


if __name__ == "__main__":
    sample = {
        "version": "1.0",
        "ts": 0,
        "state": {
            "state": {"valid": True},
            "action": {"allowed": True}
        },
        "decision": "ALLOW"
    }

    ok = validate_receipt(sample)
    raise SystemExit(0 if ok else 1)
