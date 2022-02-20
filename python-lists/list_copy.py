# Copying lists:
# Assignment operators are using for storing original and copy in the same memory address.
org_list_a = [1,2,3,4,5]
print("Address of org list: ", id(org_list_a))
copy_list_a = org_list_a
print("Address of copy list: ", id(copy_list_a))
copy_list_a.append(10)
print("Original list: ", org_list_a)
print("Copy List: ", copy_list_a)
print("")

# To create on different memory location:
# 1. copy() 
# 2. list(original_list) 
# 3. original_list[:]
print("Address of org list: ", id(org_list_a))
copy_list_b = org_list_a.copy()
print("Address of copy list: ", id(copy_list_b))

if id(org_list_a) != id(copy_list_b):
    print("On different locations.")
else:
    print("Stored in same location.")