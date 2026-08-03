# potions.py
# This module only contains the blueprints (classes)
# for magical items.

class Potion:
    """
    A blueprint for a magical potion in the shop.
    """

    # 1. The Constructor Spell
    def __init__(self, name, price, effect):
        # 2. The Attributes
        self.name = name
        self.price = price
        self.effect = effect

     # 3. The Behavior (Method)
    def display_info(self):
        """Prints the potion's stats neatly."""
        print(f"--- {self.name} ---")
        print(f"  Effect: {self.effect}")
        print(f"  Price: {self.price} Gold")
        print("==========================")
