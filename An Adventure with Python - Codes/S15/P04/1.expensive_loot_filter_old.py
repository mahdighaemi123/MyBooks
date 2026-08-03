# The "Old" Way (from Chapter 5)
loot_prices = [100, 50, 20, 400, 30]
expensive_loot = []

for price in loot_prices:
    if price > 60:
        expensive_loot.append(price)

print(f"Old Way: {expensive_loot}")
