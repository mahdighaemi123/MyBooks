# The "Pythonic" Way (List Comprehension)
loot_prices = [100, 50, 20, 400, 30]

expensive_loot = [price for price in loot_prices if price > 60]

print(f"Pythonic Way: {expensive_loot}")

# Transformation with List Comprehension
doubled_prices = [price * 2 for price in loot_prices]
print(f"Doubled Prices: {doubled_prices}")
