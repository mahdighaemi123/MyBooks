import numpy as np

nums = np.array([1, 2, 3, 4, 5, 6])
# Filter only even numbers
evens = nums[nums % 2 == 0]
print(evens)
