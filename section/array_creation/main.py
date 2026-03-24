import numpy as np
# Create an array of zeros of size 5
zeros_array_1d = np.zeros(5)
# Create an array of zeros of shape 2x4
zeros_array_2d = np.zeros((2,4))
# Create an array of ones of size 3
ones_array_1d = np.ones(3)
# create an array of ones of shape 2x3
ones_array_2d = np.ones((2,3))
# Create an array of sevens of shape 2x2
sevens_array_2d = np.full((2,2), 7)
print(f'1D zeros array: {zeros_array_1d}, 1D ones array: {ones_array_1d}')
print(f'2D zeros array:\n{zeros_array_2d}')
print(f'2D ones array:\n{ones_array_2d}')
print(f'2D sevens array:\n{sevens_array_2d}')