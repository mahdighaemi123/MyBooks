import pandas as pd

df = pd.read_csv("adventurers.csv")

# Count how many people are in each city
print(df["City"].value_counts())