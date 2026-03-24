import numpy as np
# Temperatures recorded in two cities over four days
city_temperatures = np.array([[12, 18, 25, 14], [32, 20, 28, 35]])
# Retrieve the correct elements of city_temperatures
print(city_temperatures[(city_temperatures <= 15) | (city_temperatures > 30)])