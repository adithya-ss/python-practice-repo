# deque = Double Ended Queue
# Add or remove elements from both ends.
# Stores elements as in a list.

from collections import deque

deque_a = deque()

# Add elements to the right.
deque_a.append(10)
deque_a.append(20)
deque_a.append(30)
deque_a.append(40)
deque_a.append(50)

print(deque_a)

# Add elements to the left.
deque_a.appendleft(5)
print(deque_a)

# Remove element from right.
deque_a.pop()
print(deque_a)

# Remove element from left.
deque_a.popleft()
print(deque_a)

# Multiple elements to the right.
deque_a.extend([50,60,70,80])
print(deque_a)

# Multiple elements to the left.
deque_a.extendleft([5,4,3,2,1])
print(deque_a)

# Make the last element as first element.
# deque_a.rotate(number_of_places)
# positive number for rotating to right
# negetive number for rotating to left.
deque_a.rotate()
print(deque_a)

deque_a.rotate(3)
print(deque_a)

deque_a.rotate(-4)
print(deque_a)