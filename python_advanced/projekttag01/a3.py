from multiprocessing import Pool, current_process
import numpy as np


def calcSurface(*args):
    height, radius = args[0][0], args[0][1]
    base = np.square(radius) * np.pi
    latSurface = radius * np.pi * np.sqrt(np.square(radius)+np.square(height))
    surface = base + latSurface
    print(f"Surface {surface:.2f} of process {current_process().pid}")
    return surface


li1 = [np.random.uniform(1, 11) for i in range(10)]
li2 = [np.random.uniform(1, 11) for i in range(10)]

# stack two lists and transpose to get 2d from 10d
pairs = np.array((li1, li2)).T

if __name__ == "__main__":
    pool = Pool()

    result = pool.map(calcSurface, pairs)

    print("Result: ", result)
