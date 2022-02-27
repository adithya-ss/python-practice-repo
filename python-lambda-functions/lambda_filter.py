# filter(function, sequence)
# Returns true/false.
# Return elements for which function evaluates to true.

# List Comprehension
print("Using list comprehension...")
list_a = [14,18,19,21,26,31]
list_odd_bool = [num % 2 != 0 for num in list_a]
list_odd = [num for num in list_a if num % 2 != 0]
print("Org list: ",list_a)
print("Odd numbers: ",list_odd_bool)
print("Odd numbers: ",list_odd)

# Filter function
list_a = [14,18,19,21,26,31]
# Print odd numbers only.
list_odd = filter(lambda num : num % 2 != 0, list_a)
print("Using filter function...")
print("Org list: ",list_a)
print("Odd numbers: ", list(list_odd))