import pytest

from qa_scripts.flaky_test_detector import analyze_history


def test_flaky_test_detector_flags_unstable_history():
    signals = analyze_history({"test_checkout": [True, False, True, False], "test_login": [True, True, True]})
    by_name = {signal.test_name: signal for signal in signals}
    assert by_name["test_checkout"].flaky is True
    assert by_name["test_login"].flaky is False


def test_flaky_test_detector_rejects_invalid_transition_threshold():
    with pytest.raises(ValueError, match="min_transitions must be at least 1"):
        analyze_history({"test_login": [True, False]}, min_transitions=0)
