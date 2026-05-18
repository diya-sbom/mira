from langchain_adapter import LangChainAdapter


class VeridianMemory:
    """
    Minimal LangChain-style memory wrapper.
    All writes pass through the LangChainAdapter.
    """

    def __init__(self, adapter):
        self.adapter = adapter
        self.store = []

    def save_context(self, inputs, outputs):
        state = {"valid": True}
        action = {
            "artifact": "memory.json",
            "allowed": True,
            "inputs": inputs,
            "outputs": outputs,
        }

        # Fail-closed verification path
        self.adapter.invoke(state, action)

        # Only executed if ALLOW
        self.store.append({
            "inputs": inputs,
            "outputs": outputs,
        })

    def load_memory_variables(self, inputs=None):
        return {"history": self.store}
