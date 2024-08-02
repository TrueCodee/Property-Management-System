class Tenant:
    tenants = []

    def __init__(self, tenant_id, name, contact_info, lease_id):
        self.tenant_id = tenant_id
        self.name = name
        self.contact_info = contact_info
        self.lease_id = lease_id

    @classmethod
    def add_tenant(cls, tenant):
        cls.tenants.append(tenant)
        print(f"Tenant {tenant.name} added.")

    @classmethod
    def edit_tenant(cls, tenant_id, new_name, new_contact_info, new_lease_id):
        for tenant in cls.tenants:
            if tenant.tenant_id == tenant_id:
                tenant.name = new_name
                tenant.contact_info = new_contact_info
                tenant.lease_id = new_lease_id
                print(f"Tenant {tenant_id} updated.")
                return
        print("Tenant not found!")

    @classmethod
    def delete_tenant(cls, tenant_id):
        cls.tenants = [
            tenant for tenant in cls.tenants if tenant.tenant_id != tenant_id]
        print(f"Tenant {tenant_id} deleted.")

    @classmethod
    def view_tenants(cls):
        for tenant in cls.tenants:
            print(
                f"ID: {tenant.tenant_id}, Name: {tenant.name}, Contact: {tenant.contact_info}, Lease ID: {tenant.lease_id}")


# Input
tenant1 = Tenant("T001", "Chris Evans", "647-555-1234", "L001")
Tenant.add_tenant(tenant1)
Tenant.view_tenants()

Tenant.edit_tenant("T001", "Chris Evans", "647-555-5678", "L002")
Tenant.view_tenants()

Tenant.delete_tenant("T001")
Tenant.view_tenants()
