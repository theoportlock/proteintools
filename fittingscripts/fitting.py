#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import sympy
from scipy.optimize import curve_fit

a,b,c,x,y = sympy.symbols("a,b,c,x,y")

def make_f2opt(lambdified): return lambda *args : lambdified(*args)
eq = sympy.Eq(y, c / (1 + sympy.exp(-b*(x-a))))
eqy = sympy.lambdify((x,a,b,c),sympy.solve(eq,y)[0])
eqy2opt = make_f2opt(eqy)
xdata = np.array([400, 600, 800, 1000, 1200, 1400, 1600])
ydata = np.array([0, 0, 0.13, 0.35, 0.75, 0.89, 0.91])

popt, pcov = curve_fit(eqy2opt, xdata, ydata, p0=[1000, 0.001, 1])

print(popt)

x = np.linspace(-1, 2000, 50)
y = eqy(x, *popt)

plt.plot(xdata, ydata, 'o', label='data')
plt.plot(x,y, label='fit')
plt.ylim(0, 1.05)
plt.legend(loc='best')
plt.show()
#plt.savefig("test.svg")
