import hashlib
import json


def build_evidence_bundle(query, retrieved_docs):
    bundle = {
        "query": query,
        "source": "external",
        "docs": retrieved_docs
    }

    canonical = json.dumps(bundle, sort_keys=True)
    bundle["evidence_hash"] = hashlib.sha256(canonical.encode()).hexdigest()

    return bundle
