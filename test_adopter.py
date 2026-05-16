# test_adopter.py

from sentinel_gatekeeper import sentinel_gatekeeper, STATE_ACTION_COMPOSITE

# Minimal stubs for demonstration
class MIRAStub:
    def verify_state(self, state_payload):
        # Return a receipt if state is valid
        if state_payload.get("valid", True):
            return "mira_receipt_001"
        return None

class DiyaStub:
    def verify_action(self, action_payload):
        # Return a record if action is valid
        if action_payload.get("allowed", True):
            return "diya_record_001"
        return None

class ExecutorStub:
    def run(self, action_payload):
        # Simulate execution
        return {"result": "success"}

class AFSStub:
    def commit(self, execution_result, post_state_receipt):
        # Simulate atomic commit
        print("AFS commit successful:", post_state_receipt)


# Minimal Adopter
class TestAdopter:
    def __init__(self, sentinel, mira, diya, executor, afs):
        self.sentinel = sentinel
        self.mira = mira
        self.diya = diya
        self.executor = executor
        self.afs = afs

    def run(self, state, action):
        payload = {
            "state": state,
            "action": action,
            "executor": self.executor,
            "afs": self.afs
        }

        decision = self.sentinel.sentinel_gatekeeper(
            STATE_ACTION_COMPOSITE,
            payload,
            mira=self.mira,
            diya=self.diya
        )

        if decision.status != "ALLOW":
            raise Exception(f"Blocked by Sentinel: {decision.reason}")

        print("Adopter succeeded, Sentinel allowed operation")
        print("Proof refs:", decision.proof_refs)


# === Run Test ===
if __name__ == "__main__":
    # Create stub instances
    mira = MIRAStub()
    diya = DiyaStub()
    executor = ExecutorStub()
    afs = AFSStub()
    sentinel = sentinel_gatekeeper  # from your sentinel_gatekeeper.py

    adopter = TestAdopter(sentinel, mira, diya, executor, afs)

    # Test input
    state_payload = {"valid": True}
    action_payload = {"allowed": True}

    # Run
    adopter.run(state_payload, action_payload)

    # Test fail-closed by disabling MIRA
    print("\nTesting fail-closed with invalid state:")
    state_payload_invalid = {"valid": False}
    try:
        adopter.run(state_payload_invalid, action_payload)
    except Exception as e:
        print(e)
