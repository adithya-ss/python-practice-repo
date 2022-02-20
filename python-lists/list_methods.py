smartphone_manufacturers = ["Apple", "Samsung", "Google", "Sony", "Realme"]
football_teams = ["Chelsea", "Manchester United", "Liverpool", "West Ham"]

# Number of items in list
print("Number of teams in list: ", len(football_teams))
print("")

# Insert item at specific index.
# - When an item is inserted at specific index, the older items shift one index upward.
#   So when an item is inserted at index 2, old item at index 2 shifts to 3, old item at index 3 shifts to 4 etc.
print("Org football teams list: ", football_teams)
football_teams.insert(2, "PSG")
print("Updated list: ", football_teams)
print("")

# Remove last item in list - pop()
# Can be assigned to variables also.
football_teams.pop()
print("Updated list after pop: ", football_teams)
football_teams.append("Manchester City")
print("Updated list: ", football_teams)
remove_team = football_teams.pop()
print("Removing ", remove_team, "...")
print("Updated list after pop again: ", football_teams)
print("")

# Remove a specific element - remove()
# Providing index will not work. Have to provide the item.
smartphone_manufacturers.remove("Sony")
print("Smartphone manufacturers after remove: ", smartphone_manufacturers)
print("")

# Remove all elements - clear()
# smartphone_manufacturers.clear()

# Reverse the items in list.
smartphone_manufacturers.reverse()
print("Reversed smartphone manufactureres: ", smartphone_manufacturers)
print("")

# Sorting a list
num_list = [10,2,1,18,67,45,23,12]
print("Before sorting: ", num_list)
num_list.sort()
print("After sorting: ", num_list)
print("")