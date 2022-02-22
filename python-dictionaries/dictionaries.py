# Dictionaries are unordered and mutable.
# Consists of a collection of key-value pairs.
# Tuples can be used as keys. But keys should always be immutable.

player_details = {"Last Name":"James", "First Name":"LeBron", "Team":"Los Angeles Lakers", "Position":"Small Forward"}
print(player_details)
print("")

# Creating a copy using assignment operator.
# When this copy is modified, the original from which the copy was created also gets modified.
# Refer line number 60 inside this script.
player_details_copy = player_details
print(player_details_copy)
print("")

# With dict function to create dictionaries, we do not have to use quotes for keys.
team_coaches = dict(name="Pep Guardiola", team="Manchester City", league="Premier League")
print(team_coaches)
print("")

# Accessing values from a dictionary using keys.
player_fname = player_details["First Name"]
player_lname = player_details["Last Name"]
player_team = player_details["Team"]
player_position = player_details["Position"]
print("Name:", player_fname,player_lname, "(",player_position,")")
print("Team:", player_team)
print("")

# Adding new field into a dictionary.
team_coaches["Age"] = 51
print(team_coaches)
# If the same key is assigned a different value, it gets overwritten inside the dictionary.
print("")

# Deleting from dictionary.
del team_coaches["Age"]
print(team_coaches)
print("")

# Checking for values inside a dictionary
if "name" in team_coaches:
    print(team_coaches["name"])
else:
    print("Dictionary does not have any fields with name as key.")
print("")

# Checking for values using a try-except block
try:
    print(player_details["Team"])
except:
    print("Error. Dictionary does not have any fields with Team as key.")
print("")

try:
    print(player_details["Team Name"])
except:
    print("Error! Dictionary does not have any fields with Team Name as key.")
print("")

player_details_copy["Height"]="6ft9in"
print("Original: ", player_details)
print("Copied: ", player_details_copy)