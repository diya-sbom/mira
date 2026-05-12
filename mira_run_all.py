#!/usr/bin/env python3
import subprocess
import shutil
import json
import requests
from pathlib import Path
from datetime import datetime
import sys

# =====================
# Paths
# =====================
mira_root = Path.home() / "mira"
consumer_repo = Path.home() / "mira-consumer-proof"

# Logging
logs_dir = mira_root / "logs"
logs_dir.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
log_file = logs_dir / f"mira_run_{timestamp}.log"

class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, data):
        for s in self.streams:
            s.write(data)
            s.flush()

    def flush(self):
        for s in self.streams:
            s.flush()

log_handle = open(log_file, "w")
sys.stdout = Tee(sys.stdout, log_handle)
sys.stderr = Tee(sys.stderr, log_handle)

print(f"Logging to: {log_file}")


ledger_file = mira_root / "bil_ledger.jsonl"
receipt_file = consumer_repo / "receipt.json"

append_ledger_script = mira_root / "append_ledger.py"
generate_receipt_script = mira_root / "generate_receipt.py"
consumer_verify_script = consumer_repo / "consumer_verify.py"
schema_validate_script = mira_root / "validate_receipt_schema.py"
api_verify_url = "http://127.0.0.1:8000/verify"  # optional API verification

# =====================
# Step 1 — Append ledger
# =====================
print("=== Step 1: Appending ledger ===")
subprocess.run(["python3", str(append_ledger_script)], check=True)

# =====================
# Step 2 — Generate receipt
# =====================
print("=== Step 2: Generating receipt ===")
subprocess.run(["python3", str(generate_receipt_script)], check=True)

# =====================
# Step 3 — Copy files safely
# =====================
print("=== Step 3: Copying ledger and receipt to consumer repo (safe) ===")
for src, dst in [(ledger_file, consumer_repo / "bil_ledger.jsonl"),
                 (receipt_file, consumer_repo / "receipt.json")]:
    if src.resolve() != dst.resolve():
        shutil.copy2(src, dst)

# =====================
# Step 3a — Commit & push to Git
# =====================
print("=== Step 3a: Committing & pushing to Git ===")
subprocess.run(["git", "-C", str(consumer_repo), "add", "bil_ledger.jsonl", "receipt.json"], check=True)
subprocess.run(["git", "-C", str(consumer_repo), "commit", "-m", "Update ledger and receipt"], check=True)
subprocess.run(["git", "-C", str(consumer_repo), "push"], check=True)

# =====================
# Step 4 — Optional API verification (safe)
# =====================
print("=== Step 4: Verifying consumer via API (safe) ===")
api_verified = False
try:
    response = requests.post(api_verify_url, json=json.load(receipt_file.open()))
    result = response.json()
    if result.get("decision") == "PASS":
        api_verified = True
        print("✅ MIRA API verification succeeded")
    else:
        print("❌ MIRA API verification failed: decision FAIL")
except Exception as e:
    print(f"❌ MIRA API verification failed: {e}")

# =====================
# Step 4b — Local verification (main guard)
# =====================
print("=== Step 4b: Receipt schema validation ===")
subprocess.run(["python3", str(schema_validate_script)], check=True)

print("=== Step 4c: Local verification ===")
subprocess.run(["python3", str(consumer_verify_script)], check=True)

print("✅ MIRA workflow completed successfully and pushed to Git")
if api_verified:
    print("✅ API verification passed as well")
