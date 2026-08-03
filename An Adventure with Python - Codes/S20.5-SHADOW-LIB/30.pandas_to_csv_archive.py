import pandas as pd

df = pd.read_csv("adventurers.csv")

# Save the modified dataframe to a new file
df.to_csv("final_report.csv", index=False)
