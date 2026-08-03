# The "Old" Way (using a full function)
leaderboard = [("Kael", 80), ("Aria", 100), ("Lyra", 75)]

# We need a helper function just for sorting


def get_score(entry):
    return entry[1]  # Returns the score


leaderboard.sort(key=get_score)
print(f"Sorted (Old): {leaderboard}")
