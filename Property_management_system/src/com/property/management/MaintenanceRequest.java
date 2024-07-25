package com.property.management;

import java.util.ArrayList;
import java.util.List;

public class MaintenanceRequest {
    private String requestID;
    private String tenantID;
    private String propertyID;
    private String description;
    private String status;
    private String dateSubmitted;
    public static List<MaintenanceRequest> requests = new ArrayList<>();

    public MaintenanceRequest(String requestID, String tenantID, String propertyID, String description, String status, String dateSubmitted) {
        this.requestID = requestID;
        this.tenantID = tenantID;
        this.propertyID = propertyID;
        this.description = description;
        this.status = status;
        this.dateSubmitted = dateSubmitted;
    }

    // Getters and Setters
    public String getRequestID() {
        return requestID;
    }

    public void setRequestID(String requestID) {
        this.requestID = requestID;
    }

    public String getTenantID() {
        return tenantID;
    }

    public void setTenantID(String tenantID) {
        this.tenantID = tenantID;
    }

    public String getPropertyID() {
        return propertyID;
    }

    public void setPropertyID(String propertyID) {
        this.propertyID = propertyID;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getDateSubmitted() {
        return dateSubmitted;
    }

    public void setDateSubmitted(String dateSubmitted) {
        this.dateSubmitted = dateSubmitted;
    }

    // Methods
    public static void submitRequest(MaintenanceRequest request) {
        requests.add(request);
        System.out.println("Maintenance request submitted: " + request.requestID);
    }

    public static void trackRequestStatus(String requestID) {
        for (MaintenanceRequest request : requests) {
            if (request.requestID.equals(requestID)) {
                System.out.println("Request status: " + request.status);
                return;
            }
        }
        System.out.println("Request not found!");
    }
}