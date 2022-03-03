# Threads - An entity within a process
# Multiple threads can be spawned from inside a single process.
# All threads share the same memory.
# Not interruptable/killable.
# Race condition - Two or more threads want to operate on something at the same time.

import threading
import time

print("Number of active threads:",threading.active_count())
print("List of all the running threads:",threading.enumerate())

def drive_car():
    time.sleep(5)
    print("You have completed your drive.")

def call_mom():
    time.sleep(10)
    print("Calling mom.")

def use_indicator():
    time.sleep(3)
    print("Your right indicator is activated.")

t1 = threading.Thread(target=drive_car)
t1.start()

t2 = threading.Thread(target=call_mom)
t2.start()

t3 = threading.Thread(target=use_indicator)
t3.start()

# drive_car()
# play_music()
# use_indicator()

t1.join()
t2.join()
t3.join()

print("Number of active threads:",threading.active_count())
print("List of all the running threads:",threading.enumerate())
print("Main thread ran for: ",time.perf_counter(),"secs")