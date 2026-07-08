from qa_scripts.synthetic_monitor import MonitorCheck, evaluate_monitor


def test_synthetic_monitor_passes_healthy_probe():
    assert evaluate_monitor(MonitorCheck("login", 200, 100)).healthy is True


def test_synthetic_monitor_flags_latency_and_errors():
    assert evaluate_monitor(MonitorCheck("login", 200, 900)).reason == "latency budget exceeded"
    assert evaluate_monitor(MonitorCheck("login", 503, 100)).reason == "server error"


def test_synthetic_monitor_rejects_invalid_inputs():
    assert evaluate_monitor(MonitorCheck("login", 99, 100)).reason == "invalid status code"
    assert evaluate_monitor(MonitorCheck("login", 200, -1)).reason == "latency cannot be negative"
