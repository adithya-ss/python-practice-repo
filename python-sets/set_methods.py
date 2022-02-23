# Add elements to a set.

chelsea_squad = set()
chelsea_squad.add("Havertz")
chelsea_squad.add("Mount")
chelsea_squad.add("Kante")
chelsea_squad.add("Silva")
chelsea_squad.add("Werner")
chelsea_squad.add("Pulisic")
chelsea_squad.add("Lukaku")
chelsea_squad.add("Alonso")
print(chelsea_squad)
print("")

# Remove elements from a set.
chelsea_squad.remove("Lukaku")
chelsea_squad.remove("Alonso")
print(chelsea_squad)
print("")
# When an element which is not there in a set is tried to be removed, a KeyError is returned.

# To avoid running into KeyError, we can use discard() instead of remove()
chelsea_squad.discard("Hazard")

# Empty the set - clear()

# Remove arbitrary element - pop()
print(chelsea_squad.pop())
print(chelsea_squad)
print("")
