from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from gate.mira_gate import apply_memory_transition
from verifier.mira_verify import hash_state

app = FastAPI()


class TransitionRequest(BaseModel):
    prev_state: dict | None
    new_state: dict
    proof: dict


@app.post("/verify")
def verify_transition(req: TransitionRequest):
    try:
        prev_state = req.prev_state
        new_state = req.new_state
        proof = req.proof

        new_state["hash"] = hash_state(new_state["data"])

        if prev_state is not None:
            prev_state["hash"] = hash_state(prev_state["data"])

        if proof.get("timestamp") in [None, "AUTO"]:
            proof["timestamp"] = datetime.utcnow().isoformat()

        if prev_state is not None and proof.get("prev_state_hash") in [None, "AUTO"]:
            proof["prev_state_hash"] = prev_state["hash"]

        if proof.get("new_state_hash") in [None, "AUTO"]:
            proof["new_state_hash"] = new_state["hash"]

        receipt = apply_memory_transition(
            prev_state,
            new_state,
            proof
        )

        return {
            "decision": "PASS",
            "receipt": receipt
        }

    except Exception as e:
        return {
            "decision": "FAIL",
            "reason": str(e)
        }
