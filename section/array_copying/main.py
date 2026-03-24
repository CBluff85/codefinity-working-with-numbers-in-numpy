import numpy as np
# Simulated quarterly sales data for two products in 2021
sales_data_2021 = np.array([[350, 420, 380, 410],
                            [270, 320, 290, 310]])
# 1) Create a copy using the .copy() method
sales_data_2022 = sales_data_2021.copy()
# 2) Update the last two elements of the first row
sales_data_2022[0, -2:] = np.array([390, 370])
print(f'Quarterly sales in 2021:\n{sales_data_2021}')
print(f'Quarterly sales in 2022:\n{sales_data_2022}')