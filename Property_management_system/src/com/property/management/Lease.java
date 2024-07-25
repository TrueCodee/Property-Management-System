package com.property.management;

import java.util.ArrayList;
import java.util.List;

public class Lease {
    private String leaseID;
    private String propertyID;
    private String tenantID;
    private String startDate;
    private String endDate;
    private double rentAmount;
    public static List<Lease> leases = new ArrayList<>();

    public Lease(String leaseID, String propertyID, String tenantID, String startDate, String endDate, double rentAmount) {
        this.leaseID = leaseID;
        this.propertyID = propertyID;
        this.tenantID = tenantID;
        this.startDate = startDate;
        this.endDate = endDate;
        this.rentAmount = rentAmount;
    }

    // Getters and Setters
    public String getLeaseID() {
        return leaseID;
    }

    public void setLeaseID(String leaseID) {
        this.leaseID = leaseID;
    }

    public String getPropertyID() {
        return propertyID;
    }

    public void setPropertyID(String propertyID) {
        this.propertyID = propertyID;
    }

    public String getTenantID() {
        return tenantID;
    }

    public void setTenantID(String tenantID) {
        this.tenantID = tenantID;
    }

    public String getStartDate() {
        return startDate;
    }

    public void setStartDate(String startDate) {
        this.startDate = startDate;
    }

    public String getEndDate() {
        return endDate;
    }

    public void setEndDate(String endDate) {
        this.endDate = endDate;
    }

    public double getRentAmount() {
        return rentAmount;
    }

    public void setRentAmount(double rentAmount) {
        this.rentAmount = rentAmount;
    }

    // Methods
    public static void createLease(Lease lease) {
        leases.add(lease);
        System.out.println("Lease created: " + lease.leaseID);
    }

    public static void editLease(String leaseID, String newPropertyID, String newTenantID, String newStartDate, String newEndDate, double newRentAmount) {
        for (Lease lease : leases) {
            if (lease.leaseID.equals(leaseID)) {
                lease.setPropertyID(newPropertyID);
                lease.setTenantID(newTenantID);
                lease.setStartDate(newStartDate);
                lease.setEndDate(newEndDate);
                lease.setRentAmount(newRentAmount);
                System.out.println("Lease updated: " + lease.leaseID);
                return;
            }
        }
        System.out.println("Lease not found!");
    }

    public static void terminateLease(String leaseID) {
        leases.removeIf(lease -> lease.leaseID.equals(leaseID));
        System.out.println("Lease terminated: " + leaseID);
    }
}