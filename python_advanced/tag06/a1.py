import numpy as np

dimensions = (3, 5)

arr = np.random.randint(1, 101, dimensions).reshape(*dimensions)

print(arr)

arr0 = np.subtract.reduce(arr, axis=0, keepdims=True)
arr1 = np.subtract.reduce(arr, axis=1, keepdims=True)


print("Zeilen subtrahiert: \n", arr0)
print("Spalten subtrahiert: \n", arr1)

print("Vorzeichenumkehr: Zeilen subtrahiert: \n", np.negative(arr0))
print("Vorzeichenumkehr: Spalten subtrahiert: \n", np.negative(arr1))
