import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def sigmoid(x, a, b):
     y = 1 / (1 + np.exp(-b*(x-a)))
     return y

xdata = np.array([400, 600, 800, 1000, 1200, 1400, 1600])
ydata = np.array([0, 0, 0.13, 0.35, 0.75, 0.89, 0.91])

popt, pcov = curve_fit(sigmoid, xdata, ydata, p0=[1000, 0.001])
print(popt)

x = np.linspace(-1, 2000, 50)
y = sigmoid(x, *popt)

plt.plot(xdata, ydata, 'o', label='data')
plt.plot(x,y, label='fit')
plt.ylim(0, 1.05)
plt.legend(loc='best')
plt.savefig("test.svg")
