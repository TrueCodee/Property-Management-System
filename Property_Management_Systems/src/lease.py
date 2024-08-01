class Lease:
    leases = []

    def __init__(self, lease_id, property_id, tenant_id, start_date, end_date, rent_amount):
        self.lease_id = lease_id
        self.property_id = property_id
        self.tenant_id = tenant_id
        self.start_date = start_date
        self.end_date = end_date
        self.rent_amount = rent_amount

    @classmethod
    def create_lease(cls, lease):
        cls.leases.append(lease)
        print(f"Lease {lease.lease_id} created.")

    @classmethod
    def edit_lease(cls, lease_id, new_property_id, new_tenant_id, new_start_date, new_end_date, new_rent_amount):
        for lease in cls.leases:
            if lease.lease_id == lease_id:
                lease.property_id = new_property_id
                lease.tenant_id = new_tenant_id
                lease.start_date = new_start_date
                lease.end_date = new_end_date
                lease.rent_amount = new_rent_amount
                print(f"Lease {lease_id} updated.")
                return
        print("Lease not found!")

    @classmethod
    def terminate_lease(cls, lease_id):
        cls.leases = [
            lease for lease in cls.leases if lease.lease_id != lease_id]
        print(f"Lease {lease_id} terminated.")
