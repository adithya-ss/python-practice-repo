from itertools import permutations
# Results in all possible orderings of input.

names = ["Lampard", "Terry", "Drogba", "Mourinho"]
perm = permutations(names)
print(list(perm))

# Specify the number of elements in each tuple.
perm_2 = permutations(names, 2)
print(list(perm_2))

