import sys


def verify_evidence_or_halt(evidence_bundle):
    if evidence_bundle.get("source") != "external":
        print("MIRA READ HALT: non-external evidence rejected")
        sys.exit(1)

    if not evidence_bundle.get("docs"):
        print("MIRA READ HALT: no external evidence found")
        sys.exit(1)

    if not evidence_bundle.get("evidence_hash"):
        print("MIRA READ HALT: missing evidence hash")
        sys.exit(1)

    return {
        "decision": "PASS",
        "receipt_id": evidence_bundle["evidence_hash"],
        "verified_context": evidence_bundle["docs"],
        "source": "external"
    }
