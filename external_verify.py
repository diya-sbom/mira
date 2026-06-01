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


def canonical_hash(receipt):
    record = dict(receipt)
    expected_hash = record.pop("record_hash")

    canonical = json.dumps(
        record,
        sort_keys=True,
        separators=(",", ":")
    )

    actual_hash = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()

    return expected_hash, actual_hash


def verify(path):
    try:
        with open(path, "r") as f:
            receipt = json.load(f)
    except Exception:
        print("BLOCK: MALFORMED_RECEIPT")
        return False

    for field in REQUIRED_FIELDS:
        if field not in receipt:
            print(f"BLOCK: MISSING_FIELD: {field}")
            return False

    if receipt["decision"] not in VALID_DECISIONS:
        print("BLOCK: INVALID_DECISION")
        return False

    expected_hash, actual_hash = canonical_hash(receipt)

    if expected_hash != actual_hash:
        print("BLOCK: HASH_MISMATCH")
        return False

    print("PASS: RECEIPT_VALID")
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 external_verify.py <receipt.json>")
        sys.exit(1)

    ok = verify(sys.argv[1])
    sys.exit(0 if ok else 1)
