import math

def simps(f, a, b, n):
    if n % 2 != 0 or n < 1:
        raise ValueError("n deve ser par e maior q 1")
    h = (b - a) / n
    soma_odd, soma_even = 0, 0
    for k in range(1,n,2):
        soma_odd += f(a+k*h)
    for k in range(2,n,2):
        soma_even += f(a + k * h)
    return (h/3) * (f(a) + 4 * soma_odd + 2 * soma_even + f(b))

def f(x):
    return math.sqrt(1 + math.cos(x)**2)

def simp(x0,x1,x3,y0,y1,y2):
    return ((x1-x0)/3)*(y0+4*y1+y2)

def simpsPonto(x, y):
    tam = (len(x) - 1) // 2
    somas = 0
    k = 0
    for i in range(tam):
        somas += simp(x[k],x[k+1],x[k+2],y[k],y[k+1],y[k+2])
        k += 2
    print(f'{somas}')


x = [0.953, 1.368, 1.783, 1.787, 1.791, 1.8045, 1.818, 1.959, 2.1, 2.5725, 3.045, 3.105, 3.165, 3.226, 3.287, 3.3165, 3.346, 3.5405, 3.735, 3.8325, 3.93]
y = [2.889, 2.389, 2.047, 2.045, 2.044, 2.038, 2.033, 2.002, 2.01, 2.322, 2.888, 2.939, 2.977, 2.998, 2.996, 2.987, 2.971, 2.695, 2.131, 1.785, 1.449]


intervalo = [0.953,3.93]
subintervalos = [4, 18, 32, 60, 98, 108, 132, 152, 194, 212, 278]

'''
n = len(subintervalos)
for i in range(n):
    print(simps(f, intervalo[0], intervalo[1], subintervalos[i]))
'''

simpsPonto(x, y)


