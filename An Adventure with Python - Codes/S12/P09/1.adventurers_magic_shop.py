# --- The Adventurer's Magic Shop ---

# 1. --- The Blueprint (Class) ---
# This is not a potion yet. It's the RECIPE for making potions.
class Potion:
    
    # 2. --- The Constructor (__init__) ---
    # This runs automatically when we create a new Potion()
    # 'self' means: "The specific object being created right now"
    def __init__(self, name, price, effect):
        # 3. --- The Attributes (Data) ---
        # We attach data to the object using 'self.'
        self.name = name
        self.price = price
        self.effect = effect
        
    # 4. --- The Behavior (Method) ---
    # A function inside a class is called a "Method"
    def display_info(self):
        print(f"--- {self.name} ---")
        print(f"Effect: {self.effect}")
        print(f"Price:  {self.price} gold")
        print("==========================")

# 5. --- Create the Shop's Stock (List) ---
magic_shop_stock = []

print("Brewing new potions for the shop...")

# 6. --- Create Beings (Objects) ---
# Now we use the Class (Blueprint) to make REAL objects
health_potion = Potion("Health Potion", 50, "Heals 25 HP")
mana_potion = Potion("Mana Potion", 70, "Restores 50 MP")
invisibility_potion = Potion("Invisibility Elixir", 300, "Grants 30s invisibility")

# 7. --- Fill the Shelves ---
# Add our new objects to the list
magic_shop_stock.append(health_potion)
magic_shop_stock.append(mana_potion)
magic_shop_stock.append(invisibility_potion)

print("") 
print("WELCOME TO THE MAGIC SHOP!")

# 8. --- Open the Shop (Loop) ---
for potion in magic_shop_stock:
    # We ask EACH potion object to display its own info
    potion.display_info()