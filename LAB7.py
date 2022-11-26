import numpy as np
import math
arrayX = [4.5, 5.0, 5.5, 6.0 , 6.5, 7.0]
arrayY = [8.442, 8.482, 8.862, 9.701, 11.132, 13.302]

#Шаг
step = arrayX[1] - arrayX[0]

array_1, array_2, array_3, array_4 = [], [], [], []

for i in range(len(arrayY)):
    array_1.append(arrayY[i] - arrayY[i-1])
array_1.pop(0)

for j in range(len(array_1)):
    array_2.append(array_1[j] - array_1[j-1])
array_2.pop (0)

for k in range(len(array_2)):
    array_3.append(array_2[k] - array_2[k-1])
array_3.pop (0)

for l in range(len(array_3)):
    array_4.append(array_3[l] - array_3[l-1])
array_4.pop (0)

y1 = 1/step * (array_1[1] - (array_2[1]/ 2) + (array_3[1] /3) - (array_4[1]/4))
y2 = 1/ (step**2) * (array_2[1] - array_3[1] + 11/12*array_4[1])

print ('First derivative =', y1)
print ('Second derivative =', y2)
