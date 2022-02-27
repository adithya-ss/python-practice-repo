# Lambda functions can also be used to invoke another function.

coordinates_list = [(4,7), (11,19), (42,18), (8,41), (10,15)]
sorted_coordinates = sorted(coordinates_list)
print("Default sorting...")
print(coordinates_list)
print(sorted_coordinates)
print("")

coordinates_list = [(4,7), (11,19), (42,18), (8,41), (10,15)]
sorted_coordinates = sorted(coordinates_list, key=lambda c: c[1])
print("Sorted based on y index...")
print(coordinates_list)
print(sorted_coordinates)
print("")

coordinates_list = [(4,7), (11,19), (42,18), (8,41), (10,15)]
sorted_coordinates = sorted(coordinates_list, key=lambda c: c[0] + c[1])
print("Sorted based sum of each coordinate...")
print(coordinates_list)
print(sorted_coordinates)