import numpy as np
# Simulated exam scores for three students in three subjects
exam_scores = np.array([[75, 82, 90], [92, 88, 78], [60, 70, 85]])
# Use the flatten() method for flattening
exam_scores_flattened = exam_scores.flatten()
# Use the reshape() method for flattening
exam_scores_reshaped = exam_scores.reshape(-1)
# Use the ravel() method for flattening
exam_scores_raveled = exam_scores.ravel()
# Set the first element of the flattened copy to 100
exam_scores_flattened[0] = 100
print(exam_scores)