# Deleting items from dictionary.

shoe_details = {"Brand" : "Nike", "Type":"Sneakers", "Size":"11", "Cost":"Rs. 3999", "Origin":"USA", "Year of Manufacture" : 2019}
print(shoe_details)
print("")

# Method 1 - pop - deletes the item with specified key.
shoe_details.pop("Year of Manufacture")
print(shoe_details)
print("")
# Method 2 - popitem - deletes the last inserted item.
shoe_details.popitem()
print(shoe_details)
print("")

# Making a copy
# Method 1 - Using dict function.
copy_a_shoes = dict(shoe_details)
copy_a_shoes["YOM"] = 2019
print(shoe_details)
print(copy_a_shoes)
print("")

# Method 2 - Using copy function.
copy_b_shoes = shoe_details.copy()
copy_b_shoes["Color"] = "Black"
print(shoe_details)
print(copy_b_shoes)
print("")

# Merging two dictionaries - update
# The key-value pairs get overwritten
f1_team_principals = {"Team":"McLaren F1 Racing", "Boss":"Zak Brown"}
print(f1_team_principals)
f1_team_principals_update = dict(Team="Alpine F1 Racing", Boss="Otmar Szafnauer", Engine="Renault")
f1_team_principals.update(f1_team_principals_update)
print(f1_team_principals)
