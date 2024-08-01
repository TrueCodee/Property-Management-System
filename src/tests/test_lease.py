import unittest
from lease import Lease


class TestLease(unittest.TestCase):

    def setUp(self):
        Lease.leases.clear()

    def test_create_lease(self):
        print("Running test_create_lease...")
        lease = Lease("L002", "P002", "T002",
                      "2024-02-01", "2025-02-01", 1300.0)
        Lease.create_lease(lease)
        self.assertIn(lease, Lease.leases)
        print(f"Lease {lease.lease_id} created: Property ID: {lease.property_id}, Tenant ID: {lease.tenant_id}, {lease.start_date} to {lease.end_date}, ${lease.rent_amount}.")

    def test_edit_lease(self):
        print("Running test_edit_lease...")
        lease = Lease("L003", "P003", "T003",
                      "2024-03-01", "2025-03-01", 1400.0)
        Lease.create_lease(lease)
        Lease.edit_lease("L003", "P003", "T003",
                         "2024-03-01", "2025-04-01", 1500.0)
        self.assertEqual(lease.end_date, "2025-04-01")
        self.assertEqual(lease.rent_amount, 1500.0)
        print(f"Lease {lease.lease_id} updated: Property ID: {lease.property_id}, Tenant ID: {lease.tenant_id}, {lease.start_date} to {lease.end_date}, ${lease.rent_amount}.")

    def test_terminate_lease(self):
        print("Running test_terminate_lease...")
        lease = Lease("L004", "P004", "T004",
                      "2024-04-01", "2025-04-01", 1600.0)
        Lease.create_lease(lease)
        Lease.terminate_lease("L004")
        self.assertNotIn(lease, Lease.leases)
        print(
            f"Lease {lease.lease_id} terminated: Property ID: {lease.property_id}, Tenant ID: {lease.tenant_id}.")


if __name__ == '__main__':
    unittest.main()
