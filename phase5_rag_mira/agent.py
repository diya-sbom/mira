from retriever import retrieve
from evidence import build_evidence_bundle
from mira_read_adapter import verify_evidence_or_halt
from output_gate import output_gate_or_halt


def main():
    query = "What does MIRA do?"

    retrieved_docs = retrieve(query)
    evidence_bundle = build_evidence_bundle(query, retrieved_docs)

    verified_context = verify_evidence_or_halt(evidence_bundle)

    proposed_answer = "MIRA returns PASS or FAIL."

    result = output_gate_or_halt(proposed_answer, verified_context)

    print("FINAL ANSWER:")
    print(result["answer"])
    print("RECEIPT:", result["receipt_id"])


if __name__ == "__main__":
    main()
