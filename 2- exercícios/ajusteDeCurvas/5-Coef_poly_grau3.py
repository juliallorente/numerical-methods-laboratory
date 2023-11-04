import numpy as np
# import scipy as sp

def best_poly (x, y, k):
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que k (o grau do polinônmio)')

    somas = {}
    somas[0] = n
    for n in range(1, 2*k + 1):
        somas[n] = sum(xi ** n for xi in x)
    A = []
    B = []
    for i in range (k + 1):
        row = []
        for j in range(k + 1):
            row.append(somas[i + j])
        A.append(row)
        if i == 0:
            B.append(sum(y))
        else:
            B.append(sum(xi ** i * yi for xi, yi in zip(x,y)))
    return np.linalg.solve(A, B)

x = [-4.8205, -4.4127, -4.3415, -3.8798, -3.639, -3.2906, -2.9451, -2.6697, -2.2212, -1.8053, -1.6862, -1.1559, -0.9223, -0.7014, -0.3743, 0.0588, 0.1853, 0.5747, 0.8539, 1.2837, 1.5605, 1.8679, 2.1604, 2.5373, 3.0728, 3.2142, 3.6838, 3.9431, 4.3507, 4.3956, 4.9846, 5.3337, 5.4208, 5.933]
y = [4.8364, 5.8717, 6.0612, 6.8779, 7.1867, 7.3356, 7.5964, 7.4222, 7.4121, 7.3741, 7.0777, 6.356, 6.4393, 6.3518, 5.8545, 5.3437, 5.3834, 4.9014, 4.6807, 4.1462, 3.5892, 3.8214, 3.4675, 3.5388, 3.4782, 3.1178, 3.8988, 4.2699, 5.085, 4.8835, 6.5581, 7.6607, 8.5137, 10.9946]

a0, a1, a2, a3 = best_poly(x, y, 3)

print(f'{a0 = } , {a1 = }, {a2 = }, {a3 = }')