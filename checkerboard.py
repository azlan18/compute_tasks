import numpy as np

# Create an 8x8 matrix filled with zeros
checkerboard_matrix = np.zeros((8, 8), dtype=int)

# Fill the matrix with a checkerboard pattern (alternating 0s and 1s)
checkerboard_matrix[1::2, ::2] = 1  # Rows starting from 1, alternate columns starting from 0
checkerboard_matrix[::2, 1::2] = 1  # Rows starting from 0, alternate columns starting from 1

# Print the checkerboard matrix
print("Checkerboard Matrix:")
print(checkerboard_matrix)
