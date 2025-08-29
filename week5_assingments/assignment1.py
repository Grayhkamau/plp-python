# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"Device: {self.brand} {self.model}"

# Child Class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call the parent constructor
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery

    def call(self, number):
        print(f"Calling {number}...")

    def charge(self):
        print(f" Charging {self.brand} {self.model}... Battery at {self.battery}%")

    def phone_info(self):
        return f"{self.device_info()}, Storage: {self.storage}GB, Battery: {self.battery}%"

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S22", 128, 80)
phone2 = Smartphone("Apple", "iPhone 14", 256, 50)

# Using methods
print(phone1.phone_info())
phone1.call("123-456-789")
phone2.charge()
