import numpy as np

dimensions = (5, 5)

arr = np.random.RandomState(42).randint(1, 3, dimensions).reshape(*dimensions)

even_cols = np.arange(0, dimensions[1], 2)
odd_rows = np.arange(1, dimensions[0], 2)

added_cols_even = np.sum(arr[even_cols, :], axis=1, keepdims=True)
added_rows_odd = np.sum(arr[:, odd_rows], axis=0, keepdims=True)

print(arr)
print(added_cols_even)
print(added_rows_odd)
