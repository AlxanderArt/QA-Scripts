from qa_scripts.risk_prioritizer import FeatureRisk, prioritize


def test_risk_prioritizer_orders_highest_score_first():
    ordered = prioritize([
        FeatureRisk("profile", 2, 2, 1),
        FeatureRisk("checkout", 5, 4, 3),
        FeatureRisk("search", 3, 3, 2),
    ])
    assert [item.feature for item in ordered] == ["checkout", "search", "profile"]
