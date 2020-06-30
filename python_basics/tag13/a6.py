a = [1, 5, 8, 4, 7, 3, 2, 2, 6, 8]

b = sum(a)/len(a)

print(f"Aufgabe 6 ohne numpy: {b}")

import numpy as np

print(f"Aufgabe 6 mit numpy: {np.array(a).mean()}")