import json
from pathlib import Path

INPUT = Path("external_input.json")
STATE_STORE = Path("state_store.json")


def adopter(input_path):
    if not input_path.exists():
        return None
    return json.loads(input_path.read_text())


def sentinel(request):
    if request is None:
        return False, None
    if request.get("_bypass_sentinel") is True:
        return False, None
    return True, request


def diya_gate(request):
    if request.get("action") != "write_state":
        return False
    if "intended_state_delta" not in request:
        return False
    return True


def executor(request):
    return request["intended_state_delta"]

def mira_verify(actual_state, intended_state):
    return actual_state == intended_state


def afs_commit(actual_state):
    STATE_STORE.write_text(json.dumps(actual_state, indent=2))
    return True


def run_chain():
    request = adopter(INPUT)

    sentinel_ok, request = sentinel(request)
    if not sentinel_ok:
        print("FAIL_CLOSED: SENTINEL_BLOCK")
        return False

    if not diya_gate(request):
        print("FAIL_CLOSED: DIYA_BLOCK_NO_EXECUTION")
        return False

    actual_state = executor(request)

    if not mira_verify(actual_state, request["intended_state_delta"]):
        print("FAIL_CLOSED: MIRA_BLOCK_NO_COMMIT")
        return False

    afs_commit(actual_state)
    print("PASS: STATE_COMMITTED")
    return True


if __name__ == "__main__":
    run_chain()
