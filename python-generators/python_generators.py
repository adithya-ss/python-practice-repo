# Generators:
    # - Do not hold the entire result in memory
    # - It yields one result at a time.
    # - We would recieve a StopIteration exception, once the limit has been reached. That is, when the generator is exhausted.
    # - More readable compared to storing result in a seperate list.
    # - Better in performance, compared to a list. Generators use less memory and execution time.

# Without Generators:
# def square_numbers(nums):
#     result = []
#     for each_num in nums:
#         result.append(each_num*each_num)
#     return result

# With Generators:
from types import new_class


def square_numbers(nums):
    for each_num in nums:
        yield(each_num*each_num)

num_list = square_numbers([1,2,3,4,5,6,7,8,9])

# print(num_list)
# print(next(num_list))
# print(next(num_list))
# print(next(num_list))
# print(next(num_list))

for num in num_list:
    print(num)

# Using List comprehension
# numbers_list = [no*no for no in list(range(0,9))]
numbers_list = (no*no for no in list(range(0,9)))
print(numbers_list)
# print (list(numbers_list))
for each_num in numbers_list:
    print(each_num)