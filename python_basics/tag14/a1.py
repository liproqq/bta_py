import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
print(x)

y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

plt.plot(x, y_sin, color="r", label="sin(x)")
plt.plot(x, y_cos, color="k", linestyle=":", label="cos(x)")
plt.plot(x, y_tan, color="b", linestyle="-.", label="tan(x)")
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")
plt.title("Funktionen")
plt.ylim(-1.05, 1.05)
plt.grid(0.1)
plt.legend()
plt.show()