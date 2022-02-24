# Dictionary which remembers the order.
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict["One"] = 1
ordered_dict["Two"] = 2
ordered_dict["Three"] = 3
ordered_dict["Four"] = 4
ordered_dict["Five"] = 5

# List of tuples
print(ordered_dict)
print("")

unordered_dict = dict()
unordered_dict["One"] = 1
unordered_dict["Two"] = 2
unordered_dict["Three"] = 3
unordered_dict["Four"] = 4
unordered_dict["Five"] = 5

# Order would not have been saved, for python versions older than 3.7
# Python 3.7 got built in ordered dictionary.
print(unordered_dict)
print("")