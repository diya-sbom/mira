import requests
import sys

API_URL = "http://127.0.0.1:8000/verify"


def verify(payload):
    try:
        res = requests.post(API_URL, json=payload)
        data = res.json()

        print("MIRA RESPONSE:", data)

        if data.get("decision") != "PASS":
            print("MIRA HALT:", data.get("reason"))
            sys.exit(1)

        return data["receipt"]

    except Exception as e:
        print("ERROR:", e)
        sys.exit(1)


def main():
    # STEP 1 — Genesis
    payload1 = {
        "prev_state": None,
        "new_state": {
            "state_id": "1",
            "version": 1,
            "data": {"value": "A"},
            "hash": "AUTO"
        },
        "proof": {
            "operation": "create",
            "actor": "agent",
            "timestamp": "AUTO"
        }
    }

    receipt1 = verify(payload1)

    # STEP 2 — Update
    payload2 = {
        "prev_state": {
            "state_id": "1",
            "version": 1,
            "data": {"value": "A"},
            "hash": receipt1["new_state_hash"]
        },
        "new_state": {
            "state_id": "2",
            "version": 2,
            "data": {"value": "B"},
            "hash": "AUTO"
        },
        "proof": {
            "operation": "update",
            "actor": "agent",
            "timestamp": "AUTO",
            "prev_state_hash": receipt1["new_state_hash"],
            "new_state_hash": "AUTO"
        }
    }

    receipt2 = verify(payload2)

    print("TASK EXECUTED: memory verified")


if __name__ == "__main__":
    main()
