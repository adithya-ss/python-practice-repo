# Process - An instance of a program.
# Memory is not shared between processes.
# Processes can be interrupted/killed.

# GIL - Global interpreter lock.
# Can be avoided by using multiprocessing.
# Allows only one thread to execute at a time.

from multiprocessing import Process, cpu_count
import os 
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    print("Number of CPU cores:",cpu_count())
    
    # proc_a = Process(target=counter, args=(100000000,))
    proc_a = Process(target=counter, args=(50000000,))
    proc_b = Process(target=counter, args=(50000000,))

    proc_a.start()
    proc_b.start()
    
    proc_a.join()
    proc_b.join()

    print("Execution completed in: ", time.perf_counter(), "secs")

if __name__ == "__main__":
    main()