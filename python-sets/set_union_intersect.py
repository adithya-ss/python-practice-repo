chelsea_squad = {"Mendy", "Azpilicueta", "Silva", "Rudiger", "Kante", "Kovacic", "Jorginho", "Mount", "Pulisic", "Havertz", "Werner"}
psg_squad = {"Mbappe", "Messi", "Neymar", "Veratti"}
england_squad = {"Mount", "Kane", "Grealish"}
italy_squad = {"Jorginho", "Veratti"}
germany_squad = {"Kimmich", "Havertz", "Werner", "Rudiger"}
brazil_squad = {"Neymar", "Silva"}
france_squad = {"Mbappe", "Kante"}

france_union = chelsea_squad.union(france_squad)
print(france_union)
print("")
france_intersect = chelsea_squad.intersection(france_squad)
print(france_intersect)
print("")
# When there are no common elements, an empty set is returned.
chelsea_psg_intersect = chelsea_squad.intersection(psg_squad)
print(chelsea_psg_intersect)
print("")

# Difference of two sets.
chelsea_diff = chelsea_squad.difference(germany_squad)
print(chelsea_diff)
print("")
germany_diff = germany_squad.difference(chelsea_squad)
print(germany_diff)
print("")

# Symmetric Difference - Elements in A and B, but not elements present in both sets.
chelsea_symm_diff_a = chelsea_squad.symmetric_difference(germany_squad)
print(chelsea_symm_diff_a)
print("")
chelsea_symm_diff_b = germany_squad.symmetric_difference(chelsea_squad)
print(chelsea_symm_diff_b)
print("")

if chelsea_symm_diff_a == chelsea_symm_diff_b:
    print("Symmetric difference returns same results either ways.")
else:
    print("Symmetric difference does not return same results either ways.")
print("")

# Union, intersection and difference methods will not modify the original set. They will always return a new set.
# To modify a set in place, we have to use update() function.

manutd_squad = {"Ronaldo", "Bruno"}
spain_squad = {"De Gea"}
print("Before update: ", manutd_squad)
manutd_squad.update(spain_squad)
print("After update: ", manutd_squad)
print("")

# Intersection update: Updates the set by keeping only the element found in both sets.
best_midfielder = {"Kante", "De Bruyne"}
france_mid = {"Kante", "Pogba"}
print("Before intersection update: ", best_midfielder)
best_midfielder.intersection_update(france_mid)
print("After intersection update: ", best_midfielder)
print("")

# Difference update: Updates the set by removing elements found in another set.
best_forward = {"Havertz", "Ronaldo", "Kane", "Mbappe"}
epl_forwards = {"Havertz", "Ronaldo", "Kane"}
print("Before difference update: ", best_forward)
best_forward.difference_update(epl_forwards)
print("After difference update: ", best_forward)
print("")

# Symmetric difference update: Updates the set by only keeping the elements found in A and B, but not those which are found in both.
best_gk = {"Donnarumma", "Mendy", "Neuer"}
german_gk = {"Neuer"}
print("Before symmetric difference update: ", best_gk)
best_gk.symmetric_difference_update(german_gk)
print("After symmetric difference update: ", best_gk)
print("")