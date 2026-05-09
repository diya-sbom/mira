import json
import sys
from pathlib import Path

def verify_receipt(path):
    receipt = json.loads(Path(path).read_text())

    decision = receipt.get("decision")

    if decision == "PASS":
        if not receipt.get("record_hash"):
            print("EXTERNAL VERIFY: INVALID PASS (missing record_hash)")
            sys.exit(1)
        print("EXTERNAL VERIFY: PASS")
        return

    if decision == "FAIL":
        print("EXTERNAL VERIFY: FAIL")
        return

    print("EXTERNAL VERIFY: INVALID RECEIPT")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 external_verify.py <receipt.json>")
        sys.exit(1)

    verify_receipt(sys.argv[1])
