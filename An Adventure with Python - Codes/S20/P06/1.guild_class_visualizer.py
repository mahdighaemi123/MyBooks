# visualize_guild.py
# The Visual Report Generator

import pandas as pd
import matplotlib.pyplot as plt

print("--- Summoning Data & Painter ---")

# 1. Read the data (Ingredients)
# We assume 'adventurers.csv' exists from the previous chapter
df = pd.read_csv("adventurers.csv")

# --- MISSION 1: The Class Distribution (Pie Chart) ---

# Count how many adventurers are in each class
# This gives us something like: Warrior: 30, Mage: 25...
class_counts = df["Class"].value_counts()

# Create a new canvas (Size: 8x8)
plt.figure(figsize=(8, 8))

# Draw the Pie
# autopct='%1.1f%%' -> Shows the percentage on the chart
plt.pie(class_counts, labels=class_counts.index,
        autopct='%1.1f%%', startangle=140)

# Add Title
plt.title("Guild Class Distribution")

# Save the spell result
plt.savefig("guild_classes.png")
print("Saved 'guild_classes.png'")

# Show it to us
plt.show()


# --- MISSION 2: The Top 5 Elites (Bar Chart) ---

# Sort by score (Highest first) and take top 5
top_5 = df.sort_values(by="Score", ascending=False).head(5)

# Create a new canvas (Size: 10 wide, 6 tall)
plt.figure(figsize=(10, 6))

# Draw the Bars
# X axis = Names, Y axis = Scores
colors = ['gold', 'silver', 'brown', 'blue', 'green']
plt.bar(top_5["Name"], top_5["Score"], color=colors)

# Decorate the map (Labels)
plt.title("Top 5 Guild Members")
plt.xlabel("Adventurer Name")
plt.ylabel("Score (0-100)")

# Add a grid behind bars to read numbers easily
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the spell result
plt.savefig("top_5_elites.png")
print("Saved 'top_5_elites.png'")

# Show it
plt.show()
