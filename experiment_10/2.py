import numpy as np
array = np.array([[5, 8, 3],[1, 6, 9],[4, 2, 7]])
print(array)
row_sums = np.sum(array, axis=1)
column_sums = np.sum(array, axis=0)
second_max = np.sort(array.flatten())[-2]
print("Row_sums:", row_sums)
print("Column_sums:", column_sums)
print("Second_maximum_element:", second_max)
