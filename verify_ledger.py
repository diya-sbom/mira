import json
import hashlib
import sys
from pathlib import Path

LEDGER = Path("bil_ledger.jsonl")

def hash_obj(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

if not LEDGER.exists():
    print("LEDGER INVALID: missing bil_ledger.jsonl")
    sys.exit(1)

previous = None

for line_number, line in enumerate(LEDGER.read_text().splitlines(), start=1):
    entry = json.loads(line)

    expected_previous = entry.get("previous_hash")
    actual_hash = entry.get("entry_hash")

    if expected_previous != previous:
        print(f"LEDGER INVALID: broken chain at line {line_number}")
        sys.exit(1)

    entry_copy = dict(entry)
    entry_copy.pop("entry_hash", None)

    recalculated = hash_obj(entry_copy)

    if recalculated != actual_hash:
        print(f"LEDGER INVALID: hash mismatch at line {line_number}")
        sys.exit(1)

    previous = actual_hash

print("LEDGER VALID: hash chain intact")
