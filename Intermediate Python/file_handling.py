filename = "shopping.txt"

items = ["Milk", "Bread", "Rice", "Eggs"]

with open(filename, "w") as file:
    for item in items:
        file.write(item + "\n")

print("Shopping list created.")

with open(filename, "r") as file:
    print("\nShopping List:")
    for line in file:
        print("-", line.strip())

with open(filename, "a") as file:
    file.write("Butter\n")

print("\nNew item added successfully.")
