import pandas as pd

df = pd.read_csv("adventurers.csv")

print(df.head(5)) # Top 5 rows
print(df.tail(5)) # Bottom 5 rows
