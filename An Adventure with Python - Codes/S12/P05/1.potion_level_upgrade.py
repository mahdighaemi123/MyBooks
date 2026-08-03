class Potion:
    pass


# 4. Changing Attributes
my_potion = Potion()
my_potion.level = 1  # Starting level

print(f"Level before upgrade: {my_potion.level}")

# Magic upgrade! Something happened in the game...
my_potion.level = 2  # We overwrite the old value
print(f"Level after upgrade: {my_potion.level}")
