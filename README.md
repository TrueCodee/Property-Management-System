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
- Python 3.x
- An IDE such as Eclipse with PyDev, PyCharm, or Visual Studio Code

### Installation
1. **Clone the repository:**
   ```bash
   git clone <https://github.com/TrueCodee/Property-Management-System>

2. **Navigate to the project directory:**
- cd property_management_system
 
 
## Running the Application
1. **Run the 'main.py' file:**
  - python main.py

## Running Tests
1. Navigate to the project directory:
   - cd property_management_system
2. Run all tests:
   - python -m unittest discover -s tests

## Usage
### Example Usage in Main.java
The 'Main' class provides examples of how to use the various features of the Property Management System:
Property Management System:
from property import Property
from tenant import Tenant
from lease import Lease
from maintenance_request import MaintenanceRequest
from payment import Payment

def demonstrate_property_management():
    print("\n--- Property Management ---")
    property = Property("P002", "456 Elm St", "House", "Available", 1500.0)
    Property.add_property(property)
    Property.edit_property("P002", "456 Elm St, Apt 2", "House", "Rented", 1600.0)
    Property.delete_property("P002")

def demonstrate_tenant_management():
    print("\n--- Tenant Management ---")
    tenant = Tenant("T002", "Jane Doe", "555-6789", "L002")
    Tenant.add_tenant(tenant)
    Tenant.edit_tenant("T002", "Jane Doe Updated", "555-9876", "L003")
    Tenant.delete_tenant("T002")

def demonstrate_lease_management():
    print("\n--- Lease Management ---")
    lease = Lease("L002", "P002", "T002", "2024-02-01", "2025-02-01", 1300.0)
    Lease.create_lease(lease)
    Lease.edit_lease("L002", "P002", "T002", "2024-02-01", "2025-03-01", 1400.0)
    Lease.terminate_lease("L002")

def demonstrate_maintenance_requests():
    print("\n--- Maintenance Requests ---")
    request = MaintenanceRequest("R002", "T002", "P002", "Broken window", "Pending", "2024-08-01")
    MaintenanceRequest.submit_request(request)
    MaintenanceRequest.track_request_status("R002")

def demonstrate_payments():
    print("\n--- Payments ---")
    payment = Payment("PAY002", "T002", "L002", 1300.0, "2024-02-01")
    Payment.make_payment(payment)
    Payment.view_payment_history("T002")

def run_tests():
    print("\n--- Running Tests ---")
    loader = unittest.TestLoader()
    suite = loader.discover('tests')
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        print("All tests passed successfully!")
    else:
        print("Some tests failed. Please check the test results for details.")

def main():
    print("Welcome to the Property Management System by Group 22")
    print("Team Members: Harshita Nagasubramanian, Vishal Srikanth, Aryan Jain, Abdullah Abdullah, Wit Qi")

    demonstrate_property_management()
    demonstrate_tenant_management()
    demonstrate_lease_management()
    demonstrate_maintenance_requests()
    demonstrate_payments()
    run_tests()


## Authors
- Aryan Jain
- Harshita Nagasubramanian 
- Vishal Srikanth 
- Abdullah Abdullah 
- Wit Qi

## License
This project is licensed under the MIT License.
    
