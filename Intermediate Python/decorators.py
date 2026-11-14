import functools
def execution_timer(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print("Function execution started")
        result = function(*args, **kwargs)
        print("Function execution completed")
        return result
    return wrapper

@execution_timer
def calculate_total(price, quantity):
    total = price * quantity
    print("Total Amount:", total)
    return total

calculate_total(250, 4)
print(help(calculate_total))
print(calculate_total.__name__)  
