import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np

x = [0.4, 0.6, 0.9, 1.2, 2]
y = [2.45, 1.63, 0.95, 0.73, 1.95]

spl = UnivariateSpline(x, y) #Побудова сплайна
xs = np.linspace(0.4, 2, 1000)
plt.plot(x,y,'ro', xs, spl(xs), 'g')
plt.show()
