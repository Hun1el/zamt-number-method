import math

def f(x):
    return x**2 + math.exp(x) - 2
def bisection_method(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("Невозможно найти корень на данном интервале")
        return None
    d = []
    header = "| {:<10} | {:<10} | {:<10} | {:<10} |".format("n", "a", "b", "E")
    separator = "*------------*------------*------------*------------*"
    d.append(separator)
    d.append(separator)
    d.append(header)
    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        e = (b - a) / 2
        print(f"Итерация {i}:\n"
              f"  C{i} = {round(c, 4)}\n"  
              f"  f(C{i}) = {round(f(c), 4)}\n"
              f"  E{i} = {round(e, 4)}\n"
              f"{'-' * 45}")
        row = "| {:<10} | {:<10.4} | {:<10.4} | {:<10.3} |".format(i, a, b, e)
        d.append(row)
        d.append(separator)
        if f(c) == 0 or e < tol:
            return c, d
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        if e < 0.001:
            break
    return (a + b) / 2, d

a = float(input("Введите a: "))
b = float(input("Введите b: "))

tol = 5e-5
iter = 12

root, d = bisection_method(a, b, tol, iter)

if root is not None:
    print(f"\nf(x) = 0 на интервале ({a}, {b}) до 3-x знаков после запятой:", round(root, 3))
    print("Значение функции в найденном корне:", round(f(root), 3))
for row in d:
    print(row)
