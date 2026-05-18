from sentinel_gatekeeper import sentinel_gatekeeper
from real_diya import RealDiya
from langchain_adapter import LangChainAdapter
from langchain_memory import VeridianMemory

adapter = LangChainAdapter(
    sentinel_gatekeeper,
    None,          
    RealDiya(),
    None
)   

memory = VeridianMemory(adapter)

try:
    memory.save_context(
        {"input": "Hello"},
        {"output": "World"}
    )
    print("MEMORY WRITE: ALLOWED")
    print(memory.load_memory_variables())
except Exception as e:
    print("MEMORY WRITE: BLOCKED")
    print(e)
