from sentinel_gatekeeper import sentinel_gatekeeper
from real_diya import RealDiya
from autogen_adapter import AutoGenAdapter

adapter = AutoGenAdapter(
    sentinel_gatekeeper,
    None,
    RealDiya(),
    None
)

try:
    adapter.write_memory({"state": {"valid": True}, "action": {"allowed": True}})
    print("AUTOGEN ADAPTER: ALLOWED")
except Exception as e:
    print("AUTOGEN ADAPTER: BLOCKED")
    print(e)
