from math import *
from tabulate import tabulate
from scipy.integrate import quad

def f(x):
    return 1 + x + x**4

def f_2(x):
    return 4 * x**3

def f_4(x):
    return 24 

a = float(input("Введите 1-е число: "))
b = float(input("Введите 2-е число: "))

n_3 = 3
h_3 = (b - a) / n_3
y_3 = [a + i*h_3 for i in range(n_3 + 1)]
f_values3 = [f(y) for y in y_3]
y_3 = [round(y, 4) for y in y_3]
f_values3 = [round(fv, 4) for fv in f_values3]
table_3 = [["x"] + y_3, ["f(x)"] + f_values3]

print("Значение функции в точках (n = 3):")
print(tabulate(table_3, headers="firstrow", tablefmt="grid"))

i_t_3 = h_3 * (((f_values3[0] + f_values3[3]) / 2) + f_values3[1] + f_values3[2])
n_6 = 6
h_6 = (b - a) / n_6
y_6 = [a + i*h_6 for i in range(n_6 + 1)]
f_values6 = [f(y) for y in y_6]
y_6 = [round(y, 4) for y in y_6]
f_values6 = [round(fv, 4) for fv in f_values6]
table_6 = [["x"] + y_6, ["f(x)"] + f_values6]

print("Значение функции в точках (n = 6):")
print(tabulate(table_6, headers="firstrow", tablefmt="grid"))

i_t_6 = h_6 * (((f_values6[0] + f_values6[6]) / 2) + sum(f_values6[1:6]))
pog = abs((i_t_3 - i_t_6) / 3)
i_c_6 = (h_6 / 3) * (f_values6[0] + f_values6[6] + 4 * sum(f_values6[1:6:2]) + 2 * sum(f_values6[2:5:2]))
m4_a = f_4(a)
m4_b = f_4(b)
max_m4 = max(m4_a, m4_b)
v_6_c = max_m4 * (((b - a) ** 5) / (180 * n_6 ** 4))
m2_a = f_2(a)
m2_b = f_2(b)
max_m2 = max(m2_a, m2_b)
v_6_t = max_m2 * (((b - a) ** 3) / (12 * n_6 ** 2))
i_nl, error = quad(f, a, b)

print(f"Формула трапеций (n=3): {i_t_3:.6f}")
print(f"Формула трапеций (n=6): {i_t_6:.6f}")
print(f"Формула Симпсона: {i_c_6:.6f}")
print(f"Формула Ньютона-Лейбница: {i_nl:.6f}")

print(f"Погрешность формулы трапеций: {v_6_t:.6f}")
print(f"Погрешность по Рунге: {pog:.6f}")
print(f"Погрешность Симпсона : {v_6_c:.6f}")
