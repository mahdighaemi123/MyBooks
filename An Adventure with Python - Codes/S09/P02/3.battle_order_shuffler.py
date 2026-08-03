import random

# A list of party members
party = ["Aria", "Kael", "Lyra", "Zane"]

print("Original order:")
print(party)

# Shuffle the list in-place (Changes the 'party' list directly)
random.shuffle(party)

print("New battle order:")
print(party)