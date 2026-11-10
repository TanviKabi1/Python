class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        return self.price + other.price

    def __gt__(self, other):
        return self.price > other.price

    def __str__(self):
        return self.name + ": Rs. " + str(self.price)

item1 = Product("Keyboard", 1200)
item2 = Product("Mouse", 800)

print(item1)
print(item2)
print("Combined Price:", item1 + item2)
print("Keyboard costs more:", item1 > item2)
