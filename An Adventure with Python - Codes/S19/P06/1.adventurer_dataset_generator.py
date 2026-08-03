# create_data.py
import pandas as pd
import numpy as np

# 1. Create dummy data using NumPy magic
# Create 100 names like "Adventurer_1", "Adventurer_2"...
names = [f"Adventurer_{i}" for i in range(1, 101)]

# Randomly choose classes for 100 people
classes = np.random.choice(["Mage", "Warrior", "Rogue", "Healer"], 100)

# Generate random scores between 50 and 100
scores = np.random.randint(50, 100, 100)

# 2. Create DataFrame (The Table)
df = pd.DataFrame({
    "Name": names,
    "Class": classes,
    "Score": scores
})

# 3. Save to CSV
df.to_csv("adventurers.csv", index=False)
print("File 'adventurers.csv' created successfully!")
