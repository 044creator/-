from math import *

x1, x1_1 = sqrt(22), 4.69
x2, x2_2 = 2/21, 0.095

def f(x1, x2, x1_1, X2_2):
    dx1 = abs((x1 - x1_1) / x1) * 100
    dx2 = abs((x2 - x2_2) / x2) * 100
    if dx1 > dx2:
        print(dx1, ">", dx2)
        print("Друга рівність точніша")
    else:
        print(dx1, "<", dx2)
        print("Перша рівність точніша")

f(x1, x2, x1_1, x2_2)