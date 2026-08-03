# A spell to make a potion with specific ingredients
def brew_potion(herb, liquid):
    print("Mixing " + herb + " with " + liquid + "...")

# Standard way (Order matters!):
brew_potion("Mint", "Water") 

# Keyword Arguments (Order doesn't matter, labels do!):
# We explicitly say which argument belongs to which parameter.
brew_potion(liquid="Dragon Blood", herb="Fire Flower")