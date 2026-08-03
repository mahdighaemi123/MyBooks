import pandas as pd

df = pd.read_csv("adventurers.csv")

# Sort by Age (Ascending)
sorted_df = df.sort_values(by="Age")
print(sorted_df)