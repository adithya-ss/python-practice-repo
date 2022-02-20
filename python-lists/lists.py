# Lists:
#   - Ordered and mutable (can be modified/changed) data structures. 
#   - Allows duplicate elements.
#   - Allows storing of multiple data types.

smartphone_manufacturers = ["Apple", "Samsung", "Google", "Sony", "Realme"]
print(smartphone_manufacturers)
print("")

# Creating an empty list and appending items.
football_teams = list()
print(football_teams)
football_teams.append("Chelsea")
football_teams.append("Dortmund")
football_teams.append("Milan")
print(football_teams)
print("")

# Indexes
print("First: " + football_teams[0])
print("Second: " + football_teams[1])
print("Third: " + football_teams[2])
print("")

# Negetive indexes
print("Last: " + football_teams[-1])
print("Second last: " + football_teams[-2])
print("Third last: " + football_teams[-3])
print("")

# Iterating through a list
for item in football_teams:
    print("Item: ", item)
print("")

# Check if an item is present in list.
if "Chelsea" in smartphone_manufacturers:
    print("Chelsea has joined the smartphone manufacturing game!")
else:
    print("Chelsea is not a smartphone manufacturer... Yet.")

print("")

# Concatinating lists
list_a = [1] * 5
list_b = [2] * 5
print("Concat: ", list_a + list_b)
print("")
