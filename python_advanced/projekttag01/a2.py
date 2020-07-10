import numpy as np


def calcSurface(height, radius):
    base = np.square(radius) * np.pi
    latSurface = radius * np.pi * np.sqrt(np.square(radius)+np.square(height))
    surface = base + latSurface

    return surface


li1 = [np.random.uniform(1, 11) for i in range(10)]
li2 = [np.random.uniform(1, 11) for i in range(10)]

# stack two lists and transpose to get 2d from 11d
pairs = np.array((li1, li2)).T

for pair in pairs:
    print(calcSurface(*pair))
