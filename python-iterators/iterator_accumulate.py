from fnmatch import fnmatch
from itertools import accumulate
import operator

# Addition.
list_a = list(range(0,10))
acc_a = accumulate(list_a)
print(list_a)
print(list(acc_a))

# Multiplication
list_b = list(range(1,5))
acc_b = accumulate(list_b, func=operator.mul)
print(list(acc_b))

# Max - Compare and retain the max element.
list_c = [10,2,15,7,18,20,22,25]
acc_c = accumulate(list_c, func=max)
print(list(acc_c))