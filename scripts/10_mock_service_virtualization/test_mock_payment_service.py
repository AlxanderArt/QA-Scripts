import importlib.util
from pathlib import Path
module_path = Path(__file__).with_name("mock_payment_service.py")
spec = importlib.util.spec_from_file_location("mock_payment_service", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
MockPaymentService = module.MockPaymentService

def test_mock_payment_authorizes_successful_payment():
    response = MockPaymentService().authorize(42.00, "tok_visa")
    assert response["status"] == "authorized"
    assert response["auth_id"].startswith("auth_")

def test_mock_payment_declines_negative_amount_and_decline_token():
    service = MockPaymentService()
    assert service.authorize(-1, "tok_visa")["reason"] == "invalid_amount"
    assert service.authorize(25, "tok_decline")["reason"] == "issuer_declined"
