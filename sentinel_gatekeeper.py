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
    if mira is None:
        return deny("MIRA_NOT_AVAILABLE")

    if diya is None:
        return deny("DIYA_NOT_AVAILABLE")

    executor = payload.get("executor")
    if executor is None:
        return deny("EXECUTOR_NOT_AVAILABLE")

    afs = payload.get("afs")
    if afs is None:
        return deny("AFS_NOT_AVAILABLE")

    state_payload = payload.get("state")
    action_payload = payload.get("action")

    # 1. Pre-state validation
    try:
        pre_state_receipt = mira.verify_state(state_payload)
    except Exception:
        return deny("PRE_STATE_VERIFICATION_ERROR")

    if not pre_state_receipt:
        return deny("PRE_STATE_REJECTED")

    # 2. Action verification
    try:
        diya_record = diya.verify_action(action_payload)
    except Exception:
        return deny("ACTION_VERIFICATION_ERROR")

    if not diya_record:
        return deny("ACTION_REJECTED")

    # 3. Execute approved action
    try:
        execution_result = executor.run(action_payload)
    except Exception:
        return deny("EXECUTION_FAILED")

    # 4. Post-state validation
    try:
        post_state_receipt = mira.verify_state(execution_result)
    except Exception:
        return deny("POST_STATE_VERIFICATION_ERROR")

    if not post_state_receipt:
        return deny("POST_STATE_REJECTED")

    # 5. Atomic commit
    try:
        afs.commit(execution_result, post_state_receipt)
    except Exception:
        return deny("AFS_COMMIT_FAILED")

    return allow({
        "pre_state_receipt": pre_state_receipt,
        "diya_verification_record": diya_record,
        "post_state_receipt": post_state_receipt
    })

    return deny("UNKNOWN_OPERATION")
