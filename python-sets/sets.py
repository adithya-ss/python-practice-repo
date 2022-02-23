# Sets:
# Mutable, but does not allow duplicate elements.
# Unordered - Arbitary order.

# Data is surrounded by curly brackets, but does not have a key-value mapping.

# Creating a set
set_new_a = {10,20,30,40,50,40,30,20,10}
# When this is printed, all duplicates are ignored.
print(set_new_a)
print("")

# Creating using set function.
set_new_b = set(["Apple", "Mango", "Banana", "Watermelon", "Banana"])
print(set_new_b)
print("")

# When a string is passed as argument to the set function, each character is considered as an individual set item.
set_new_str = set("Python")
print(set_new_str)
print("")

unique_char_cnt = set("HakunaMatata")
print(unique_char_cnt)
print("Number of unique characters: ", len(unique_char_cnt))
print("")

# An empty set can be created only with the set() function. 
# set_ex = {} will result in the creation of a dictionary.

# Iterate through the set.
for elem in set_new_b:
    print(elem)
print("")

# Check if element is present in set.
if "Jackfruit" in set_new_b:
    print("Jackfruit found.")
else:
    print("Jackfruit not found.")
print("")

set_a = {10,20,30}
print("Is set_new_a, a subset of set_a? ", set_new_a.issubset(set_a))
print("Is set_a, a subset of set_new_a? ", set_a.issubset(set_new_a))
print("")

print("Is set_new_a, a superset of set_a? ", set_new_a.issuperset(set_a))
print("Is set_a, a superset of set_new_a? ", set_a.issuperset(set_new_a))
print("")

set_z = {90,100}
print("Is set_new_a, a superset of set_a? ", set_new_a.isdisjoint(set_a))
print("Is set_a, a superset of set_new_a? ", set_a.isdisjoint(set_z))
print("")

# Copying of sets is similar to copying lists.
indian_states = {"Karnataka", "Himachal Pradesh", "Kashmir"}
ind_states_cp = indian_states
print("Before change: ", indian_states, "; ", ind_states_cp)
ind_states_cp.add("Kerala")
print("After update: ", indian_states, "; ", ind_states_cp)
print("")

indian_states = {"Karnataka", "Himachal Pradesh", "Kashmir"}
ind_states_cp = set(indian_states)
print("Before change: ", indian_states, "; ", ind_states_cp)
ind_states_cp.add("Kerala")
print("After update: ", indian_states, "; ", ind_states_cp)
print("")

indian_states = {"Karnataka", "Himachal Pradesh", "Kashmir"}
ind_states_cp = indian_states.copy()
print("Before change: ", indian_states, "; ", ind_states_cp)
ind_states_cp.add("Kerala")
print("After update: ", indian_states, "; ", ind_states_cp)
print("")