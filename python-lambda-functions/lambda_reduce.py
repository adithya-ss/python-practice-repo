# reduce(function, sequence)
# Repeatedly applies the function to all elements and returns a single value.

from functools import reduce

list_a = [12,14,1,2,17,21]
list_sum = reduce(lambda num1, num2 : num1 + num2, list_a)
print("Org List: ", list_a)
print("Sum of elements: ", list_sum)