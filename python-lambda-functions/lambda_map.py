# map(function, sequence)

list_a = [11,12,13,14,15]

# List comprehension
new_list = [each_num * 2 for each_num in list_a]
print("List comprehension...")
print(list_a)
print(new_list)
print("")

# Map function
list_b = map(lambda num:num * 2, list_a)
print("Map function...")
print(list_a)
print(list(list_b))