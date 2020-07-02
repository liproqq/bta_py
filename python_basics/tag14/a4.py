# Aufgabe:

# Schreibe ein Programm, welches 100 mal mit zwei (sechsseitigen) Würflen würfelt.
# Gib die die Häuffigkeit der Summe der Augenpaare in einem Histogramm aus.

# (z.B: Wie häufig wurde die Summe 7 gewürfelt, oder die Summe 13 oder...)


import numpy as np
import matplotlib.pyplot as plt

start, end, size = 1, 7, 10000

x1 = np.random.randint(start, end, size)
x2 = np.random.randint(start, end, size)

x3 = x1 + x2
bins = np.arange(2,14) -0.5

n, bins, patches = plt.hist(x3, bins, edgecolor="k")
plt.show()
