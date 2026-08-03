import numpy as np

# 1
# Create numbers from 0 to 9
seq = np.arange(10) 
print(seq) # [0 1 2 3 4 5 6 7 8 9]

# 2
# Create a 3x3 matrix of zeros
zeros = np.zeros((3, 3))
print(zeros)

# 3
# 5 random numbers between 1 and 100
lucky_numbers = np.random.randint(1, 100, 5)
print(lucky_numbers)

# 4
arr = np.arange(12) # 0 to 11 (12 items)
# Change to 3 rows, 4 columns
matrix = arr.reshape(3, 4)

# 5
scores = np.array([10, 50, 90, 20])
print(f"Max Score: {np.max(scores)}") # 90
print(f"Total Score: {np.sum(scores)}") # 170

# 6
print(f"Average Score: {np.mean(scores)}")

# 7
sorted_scores = np.sort(scores)
print(sorted_scores) # [10 20 50 90]

# 8
items = np.array(["Sword", "Shield", "Sword", "Potion"])
print(np.unique(items)) # ['Potion' 'Shield' 'Sword']

# 9
# Find all scores greater than 40
high_scores = scores[scores > 40] 
print(high_scores) # [50 90]

# 10
a = np.array([1, 2])
b = np.array([3, 4])
c = np.concatenate((a, b))
print(c) # [1 2 3 4]