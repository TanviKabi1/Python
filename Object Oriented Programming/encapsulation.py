class Product:
    def __init__(self, product_id, price):
        self.product_id = product_id
        self.__price = price

    def update_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print("Price updated successfully")
        else:
            print("Price must be positive")

    def get_price(self):
        return self.__price

    def show_product(self):
        print("Product ID:", self.product_id)
        print("Product Price:", self.__price)

item = Product("P101", 2500)
item.show_product()
item.update_price(2800)
print("Current Price:", item.get_price())
