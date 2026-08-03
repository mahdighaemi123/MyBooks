# analyze_scores.py
# The Pandas Analysis Tool

import pandas as pd

print("--- Loading the Ancient Scroll (CSV) ---")

# 1. Read the file (Import Data)
# This loads the CSV into a DataFrame called 'df'
df = pd.read_csv("adventurers.csv")

# Show the first 5 rows just to peek at the data
print("First 5 adventurers:")
print(df.head())
print("-" * 40)


# 2. Statistical Magic
# Calculate the average of the "Score" column
average_score = df["Score"].mean()
print(f"Average Guild Score: {average_score:.2f}")

# Count how many adventurers are in each Class
print("\nClass Distribution:")
print(df["Class"].value_counts())


# 3. Filtering the Elites
# We want only rows where Score is greater than 85
print("\n--- Searching for Elites (Score > 85) ---")

elites = df[df["Score"] > 85]

# Sort them by Score (Highest score on top)
elites_sorted = elites.sort_values(by="Score", ascending=False)

print(f"Found {len(elites_sorted)} elite adventurers.")
print(elites_sorted.head()) # Show top 5 elites


# 4. Saving the Result
print("\n--- Saving the Elite List ---")
# index=False means we don't save the row numbers (0, 1, 2...)
elites_sorted.to_csv("elites.csv", index=False)
print("Saved to 'elites.csv'. Mission Complete!")
