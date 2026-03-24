import numpy as np
# Sales data for the past week (Monday to Sunday)
weekly_sales = np.array([150, 200, 170, 180, 160, 210, 190])
# Create a slice of weekly_sales with every second day's sales starting from the second day
alternate_day_sales = weekly_sales[1::2]
print(alternate_day_sales)