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

x = [-4.0978, -3.9133, -3.6207, -3.338, -3.2335, -3.0929, -2.7721, -2.6375, -2.333, -1.9757, -1.9005, -1.7181, -1.3718, -1.2484, -0.905, -0.7925, -0.38, -0.2549, 0.0213, 0.3304, 0.5156, 0.7431, 0.8045, 1.1827, 1.367, 1.5996, 1.8175, 2.1073, 2.3542, 2.4709, 2.8028, 2.898, 3.2681, 3.5119, 3.7486, 3.9409, 4.2493]
y = [4.0489, 3.7961, 6.5524, 6.3337, 6.9593, 7.1258, 6.6881, 5.7914, 6.7923, 5.0524, 4.6179, 4.7485, 4.0342, 4.2472, 4.0831, 3.703, 4.593, 5.4049, 4.9549, 5.4477, 5.4114, 5.9578, 6.738, 6.4916, 4.681, 5.5529, 5.3726, 4.7696, 4.2511, 4.215, 3.5008, 2.2574, 2.7, 3.3284, 3.7519, 5.2379, 7.4875]

a0, a1, a2, a3, a4, a5 = best_poly(x, y, 5)

print(f'{a0 = } , {a1 = }, {a2 = }, {a3 = }, {a4 = }, {a5 = }')