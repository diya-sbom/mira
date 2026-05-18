from sentinel_gatekeeper import sentinel_gatekeeper
from real_diya import RealDiya
from crewai_adapter import CrewAIAdapter

adapter = CrewAIAdapter(
    sentinel_gatekeeper,
    None,
    RealDiya(),
    None
)

try:
    adapter.write_memory({
        "state": {"valid": True},
        "action": {"allowed": True}
    })
    print("CREWAI ADAPTER: ALLOWED")
except Exception as e:
    print("CREWAI ADAPTER: BLOCKED")
    print(e)
