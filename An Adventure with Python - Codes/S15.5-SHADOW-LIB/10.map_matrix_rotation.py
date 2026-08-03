map_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Nested List Comprehension to swap rows and columns
rotated = [[row[i] for row in map_matrix] for i in range(len(map_matrix[0]))]

print(rotated)
