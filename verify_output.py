import json
import sys
from pathlib import Path

OUTPUT = Path("protected_output/output.txt")
RECEIPT = Path("protected_output/receipt.json")

def fail(reason):
    print(f"INVALID OUTPUT: {reason}")
    sys.exit(1)

if not OUTPUT.exists():
    fail("missing output.txt")

if not RECEIPT.exists():
    fail("missing receipt.json")

receipt = json.loads(RECEIPT.read_text())

if receipt.get("decision") != "PASS":
    fail("receipt decision is not PASS")

if not receipt.get("record_hash"):
    fail("missing record_hash")

print("VALID OUTPUT: MIRA receipt present")
