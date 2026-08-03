import pandas as pd
df = pd.read_excel("items.xlsx")

# 1
print(df.head(2))  # Show first 2 rows

# 2
df.info()

# 3
print(df.describe())

# 4
print(df.columns)  # Index(['Item', 'Price', 'Stock'], dtype='object')

# 5
print(df.shape)  # (4, 3) -> 4 rows, 3 columns

# 6
# Sort by Price (High to Low)
sorted_df = df.sort_values(by="Price", ascending=False)

# 7
avg_price = df["Price"].mean()

# 8
df.to_csv("new_inventory.csv", index=False)

# 9
# Row 0, Column 0
item_name = df.iloc[0, 0]  # "Health Potion"

# 10
# Calculate total value (Price * Stock)
df["Total Value"] = df["Price"] * df["Stock"]