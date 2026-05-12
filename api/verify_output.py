import json
import sys
from pathlib import Path

output_path = Path("protected_output/output.txt")
receipt_path = Path("protected_output/receipt.json")

if not output_path.exists():
    print("INVALID OUTPUT: missing output.txt")
    sys.exit(1)

if not receipt_path.exists():
    print("INVALID OUTPUT: missing receipt.json")
    sys.exit(1)

with open(receipt_path, "r") as f:
    receipt = json.load(f)

if receipt.get("decision") != "PASS":
    print("INVALID OUTPUT: receipt decision is not PASS")
    sys.exit(1)

if not receipt.get("record_hash"):
    print("INVALID OUTPUT: missing record_hash")
    sys.exit(1)

print("VALID OUTPUT: MIRA receipt present")
