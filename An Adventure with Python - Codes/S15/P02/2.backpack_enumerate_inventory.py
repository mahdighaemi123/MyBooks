# The "Pythonic" Way
backpack = ["Sword", "Shield", "Health Potion"]
print("Backpack Inventory (Pythonic):")

# enumerate gives us (index, item) pairs
# We use tuple unpacking to catch them! 
for index, item in enumerate(backpack):
    print(f"{index}: {item}")