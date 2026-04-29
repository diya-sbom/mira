from fastapi import FastAPI
import json, time, hashlib, os

app = FastAPI()

LEDGER_PATH = "ledger.jsonl"

def canonical_hash(obj):
    data = json.dumps(obj, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(data.encode()).hexdigest()

def write_ledger(entry):
    os.makedirs(".", exist_ok=True)
    with open(LEDGER_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")

@app.post("/verify")
def verify(state: dict):
    ts = int(time.time())

    decision = "PASS" if "proof" in state else "FAIL"

    record = {
        "ts": ts,
        "state": state,
        "decision": decision
    }
    record_hash = canonical_hash(record)

    ledger_entry = {
        "record_hash": record_hash,
        "ts": ts,
        "decision": decision
    }

    write_ledger(ledger_entry)

    return {
        "decision": decision,
        "record_hash": record_hash
    }
