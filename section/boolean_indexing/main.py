import numpy as np
# Ratings of various products
product_ratings = np.array([4, 2, 5, 3, 7, 1])
# Retrieve the correct elements of product_ratings
print(product_ratings[(product_ratings>= 3) & (product_ratings != 5)])