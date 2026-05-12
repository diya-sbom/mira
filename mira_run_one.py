#!/usr/bin/env python3
import subprocess
import shutil
from pathlib import Path

# Paths
mira_root = Path.home() / "mira"
consumer_repo = Path.home() / "mira-consumer-proof"
ledger_file = mira_root / "bil_ledger.jsonl"
receipt_file = mira_root / "receipt.json"

# Step 1: Append ledger
print("=== Step 1: Appending ledger ===")
subprocess.run(["python3", str(mira_root / "append_ledger.py")], check=True)

# Step 2: Generate receipt
print("=== Step 2: Generating receipt ===")
subprocess.run(["python3", str(mira_root / "generate_receipt.py")], check=True)

# Step 3: Copy files to consumer repo
print("=== Step 3: Copying ledger and receipt to consumer repo ===")
shutil.copy2(ledger_file, consumer_repo / "bil_ledger.jsonl")
shutil.copy2(receipt_file, consumer_repo / "receipt.json")

# Step 3a: Git commit & push
print("=== Step 3a: Committing & pushing to Git ===")
subprocess.run(["git", "-C", str(consumer_repo), "add", "bil_ledger.jsonl", "receipt.json"], check=True)
subprocess.run(["git", "-C", str(consumer_repo), "commit", "-m", "Update ledger and receipt"], check=True)
subprocess.run(["git", "-C", str(consumer_repo), "push"], check=True)

# Step 4: Verify consumer
print("=== Step 4: Verifying consumer ===")
subprocess.run(["python3", str(consumer_repo / "consumer_verify.py")], check=True)

print("✅ MIRA workflow completed successfully and pushed to Git")
