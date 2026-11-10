def countdown(start):
    while start > 0:
        yield start
        start -= 1


def square_generator(values):
    for value in values:
        yield value * value


print("Countdown:")
for number in countdown(5):
    print(number, end=" ")

print("\nGenerated Squares:")
for square in square_generator([2, 4, 6, 8]):
    print(square, end=" ")
print()
