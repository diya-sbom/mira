from verifier.mira_verify import verify_transition, generate_receipt
from store.memory_store import append_state, get_last_receipt_hash


def apply_memory_transition(prev_state, new_state, proof):
    decision, reason = verify_transition(prev_state, new_state, proof)

    if decision != "PASS":
        raise Exception(f"MIRA REJECTED: {reason}")

    prev_receipt_hash = get_last_receipt_hash()

    receipt = generate_receipt(
        prev_state,
        new_state,
        decision,
        reason,
        prev_receipt_hash=prev_receipt_hash
    )

    append_state(new_state, receipt)

    return receipt
