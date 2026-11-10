class Battery:
    def charge(self):
        print("Battery is charging")

class Smartphone:
    def __init__(self, model):
        self.model = model
        self.battery = Battery()

    def use_phone(self):
        print("Phone Model:", self.model)
        self.battery.charge()
        print("Smartphone is ready to use")

phone = Smartphone("Samsung Galaxy")
phone.use_phone()
