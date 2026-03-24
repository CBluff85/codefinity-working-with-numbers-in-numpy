import numpy as np
# Simulated exam scores for three students in three subjects
exam_scores = np.array([[75, 82, 90], [92, 88, 78], [60, 70, 85]])
# Create an array with every column sorted by scores in descending order
top_scores_subject = np.sort(exam_scores, axis=0)[::-1]
# Create a 1D array of all scores sorted in ascending order
sorted_scores = np.sort(exam_scores, axis=None)
print(top_scores_subject)
print(sorted_scores)