import unittest
from tenant import Tenant


class TestTenant(unittest.TestCase):

    def setUp(self):
        Tenant.tenants.clear()

    def test_add_tenant(self):
        print("Running test_add_tenant...")
        tenant = Tenant("T002", "Jane Doe", "555-6789", "L002")
        Tenant.add_tenant(tenant)
        self.assertIn(tenant, Tenant.tenants)
        print(
            f"Tenant {tenant.tenant_id} added: {tenant.name}, {tenant.contact_info}, Lease ID: {tenant.lease_id}.")

    def test_edit_tenant(self):
        print("Running test_edit_tenant...")
        tenant = Tenant("T003", "John Smith", "555-1122", "L003")
        Tenant.add_tenant(tenant)
        Tenant.edit_tenant("T003", "John Smith Updated", "555-3344", "L004")
        self.assertEqual(tenant.name, "John Smith Updated")
        self.assertEqual(tenant.contact_info, "555-3344")
        self.assertEqual(tenant.lease_id, "L004")
        print(
            f"Tenant {tenant.tenant_id} updated: {tenant.name}, {tenant.contact_info}, Lease ID: {tenant.lease_id}.")

    def test_delete_tenant(self):
        print("Running test_delete_tenant...")
        tenant = Tenant("T004", "Alice Brown", "555-9876", "L005")
        Tenant.add_tenant(tenant)
        Tenant.delete_tenant("T004")
        self.assertNotIn(tenant, Tenant.tenants)
        print(f"Tenant {tenant.tenant_id} deleted: {tenant.name}.")


if __name__ == '__main__':
    unittest.main()
