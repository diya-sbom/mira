# sentinel_gatekeeper.py

STATE_ONLY = "STATE_ONLY"
ACTION_ONLY = "ACTION_ONLY"
STATE_ACTION_COMPOSITE = "STATE_ACTION_COMPOSITE"

class SentinelDecision:
    def __init__(self, status, reason=None, proof_refs=None):
        self.status = status
        self.reason = reason
        self.proof_refs = proof_refs or {}

def allow(proof_refs=None):
    return SentinelDecision(
        status="ALLOW",
        reason=None,
        proof_refs=proof_refs or {}
    )

def deny(reason):
    return SentinelDecision(
        status="DENY",
        reason=reason,
        proof_refs={}
    )

def sentinel_gatekeeper(operation_type, payload, mira=None, diya=None):
    if operation_type == STATE_ONLY:
        if mira is None:
            return deny("MIRA_NOT_AVAILABLE")
        try:
            mira_result = mira.verify_state(payload)
        except Exception:
            return deny("MIRA_VERIFICATION_ERROR")

        if not mira_result:
            return deny("STATE_REJECTED_BY_MIRA")

        return allow()

    elif operation_type == ACTION_ONLY:
        if diya is None:
            return deny("DIYA_NOT_AVAILABLE")
        try:
            diya_result = diya.reconcile_sbom(payload)
        except Exception:
            return deny("ACTION_REJECTED_BY_DIYA")

        if not diya_result:
            return deny("ACTION_DENIED_BY_DIYA")

        return allow()

    elif operation_type == STATE_ACTION_COMPOSITE:
        if mira is None:
            return deny("MIRA_NOT_AVAILABLE")
        if diya is None:
            return deny("DIYA_NOT_AVAILABLE")
        try:
            if mira.verify_intent(payload):
                if diya.execute_secure(payload):
                    if mira.verify_post_state(payload):
                        return allow()
        except Exception:
            return deny("COMPOSITE_VERIFICATION_ERROR")
        
        return deny("STATE_ACTION_COMPOSITE_DENIED")

    else:
        return deny("UNKNOWN_OPERATION_TYPE")
