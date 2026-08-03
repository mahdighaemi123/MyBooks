# --- The High Score Board ---

# 1. Setup the data
# We use a LIST of TUPLES.
# Each tuple is (Name, Score) and creates a solid, unchangeable pair.
high_scores = [
    ("Aria", 100),
    ("Kael", 80),
    ("Lyra", 75),
    ("Zane", 60),
    ("Finn", 30)
]

print("--- All Scores ---")

# 2. Display all scores using "Tuple Unpacking"
# Instead of getting one item, we get "name" and "score" directly!
for name, score in high_scores:
    # Remember to convert score (int) to string (str) for printing
    print(name + " scored " + str(score) + " points")

print("")  # An empty print() adds a blank line for better look
print("--- TOP 3 CHAMPIONS ---")

# 3. Get the Top 3 using "Slicing"
# Logic: Start at index 0, Stop BEFORE index 3 (so we get 0, 1, 2)
top_3_list = high_scores[0:3]

# 4. Display the Top 3 with ranking
rank = 1  # We start ranking from 1

for name, score in top_3_list:
    # We print the Rank, Name, and Score all together
    print(str(rank) + ". " + name + " scored " + str(score) + " points")

    # Increase rank for the next champion
    rank = rank + 1
