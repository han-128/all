def f1(x, y):
    return 2**(x)-x+y-2

def f2(x, y):
    return (x-1)**2+y**2-1

def fy(x, y):
    return -2**(x) + x + 2

def fx(x,y):
    return -y**2/x+2

def ff(p):
    x, y=p
    return (f1(x, y), f2(x, y))
kol_yakobi, kol_gaus, kol_new = 0, 0, 0


def met_yakobi(x0, y0, eps):
    global kol_yakobi
    k = 0
    x1 = fx(x0, y0)
    y1 = fy(x0, y0)
    while abs(x0 - x1) > eps or abs(y0 - y1) > eps:
        k += 1
        x0 = x1
        y0 = y1
        x1 = fx(x0, y0)
        y1 = fy(x0, y0)
    kol_yakobi = k
    otv = [x1, y1]
    return otv


def met_gaus_zen(x0, y0, eps):
    k = 1
    x1 = fx(x0, y0)
    y1 = fy(x0, y0)
    while abs(x0 - x1) > eps or abs(y0 - y1) > eps:
        k += 1
        x0 = x1
        y0 = y1
        x1 = fx(x0, y0)
        y1 = fy(x1, y0)
    global kol_gaus
    kol_gaus = k
    otv = [x1, y1]
    return otv


def met_newton(x0, y0, eps):
    k = 1
    dx = x0
    dy = y0
    while (abs(dx) > eps) and (abs(dy) > eps):
        k += 1
        f1_val = f1(x0, y0)
        f2_val = f2(x0, y0)
        f1_dx = 2**x0*log(abs(x0)) - 1
        f1_dy = 1
        f2_dx = 2 * x0 - 2
        f2_dy = 2 * y0
        dx = (f1_dy * f2_val - f2_dy * f1_val) / (f1_dx * f2_dy - f2_dx * f1_dy)
        dy = (f1_val * f2_dy - f2_val * f1_dx) / (f1_dx * f2_dy - f2_dx * f1_dy)
        #dy = - (f1_val + f1_dx * dx) / f1_dy
        x0 = x0 + dx
        y0 = y0 + dy
    global kol_new
    kol_new = k
    otv = [x0, y0]
    return otv
x0 = 1
y0 = 1
eps = 0.01

otv_yakobi = met_yakobi(x0, y0, eps)
otv_gaus = met_gaus_zen(x0, y0, eps)
otv_new = met_newton(x0, y0, eps)