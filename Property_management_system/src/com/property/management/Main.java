package com.property.management;

public class Main {
    public static void main(String[] args) {
        // Example usage of the classes

        // Create instances
        Property property = new Property("P001", "123 Main St", "Apartment", "Available", 1200.0);
        Tenant tenant = new Tenant("T001", "John Doe", "555-1234", "L001");
        Lease lease = new Lease("L001", "P001", "T001", "2024-01-01", "2025-01-01", 1200.0);
        MaintenanceRequest request = new MaintenanceRequest("R001", "T001", "P001", "Leaky faucet", "Pending", "2024-07-25");
        Payment payment = new Payment("PAY001", "T001", "L001", 1200.0, "2024-01-01");

        // Add instances to their respective lists
        Property.addProperty(property);
        Tenant.addTenant(tenant);
        Lease.createLease(lease);
        MaintenanceRequest.submitRequest(request);
        Payment.makePayment(payment);

        // Output some data to confirm functionality
        System.out.println("Property added: " + property.getAddress());
        System.out.println("Tenant added: " + tenant.getName());
        System.out.println("Lease created: " + lease.getStartDate());
        System.out.println("Maintenance request submitted: " + request.getDescription());
        System.out.println("Payment made: $" + payment.getAmount());
    }
}