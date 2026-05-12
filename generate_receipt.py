import json
import os

# Path to your main MIRA repo
mira_root = os.path.expanduser("~/mira")

# Open the ledger using absolute path
ledger_path = os.path.join(mira_root, "bil_ledger.jsonl")
with open(ledger_path) as f:
    lines = f.readlines()

latest = json.loads(lines[-1])
receipt = {
    "timestamp": latest["timestamp"],
    "decision": "PASS",
    "record_hash": latest["entry_hash"]
}

# Output the receipt to mira-consumer-proof
consumer_repo = os.path.expanduser("~/mira-consumer-proof")
receipt_path = os.path.join(consumer_repo, "receipt.json")
with open(receipt_path, "w") as f:
    json.dump(receipt, f)

print(f"✅ Generated receipt at {receipt_path}")
