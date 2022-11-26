import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.sin(x)

x = np.array ([i*0.1 for i in range(1, 11 )]) # задаємо x генератором списків
y = np.array(func(x))
print ('x =',x)
print ('y =',y)

mean_x = np.mean(x) #середнє значення х
mean_y = np.mean(y) #cереднє значення y

mean_x2 = np.mean(x**2)
mean_xy = np.mean (x*y)

print(' Середній х =', mean_x, '\n', 'Середній у =', mean_y, '\n', 'Середній ху =', mean_xy, '\n', 'Середній х2 = ',mean_x2)
a1 = (mean_xy - mean_x*mean_y)/(mean_x2-(np.mean(x))**2)
a0 = mean_y - (a1* mean_x)

print('Коефіцієнти: ', 'a0=', round(a0,4), 'a1=', round(a1,4))

plt.plot(x, a0 + a1*x, 'r', label='Линия')
plt.scatter(x, y, 20, label='Точки')

plt.title('Метод найменших квадратів')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()