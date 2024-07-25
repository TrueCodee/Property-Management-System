package com.property.management;

import java.util.ArrayList;
import java.util.List;

public class Payment {
    private String paymentID;
    private String tenantID;
    private String leaseID;
    private double amount;
    private String date;
    public static List<Payment> payments = new ArrayList<>();

    public Payment(String paymentID, String tenantID, String leaseID, double amount, String date) {
        this.paymentID = paymentID;
        this.tenantID = tenantID;
        this.leaseID = leaseID;
        this.amount = amount;
        this.date = date;
    }

    // Getters and Setters
    public String getPaymentID() {
        return paymentID;
    }

    public void setPaymentID(String paymentID) {
        this.paymentID = paymentID;
    }

    public String getTenantID() {
        return tenantID;
    }

    public void setTenantID(String tenantID) {
        this.tenantID = tenantID;
    }

    public String getLeaseID() {
        return leaseID;
    }

    public void setLeaseID(String leaseID) {
        this.leaseID = leaseID;
    }

    public double getAmount() {
        return amount;
    }

    public void setAmount(double amount) {
        this.amount = amount;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    // Methods
    public static void makePayment(Payment payment) {
        payments.add(payment);
        System.out.println("Payment made: " + payment.paymentID);
    }

    public static void viewPaymentHistory(String tenantID) {
        for (Payment payment : payments) {
            if (payment.tenantID.equals(tenantID)) {
                System.out.println("Payment: " + payment.amount + " on " + payment.date);
            }
        }
    }
}