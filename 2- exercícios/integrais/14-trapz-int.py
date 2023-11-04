import math

def trapz(f, a, b, n):
    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += f(a)
    soma += f(b)
    soma *= (h/2.0)
    print(f'Area aproximadamente: {soma}')

#def f(x):
 #   return math.sqrt(math.sin(math.cos(math.log(x**2 + 1) + 2) + 3) + 4)

def trapzPonto(x, y):
    tam = len(x) - 1
    somas = 0
    for i in range(tam):
        h = x[i+1] - x[i]
        somas += (h/2) * (y[i] + y[i+1])
    print(f'Area = {somas}')


x = [0, 10/3600, 20/3600, 30/3600, 40/3600, 50/3600, 60/3600]
y = [225.3, 110.56, 171.44, 191.23, 267.05, 154.21, 287.42]

intervalo = [0,60]
#subintervalos = [1, 22, 47, 50, 92, 138, 209, 263, 564, 972, 1845, 5145]

'''
n = len(subintervalos)
for i in range(n):
    trapz(f, intervalo[0], intervalo[1], subintervalos[i])
'''

trapzPonto(x, y)
