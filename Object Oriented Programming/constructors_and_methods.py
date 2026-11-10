class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, percentage):
        discount = self.price * percentage / 100
        self.price -= discount
        print("Discount Applied:", discount)

    def update_price(self, new_price):
        self.price = new_price

    def show_details(self):
        print("Mobile Brand:", self.brand)
        print("Final Price:", self.price)

phone = Mobile("Samsung", 30000)
phone.show_details()
phone.apply_discount(10)
phone.update_price(25500)
phone.show_details()
