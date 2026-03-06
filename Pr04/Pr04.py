import math
from tabulate import tabulate

def f(x):
    return math.log(x + 3) - x

def ffx(x):
    return abs(1 / (x + 3) - 1)

a = float(input("Введите 1 точку интервала: "))
b = float(input("Введите 2 точку интервала: "))
tol = 0.00001

if f(a) * f(b) < 0:
    c1 = (b + a) / 2
    fc1 = f(c1)
    delt1 = (b - a) / 2
    c2 = (c1 + b) / 2
    fc2 = f(c2)
    delt2 = (b - c1)
    c3 = (c1 + c2) / 2
    fc3 = f(c3)
    delt3 = (c2 - c1) / 2
    c4 = (c1 + c3) / 2
    fc4 = f(c4)
    delt4 = (c3 - c1) / 2
else:
    print("На отрезках разные знаки")

fi_a = ffx(c4)
fi_b = ffx(c3)

if max(fi_a, fi_b) < 1:
    q = max(fi_a, fi_b)
    accuracy = (tol * (1 - q)) / q
else:
    print("Значения производной > 1. Итер. процесс не сходится")

table = []
headers = ["n", "x_n", "x+3", "ln(x+3)", "E"]

n = 0
xn = (a + b) / 2
x_plus_3 = xn + 3
ln_x_plus_3 = math.log(x_plus_3)
E = None
table.append([n, xn, x_plus_3, ln_x_plus_3, E])

for n in range(1, 45):
    xn_new = math.log(xn + 3)
    x_plus_3 = xn_new + 3
    ln_x_plus_3 = math.log(x_plus_3)
    if ln_x_plus_3 == 0:
        break
    E = abs(ln_x_plus_3 - table[n - 1][3]) if n > 0 else None
    table.append([n, xn_new, x_plus_3, ln_x_plus_3, E])
    if abs(ln_x_plus_3 - xn_new) <= tol:
        break
    xn = xn_new

print(tabulate(table, headers=headers, floatfmt=".5f", tablefmt="grid"))
if ln_x_plus_3 != 0:
    print(f"q: {xn_new:.5f}")
else:
    print("Корень не найден, так как ln(x+3) равно 0.")

