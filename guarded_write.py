import requests
import sys
from pathlib import Path

API = "http://127.0.0.1:8000/verify"
OUTPUT_DIR = Path("protected_output")
OUTPUT_FILE = OUTPUT_DIR / "output.txt"

def verify(state):
    r = requests.post(API, json=state, timeout=5)
    return r.json()

def write_file(content):
    OUTPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(content)

state = {
    "data": "write request",
    "proof": "valid-proof"
}

result = verify(state)

if result.get("decision") != "PASS":
    print("BLOCKED: MIRA FAIL")
    sys.exit(1)

print("ALLOWED: writing file")
write_file("Hello from MIRA-controlled execution")
