from qa_scripts.release_readiness import ReadinessCheck, evaluate_readiness


def test_release_readiness_identifies_blockers():
    result = evaluate_readiness([
        ReadinessCheck("tests", True, "qa"),
        ReadinessCheck("rollback plan", False, "release-manager"),
    ])
    assert result.ready is False
    assert result.blockers[0].name == "rollback plan"
