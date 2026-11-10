class Appliance:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)


class WashingMachine(Appliance):
    def __init__(self, brand, capacity, price):
        super().__init__(brand)
        self.capacity = capacity
        self.price = price

    def display_details(self):
        self.show_brand()
        print("Capacity:", self.capacity, "kg")
        print("Price: Rs.", self.price)


machine = WashingMachine("LG", 8, 32000)
machine.display_details()
