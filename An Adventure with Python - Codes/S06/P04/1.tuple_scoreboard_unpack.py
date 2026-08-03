# Our High Score board
# It's a LIST (backpack) containing Tuples (sealed records)
high_scores = [
    ("Aria", 100),
    ("Kael", 80),
    ("Lyra", 75),
    ("Zane", 60),
    ("Finn", 30)
]

print("--- All Scores (unpacked) ---")
 
# Instead of: for entry in high_scores:
# We write:   for name, score in high_scores:
# Python unpacks each tuple (like '("Aria", 100)')
# into 'name' and 'score' in each loop.
for name, score in high_scores:
    # Now we use str() to join text and numbers (from Chapter 4)
    print(name + " scored " + str(score) + " points")