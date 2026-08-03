import pandas as pd

df = pd.read_csv("adventurers.csv")

names = df["Name"]
print(names)
