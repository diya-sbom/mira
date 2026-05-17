from langchain_adapter import LangChainAdapter
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
        print("AFS commit")


mira = MIRAStub()
diya = RealDiya()
executor = Executor()
afs = AFSStub()

adapter = LangChainAdapter(
    mira=mira,
    diya=diya,
    executor=executor,
    afs=afs,
)

state = {"valid": True}
action = {
    "artifact": "artifact.txt",
    "allowed": True
}

try:
    result = adapter.invoke(state, action)
    print("LANGCHAIN ADAPTER: ALLOW", result.status, result.reason)
except Exception as e:
    print("LANGCHAIN ADAPTER: BLOCKED")
    print(e)
