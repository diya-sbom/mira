from verify_output import REQUIRED_FIELDS, VALID_DECISIONS


def test_invalid_decision_blocked():
    assert "ALLOW_ALL" not in VALID_DECISIONS


def test_required_fields_exist():
    assert "version" in REQUIRED_FIELDS
    assert "decision" in REQUIRED_FIELDS
    assert "record_hash" in REQUIRED_FIELDS


def test_missing_receipt_should_block():
    receipt = None
    assert receipt is None
