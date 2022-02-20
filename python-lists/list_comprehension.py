list_numbers = list(range(1,20,2))

# Create a new list of square numbers from original list.
squared_numbers = [num*num for num in list_numbers]
print("ORG: ", list_numbers)
print("Squared: ", squared_numbers)

# Syntax for list comprehension
# [(1)expression (2)for in loop]