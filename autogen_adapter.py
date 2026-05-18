from langchain_adapter import LangChainAdapter


class AutoGenAdapter(LangChainAdapter):
    """
    Minimal AutoGen integration.

    AutoGen memory/tool actions must pass through Veridian.
    """

    def write_memory(self, payload):
        state = payload.get("state", {"valid": True})
        action = payload.get("action", payload)

        return self.invoke(state, action)
