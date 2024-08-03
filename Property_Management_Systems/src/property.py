class Property:
    properties = []

    def __init__(self, property_id, address, property_type, status, rent_amount):
        self.property_id = property_id
        self.address = address
        self.property_type = property_type
        self.status = status
        self.rent_amount = rent_amount

    @classmethod
    def add_property(cls, property):
        cls.properties.append(property)
        print(f"Property {property.address} added.")

    @classmethod
    def edit_property(cls, property_id, new_address, new_type, new_status, new_rent_amount):
        for property in cls.properties:
            if property.property_id == property_id:
                property.address = new_address
                property.property_type = new_type
                property.status = new_status
                property.rent_amount = new_rent_amount
                print(f"Property {property_id} updated.")
                return
        print("Property not found!")

    @classmethod
    def delete_property(cls, property_id):
        cls.properties = [
            property for property in cls.properties if property.property_id != property_id]
        print(f"Property {property_id} deleted.")

    @classmethod
    def view_properties(cls):
        for property in cls.properties:
            print(f"ID: {property.property_id}, Address: {property.address}, Type: {property.property_type}, Status: {property.status}, Rent: {property.rent_amount}")


# Input
property1 = Property("P001", "201 Lester", "Apartment", "Available", 1200.0)
Property.add_property(property1)
Property.view_properties()

Property.edit_property("P001", "201 Lester, Apt 2",
                       "Apartment", "Rented", 1300.0)
Property.view_properties()

Property.delete_property("P001")
Property.view_properties()
