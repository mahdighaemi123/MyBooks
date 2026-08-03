import json

shopping_list = ["Apple", "Bread", "Milk"]

print("Saving list to file...")

# Open file in WRITE mode ("w")
with open("market.json", "w") as f:
    # Magic: Dump the list DIRECTLY into the file 'f'
    json.dump(shopping_list, f)

print("Saved successfully!")