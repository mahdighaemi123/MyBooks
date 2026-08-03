# Our list of adventurers
adventurers = ["Aria", "Kael", "Lyra", "Zane", "Finn", "Bora"]

# 1. The Standard Slice (Start to End)
# Get from index 1 up to (but not including) 4
team_alpha = adventurers[1:4]
print("Team Alpha:", team_alpha)
# Output: ['Kael', 'Lyra', 'Zane']

# 2. The Shortcut Magic (Leaving blank)
# Empty start = Start from 0
first_three = adventurers[:3]
print("First Three:", first_three)
# Output: ['Aria', 'Kael', 'Lyra']

# Empty end = Go to the very end
from_third_onwards = adventurers[2:]
print("From Lyra to End:", from_third_onwards)
# Output: ['Lyra', 'Zane', 'Finn', 'Bora']

# 3. The Jump Spell (Step = 2)
# Start from 0, go to end, take every 2nd person
odd_team = adventurers[::2]
print("Odd Team:", odd_team)
# Output: ['Aria', 'Lyra', 'Finn'] (Index 0, 2, 4)

# 4. The Time Reversal Spell (Reversing a list)
# Start from end, go to start, step -1
reversed_team = adventurers[::-1]
  
print("Reversed Team:", reversed_team)
# Output: ['Bora', 'Finn', 'Zane', 'Lyra', 'Kael', 'Aria']
