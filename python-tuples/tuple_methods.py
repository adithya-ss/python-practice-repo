user_details = ("Scott", "Micheal", "Dunder Mifflin Paper Company", "General Manager", 16, 40, "Scranton")

# Length of a tuple:
print("Number of fields in user_details tuple: ", len(user_details))
print("")

# Number of occurrances of a perticular data item inside tuple.
print("Number of times first name is mentioned: ", user_details.count("Micheal"))
print("")

# Get the index of an element - First occurrance.
print("Last name is present at index: ", user_details.index("Scott"))
print("")

# Convert tuple into a list.
print("Old type: ", type(user_details))
print(user_details)
user_details = list(user_details)
print("New type: ", type(user_details))
print(user_details)
print("")

print("Old type: ", type(user_details))
print(user_details)
user_details = tuple(user_details)
print("New type: ", type(user_details))
print(user_details)
print("")

