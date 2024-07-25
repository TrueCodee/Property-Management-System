package tests;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import com.property.management.Property;

public class PropertyTest {

    @BeforeEach
    public void setUp() {
        // Clear the properties list before each test
        Property.properties.clear();
    }

    @Test
    public void testAddProperty() {
        Property property = new Property("P002", "456 Elm St", "House", "Available", 1500.0);
        Property.addProperty(property);
        assertTrue(Property.properties.contains(property), "Property should be added to the list");
    }

    @Test
    public void testEditProperty() {
        Property property = new Property("P003", "789 Oak St", "Condo", "Available", 1800.0);
        Property.addProperty(property);
        Property.editProperty("P003", "789 Oak St, Apt 5", "Condo", "Rented", 2000.0);
        assertEquals("789 Oak St, Apt 5", property.getAddress());
        assertEquals("Rented", property.getStatus());
        assertEquals(2000.0, property.getRentAmount());
    }

    @Test
    public void testDeleteProperty() {
        Property property = new Property("P004", "101 Pine St", "Apartment", "Available", 1600.0);
        Property.addProperty(property);
        Property.deleteProperty("P004");
        assertFalse(Property.properties.contains(property), "Property should be removed from the list");
    }
}