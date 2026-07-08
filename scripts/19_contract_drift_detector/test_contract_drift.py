from qa_scripts.contract_drift import detect_contract_drift


def test_contract_drift_detects_missing_and_unexpected_fields():
    drift = detect_contract_drift({"id": "integer", "email": "string"}, {"id": "string", "name": "string"})
    assert [(item.field, item.expected_type, item.actual_type) for item in drift] == [
        ("email", "string", "missing"),
        ("id", "integer", "string"),
        ("name", "unexpected", "string"),
    ]
