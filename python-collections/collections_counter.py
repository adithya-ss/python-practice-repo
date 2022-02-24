# Collections module implements special container data type.
# Provides additional functionalities compared to lists, tuples and dictionaries.

# Collections - Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter - Stores the elements as dictionary keys and thier counts as dictionary values.
from collections import Counter

sample_string = "HakunaMatata"
new_counter = Counter(sample_string)

# A dictionary of elements with its count values.
print(new_counter)

# A tuple of elements with its count values.
print(new_counter.items())

# Unique elements, in other words, the keys of the dicrionary.
print(new_counter.keys())

# Count values from the dictionary.
print(new_counter.values())

# Return an iterable of all the elements/keys.
print(list(new_counter.elements()))
print("")

# Get the most common element(s) with count.
print("Most common element with count: ", new_counter.most_common(1))
print("Two most common elements with count: ", new_counter.most_common(2))
print("")

# Get the most common element(s) only.
print("Most common element without count: ", new_counter.most_common(1)[0][0])
print("")