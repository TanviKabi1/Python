def check_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        if age < 18:
            print("You are not eligible to register.")
        else:
            print("Registration successful.")
    except ValueError as error:
        print("Invalid Input:", error)
    finally:
        print("Age verification completed.")

check_age()
