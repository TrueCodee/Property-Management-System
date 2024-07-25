package tests;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import com.property.management.Payment;

public class PaymentTest {

    @BeforeEach
    public void setUp() {
        Payment.payments.clear();
    }

    @Test
    public void testMakePayment() {
        Payment payment = new Payment("PAY001", "T001", "L001", 1200.0, "2024-01-01");
        Payment.makePayment(payment);
        assertTrue(Payment.payments.contains(payment), "Payment should be made and added to the list");
    }

    @Test
    public void testViewPaymentHistory() {
        Payment payment1 = new Payment("PAY002", "T002", "L002", 1300.0, "2024-02-01");
        Payment payment2 = new Payment("PAY003", "T002", "L002", 1300.0, "2024-03-01");
        Payment.makePayment(payment1);
        Payment.makePayment(payment2);
        assertEquals(2, Payment.payments.size(), "There should be two payments in the history");
    }
}