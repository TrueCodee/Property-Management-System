package tests;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import com.property.management.Tenant;

public class TenantTest {

    @BeforeEach
    public void setUp() {
        Tenant.tenants.clear();
    }

    @Test
    public void testAddTenant() {
        Tenant tenant = new Tenant("T002", "Jane Doe", "555-6789", "L002");
        Tenant.addTenant(tenant);
        assertTrue(Tenant.tenants.contains(tenant), "Tenant should be added to the list");
    }

    @Test
    public void testEditTenant() {
        Tenant tenant = new Tenant("T003", "John Smith", "555-1122", "L003");
        Tenant.addTenant(tenant);
        Tenant.editTenant("T003", "John Smith", "555-3344", "L004");
        assertEquals("John Smith", tenant.getName());
        assertEquals("555-3344", tenant.getContactInfo());
        assertEquals("L004", tenant.getLeaseID());
    }

    @Test
    public void testDeleteTenant() {
        Tenant tenant = new Tenant("T004", "Alice Brown", "555-2233", "L005");
        Tenant.addTenant(tenant);
        Tenant.deleteTenant("T004");
        assertFalse(Tenant.tenants.contains(tenant), "Tenant should be removed from the list");
    }
}