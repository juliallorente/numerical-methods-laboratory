def true_euler(f, k, x0, y0, h, n):
    for i in range(n):
        y0 += h * f(x0, y0, k)
        x0 += h        
        #print(f'x_{i + 1}={x0} e y_{i+1}={y0}')
    print(f'{y0}')

def euler_mid(f, k, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0, k)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1, k)
        y0 = y0 + h * m2
        x0 += h
        yield x0, y0

if __name__ == '__main__':
    def f(x, y, k):
        return k*y + 66501 # valor de v
    
    x0, y0 = 0.0, 1262692 # x0 = t, y0 = individuos
    h = 0.0625
    k = 0.0792 # gama
    n = int(1 / h)
    #true_euler(f, k, x0, y0, h, n)

    r2 = euler_mid(f, k, x0, y0, h, n)
    x2, y2 = zip(*r2)
    print(y2)
