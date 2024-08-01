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
