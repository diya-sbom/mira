class Executor:
    def run(self, action_payload):
        if not action_payload:
            raise Exception("NO_ACTION_PAYLOAD")

        return {
            "executed": True,
            "action": action_payload,
            "result": "EXECUTION_COMPLETE"
        }
