from multiprocessing import Process
import os
import time

'''import threading

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

print("Both threads completed")'''

def square_numbers():
    for i in range(600):
        i*i
        

if __name__ == '__main__':
    processes = []
    num_processes = os.cpu_count()

    for i in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print('end main')

   
