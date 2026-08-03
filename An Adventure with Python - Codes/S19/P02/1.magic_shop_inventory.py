import pandas as pd

# 1. Prepare data (Dictionary of Lists)
data = {
    "Item": ["Health Potion", "Mana Potion", "Iron Sword"],
    "Price": [50, 70, 150],
    "Stock": [10, 5, 2]
}

# 2. Create the DataFrame
df = pd.DataFrame(data)

print("--- My Magic Shop Inventory ---")
print(df)