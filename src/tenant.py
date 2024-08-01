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
