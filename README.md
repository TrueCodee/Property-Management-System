# Property Management System

## Overview
This project is a Property Management System developed for the CP 317 – Software Engineering course. It allows users to manage properties, tenants, leases, maintenance requests, and payments.

## Features
- **Property Management:** Add, edit, and delete properties.
- **Tenant Management:** Add, edit, and delete tenants.
- **Lease Management:** Create, edit, and terminate leases.
- **Maintenance Requests:** Submit and track maintenance requests.
- **Payments:** Make and view payment history.

## Setup

### Prerequisites
- Java Development Kit (JDK) 8 or later
- An IDE such as Eclipse or IntelliJ IDEA
- JUnit 5 for testing

### Installation
1. **Clone the repository:**
   ```bash
   git clone <https://github.com/TrueCodee/Property-Management-System>

2. **Open the project in your preferred IDE:**
- In Eclipse:
  - Go to 'File > Open Projects from File System...'
  - Select the cloned project directory
- In IntelliJ IDEA:
  - Go to 'File > Open'
  - Select the cloned project directory
 
3. ** Add JUnit 5 to your project:**
- In Eclipse:
  - Right-click on the project and select 'Properties'
  - Go to 'Java Build Path > Libraries > Add Library... > JUnit > Next > JUnit 5 > Finish'
- In IntelliJ IDEA:
  - Go to 'File > Project Structure > Libraries'
  - Click '+' and add JUnit 5
 
## Running the Application
1. **Navigate to the 'Main' class:**
  - In Eclipse: 'src/com/property/management/Main.java'
  - In IntelliJ IDEA: 'src/com/property/management/Main.java'
2. **Run the 'Main' class:**
  - Right-click on 'Main.java' and select 'Run As > Java Application' (Eclipse)
  - Right-click on Main.java and select Run 'Main.main()' (IntelliJ IDEA)

## Usage
### Example Usage in Main.java
The 'Main' class provides examples of how to use the various features of the Property Management System:
Property Management System:
public class Main {
    public static void main(String[] args) {
        // Example usage of the classes

        // Property example
        Property property = new Property("P001", "123 Main St", "Apartment", "Available", 1200.0);
        Property.addProperty(property);
        System.out.println("Property added: " + property.getAddress());

        // Tenant example
        Tenant tenant = new Tenant("T001", "John Doe", "555-1234", "L001");
        Tenant.addTenant(tenant);
        System.out.println("Tenant added: " + tenant.getName());

        // Lease example
        Lease lease = new Lease("L001", "P001", "T001", "2024-01-01", "2025-01-01", 1200.0);
        Lease.createLease(lease);
        System.out.println("Lease created: " + lease.getStartDate());

        // Maintenance request example
        MaintenanceRequest request = new MaintenanceRequest("R001", "T001", "P001", "Leaky faucet", "Pending", "2024-07-25");
        MaintenanceRequest.submitRequest(request);
        System.out.println("Maintenance request submitted: " + request.getDescription());

        // Payment example
        Payment payment = new Payment("PAY001", "T001", "L001", 1200.0, "2024-01-01");
        Payment.makePayment(payment);
        System.out.println("Payment made: $" + payment.getAmount());
    }
}

## Running Tests
Unit tests are provided in the tests package. To run the tests:

### Run all 'tests' in the tests package:
- Right-click on the 'tests' package
- Select 'Run As > JUnit Test' (Eclipse)
- Select Run 'All Tests' (IntelliJ IDEA)

### Verify test results:
- Ensure all tests pass without errors. The JUnit view will display green for passed tests and red for failed tests.

## Project Structure
property-management-system/
│
├── src/
│   ├── com/property/management/
│   │   ├── Lease.java
│   │   ├── Main.java
│   │   ├── MaintenanceRequest.java
│   │   ├── Payment.java
│   │   ├── Property.java
│   │   └── Tenant.java
│   └── tests/
│       ├── LeaseTest.java
│       ├── MaintenanceRequestTest.java
│       ├── PaymentTest.java
│       ├── PropertyTest.java
│       └── TenantTest.java
│
├── README.md
└── ... (other project files)

## Authors
- Aryan Jain
- Harshita Nagasubramanian 
- Vishal Srikanth 
- Abdullah Abdullah 
- Wit Qi

## License
This project is licensed under the MIT License.
    
