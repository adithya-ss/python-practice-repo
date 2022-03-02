# There are 2 different types of decorators.
# 1. Function Decorators.
# 2. Class Decorators.
# Syntax: @decorator_name

# A function decorator is something when a function takes another function as argument and extends the
# behaviour of the first function without explicitly modifying it.

# Functions in python are first class objects - This means that like any other object, they can be defined as
# another function, passed as an argument and even return from another function.

import random
import functools

def my_decorator(func):
    @functools.wraps(func)
    def my_wrapper(*args, **kwargs):
        print("Starting decorator...")
        result = func(*args, **kwargs)
        print("Ending decorator...")
        return result
    return my_wrapper

@my_decorator
def modify_random_number():
    rand_num = random.randrange(1,7)
    print("Before decorator was called:", rand_num)
    return rand_num + 10

help(modify_random_number)
print(modify_random_number.__name__)
print("")
res = modify_random_number()
print("After decorator was called:", res)
