import numpy as np
# Employee salaries
salaries = np.array([45000, 38000, 52000, 47000, 43000, 39000])
# Sort the salaries in descending order
sorted_salaries = np.sort(salaries)[::-1]
# Print top 3 salaries
print(sorted_salaries[:3])