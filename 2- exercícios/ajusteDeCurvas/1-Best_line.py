import numpy as np

def best_line(x, y):
    n = len(x)
    # soma das coordenadas x
    sum_x = sum(x)
    # soma das coordenadas x**2
    sum_x2 = sum(xi ** 2 for xi in x)
    # soma das coordenadas y
    sum_y = sum(y)
    #soma das coordenadas x*y
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    # Matriz dos coeficientes
    A = [[n, sum_x], [sum_x, sum_x2]]
    # Matriz dos termos independentes
    B = [sum_y, sum_xy]

    return np.linalg.solve(A, B)

# exemplo:
x = [0.2425, 0.4441, 0.7044, 1.041, 1.4846, 1.7121, 2.1722, 2.2759, 2.535, 3.0876, 3.2495, 3.7358, 3.983, 4.2306, 4.5366, 4.8182, 5.0298, 5.5081, 5.7567, 6.1234, 6.3679, 6.812, 6.9611, 7.2854, 7.5239, 8.1033, 8.2798, 8.5242, 8.8026, 9.1974, 9.6658, 9.9926]
y = [1.8741, 2.0369, 1.1305, 1.0371, 0.7347, 0.1858, -0.217, -0.3728, -0.9992, -1.218, -1.4081, -1.8223, -2.2975, -2.7196, -3.0228, -4.3099, -3.4301, -3.8281, -4.2322, -4.3367, -5.0144, -5.0391, -5.256, -5.6887, -5.8928, -6.3678, -6.8442, -7.1516, -7.099, -7.9491, -8.0695, -8.7276]

a0, a1 = best_line(x, y)

print(f'{a0 = } e {a1 = }')
