adventurers = ["Aria", "Kael", "Lyra"]
scores = [100, 80, 75]
# The "Pythonic" Way
print("Leaderboard (Pythonic):")

# zip creates pairs: ("Aria", 100), ("Kael", 80), ...
for name, score in zip(adventurers, scores):
    print(f"{name}: {score}")
