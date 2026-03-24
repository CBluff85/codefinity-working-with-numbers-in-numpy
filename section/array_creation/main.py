import numpy as np
# Create an array of even numbers from 2 to 21 exclusive
even_numbers = np.arange(2, 21, 2)
# Create an array of 10 equally spaced numbers between 5 and 6 exclusive
samples = np.linspace(5, 6, 10, endpoint=False)
print(even_numbers)
print(samples)