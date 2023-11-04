import math

def RK2(f, x0, y0, h, n, b=0.981):
    a = 1 - b
    p = 1 / (2 * b)
    q = p
    for _ in range(n):
        m1 = f(x0,y0)
        m2 = f(x0+p*h, y0+q*h*m1)
        y0 += (a * m1 + b * m2) * h
        x0 += h
        yield [x0,y0]


#Q11 Prova:
def f(x,y):
    return -y/(math.sqrt(8.217**2 - y**2)) # a

x0, y0 = 1.239, 5.725
e = RK2(f,x0,y0, h=0.086,n=10)
for xi, yi in e:
    print(xi, yi)