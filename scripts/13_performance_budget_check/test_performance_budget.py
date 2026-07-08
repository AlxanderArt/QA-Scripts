from qa_scripts.performance_budget import evaluate_budget


def test_performance_budget_passes_healthy_metrics():
    assert evaluate_budget({"p95_ms": 200, "error_rate": 0, "bundle_kb": 200}).passed is True


def test_performance_budget_reports_violations():
    result = evaluate_budget({"p95_ms": 900, "error_rate": 0.02, "bundle_kb": 100})
    assert result.passed is False
    assert {violation.metric for violation in result.violations} == {"p95_ms", "error_rate"}
    assert {violation.reason for violation in result.violations} == {"budget exceeded"}


def test_performance_budget_reports_missing_required_metrics():
    result = evaluate_budget({"p95_ms": 200, "error_rate": 0})
    assert result.passed is False
    assert [(violation.metric, violation.actual, violation.limit, violation.reason) for violation in result.violations] == [
        ("bundle_kb", None, 350.0, "missing required metric")
    ]


def test_performance_budget_rejects_non_numeric_metrics():
    result = evaluate_budget({"p95_ms": "fast", "error_rate": 0, "bundle_kb": True})
    assert result.passed is False
    assert [(violation.metric, violation.reason) for violation in result.violations] == [
        ("p95_ms", "metric must be numeric"),
        ("bundle_kb", "metric must be numeric"),
    ]
