from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class PaymentResponse:
    status: str
    amount: str | None = None
    auth_id: str | None = None
    reason: str | None = None

    def as_dict(self) -> dict[str, str]:
        return {key: value for key, value in self.__dict__.items() if value is not None}


class MockPaymentService:
    """Deterministic service double for payment integration tests."""

    def __init__(self) -> None:
        self.transactions: list[PaymentResponse] = []

    def authorize(self, amount: float | Decimal, card_token: str) -> dict[str, str]:
        normalized_amount = Decimal(str(amount)).quantize(Decimal("0.01"))
        if normalized_amount <= 0:
            return PaymentResponse(status="declined", reason="invalid_amount").as_dict()
        if card_token == "tok_decline":
            return PaymentResponse(status="declined", reason="issuer_declined").as_dict()
        response = PaymentResponse(
            status="authorized",
            auth_id=f"auth_{len(self.transactions) + 1:04d}",
            amount=str(normalized_amount),
        )
        self.transactions.append(response)
        return response.as_dict()
