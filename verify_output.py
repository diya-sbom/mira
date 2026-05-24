import json
import hashlib
import sys

REQUIRED_FIELDS = [
    "version",
    "ts",
    "state",
    "decision",
    "record_hash"
]

VALID_DECISIONS = ["ALLOW", "DENY"]

with open("canonical/pass.json", "r") as f:
    receipt = json.load(f)

for field in REQUIRED_FIELDS:
    if field not in receipt:
        print(f"MISSING_FIELD: {field}")
        sys.exit(1)

if receipt["decision"] not in VALID_DECISIONS:
    print("INVALID_DECISION")
    sys.exit(1)

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
    sys.exit(1)

print("RECEIPT_VALID")
sys.exit(0)
