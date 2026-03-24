import numpy as np
arr = np.array([8, 18, 9, 16, 7, 1, 3])
# Calculate an average of the first, fourth and last elements 
average = (arr[0] + arr[3] + arr[-1]) / 3
print(average)