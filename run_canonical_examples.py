import json

from sentinel_gatekeeper import sentinel_gatekeeper, STATE_ACTION_COMPOSITE


class MIRAStub:
    def verify_state(self, payload):
        return payload.get("valid", False)

    def verify_intent(self, payload):
        return True

    def verify_post_state(self, payload):
        return True


class DiyaStub:
    def reconcile_sbom(self, payload):
        return payload.get("allowed", False)

    def execute_secure(self, payload):
        return self.reconcile_sbom(payload)


class ExecutorStub:
    def run(self, action_payload):
        return {
            "valid": True,
            "executed": True,
            "action": action_payload
        }


class AFSStub:
    def commit(self, execution_result, receipt):
        return True


def run_example(path):
    with open(path, "r") as f:
        example = json.load(f)

    payload = {
        "state": example["state"],
        "action": example["action"],
        "executor": ExecutorStub(),
        "afs": AFSStub(),
    }

    decision = sentinel_gatekeeper(
        STATE_ACTION_COMPOSITE,
        payload,
        mira=MIRAStub(),
        diya=DiyaStub(),
    )

    expected = example["expected_decision"]
    actual = decision.status

    print(path)
    print("Expected:", expected)
    print("Actual:", actual)

    if expected == actual:
        print("RESULT: PASS\n")
        return True

    print("RESULT: FAIL\n")
    return False


if __name__ == "__main__":
    results = [
        run_example("canonical/allow.json"),
        run_example("canonical/fail.json"),
    ]
    if not all(results):
        raise SystemExit(1)

    print("CANONICAL EXAMPLES: ALL PASS")
