from sentinel_gatekeeper import (
    sentinel_gatekeeper,
    STATE_ONLY,
    ACTION_ONLY,
    STATE_ACTION_COMPOSITE,
)


class MIRAStub:
    def verify_state(self, payload):
        return True

    def verify_intent(self, payload):
        return True

    def verify_post_state(self, payload):
        return True


class DiyaStub:
    def reconcile_sbom(self, payload):
        return True

    def execute_secure(self, payload):
        return True


class TestAdopter:
    def __init__(self, sentinel, mira, diya):
        self.sentinel = sentinel
        self.mira = mira
        self.diya = diya

    def run_state_only(self):
        decision = self.sentinel(
            STATE_ONLY,
            {"valid": True},
            mira=self.mira,
            diya=self.diya,
        )
        print("STATE_ONLY:", decision.status, decision.reason)

    def run_action_only(self):
        decision = self.sentinel(
            ACTION_ONLY,
            {"allowed": True},
            mira=self.mira,
            diya=self.diya,
        )
        print("ACTION_ONLY:", decision.status, decision.reason)

    def run_composite(self):
        payload = {
            "state": {"valid": True},
            "action": {"allowed": True},
        }

        decision = self.sentinel(
            STATE_ACTION_COMPOSITE,
            payload,
            mira=self.mira,
            diya=self.diya,
        )
        print("STATE_ACTION_COMPOSITE:", decision.status, decision.reason)


if __name__ == "__main__":
    mira = MIRAStub()
    diya = DiyaStub()

    adopter = TestAdopter(
        sentinel_gatekeeper,
        mira,
        diya,
    )

    adopter.run_state_only()
    adopter.run_action_only()
    adopter.run_composite()
