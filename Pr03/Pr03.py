import math

def f(x):
    return x**3 - 3*x**2 - 24*x - 3

def f_prime(x):
    return 3*x**2 - 6*x - 24

def f_2prime(x):
    return 6*x - 6

def combined_method(a, b, tol, max_iter):
    d = []
    header = "| {:<10} | {:<10} | {:<10} | {:<10} |".format("n", "a_n", "b_n", "E_n")
    separator = "*------------*------------*------------*------------*"
    d.append(separator)
    d.append(header)

    for i in range(1, max_iter + 1):
        f_a = f(a)
        f_b = f(b)

        if f_a == f_b:
            print("Ошибка: Деление на ноль! Знаменатель равен нулю.")
            return None

        f2prime_a = f_2prime(a)
        f2prime_b = f_2prime(b)
        fprime_a = f_prime(a)
        fprime_b = f_prime(b)

        if f2prime_a * fprime_a > 0:
            a_n = a - f(a) * (b - a) / (f_b - f_a)
            b_n = b - f_b / f_prime(b)
        else:
            b_n = b - f_b * (b - a) / (f_b - f_a)
            a_n = a - f(a) / f_prime(a)
        e_n = abs(b_n - a_n)
        print(f"Итерация {i}:\n"
              f"  a_{i} = {round(a_n, 3)}\n"
              f"  b_{i} = {round(b_n, 3)}\n"
              f"  E_{i} = {round(e_n, 3)}\n"
              f"{'-' * 45}")
        row = "| {:<10} | {:<10} | {:<10} | {:<10} |".format(i, round(a_n, 3), round(b_n, 3), round(e_n, 3))
        d.append(row)
        d.append(separator)

        if e_n < tol or abs(f(a_n)) < tol:
            return (a_n + b_n) / 2, d
        a = a_n
        b = b_n
    print("Ошибка: Достигнуто максимальное количество итераций!")
    return None

def find_roots_in_intervals(intervals):
    for interval in intervals:
        print(f"\nИнтервал ({interval[0]}, {interval[1]}):")
        a = interval[0]
        b = interval[1]
        tol = 0.001
        max_iter = 12
        root, d = combined_method(a, b, tol, max_iter)
        if root is not None:
            print(f"Приближенный корень на интервале: ({a}, {b}): q =", round(root, 3))
        for row in d:
            print(row)

def get_intervals_from_user():
    intervals = []
    num_intervals = int(input("Введите количество интервалов: "))
    for i in range(num_intervals):
        a = float(input(f"Введите начало интервала {i+1}: "))
        b = float(input(f"Введите конец интервала {i+1}: "))
        intervals.append((a, b))
    return intervals

intervals = get_intervals_from_user()
find_roots_in_intervals(intervals)
