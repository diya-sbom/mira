import sys


def output_gate_or_halt(answer, verified_context):
    context_lines = verified_context.get("verified_context", [])

    if not context_lines:
        print("MIRA OUTPUT HALT: no verified context")
        sys.exit(1)

    supported = False

    for line in context_lines:
        if line.lower() in answer.lower():
            supported = True
            break

    if not supported:
        print("MIRA OUTPUT HALT: answer not supported by verified context")
        sys.exit(1)

    return {
        "decision": "ALLOW",
        "answer": answer,
        "receipt_id": verified_context["receipt_id"]
    }
