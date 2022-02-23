# Frozen sets are immutable versions of sets.
months_in_year = frozenset(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])

print(months_in_year)

# Following operations will result in error.
months_in_year.add("Augtober")
months_in_year.remove("September")

# Union, intersection and difference methods will work.