# Tuple - Ordered, immutable data type.
# Similar to lists, main difference being the immutable nature. Once created, can not be changed.
# Commonly used for objects that belong together.

phone_info = ("Apple", "iPhone11", 128, 6.3)
# Parenthesis are optional.
print(phone_info)

company = phone_info[0]
model = phone_info[1]
storage = phone_info[2]
screen_size = phone_info[3]

print("Company: ", company)
print("Model: ", model)
print("Storage in GB: ", storage)
print("Screen size in inches: ", screen_size)
print("")
# Negetive indexes can also be used, similar to lists

# Creating a tuple from iterable, for instance list.
pc_info = tuple(["Lenovo", "ThinkPad520", 1024, 15])
print(pc_info, " : ", type(pc_info))
for element in pc_info:
    print(element)

# Check if an element exists in a tuple.
if "Lenovo" in pc_info:
    print("Your PC is manufactured by Lenovo.")
else:
    print("Unknown pc data")