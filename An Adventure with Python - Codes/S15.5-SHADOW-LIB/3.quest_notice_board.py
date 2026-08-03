quests = ["Save Village", "Find Sword", "Defeat Boss"]

# Enumerate allows us to get the index and item together
for index, quest in enumerate(quests, 1):
    print(f"{index}. {quest}")
