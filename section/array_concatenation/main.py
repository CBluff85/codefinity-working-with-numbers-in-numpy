import numpy as np
# Simulated data for quarterly sales of two products in 2021 and 2022
sales_data_2021 = np.array([[350, 420, 380, 410], [270, 320, 290, 310]])
sales_data_2022 = np.array([[370, 430, 400, 390], [280, 330, 300, 370]])
# Concatenate the sales data for both products by columns
combined_sales_by_product = np.concatenate((sales_data_2021,sales_data_2022), axis = 1)
print(f'Combined sales by product:\n{combined_sales_by_product}')