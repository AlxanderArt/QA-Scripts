from qa_scripts.mock_payment_service import MockPaymentService


def test_mock_payment_authorizes_successful_payment_with_stable_id_and_amount():
    service = MockPaymentService()
    response = service.authorize(42.0, "tok_visa")
    assert response == {"status": "authorized", "auth_id": "auth_0001", "amount": "42.00"}
    assert service.authorize(7.5, "tok_visa")["auth_id"] == "auth_0002"


def test_mock_payment_declines_negative_amount_and_decline_token():
    service = MockPaymentService()
    assert service.authorize(-1, "tok_visa")["reason"] == "invalid_amount"
    assert service.authorize(25, "tok_decline")["reason"] == "issuer_declined"
