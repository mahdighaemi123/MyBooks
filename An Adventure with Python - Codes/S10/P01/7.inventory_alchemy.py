# 1. Your inventory with weak items
inventory = "Rusty Sword, Rusty Shield, Rusty Armor"
 
# 2. The Alchemy Spell: Change ALL "Rusty" to "Golden"
# Input 1: Old text (What to find)
# Input 2: New text (What to replace with)
upgraded_inventory = inventory.replace("Rusty", "Golden")
 
print(upgraded_inventory)
# Output: "Golden Sword, Golden Shield, Golden Armor"