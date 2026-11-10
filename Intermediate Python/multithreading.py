import threading

def print_numbers():
    for number in range(1, 6):
        print("Number:", number)

def print_letters():
    for letter in "ABCDE":
        print("Letter:", letter)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

print("Both threads completed")
