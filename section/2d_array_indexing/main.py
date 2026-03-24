import numpy as np
# Creating a 5x5 matrix representing stock prices
stock_prices = np.array([
    [120, 130, 140, 150, 160],
    [210, 220, 230, 240, 250],
    [310, 320, 330, 340, 350],
    [410, 420, 430, 440, 450],
    [510, 520, 530, 540, 550]
])
# Retrieve all the stock prices of the first company over five days with a positive index
first_company_prices = stock_prices[0]
# Retrieve the stock price of the third company on the second day with positive indices
third_company_second_day_price = stock_prices[2,1]
# Retrieve the stock price of the last company on the last day with negative indices
last_company_last_day_price = stock_prices[-1,-1]
print(first_company_prices)
print(third_company_second_day_price)
print(last_company_last_day_price)