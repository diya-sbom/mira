from dataclasses import dataclass
from typing import Optional, Dict, Any


STATE_ONLY = "STATE_ONLY"
ACTION_ONLY = "ACTION_ONLY"
STATE_ACTION_COMPOSITE = "STATE_ACTION_COMPOSITE"

ALLOW = "ALLOW"
DENY = "DENY"


@dataclass
class SentinelDecision:
    status: str
    reason: Optional[str] = None
    proof_refs: Optional[Dict[str, Any]] = None


def allow(proof_refs=None):
    return SentinelDecision(
        status=ALLOW,
        reason=None,
        proof_refs=proof_refs or {}
    )


def deny(reason):
    return SentinelDecision(
        status=DENY,
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

        return allow({
            "mira_receipt": mira_result
        })

     if operation_type == ACTION_ONLY:
         if diya is None:
              return deny("DIYA_NOT_AVAILABLE")

    try:
        diya_result = diya.verify_action(payload)
    except Exception:
        return deny("DIYA_VERIFICATION_ERROR")

    if not diya_result:
        return deny("ACTION_REJECTED_BY_DIYA")

    return allow({
        "diya_verification_record": diya_result
    })

    if operation_type == STATE_ACTION_COMPOSITE:
        return deny("COMPOSITE_ROUTING_NOT_IMPLEMENTED")

    return deny("UNKNOWN_OPERATION")
