import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 50)
y1 = np.exp(x)
y2 = 2 - x**2

plt.figure(figsize=(8, 6))

plt.plot(x, y1, label="y = e^x")
plt.plot(x, y2, label="y = 2 - x^2")
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)

plt.text(6, 0.2, "x", fontsize=12)
plt.text(0.2, 7, "y", fontsize=12)

plt.title("Графики функций")
plt.legend()

plt.axis("equal")
plt.show()
