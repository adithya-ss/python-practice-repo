# List slicing : [start_index:end_index:step]
# When start index is not specified, it starts all the way from the beginning.
# When the end index is not specified, it stops at the last item.
# Negetive indexes can be used.
# Step index can be used to skip those many items between one and the next.
 
number_list = list(range(1,10))
print("Numbers: ", number_list)
print("")

list_sliced = number_list[4:9]
print("List after slicing from original number list: ", list_sliced)
print("")

list_sliced_step = number_list[::3]
print("Step of 3: ", list_sliced_step)
print("")

# Print list in reverse using step index:
print("Reverse using step: ", number_list[::-1])
print("Original list: ", number_list)