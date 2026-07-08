import pytest

from qa_scripts.risk_prioritizer import FeatureRisk, prioritize


def test_risk_prioritizer_orders_highest_score_first():
    ordered = prioritize([
        FeatureRisk("profile", 2, 2, 1),
        FeatureRisk("checkout", 5, 4, 3),
        FeatureRisk("search", 3, 3, 2),
    ])
    assert [item.feature for item in ordered] == ["checkout", "search", "profile"]


def test_risk_prioritizer_rejects_out_of_range_scores():
    with pytest.raises(ValueError, match="customer_impact must be an integer between 1 and 5"):
        FeatureRisk("billing", 0, 3, 2)
    with pytest.raises(ValueError, match="change_frequency must be an integer between 1 and 5"):
        FeatureRisk("billing", 3, True, 2)
