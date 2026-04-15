from verifier.mira_verify import verify_transition, generate_receipt
from store.memory_store import append_state


def apply_memory_transition(prev_state, new_state, proof):
    decision, reason = verify_transition(prev_state, new_state, proof)

    if decision != "PASS":
        raise Exception(f"MIRA REJECTED: {reason}")

    receipt = generate_receipt(prev_state, new_state, decision, reason)

    append_state(new_state, receipt)

    return receipt
