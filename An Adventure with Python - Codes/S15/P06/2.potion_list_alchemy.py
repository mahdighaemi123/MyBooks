# --- The List Alchemy ---

# 1. Our inventory of potions (The Raw Material)
potions = [
    {"name": "Lesser Healing", "type": "Heal", "price": 50},
    {"name": "Mana Potion", "type": "Mana", "price": 70},
    {"name": "Greater Healing", "type": "Heal", "price": 150},
    {"name": "Invisibility", "type": "Stealth", "price": 200}
]

# 2. --- The Apprentice's Way (Slow & Steady) ---
# He creates an empty list, walks to the shelf, checks one by one...
print("Apprentice's Result:")
healing_potion_names = []
for potion in potions:
    if potion["type"] == "Heal":
        name_upper = potion["name"].upper()
        healing_potion_names.append(name_upper)

print(healing_potion_names)

print("-" * 20)

# 3. --- The Master's Way (List Comprehension) ---
# ONE powerful line to do everything at once!
print("Master's Result:")

# Structure: [ TRANSFORM  for ITEM in LIST  if CONDITION ]
healing_potion_names = [
    potion["name"].upper()        # 1. What we want (The Transformation)
    for potion in potions         # 2. Where we look (The Iteration)
    if potion["type"] == "Heal"   # 3. The Filter condition
]

print(healing_potion_names)
