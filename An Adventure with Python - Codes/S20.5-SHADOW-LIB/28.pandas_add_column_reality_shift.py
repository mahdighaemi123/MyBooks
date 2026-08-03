import pandas as pd

df = pd.read_csv("adventurers.csv")

# Create new column based on math
df["Level_Up_Gold"] = df["Gold"] * 10
print(df)