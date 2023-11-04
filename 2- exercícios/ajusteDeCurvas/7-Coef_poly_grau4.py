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

x = [-4.4464, -3.9848, -3.9328, -3.651, -3.4011, -3.1079, -2.874, -2.4088, -2.3212, -2.0756, -1.6372, -1.4779, -1.3075, -1.0694, -0.6249, -0.4521, -0.2058, 0.2097, 0.2869, 0.6479, 0.9712, 1.2021, 1.4701, 1.7969, 2.0501, 2.1139, 2.41, 2.8104, 3.0292, 3.2627, 3.6279, 3.8436, 3.9871, 4.4056, 4.5879, 4.8079]
y = [2.2439, 5.1857, 5.0671, 5.7886, 6.6379, 7.1442, 7.0955, 6.8385, 7.3224, 6.7378, 5.6444, 5.2891, 5.3095, 4.9037, 4.6788, 4.6385, 5.2359, 4.4138, 4.327, 4.4178, 4.956, 5.0455, 5.7394, 6.2111, 7.0596, 6.6288, 7.5257, 8.1189, 8.9322, 9.2553, 8.9877, 8.3097, 8.8626, 7.998, 7.2177, 6.1472]

a0, a1, a2, a3, a4 = best_poly(x, y, 4)

print(f'{a0 = } , {a1 = }, {a2 = }, {a3 = }, {a4 = }')