my_dict = {"name":"Max", "age":28, "city":"New York"}
print(my_dict)


my_dict_2 = dict(name="Lisa", age=27, city="Boston")
print(my_dict_2)


my_dict = {"name":"Max", "age":28, "city":"New York"}

if "name" in my_dict:
    print(my_dict["name"])


try:
    print(my_dict["firstname"])
except KeyError:
    print("No key found")  

for key in my_dict:
    print(key, my_dict[key])


for key in my_dict.keys():
    print(key)


for value in my_dict.values():
    print(value)


for key, value in my_dict.items():
    print(key, value)

dict_org = {"name":"Max", "age":28, "city":"New York"}


dict_copy = dict_org


dict_copy["name"] = "Lisa"
print(dict_copy)
print(dict_org)

dict_org = {"name":"Max", "age":28, "city":"New York"}

dict_copy = dict_org.copy()


dict_copy["name"] = "Lisa"
print(dict_copy)
print(dict_org)