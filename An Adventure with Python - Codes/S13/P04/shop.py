# shop.py
# The main application for our magic shop.

# 1. Summon the blueprint from our other file
# We import the Potion class directly from the potions.py file
from potions import Potion

print("--- Welcome to the Adventurer's Magic Shop! ---")
print("Stocking the shelves...")

# 2. Create the shop's inventory (a list)
magic_shop_stock = []

# 3. Create the beings (Objects) from the blueprint
health_potion = Potion(name="Health Potion", price=50, effect="+25 HP")
mana_potion = Potion(name="Mana Potion", price=70, effect="+50 MP")
strength_potion = Potion(name="Potion of Strength",
                         price=150, effect="+5 Strength for 3 min")

# 4. Fill the shelves
magic_shop_stock.append(health_potion)
magic_shop_stock.append(mana_potion)
magic_shop_stock.append(strength_potion)

print("--- Today's Wares ---")

# 5. Open the shop and display the items
for item in magic_shop_stock:
    # We call the display_info() method on EACH potion object
    item.display_info()
