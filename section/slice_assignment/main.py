import numpy as np
# Product prices
prices = np.array([15, 8, 22, 7, 12, 5])
# Assign 20 to every price greater than 10
prices[prices > 10] = 20

# Product ratings for two categories over three criteria
ratings = np.array([[6, 8, 9], [7, 5, 10]])
# Assign an array with elements 9, 8 to the last two elements of the second row of ratings
ratings[1, 1:] = np.array([9, 8])

print(prices)
print(ratings)