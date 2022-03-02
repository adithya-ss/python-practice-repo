import random

def use_numbers(first, second):
    def work_with_numbers(func):
        def my_wrapper(*args, **kwargs):
            print("Multiplying: ", first * second)
            result = func(*args, **kwargs)
            print("Raising powers: ", first ** second)
            return result
        return my_wrapper
    return work_with_numbers

num1 = random.randrange(5,8)
num2 = random.randrange(3,6)

@use_numbers(num1, num2)
def use_random_numbers(n1, n2):
    print("First number:", n1, "; Second number:", n2)

use_random_numbers(num1, num2)