import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-2.99, 4, 75)
x2 = np.linspace(-5, 4, 75)

y1 = np.log(x1 + 3)
y2 = x2

plt.figure(figsize=(8, 6))

plt.plot(x1, y1, label="y = ln(x+3)")
plt.plot(x2, y2, label="y = x")
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)

plt.text(6, 0.2, "x", fontsize=12)
plt.text(0.2, 4, "y", fontsize=12)

plt.title("Графики функций")
plt.legend()

plt.axis("equal")
plt.show()

