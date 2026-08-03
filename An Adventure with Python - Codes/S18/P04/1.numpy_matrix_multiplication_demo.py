import numpy as np

# Creating a 2x3 Matrix (2 rows, 3 columns)
matrix_a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("--- Matrix A ---")
print(matrix_a)
print(f"Shape: {matrix_a.shape}")  # Output: (2, 3)

matrix_b = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

# Multiplying Matrix A (2x3) by Matrix B (3x2)
# Result will be a 2x2 Matrix
result = np.dot(matrix_a, matrix_b)
# Or simply: result = matrix_a @ matrix_b

print("--- Matrix Multiplication Result ---")
print(result)
