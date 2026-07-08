from pathlib import Path

def test_login_feature_has_given_when_then_acceptance_criteria():
    feature = Path(__file__).with_name("login.feature").read_text()
    assert "Feature:" in feature
    assert "Scenario:" in feature
    assert "Given" in feature and "When" in feature and "Then" in feature
    assert "account locked" in feature.lower()
