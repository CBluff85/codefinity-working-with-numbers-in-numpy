import numpy as np
# Simulated exams scores of three students from three subjects
exams_scores = np.array([[100, 82, 95], [56, 70, 90], [45, 98, 66]])
coefficients = np.array([0.5, 0.3, 0.2])
# Calculate the dot product between exam_scores and coefficients
final_scores = np.dot(exams_scores,coefficients)
print(final_scores)