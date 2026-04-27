import json
import requests
import sys

MIRA_URL = "http://127.0.0.1:8000/verify"


def run_file(path):
    with open(path, "r") as f:
        payload = json.load(f)

    try:
        res = requests.post(MIRA_URL, json=payload)
        result = res.json()
    except Exception as e:
        print("MIRA unavailable:", e)
        sys.exit(1)

    print(path)
    print(result)
    print()


run_file("examples/canonical/pass.json")
run_file("examples/canonical/fail.json")
