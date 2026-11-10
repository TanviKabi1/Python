class AreaCalculator:
    def calculate_area(self, length, width=None):
        if width is None:
            return 3.14 * length * length
        return length * width

shape = AreaCalculator()

print("Area of Circle:", shape.calculate_area(7))
print("Area of Rectangle:", shape.calculate_area(10, 5))
