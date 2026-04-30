import requests
import sys
import json
from pathlib import Path

API = "http://127.0.0.1:8000/verify"
OUTPUT = Path("protected_output/output.txt")

def verify(state):
    try:
        r = requests.post(API, json=state, timeout=5)
        return r.json()
    except Exception:
        return {"decision": "FAIL"}

def write_with_enforcement(content, state):
    result = verify(state)

    if result.get("decision") != "PASS":
        print("ENFORCEMENT BLOCK: no valid MIRA proof")
        sys.exit(1)

    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(content)

    # attach receipt
    receipt = {
        "state": state,
        "decision": result.get("decision"),
        "record_hash": result.get("record_hash")
    }

    with open("protected_output/receipt.json", "w") as f:
        json.dump(receipt, f, indent=2)

    print("WRITE SUCCESS with MIRA receipt")

if __name__ == "__main__":
    state = {
        "data": "write request",
        "proof": "valid-proof"
    }

    write_with_enforcement("Controlled write", state)
