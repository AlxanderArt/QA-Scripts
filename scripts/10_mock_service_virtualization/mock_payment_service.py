class MockPaymentService:
    def __init__(self):
        self.transactions = []
    def authorize(self, amount: float, card_token: str):
        if amount <= 0:
            return {"status": "declined", "reason": "invalid_amount"}
        if card_token == "tok_decline":
            return {"status": "declined", "reason": "issuer_declined"}
        tx = {"status": "authorized", "auth_id": f"auth_{len(self.transactions)+1}", "amount": amount}
        self.transactions.append(tx)
        return tx
