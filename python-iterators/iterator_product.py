from itertools import product

list_a = [11,22]
list_b = [7,9]

# Cartesian product of iterables - Results is a list of tuples.
prod = product(list_a,list_b)
prod_rpt = product(list_a, list_b, repeat=2)
print(list(prod))
print(list(prod_rpt))