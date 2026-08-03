import numpy as np

# Old way
numbers = [1, 2, 3]
doubled = []
for x in numbers:
    doubled.append(x * 2)

# NumPy way
arr = np.array([1, 2, 3])
doubled = arr * 2  # Magic! No loop needed.

print(doubled)  # Output: [2 4 6]
