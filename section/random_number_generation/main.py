import numpy as np
# Generate a 1D array of random floats in [0, 1) with 4 elements
random_floats_array = np.random.rand(4)
# Generate a 2D array of random floats in [0, 1) of shape 3x2
random_floats_matrix = np.random.rand(3, 2)
# Generate a 2D array of random integers in [10, 21) of shape 3x2
random_integers_matrix = np.random.randint(10, 21, size=(3,2))
print(random_floats_array)
print(random_floats_matrix)
print(random_integers_matrix)