import pandas as pd

df = pd.read_csv("adventurers.csv")

df.info()     # Check column types
df.describe() # Check statistics
