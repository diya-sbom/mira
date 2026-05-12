#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

RECEIPT = Path.home() / "mira-consumer-proof" / "receipt.json"

if not RECEIPT.exists():
    print("SCHEMA INVALID: missing receipt.json")
    sys.exit(1)

receipt = json.loads(RECEIPT.read_text())

required = ["timestamp", "decision", "record_hash"]

for field in required:
    if field not in receipt:
        print(f"SCHEMA INVALID: missing {field}")
        sys.exit(1)

if receipt["decision"] not in ["PASS", "FAIL"]:
    print("SCHEMA INVALID: decision must be PASS or FAIL")
    sys.exit(1)

if not isinstance(receipt["record_hash"], str):
    print("SCHEMA INVALID: record_hash must be string")
    sys.exit(1)

if not re.match(r"^[a-f0-9]{64}$", receipt["record_hash"]):
    print("SCHEMA INVALID: record_hash must be 64-char hex")
    sys.exit(1)

print("SCHEMA VALID: receipt.json")
