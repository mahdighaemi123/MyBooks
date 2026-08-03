import json
print("Loading list from file...")

# Open file in READ mode ("r")
with open("market.json", "r") as f:
    # Magic: Read from file 'f' and convert back to Python List
    loaded_data = json.load(f)

print("List restored:")
print(loaded_data)      # Output: ['Apple', 'Bread', 'Milk']
print(loaded_data[1])   # Output: Bread