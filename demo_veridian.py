from sentinel_gatekeeper import sentinel_gatekeeper, STATE_ACTION_COMPOSITE
from real_diya import RealDiya
from executor import Executor


class MIRAStub:
    def verify_state(self, payload):
        return payload.get("valid", False)

    def verify_intent(self, payload):
        return True

    def verify_post_state(self, payload):
        return True


class AFSStub:
    def commit(self, execution_result, receipt):
        print("AFS: committed verified state")


def main():
    mira = MIRAStub()
    diya = RealDiya()
    executor = Executor()
    afs = AFSStub()

    payload = {
        "state": {"valid": True},
        "action": {
            "artifact": "artifact.txt",
            "allowed": True
        },
        "executor": executor,
        "afs": afs,
    }

    decision = sentinel_gatekeeper(
        STATE_ACTION_COMPOSITE,
        payload,
        mira=mira,
        diya=diya,
    )

    print("VERIDIAN DECISION:", decision.status)
    print("REASON:", decision.reason)

    if decision.status == "ALLOW":
        print("VERIDIAN SYSTEM: PASS")
    else:
        print("VERIDIAN SYSTEM: BLOCKED")


if __name__ == "__main__":
    main()
