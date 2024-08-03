class Payment:
    payments = []

    def __init__(self, payment_id, tenant_id, lease_id, amount, date):
        self.payment_id = payment_id
        self.tenant_id = tenant_id
        self.lease_id = lease_id
        self.amount = amount
        self.date = date

    @classmethod
    def make_payment(cls, payment):
        cls.payments.append(payment)
        print(f"Payment {payment.payment_id} made.")

    @classmethod
    def view_payment_history(cls, tenant_id):
        for payment in cls.payments:
            if payment.tenant_id == tenant_id:
                print(f"Payment: ${payment.amount} on {payment.date}")


# Input
payment1 = Payment("PAY001", "T001", "L001", 1200.0, "2024-01-01")
Payment.make_payment(payment1)
Payment.view_payment_history("T001")

payment2 = Payment("PAY002", "T001", "L001", 1300.0, "2024-02-01")
Payment.make_payment(payment2)
Payment.view_payment_history("T001")
