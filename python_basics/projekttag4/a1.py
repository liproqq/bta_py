import numpy as np
import matplotlib.pyplot as plt

line = np.linspace(-10, 10, endpoint=True)


def func1(line):
    return line*3+5


def func2(line):
    return np.square(line)


def func3(line):
    return np.sqrt(line)


plt.plot(line, func1(line), label="x*3+5")
plt.plot(line, func2(line), label="x²")
plt.plot(line, func3(line), label="√x")
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")
plt.title("Funktionen")
plt.legend()

plt.show()
