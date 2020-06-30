a = [20.1, 20.8, 21.9, 22.5, 22.7, 21.8, 21.3, 20.9, 20.1]

b = [ (C * 9/5)+32 for C in a]

print(f"Aufgabe ohne numpy: {b}")

import numpy as np

arr = np.array(a) * 9/5 + 32

print(f"Aufgabe ohne numpy: {arr}")