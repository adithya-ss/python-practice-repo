# JSON - JavaScript Object Notation
# Used for lightweight data exchange

# Python dictionary to JSON - Serialization / encoding.

import json

player = {"player_name":"John Terry", 
    "age":42, 
    "country": "United Kingdom",
    "clubs_played_for":["Chelsea FC", "Aston Villa FC"],
    "coach":True,
}

playerJSON = json.dumps(player, indent=4)
# seperators can also be specified using seperators=('; ', '= ')
# sort_keys=True will create the JSON by sorting the keys in asc order, alphabetically.
print("After converting to JSON:")
print(playerJSON)
print("")

with open('./python-json/player.json','w') as player_file:
    json.dump(player, player_file, indent=4)

# JSON to python dictionary - Deserialization / decoding.

player_dict = json.loads(playerJSON)
print("After converting to dictionary:")
print(player_dict)
print("")
