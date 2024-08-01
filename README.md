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

if __name__ == "__main__":
    # Example usage of the classes

    # Property example
    property = Property("P001", "123 Main St", "Apartment", "Available", 1200.0)
    Property.add_property(property)
    print("Property added:", property.address)

    # Tenant example
    tenant = Tenant("T001", "John Doe", "555-1234", "L001")
    Tenant.add_tenant(tenant)
    print("Tenant added:", tenant.name)

    # Lease example
    lease = Lease("L001", "P001", "T001", "2024-01-01", "2025-01-01", 1200.0)
    Lease.create_lease(lease)
    print("Lease created:", lease.start_date)

    # Maintenance request example
    request = MaintenanceRequest("R001", "T001", "P001", "Leaky faucet", "Pending", "2024-07-25")
    MaintenanceRequest.submit_request(request)
    print("Maintenance request submitted:", request.description)

    # Payment example
    payment = Payment("PAY001", "T001", "L001", 1200.0, "2024-01-01")
    Payment.make_payment(payment)
    print("Payment made: $", payment.amount)



## Authors
- Aryan Jain
- Harshita Nagasubramanian 
- Vishal Srikanth 
- Abdullah Abdullah 
- Wit Qi

## License
This project is licensed under the MIT License.
    
