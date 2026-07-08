from qa_scripts.quality_gate import evaluate


def test_quality_gate_passes_healthy_run():
    result = evaluate({"passed": 98, "failed": 2, "critical_defects": 0})
    assert result.passed is True
    assert result.reason == "quality gate passed"


def test_quality_gate_fails_empty_or_critical_runs():
    assert evaluate({"passed": 0, "failed": 0, "critical_defects": 0}).passed is False
    critical = evaluate({"passed": 100, "failed": 0, "critical_defects": 1})
    assert critical.passed is False
    assert critical.reason == "critical defects exceed threshold"


def test_quality_gate_rejects_negative_counts():
    result = evaluate({"passed": -1, "failed": 0, "critical_defects": 0})
    assert result.passed is False
    assert result.reason == "result counts cannot be negative"


def test_quality_gate_rejects_non_integer_counts():
    malformed_values = ["many", "1", 1.5, True, None]
    for field in ("passed", "failed", "critical_defects"):
        for value in malformed_values:
            payload: dict[str, object] = {"passed": 1, "failed": 0, "critical_defects": 0}
            payload[field] = value
            result = evaluate(payload)
            assert result.passed is False
            assert result.reason == "result counts must be integers"
