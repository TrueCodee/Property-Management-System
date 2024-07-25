package com.property.management;

import java.util.ArrayList;
import java.util.List;

public class Property {
    private String propertyID;
    private String address;
    private String type;
    private String status;
    private double rentAmount;
    public static List<Property> properties = new ArrayList<>();

    public Property(String propertyID, String address, String type, String status, double rentAmount) {
        this.propertyID = propertyID;
        this.address = address;
        this.type = type;
        this.status = status;
        this.rentAmount = rentAmount;
    }

    // Getters and Setters
    public String getPropertyID() {
        return propertyID;
    }

    public void setPropertyID(String propertyID) {
        this.propertyID = propertyID;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public double getRentAmount() {
        return rentAmount;
    }

    public void setRentAmount(double rentAmount) {
        this.rentAmount = rentAmount;
    }

    // Methods
    public static void addProperty(Property property) {
        properties.add(property);
        System.out.println("Property added: " + property.address);
    }

    public static void editProperty(String propertyID, String newAddress, String newType, String newStatus, double newRentAmount) {
        for (Property property : properties) {
            if (property.propertyID.equals(propertyID)) {
                property.setAddress(newAddress);
                property.setType(newType);
                property.setStatus(newStatus);
                property.setRentAmount(newRentAmount);
                System.out.println("Property updated: " + property.address);
                return;
            }
        }
        System.out.println("Property not found!");
    }

    public static void deleteProperty(String propertyID) {
        properties.removeIf(property -> property.propertyID.equals(propertyID));
        System.out.println("Property deleted: " + propertyID);
    }
}