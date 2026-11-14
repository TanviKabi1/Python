
from threading import Thread,Lock
import os
import time
from queue import Queue

def square_numbers():
    for i in range(1000):
        result = i * i

        
if __name__ == "__main__":        
    threads = []
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

   
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
   
#-----------------------------

database_value = 0

def increase():
    global database_value 

    with lock:
        lock.aquire()
        local_copy = database_value
        
        local_copy += 1
        time.sleep(0.1)
        
        database_value = local_copy


if __name__ == "__main__":

    lock = Lock()
    print('Start value: ', database_value)

    t1 = Thread(target=increase)
    t2 = Thread(target=increase)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)

    print('end main')

#-------------------------------
q = Queue()


q.put(1)
q.put(2) 
q.put(3) 

first = q.get() 
print(first)