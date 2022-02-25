# groupby - Makes an iterator that returns keys and groups from a iterable.

from itertools import groupby

# -------------------------------------------------------------------
# Example 1: Number grouping
# -------------------------------------------------------------------

def smaller_than_thirty(num):
    return num < 30

list_a = [10,20,30,40]

group_obj = groupby(list_a, key=smaller_than_thirty)
# print(group_obj) # Returns an iterable.

lambda_obj = groupby(list_a, key=lambda num:num <30)
# print(lambda_obj) # Returns an iterable.

for key, value in group_obj:
    print(key, list(value))
print("")
for key, value in lambda_obj:
    print(key, list(value))

print("")
# -------------------------------------------------------------------
# Example 2: Working with group by on dictionaries
# -------------------------------------------------------------------

player_dict = [{'Name':'Robert Lewandowski', 'Position':'Forward'}, {'Name':'Kylian Mbappe', 'Position':'Forward'},
{'Name':'Ngolo Kante', 'Position':'Midfielder'}, {'Name':'Marco Reus', 'Position':'Midfielder'}, 
{'Name':'Thiago Silva', 'Position':'Defender'}, {'Name':'Sergio Ramos', 'Position':'Defender'}, 
{'Name':'Eduardo Mendy', 'Position':'Goalkeeper'}, {'Name':'Alisson', 'Position':'Goalkeeper'}]

# Group only midfielders
player_group = groupby(player_dict, key=lambda player : player['Position'] == 'Midfielder')
for key, value in player_group:
    print(key, list(value))