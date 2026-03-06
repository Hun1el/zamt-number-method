import numpy as np

A = np.array([[9.9, -1.5, 2.6],
              [0.4, 13.6, -4.2],
              [0.7, 0.4, 7.1]])
b = np.array([0, 8.2, -1.3])

D = np.diag(np.diag(A))
D_inv = np.linalg.inv(D)
B = D_inv @ (D - A)
c = D_inv @ b
x = np.zeros_like(b)

E = 0.001
max_iter = 25
for i in range(max_iter):
    x_n = B @ x + c
    if np.linalg.norm(x_n - x) < E:
        print("Сходимость достигнута на итерации", i + 1)
        x = x_n
        break
    x = x_n
    print("Итерация", i + 1, ", текущее решение:", x.round(3))
else:
    print("Достигнуто максимальное количество итераций")
print("Полученное решение:", x.round(3))

