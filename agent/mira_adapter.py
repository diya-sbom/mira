import requests
import sys

MIRA_URL = "http://127.0.0.1:8000/verify"


def verify_or_halt(payload):
    try:
        response = requests.post(MIRA_URL, json=payload)
        result = response.json()
    except Exception as e:
        print("MIRA unavailable:", e)
        sys.exit(1)

    if result.get("decision") != "PASS":
        print("MIRA HALT:", result)
        sys.exit(1)

    return result["receipt"]
