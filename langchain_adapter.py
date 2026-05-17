from sentinel_gatekeeper import sentinel_gatekeeper, STATE_ACTION_COMPOSITE


class LangChainAdapter:
    """
    Minimal fail-closed adapter.

    Any LangChain agent/tool call must pass through Sentinel.
    """

    def __init__(self, mira, diya, executor, afs):
        self.mira = mira
        self.diya = diya
        self.executor = executor
        self.afs = afs

    def invoke(self, state, action):
        payload = {
            "state": state,
            "action": action,
            "executor": self.executor,
            "afs": self.afs,
        }

        decision = sentinel_gatekeeper(
            STATE_ACTION_COMPOSITE,
            payload,
            mira=self.mira,
            diya=self.diya,
        )

        if decision.status != "ALLOW":
            raise Exception(f"VERIDIAN_BLOCKED: {decision.reason}")

        return decision
