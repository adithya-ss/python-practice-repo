from ast import arg
import functools
import datetime

def new_decorator(my_func):
    @functools.wraps(my_func)
    def new_wrapper(*args, **kwargs):
        print("Checking time and date...")
        result = my_func(*args, **kwargs)
        print("Ending...")
        return result
    return new_wrapper

def see_workflow(my_func):
    @functools.wraps(my_func)
    def wf_wrapper(*args, **kwargs):
        func_args = [repr(val) for val in args]
        func_kwargs = [f"{key}={val!r}" for key, val in kwargs.items()]
        signature = ", ".join(func_args + func_kwargs)
        print(f"Calling {my_func.__name__}({signature})")
        res = my_func(*args, **kwargs)
        print(f"{my_func.__name__!r} returned {res!r}")
        return res
    return wf_wrapper

@see_workflow
@new_decorator
def print_date_time(now):
    now = f'It is {now}'
    print(now)
    return now

curr_dt = datetime.datetime.now()
print_date_time(curr_dt)