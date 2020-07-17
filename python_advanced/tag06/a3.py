import numpy as np

arr = np.zeros((3, 5), dtype="int")
arr[:, range(1, arr.shape[1], 2)] += 1
print(arr)
arr[range(1, arr.shape[0], 2), :] += 1
print(arr)
