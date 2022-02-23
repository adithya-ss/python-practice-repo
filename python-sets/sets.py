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

