a = [1, 5, 8, 4, 7, 3]
b = [i+3 for i in a]
print(f"Aufgabe 4 ohne numpy:\t {b}")

import numpy as np

arr = np.array(a)

arr2 = arr + 3

print(f"Aufgabe 4 mit numpy:\t  {arr2}")

print(arr2[2:4])