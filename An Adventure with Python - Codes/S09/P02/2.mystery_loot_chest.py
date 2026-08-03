import random

# A chest of possible loot
loot_options = ["Gold Coin", "Health Potion", "Rusty Dagger", "Diamond"]

# Use the 'choice' tool to pick ONE item blindly
found_item = random.choice(loot_options)

print("You opened the chest and found a...")
print(found_item)

# Try running this multiple times!