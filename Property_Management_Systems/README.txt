# Property Management System

## Overview
This project is a Property Management System developed for the CP 317 – Software Engineering course. It allows users to manage properties, tenants, leases, maintenance requests, and payments.

## Features
- **Property Management**: Add, edit, and delete properties.
- **Tenant Management**: Add, edit, and delete tenants.
- **Lease Management**: Create, edit, and terminate leases.
- **Maintenance Requests**: Submit and track maintenance requests.
- **Payments**: Make and view payment history.

## Setup

### Prerequisites
- Python 3.8 or later
- An IDE such as Eclipse with PyDev or VSCode
- pytest for testing

### Installation
1. **Clone the repository:**
    ```sh
    git clone <https://github.com/TrueCodee/Property-Management-System>
    ```

2. **Open the project in your preferred IDE:**
    - **In Eclipse with PyDev:**
        - Go to `File > Import`
        - Select `Existing Projects into Workspace`
        - Select the cloned project directory and click `Finish`
    - **In VSCode:**
        - Go to `File > Open Folder`
        - Select the cloned project directory

3. **Install the required packages:**
    - Navigate to the project directory in your terminal
    - Run the following command to install the necessary packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application
1. **Navigate to the `main.py` file:**
    - In Eclipse: `src/main.py`
    - In VSCode: `src/main.py`

2. **Run the `main.py` file:**
    - **In Eclipse with PyDev:**
        - Right-click on `main.py` and select `Run As > Python Run`
    - **In VSCode:**
        - Open `main.py` and click the `Run` button or use the shortcut `F5`

## Usage
### Example Usage in `main.py`
The `main.py` file provides examples of how to use the various features of the Property Management System:

```python
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
```

## Running Tests
Unit tests are provided in the `tests` package. To run the tests:

1. **Run all tests in the `tests` package:**
    - Navigate to the project directory in your terminal
    - Run the following command:
    ```sh
    pytest tests/
    ```

2. **Verify test results:**
    - Ensure all tests pass without errors. The pytest output will show the status of each test.

## Authors
- Aryan Jain
- Harshita Nagasubramanian
- Vishal Srikanth
- Abdullah Abdullah
- Wit Qi

## License
This project is licensed under the MIT License.
