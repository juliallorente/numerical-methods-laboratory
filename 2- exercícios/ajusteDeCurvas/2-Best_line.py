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
x = [0.0778, 0.2285, 0.3042, 0.4816, 0.5059, 0.6085, 0.7259, 0.8837, 1.0801, 1.0849, 1.2723, 1.431, 1.4995, 1.6476, 1.7172, 1.9034, 1.9905, 2.1141, 2.1717, 2.3795, 2.47, 2.6121, 2.671, 2.8421, 3.0091, 3.0184, 3.1968, 3.3247, 3.3804, 3.5282, 3.6643, 3.7408, 3.9142, 4.0407, 4.1522, 4.2891, 4.3883, 4.5299, 4.6261, 4.7425, 4.9127, 5.0345, 5.0873, 5.1877, 5.3902, 5.4986, 5.6375, 5.7672, 5.8452, 5.9792, 6.0378, 6.2339, 6.2672, 6.44, 6.6171, 6.7345, 6.7913, 6.9452, 7.0716, 7.1472, 7.2398, 7.4655, 7.4936, 7.6492, 7.7961, 7.9114, 8.0227, 8.1106, 8.2523, 8.3459, 8.5355, 8.5663, 8.7651, 8.8495, 8.9272, 9.1513, 9.1986, 9.3373, 9.4915, 9.5685, 9.7404, 9.8513, 9.9085]
y = [3.3646, 3.4894, 3.5746, 4.6865, 5.3877, 4.3311, 4.3849, 4.5736, 4.6574, 4.5248, 4.9285, 5.1907, 5.3012, 5.3017, 5.5143, 5.9691, 5.6754, 6.1648, 7.9825, 6.6644, 6.5903, 6.5027, 6.9276, 6.7753, 6.9213, 6.986, 7.2083, 7.5899, 8.4447, 7.9326, 7.991, 8.638, 8.2782, 7.5183, 8.4314, 8.861, 9.5193, 8.9231, 9.1206, 9.1141, 8.8305, 8.8448, 10.4734, 9.1023, 10.1664, 10.0131, 10.4652, 11.3561, 10.5068, 9.9438, 10.7948, 11.2309, 11.056, 11.4242, 11.399, 11.8129, 12.3076, 11.8297, 11.8286, 11.2642, 12.4218, 12.142, 12.6955, 11.9328, 11.7588, 13.0712, 11.3556, 13.6718, 13.3224, 13.4385, 13.8125, 13.6298, 13.8856, 14.1443, 14.51, 14.2417, 14.6689, 13.7473, 13.388, 14.1073, 14.7824, 15.3886, 16.0951]

a0, a1 = best_line(x, y)

print(f'{a0 = } e {a1 = }')