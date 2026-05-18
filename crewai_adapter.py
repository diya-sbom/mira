from langchain_adapter import LangChainAdapter


class CrewAIAdapter(LangChainAdapter):
    """
    Minimal CrewAI integration.

    CrewAI tasks and memory updates must pass through Veridian.
    """

    def write_memory(self, payload):
        state = payload.get("state", {"valid": True})
        action = payload.get("action", payload)
        return self.invoke(state, action)
