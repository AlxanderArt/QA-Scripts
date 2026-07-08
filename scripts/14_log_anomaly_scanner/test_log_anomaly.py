from qa_scripts.log_anomaly import scan_logs


def test_log_anomaly_scanner_classifies_findings():
    findings = scan_logs(["INFO ok", "ERROR database timeout", "Traceback in worker"])
    assert [finding.severity for finding in findings] == ["high", "critical"]
