def heun(f,x0,y0,h,n):
    r = []
    for _ in range(n):
        m1 = f(x0,y0)
        m2 = f(x0 + h, y0 + h * m1)
        y1 = y0 + h *(m1 + m2) / 2
        x0 += h
        y0 = y1
        r.append((x0,y0))
    return r

#Q9 Prova:
def f(x,y):
    return 0.0755 * y - 37441

x0, y0 = 0,1929228
e = heun(f,x0,y0, h=0.0625,n=int(1/0.0625))

for xi, yi in e:
    print(xi, yi)