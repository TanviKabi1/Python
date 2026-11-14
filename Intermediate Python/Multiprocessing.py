from multiprocessing import Process,Value,Array,Lock,Pool
from multiprocessing import Queue
import numbers
import time

def cube(number):
    return number * number * number
if __name__ == "__main__": 
    numbers = range(10)
    pool = Pool()

    result = pool.map(cube,numbers)

    pool.close()
    pool.join()

    print(result)
