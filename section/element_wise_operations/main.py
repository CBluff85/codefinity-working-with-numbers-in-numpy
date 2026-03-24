import numpy as np
# Simulated quarterly sales data for two products in 2021 and 2022
sales_data_2021 = np.array([[350, 420, 380, 410], [270, 320, 290, 310]])
sales_data_2022 = np.array([[360, 440, 390, 430], [280, 330, 300, 320]])
# Calculate the quarterly revenue growth for each product in percents
revenue_growth = (sales_data_2022-sales_data_2021) / sales_data_2021 * 100
# Rounding each of the elements to 2 decimal places
revenue_growth = np.round(revenue_growth, 2)
print(f'Revenue growth by quarter for each product:\n{revenue_growth}')