team_coaches = dict(name="Thomas Tuchel", team="Chelsea", league="Premier League")

# Method 1 - Using for in loop - Prints only keys.
for key in team_coaches:
    print(key)

print("")

# Method 2 - Using for in .keys - Prints only keys.
for each_key in team_coaches.keys():
    print(each_key)

print("")

# Method 3 - Using values - Prints only values.
for each_value in team_coaches.values():
    print(each_value)

print("")

# Method 4 - Using key-value pair - Prints both key and value.
for key, value in team_coaches.items():
    print(key, ":", value)

print("")
