import numpy as np
# Simulated quarterly sales data for two products in 2021
sales_data_2021 = np.array([350, 420, 380, 410, 270, 320, 290, 310])
# Reshape the sales data to a 2D array using the appropriate method
sales_data_2021 = np.reshape(sales_data_2021, (2,4))
print(f'Quarterly sales in 2021 for product 1: {sales_data_2021[0]}')
print(f'Quarterly sales in 2021 for product 2: {sales_data_2021[1]}')