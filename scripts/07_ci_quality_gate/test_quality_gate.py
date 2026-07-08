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
