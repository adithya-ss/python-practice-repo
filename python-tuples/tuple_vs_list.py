import sys
import timeit

# Comparing sizes of list and tuple.
list_data = list(range(1,100,3))
tuple_data = tuple(range(1,100,3))
print("Size of list: ", sys.getsizeof(list_data), " bytes")
print("Size of tuple: ", sys.getsizeof(tuple_data), " bytes")

# Time taken to create - List vs Tuple
print("Time taken to create a list 1000000 times: ", timeit.timeit(stmt="[10,20,30,40,50]", number=1000000))
print("Time taken to create a tuple 1000000 times: ", timeit.timeit(stmt="(10,20,30,40,50)", number=1000000))