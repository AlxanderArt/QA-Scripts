import pytest

from qa_scripts.test_data_factory import build_user, build_user_batch


def test_data_factory_generates_deterministic_users():
    assert build_user(1)["email"] == "qa-user-0001@example.test"
    assert build_user_batch(2)[1]["id"] == "user_0002"


def test_data_factory_rejects_invalid_sequence():
    with pytest.raises(ValueError, match="sequence must be positive"):
        build_user(0)
