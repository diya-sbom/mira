import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone

RECEIPT = Path("protected_output/receipt.json")
LEDGER = Path("bil_ledger.jsonl")

if not RECEIPT.exists():
    raise SystemExit("LEDGER BLOCK: missing receipt.json")

receipt = json.loads(RECEIPT.read_text())

entry = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "decision": receipt.get("decision"),
    "record_hash": receipt.get("record_hash"),
}

entry_hash = hashlib.sha256(
    json.dumps(entry, sort_keys=True).encode()
).hexdigest()

entry["entry_hash"] = entry_hash

with open(LEDGER, "a") as f:
    f.write(json.dumps(entry) + "\n")

print("BIL LEDGER APPEND:", entry_hash)
