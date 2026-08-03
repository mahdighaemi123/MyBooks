import json

# 1. A Python List (It is ALIVE, we can edit it)
my_list = ["Sword", "Shield", 100, True, None]

# 2. Convert to JSON String (Freezing it into text)
# dumps = Dump String
json_string = json.dumps(my_list)

print("--- JSON String ---")
print(json_string)       
# Output: ["Sword", "Shield", 100, true, null]
# Notice: True -> true, None -> null, Quotes are double ("")

print(type(json_string)) 
# Output: <class 'str'> (It is just text now!)