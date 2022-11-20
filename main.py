import matplotlib.pyplot as plt
import numpy as np

x_limit = [-200, 200]
koef = [-12, -18, 5, 10, -30]
color = 'r'


def func(x, a, b, c, d, e):
    return a * x ** 4 * np.sin(np.cos(x)) + b * x ** 3 + c * x ** 2 + d * x + e


x = np.arange(x_limit[0], x_limit[1], 0.1)

change_x = []
change_dir = 1

for i in range(len(x) - 1):
    if change_dir == -1:
        if func(x[i], *koef) < func(x[i + 1], *koef):
            change_x.append((x[i], func(x[i], *koef)))
            change_dir = 1
    else:
        if func(x[i], *koef) > func(x[i + 1], *koef):
            change_x.append((x[i], func(x[i], *koef)))
            change_dir = -1


def change_color():
    global color
    if color == 'r':
        color = 'b'
    else:
        color = 'r'
    return color


plt.figure(dpi=100, figsize=(10, 5))
current_x = np.arange(x_limit[0], change_x[0][0], 0.1)
plt.plot(current_x, func(current_x, *koef), change_color())
for i in range(len(change_x) - 1):
    current_x = np.arange(change_x[i][0], change_x[i + 1][0], 0.1)
    plt.plot(current_x, func(current_x, *koef), change_color())
current_x = np.arange(change_x[-1][0], x_limit[1], 0.1)
plt.plot(current_x, func(current_x, *koef), change_color())

plt.show()
