# We found the loot
gold_coins_chest1 = 50
gold_coins_chest2 = 75
adventurers_count = 4
 
# --- Performing the magic of math ---
 
# 1. Add the loot from both chests
total_gold = gold_coins_chest1 + gold_coins_chest2
 
# 2. Divide the loot among the party members
gold_per_adventurer = total_gold / adventurers_count
 
# --- Displaying the results ---
print("Total gold found:")
print(total_gold) # Output: 125
 
print("Share per adventurer:")
print(gold_per_adventurer) # Output: 31.25