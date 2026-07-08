from qa_scripts.accessibility_audit import audit_login_markup, sample_accessible_login


def test_accessibility_audit_passes_accessible_markup():
    report = audit_login_markup(sample_accessible_login())
    assert report.passed is True
    assert report.issues == ()


def test_accessibility_audit_reports_missing_label():
    elements = sample_accessible_login()
    elements["email"] = {}
    report = audit_login_markup(elements)
    assert report.passed is False
    assert "email input needs visible label" in report.issues
