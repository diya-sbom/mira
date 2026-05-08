import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone

RECEIPT = Path("protected_output/receipt.json")
LEDGER = Path("bil_ledger.jsonl")

if not RECEIPT.exists():
    raise SystemExit("LEDGER BLOCK: missing receipt.json")

receipt = json.loads(RECEIPT.read_text())

def hash_obj(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

def last_entry_hash():
    if not LEDGER.exists():
        return None
    lines = LEDGER.read_text().strip().splitlines()
    if not lines:
        return None
    last = json.loads(lines[-1])
    return last.get("entry_hash")

entry = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "decision": receipt.get("decision"),
    "record_hash": receipt.get("record_hash"),
    "previous_hash": last_entry_hash()
}

entry["entry_hash"] = hash_obj(entry)

with open(LEDGER, "a") as f:
    f.write(json.dumps(entry) + "\n")

print("BIL LEDGER APPEND:", entry["entry_hash"])
