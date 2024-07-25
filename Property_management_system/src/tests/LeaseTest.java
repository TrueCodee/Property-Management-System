package tests;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import com.property.management.Lease;

public class LeaseTest {

    @BeforeEach
    public void setUp() {
        Lease.leases.clear();
    }

    @Test
    public void testCreateLease() {
        Lease lease = new Lease("L001", "P001", "T001", "2024-01-01", "2025-01-01", 1200.0);
        Lease.createLease(lease);
        assertTrue(Lease.leases.contains(lease), "Lease should be created and added to the list");
    }

    @Test
    public void testEditLease() {
        Lease lease = new Lease("L002", "P002", "T002", "2024-01-01", "2025-01-01", 1300.0);
        Lease.createLease(lease);
        Lease.editLease("L002", "P003", "T003", "2024-02-01", "2025-02-01", 1400.0);
        assertEquals("P003", lease.getPropertyID());
        assertEquals("T003", lease.getTenantID());
        assertEquals("2024-02-01", lease.getStartDate());
        assertEquals("2025-02-01", lease.getEndDate());
        assertEquals(1400.0, lease.getRentAmount());
    }

    @Test
    public void testTerminateLease() {
        Lease lease = new Lease("L003", "P004", "T004", "2024-01-01", "2025-01-01", 1500.0);
        Lease.createLease(lease);
        Lease.terminateLease("L003");
        assertFalse(Lease.leases.contains(lease), "Lease should be terminated and removed from the list");
    }
}