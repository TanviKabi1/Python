zeros = [0] * 10
onetwos = [1, 2] * 5
print(zeros)
print(onetwos)

zeros = (0,) * 10
onetwos = (1, 2) * 5
print(zeros)
print(onetwos)

A_string = "A" * 10
AB_string = "AB" * 5
print(A_string)
print(AB_string)
#----------------------------

def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
        
my_function("Hey", 3, [0, 1, 2], name="Alex", age=8)


#-------


def foo(a, b, c):
    print(a, b, c)

my_list = [1, 2, 3]
foo(*my_list)

my_string = "ABC"
foo(*my_string)

my_dict = {'a': 4, 'b': 5, 'c': 6}
foo(**my_dict)

#-----------------------

numbers = (1, 2, 3, 4, 5, 6, 7, 8)

*beginning, last = numbers
print(beginning)
print(last)

my_tuple = (1, 2, 3)
my_set = {4, 5, 6}
my_list = [*my_tuple, *my_set]
print(my_list)