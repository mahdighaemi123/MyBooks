import pandas as pd

df = pd.read_csv("adventurers.csv")

# Show rows where Gold is greater than 500
rich = df[df["Gold"] > 500]
print(rich)