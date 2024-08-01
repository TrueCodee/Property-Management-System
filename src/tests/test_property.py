import unittest
from property import Property


class TestProperty(unittest.TestCase):

    def setUp(self):
        Property.properties.clear()

    def test_add_property(self):
        print("Running test_add_property...")
        property = Property("P002", "456 Elm St", "House", "Available", 1500.0)
        Property.add_property(property)
        self.assertIn(property, Property.properties)
        print(
            f"Property {property.property_id} added: {property.address}, {property.status}, ${property.rent_amount}.")

    def test_edit_property(self):
        print("Running test_edit_property...")
        property = Property("P003", "789 Oak St", "Condo", "Available", 1800.0)
        Property.add_property(property)
        Property.edit_property("P003", "789 Oak St, Apt 5",
                               "Condo", "Rented", 2000.0)
        self.assertEqual(property.address, "789 Oak St, Apt 5")
        self.assertEqual(property.status, "Rented")
        self.assertEqual(property.rent_amount, 2000.0)
        print(
            f"Property {property.property_id} updated: {property.address}, {property.status}, ${property.rent_amount}.")

    def test_delete_property(self):
        print("Running test_delete_property...")
        property = Property("P004", "101 Pine St",
                            "Apartment", "Available", 1600.0)
        Property.add_property(property)
        Property.delete_property("P004")
        self.assertNotIn(property, Property.properties)
        print(f"Property {property.property_id} deleted: {property.address}.")


if __name__ == '__main__':
    unittest.main()
