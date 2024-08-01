import unittest
from payment import Payment
from io import StringIO
import sys


class TestPayment(unittest.TestCase):

    def setUp(self):
        Payment.payments.clear()

    def test_make_payment(self):
        print("Running test_make_payment...")
        payment = Payment("PAY002", "T002", "L002", 1300.0, "2024-02-01")
        Payment.make_payment(payment)
        self.assertIn(payment, Payment.payments)
        print(f"Payment {payment.payment_id} recorded for {payment.amount}.")

    def test_view_payment_history(self):
        print("Running test_view_payment_history...")
        payment1 = Payment("PAY003", "T003", "L003", 1400.0, "2024-03-01")
        payment2 = Payment("PAY004", "T003", "L003", 1500.0, "2024-04-01")
        Payment.make_payment(payment1)
        Payment.make_payment(payment2)

        captured_output = StringIO()
        sys.stdout = captured_output
        Payment.view_payment_history("T003")
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip().split('\n')
        self.assertIn("Payment: $1400.0 on 2024-03-01", output)
        self.assertIn("Payment: $1500.0 on 2024-04-01", output)
        print(f"Payment history for T003: {output}")


if __name__ == '__main__':
    unittest.main()
