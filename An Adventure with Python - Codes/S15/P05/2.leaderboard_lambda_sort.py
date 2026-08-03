# The "Pythonic" Way (using lambda)
leaderboard = [("Kael", 80), ("Aria", 100), ("Lyra", 75)]

# We create an anonymous function "on the fly"
leaderboard.sort(key=lambda entry: entry[1])  # Sort by the 2nd item (score)

print(f"Sorted (Pythonic): {leaderboard}")
