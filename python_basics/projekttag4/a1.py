import numpy as np
import matplotlib.pyplot as plt

line = np.linspace(-10, 10, endpoint=True)


def func1(line):
    return line*3+5


def func2(line):
    return line**2


def func3(line):
    return line**.5


plt.plot(func1(line))
plt.plot(func2(line))
plt.plot(func3(line))
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")
plt.title("-10 - 10 Funktionen")
plt.legend(["Funktion 1", "Funktion 2", "Funktion 3"])

plt.show()
