def RK2(f, x0, y0, h, n, b=0.689):
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
    return y*(1-x)+x+2

x0, y0 = 1.126, 1.922
e = RK2(f,x0,y0, h=0.132,n=10)
for xi, yi in e:
    print(xi, yi)