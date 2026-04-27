import sys
import requests

MIRA_URL = "http://localhost:8000/verify"

def call_mira(state):
    try:
        response = requests.post(MIRA_URL, json=state, timeout=5)
        result = response.json()
        return result.get("decision") == "PASS"
    except Exception:
        return False  # fail-closed

if __name__ == "__main__":
    state = {
        "data": "external system request",
       
    }

    if not call_mira(state):
        print("EXTERNAL CALLER: MIRA FAIL — execution halted")
        sys.exit(1)

    print("EXTERNAL CALLER: MIRA PASS — execution allowed")
