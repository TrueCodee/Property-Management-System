package tests;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import com.property.management.MaintenanceRequest;

public class MaintenanceRequestTest {

    @BeforeEach
    public void setUp() {
        MaintenanceRequest.requests.clear();
    }

    @Test
    public void testSubmitRequest() {
        MaintenanceRequest request = new MaintenanceRequest("R001", "T001", "P001", "Leaky faucet", "Pending", "2024-07-25");
        MaintenanceRequest.submitRequest(request);
        assertTrue(MaintenanceRequest.requests.contains(request), "Maintenance request should be submitted and added to the list");
    }

    @Test
    public void testTrackRequestStatus() {
        MaintenanceRequest request = new MaintenanceRequest("R002", "T002", "P002", "Broken window", "Pending", "2024-07-26");
        MaintenanceRequest.submitRequest(request);
        MaintenanceRequest.trackRequestStatus("R002");
        assertEquals("Pending", request.getStatus());
    }
}