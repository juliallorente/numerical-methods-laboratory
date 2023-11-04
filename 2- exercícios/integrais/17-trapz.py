import math

from numpy import double


def trapz(f, a, b, n):
    h = (b-a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k*h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h/2) * soma


def f(x):
    return -x*(x-21)*(x+1)
a = 0
b = 12
n = 31


r = trapz(f, a, b, n)

print(r)