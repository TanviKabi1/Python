
tuple_1 = ("Max", 28, "New York")
tuple_2 = "Linda", 25, "Miami" 

tuple_3 = (25,)
print(tuple_1)
print(tuple_2)
print(tuple_3)

tuple_4 = tuple([1,2,3])
print(tuple_4)

my_tuple = ('a','p','p','l','e',)

print(len(my_tuple))

print(my_tuple.count('p'))

print(my_tuple.index('l'))


my_tuple = ('a', 'b') * 5
print(my_tuple)


my_tuple = (1,2,3) + (4,5,6)
print(my_tuple)

my_list = ['a', 'b', 'c', 'd']
list_to_tuple = tuple(my_list)
print(list_to_tuple)

tuple_to_list = list(list_to_tuple)
print(tuple_to_list)


string_to_tuple = tuple('Hello')
print(string_to_tuple)