import sys
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

def mygen():
    yield 1
    yield 2
    yield 3

g = mygen()
for i in g:
    print(i)  

def countdown(num):
    print('starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

value=next(cd)
print(value) 

print(next(cd))


def fibonacci(n):
    a, b = 0, 1
    while a< n:
        yield a
        a, b = b, a + b

fib= fibonacci(10)
for i in fib:
    print(i, end=",")


g = (1 for i in range(100000)if i%2==0)
print(sys.getsizeof(g))

l = [i for i in range(106800)if i%2 == 0]
print(sys.getsizeof(l))  