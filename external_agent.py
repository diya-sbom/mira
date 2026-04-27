from agent.mira_adapter import verify_or_halt


def main():
    payload1 = {
        "prev_state": None,
        "new_state": {
            "state_id": "1",
            "version": 1,
            "data": {"value": "A"}
        },
        "proof": {
            "operation": "create",
            "actor": "external-agent",
            "timestamp": "AUTO"
        }
    }

    receipt1 = verify_or_halt(payload1)

    payload2 = {
        "prev_state": {
            "state_id": "1",
            "version": 1,
            "data": {"value": "A"}
        },
        "new_state": {
            "state_id": "2",
            "version": 2,
            "data": {"value": "B"}
        },
        "proof": {
            "operation": "update",
            "actor": "external-agent",
            "timestamp": "AUTO",
            "prev_state_hash": receipt1["new_state_hash"],
            "new_state_hash": "AUTO"
        }
    }

    verify_or_halt(payload2)

    print("External dependency confirmed")


if __name__ == "__main__":
    main()
