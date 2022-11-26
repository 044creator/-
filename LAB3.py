from math import *
from numpy import *
from scipy.misc import derivative

def search (x): #Допоміжна функція пошуку f(0)
    return (3*pow(x, 4)) - (4*pow(x, 3)) + (2*pow(x, 2)) - (4*x) - 1

# метод Ньютона

def nuton(a,b,eps):
    df2 = derivative(search, b, n = 2)
    if (search(b) * df2>0):
        xi = b
    else:
        xi = a
    df = derivative(search,xi, n= 1)
    xi_1 = xi - search(xi) / df
    while (abs(xi_1 - xi) > eps):
        xi = xi_1
        xi_1 = xi - search(xi) / df
    return print ('Метод Ньютона x = ', xi_1)

nuton (sqrt(3)/3, 1, 0.01)

# метод комбінований

def komb(a,b,eps):
    if (derivative(search, a, n = 1) * derivative(search, a, n = 2)>0):
        a0 = a
        b0 = b
    else:
        a0 = b
        b0 = a
    ai = a0
    bi = b0
    while abs(ai - bi) > eps:
        ai_1 = ai - search(ai)*(bi - ai)/(search(bi) - search(ai))
        bi_1 = bi - search(bi)/derivative(search,bi, n = 2)
        ai = ai_1
        bi = bi_1
    x = (ai_1 + bi_1)/2
    return print('Комбінований метод x = ', x)

komb(sqrt(3)/3, 1, 0.01)