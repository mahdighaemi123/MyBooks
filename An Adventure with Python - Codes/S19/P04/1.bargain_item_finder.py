import pandas as pd
df = pd.read_excel("items.xlsx")

# Filter: Find items cheaper than 60 gold
cheap_items = df[df["Price"] < 60]

print("\n--- Bargain Bin (< 60 Gold) ---")
print(cheap_items)
