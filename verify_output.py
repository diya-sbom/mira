import json
import hashlib
import sys

REQUIRED_FIELDS = [
    "version",
    "ts",
    "state",
    "decision",
    "record_hash",
]

VALID_DECISIONS = ["ALLOW", "DENY"]


def verify_receipt(path="canonical/pass.json"):
    with open(path, "r") as f:
        receipt = json.load(f)

    for field in REQUIRED_FIELDS:
        if field not in receipt:
            print(f"MISSING_FIELD: {field}")
            return False

    if receipt["decision"] not in VALID_DECISIONS:
        print("INVALID_DECISION")
        return False

    record_copy = dict(receipt)
    expected_hash = record_copy.pop("record_hash")

    canonical = json.dumps(
        record_copy,
        sort_keys=True,
        separators=(",", ":")
    )

    actual_hash = hashlib.sha256(
        canonical.encode()
    ).hexdigest()

    if actual_hash != expected_hash:
        print("HASH_MISMATCH")
        return False

    print("RECEIPT_VALID")
    return True


def main():
    ok = verify_receipt()
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
