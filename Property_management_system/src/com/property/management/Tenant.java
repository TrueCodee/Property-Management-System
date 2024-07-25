package com.property.management;

import java.util.ArrayList;
import java.util.List;

public class Tenant {
    private String tenantID;
    private String name;
    private String contactInfo;
    private String leaseID;
    public static List<Tenant> tenants = new ArrayList<>();

    public Tenant(String tenantID, String name, String contactInfo, String leaseID) {
        this.tenantID = tenantID;
        this.name = name;
        this.contactInfo = contactInfo;
        this.leaseID = leaseID;
    }

    // Getters and Setters
    public String getTenantID() {
        return tenantID;
    }

    public void setTenantID(String tenantID) {
        this.tenantID = tenantID;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getContactInfo() {
        return contactInfo;
    }

    public void setContactInfo(String contactInfo) {
        this.contactInfo = contactInfo;
    }

    public String getLeaseID() {
        return leaseID;
    }

    public void setLeaseID(String leaseID) {
        this.leaseID = leaseID;
    }

    // Methods
    public static void addTenant(Tenant tenant) {
        tenants.add(tenant);
        System.out.println("Tenant added: " + tenant.name);
    }

    public static void editTenant(String tenantID, String newName, String newContactInfo, String newLeaseID) {
        for (Tenant tenant : tenants) {
            if (tenant.tenantID.equals(tenantID)) {
                tenant.setName(newName);
                tenant.setContactInfo(newContactInfo);
                tenant.setLeaseID(newLeaseID);
                System.out.println("Tenant updated: " + tenant.name);
                return;
            }
        }
        System.out.println("Tenant not found!");
    }

    public static void deleteTenant(String tenantID) {
        tenants.removeIf(tenant -> tenant.tenantID.equals(tenantID));
        System.out.println("Tenant deleted: " + tenantID);
    }
}