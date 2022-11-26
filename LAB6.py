from numpy import *
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

x = array([-2, -1, 0, 1], dtype=float)
y = array([-7, 4, 1, 2], dtype=float)


def Langranz(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z

xNew = linspace(min(x), max(x), 1000)
yNew = [Langranz(x, y, i) for i in xNew]
plt.plot(x, y, "o", xNew, yNew)
plt.title("Langrange Polynomial")
plt.grid(True)
plt.show()