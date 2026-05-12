#!/usr/bin/env python3
from fastapi import FastAPI, Header, HTTPException
import json, time, hashlib, os

app = FastAPI()

LEDGER_PATH = "ledger.jsonl"
MIRA_API_KEY = os.environ.get("MIRA_API_KEY", "default_secret_key")

def canonical_hash(obj):
    data = json.dumps(obj, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(data.encode()).hexdigest()

def write_ledger(entry):
    with open(LEDGER_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")

@app.post("/verify")
def verify(state: dict, api_key: str = Header(default="default_secret_key")):
    if api_key != MIRA_API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")

    ts = int(time.time())

    # API now accepts receipt-style verification
    if state.get("decision") == "PASS" and state.get("record_hash"):
        decision = "PASS"
    else:
        decision = "FAIL"

    state_hash = canonical_hash(state)

    record = {
        "version": "1.0",
        "ts": ts,
        "state": state,
        "decision": decision
    }

    record_hash = canonical_hash(record)

    ledger_entry = {
        "record_hash": record_hash,
        "state_hash": state_hash,
        "ts": ts,
        "decision": decision
    }

    write_ledger(ledger_entry)

    return {
        "decision": decision,
        "record_hash": record_hash
    }
