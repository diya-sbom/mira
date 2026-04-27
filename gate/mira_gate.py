from verifier.mira_verify import verify_transition, generate_receipt
from store.memory_store import append_state, get_last_receipt_hash
from ledger.ledger import append_receipt

def apply_memory_transition(prev_state, new_state, proof):
    prev_receipt_hash = get_last_receipt_hash()

    if prev_receipt_hash is None:
        prev_state = None

    decision, reason = verify_transition(prev_state, new_state, proof)

    if decision != "PASS":
        raise Exception(f"MIRA REJECTED: {reason}")

    receipt = generate_receipt(
        prev_state if prev_state is not None else {"hash": "GENESIS"},
        new_state,
        decision,
        reason,
        prev_receipt_hash=prev_receipt_hash
    )

    append_state(new_state, receipt)

    append_receipt(receipt)

    return receipt
