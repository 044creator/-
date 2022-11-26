from math import *

x0 = 0.65
y0 = 0.55

def f1(x):
    return (1 + sin(x-0.5))/2
def f2(y):
    return -cos(y)+1.5

def iter(x, y, e):
    xn = x
    yn = y
    xn1 = f1(x)
    yn1 = f2(y)
    n = 1
    while ((abs(xn1-xn)>=e)&(abs(yn1-yn)>=e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n += 1
    print("Итерации:")
    print('x =', xn, '\ny =', yn, '\nКоличество итераций = ', n)
iter(x0, y0, 0.0001)
