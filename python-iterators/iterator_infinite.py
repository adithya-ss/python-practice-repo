from itertools import count, cycle, repeat
from operator import le

# Infinite loop starting from 5, adds 1 for each iteration.
for number in count(5):
    print(number)
    # Stop infinite loop on this condition.
    if number > 12:
        break

# repeat
name = "Mourinho"
for letter in repeat('M', 3):
    print(letter)
print("")

# cycle: Cycle infinitely through an iterable.
list_a = [10,20,30]
# for num in cycle(list_a):
#     print(num)

# How to stop a cycle? How to keep track of iterations.
iter_rep = 0
iter_start = 0
iter_end = len(list_a)
  
for number in cycle(list_a):
    if(iter_start == 0):
        pass

    print(number, end =" ")

    if(iter_start == iter_end-1):
          
        if(iter_rep>= 2):
            break
        else:
            iter_rep+= 1
            iter_start = 0
            print("\n")
    else:
        iter_start+= 1