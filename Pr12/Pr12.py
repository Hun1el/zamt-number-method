from math import e
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

x_0 = float(input("Введите x_0: "))
y_0 = float(input("Введите y_0: "))
h = float(input("Введите шаг: "))

def func(x, y):
    return e**x + y

a_x = [x_0]
a_y = [y_0]
tab = PrettyTable()
tab.field_names = ["x_i", "y*_i", "y_i", "E_i"]

for i in range(10):
    vr1 = h * func(x_0, y_0)
    vr2 = h * func(x_0 + h / 2, y_0 + vr1 / 2)
    ys = y_0 + vr2
    y_0 = y_0 + vr1
    x_0 = x_0 + h
    a_x.append(x_0)
    a_y.append(ys)
    E = abs(ys - y_0)
    tab.add_row([round(x_0, 3), round(ys, 3), round(y_0, 3), round(E, 3)])

print(tab)

x_new = np.linspace(0, 0.99, 10)
spl = interp1d(a_x, a_y)
y_new = spl(x_new)

plt.plot(x_new, y_new)
plt.plot(a_x, a_y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y(x)')
plt.grid(True)
plt.legend()
plt.show()