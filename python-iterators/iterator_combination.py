from itertools import combinations, combinations_with_replacement

teams = ["Chelsea", "Real Madrid", "Bayern Munich", "PSG", "Milan"]

# Should always specify the combination length.

# Unique elements in each combination.
comb = combinations(teams,3)
print(list(comb))

# Combinations with repititions.
comb_rplc = combinations_with_replacement(teams,2)
print(list(comb_rplc))