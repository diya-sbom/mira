import json
import os

LEDGER_FILE = "ledger/ledger.jsonl"


def append_receipt(receipt):
    if not receipt:
        raise Exception("Ledger blocked: missing receipt")

    if receipt.get("decision") != "PASS":
        raise Exception("Ledger blocked: invalid receipt decision")

    if not receipt.get("receipt_hash"):
        raise Exception("Ledger blocked: missing receipt hash")

    with open(LEDGER_FILE, "a") as f:
        f.write(json.dumps(receipt) + "\n")

    print("Receipt appended to ledger")
