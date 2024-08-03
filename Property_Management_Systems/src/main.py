from property import Property
from tenant import Tenant
from lease import Lease
from maintenance_request import MaintenanceRequest
from payment import Payment


def demonstrate_property_management():
    print("\n--- Property Management ---")
    property = Property("P002", "456 Elm St", "House", "Available", 1500.0)
    Property.add_property(property)
    Property.edit_property("P002", "456 Elm St, Apt 2",
                           "House", "Rented", 1600.0)
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
    Lease.edit_lease("L002", "P002", "T002",
                     "2024-02-01", "2025-03-01", 1400.0)
    Lease.terminate_lease("L002")


def demonstrate_maintenance_requests():
    print("\n--- Maintenance Requests ---")
    request = MaintenanceRequest(
        "R002", "T002", "P002", "Broken window", "Pending", "2024-08-01")
    MaintenanceRequest.submit_request(request)
    MaintenanceRequest.track_request_status("R002")
    MaintenanceRequest.resolve_request("R002")


def demonstrate_payments():
    print("\n--- Payments ---")
    payment = Payment("PAY002", "T002", "L002", 1300.0, "2024-02-01")
    Payment.make_payment(payment)
    Payment.view_payment_history("T002")


def main():
    print("Welcome to the Property Management System by Group 22")
    print("Team Members: Harshita Nagasubramanian, Vishal Srikanth, Aryan Jain, Abdullah Abdullah, Wit Qi")

    demonstrate_property_management()
    demonstrate_tenant_management()
    demonstrate_lease_management()
    demonstrate_maintenance_requests()
    demonstrate_payments()


if __name__ == "__main__":
    main()
