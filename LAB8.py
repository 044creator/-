import numpy as np
from math import factorial


x = [0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23]
y = [5.5154, 5.4669, 5.3263, 5.1930, 5.0664, 4.9461, 4.8317, 4.7226, 4.6185, 4.5191, 4.4242]
h = x[1] - x[0]
x1 = 0.189
x2 = 0.227
q = (x1 - x[0]) / h
q1 = (x2 - x[-1]) / h

def n(y,j): #обчислення кінцевих різниць
    mas=[]
    for i in range(len(y)):
        mas.append(y[i] - y[i-1])
    mas.pop(0)
    if j == 1:
        return mas
    else:
        j-=1
        return n(mas, j)

#Перша інтерполяційна формула Ньютона
s_1 = y[0]+q*n(y,1)[0]+q*(q-1)*n(y,2)[0]/factorial(2)
s_2 = q*(q-1)*(q-2)*n(y,3)[0]/factorial(3)
s_3 = q*(q-1)*(q-2)*(q-3)*n(y,4)[0]/factorial(4)
s_4 = q*(q-1)*(q-2)*(q-3)*(q-4)*n(y,5)[0]/factorial(5)
n_1 = s_1 + s_2 + s_3 + s_4
print ('Значення x1 =', x1, 'по первій інтерполяційній формулі', round(n_1,4))

#Друга інтерполяційна формула Ньютона
s_1 = y[-1]+q1*n(y,1)[-1]+q1*(q1+1)*n(y,2)[-1]/factorial(2)
s_2 = q1*(q1+1)*(q1+2)*n(y,3)[-1]/factorial(3)
s_3 = q1*(q1+1)*(q1+2)*(q1+3)*n(y,4)[-1]/factorial(4)
s_4 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*n(y,5)[-1]/factorial(5)
n_1 = s_1 + s_2 + s_3 + s_4

print ('Значення x2 =', x2, 'по другій інтерполяційній формулі', round(n_1, 4))