names = ["arun", "meera", "karthik", "divya", "rahul"]

capitalized = [name.capitalize() for name in names]
long_names = [name for name in names if len(name) > 4]
name_lengths = {name: len(name) for name in names}

print("Original Names:", names)
print("Capitalized Names:", capitalized)
print("Names with More Than 4 Characters:", long_names)
print("Name Lengths:", name_lengths)
