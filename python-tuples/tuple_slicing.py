number_tuple = tuple(range(1,20,2))
print(type(number_tuple), " : ", number_tuple)
print("")

# Syntax: [start:end:step]
# End index is non-inclusive.
# When start index is not specified, it starts all the way from the beginning.
# When the end index is not specified, it stops at the last item.
# Negetive indexes can be used.
# Step index can be used to skip those many items between one and the next.

print("Print second to fifth elements", number_tuple[1:5])
print("")

print("Starting to end, skip every second element: ", number_tuple[::2])
print("")

# Print list in reverse using negetive step index:
print("Reverse using step: ", number_tuple[::-1])
print("Original tuple: ", number_tuple)
print("")

# Unpacking a tuple.
l_name, f_name, company, designation, exp, age, branch_name = ("Scott", "Micheal", "Dunder Mifflin Paper Company", "General Manager", 16, 40, "Scranton")
print("First name: ", f_name)
print("Last name: ", l_name)
print("Age: ", age)
print("Designation: ", designation)
print("Company name: ", company)
print("Branch name: ", branch_name)
print("Years of experience: ", exp)
print("")

# Unpack multiple elements
tuple_unpack = (10,20,30,40,50)
num1, num2, *num3 = tuple_unpack
print(num1)
print(num2)
print(num3)
print("")
# * is converted into a list of items.
