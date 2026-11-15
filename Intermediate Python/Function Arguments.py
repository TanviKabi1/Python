def foo(a,b,c,d=4):
    print(a,b,c,d)
foo(1, 2, 3)

def foo1(a,b,*args,**kwargs):
    print(a,b)
    for arg in args:
        print (arg)
    for key in kwargs:
        print(key,kwargs[key])

foo1(1, 2, 3, 4, 5, six=6, seven=7)
print()

foo1(1, 2, three=3)

def foo2():
    x = number 
    print('number in function:', x)

number = 0
foo2()


def foo3():
    global number 
    number = 3

print('number before foo2(): ', number)
foo3() 
print('number after foo2(): ', number)


def foo4(a_list):
    a_list[0] = -100
    a_list[2] = "Paul"
    
my_list = [1, 2, "Max"]
print('my_list before foo():', my_list)
foo4(my_list)
print('my_list after foo():', my_list)

def foo5(a_list):
    a_list += [4, 5] 
    
def bar(a_list):
    a_list = a_list + [4, 5]

my_list = [1, 2, 3]
print('my_list before foo5():', my_list)
foo5(my_list)
print('my_list after foo5():', my_list)

my_list = [1, 2, 3]
print('my_list before bar():', my_list)
bar(my_list)
print('my_list after bar():', my_list)