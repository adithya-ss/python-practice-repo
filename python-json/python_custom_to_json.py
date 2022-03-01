import json

class Player:
    def __init__(self, name, age, team):
        self.name = name
        self.age = age
        self.team = team

new_player = Player("Eden Hazard", 31, "Real Madrid") 

# Method 1: Write a custom encoding function
def encode_player_to_json(obj):
    if isinstance(obj, Player):
        return {'player_name':obj.name, 'age':obj.age, 'team':obj.team, obj.__class__.__name__:True}
    else:
        raise TypeError("Object of type Player is not JSON serializable.")

# Method 2: Write a custom JSON encoder.
from json import JSONEncoder
class PlayerEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Player):
            return {'player_name':obj.name, 'age':obj.age, 'team':obj.team, obj.__class__.__name__:True}
        # Handle through base JSON encoder. 
        return JSONEncoder.default(self, obj)

print("Method 1: Write a custom encoding function")
newPlayerJSON = json.dumps(new_player, default=encode_player_to_json, indent=4)
print(newPlayerJSON)

print("")
print("Method 2: Write a custom JSON encoder.")
newPlayerJSON = json.dumps(new_player, cls=PlayerEncoder, indent=4)
print(newPlayerJSON)

# Method 3: Use the encoder directly.
print("")
print("Method 3: Use the encoder directly.")
newPlayerJSON = PlayerEncoder().encode(new_player)
print(newPlayerJSON)

# Decoding into a dictionary.
print("")
print("Decoding : Converting into a dictionary...")
player_dict = json.loads(newPlayerJSON)
print(type(player_dict), " : ", player_dict)

# Decode into a custom object.
def decode_player(dct):
    if Player.__name__ in dct:
        return Player(name=dct['player_name'], age=dct['age'], team=dct['team'])
    # Simply return a dictionary. Decoded into a dictionary, instead of the object type.
    return dct 

# Decoding into a custom object.
print("")
print("Decoding : Converting into a custom object type...")
player_dict = json.loads(newPlayerJSON, object_hook=decode_player)
print("Name: ",player_dict.name)
print("Age: ",player_dict.age)
print("Team: ",player_dict.team)