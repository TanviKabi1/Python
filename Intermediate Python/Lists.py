my_list = ["banana", "cherry", "apple"]


print("Length:", len(my_list))


my_list.append("orange")


my_list.insert(1, "blueberry")
print(my_list)


item = my_list.pop()
print("Popped item: ", item)


my_list.remove("cherry") 
print(my_list)


my_list.clear()
print(my_list)


my_list = ["banana", "cherry", "apple"]
my_list.reverse()
print('Reversed: ', my_list)


my_list.sort()
print('Sorted: ', my_list)


my_list = ["banana", "cherry", "apple"]
new_list = sorted(my_list)


list_with_zeros = [0] * 5
print(list_with_zeros)


list_concat = list_with_zeros + my_list
print(list_concat)

string_to_list = list('Hello')
print(string_to_list)