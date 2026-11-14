from multiprocessing import Process
import os
import time



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

   
