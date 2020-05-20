#!/usr/bin/env python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy
from scipy.optimize import curve_fit

def make_f2opt(lambdified): return lambda *args : lambdified(*args)
# normal curve
'''
a,b,c,x,y = sympy.symbols("a,b,c,x,y")
eq = sympy.Eq(y, a*sympy.exp(-c*(b-x)**2))
eqy = sympy.solve(eq,y)[0]
function = sympy.lambdify((x,a,b,c),eqy)
eqy2opt = make_f2opt(eqy)
'''

# growth curve
'''
a,b,c,x,y = sympy.symbols("a,b,c,x,y")
eq = sympy.Eq(y, c / (1 + sympy.exp(-b*(x-a))))
eqy = sympy.solve(eq,y)[0]
function = sympy.lambdify((x,a,b,c),eqy)
eqy2opt = make_f2opt(function)
'''

# exponential decay
'''
A,B,C,X,Y = sympy.symbols("a,b,c,x,y")
eq = sympy.Eq(Y, A*sympy.exp(-B*X)+C)
eqy = sympy.solve(eq,Y)[0]
function = sympy.lambdify((X,A,B,C),eqy)
eqy2opt = make_f2opt(function)
'''

file = sys.argv[1]
df = pd.read_csv(file)
xdata = df[list(df)[0]]
ydata = df[list(df)[1]]

x = np.linspace(0, 2.5, 50)

# curve_fit
'''
popt, pcov = curve_fit(eqy2opt, xdata, ydata, p0=[1000, 0.001, 1])
y = function(x, *popt)
'''

# polyfit
'''
popt, pcov = np.polyfit(xdata, ydata, 5 , cov=True)
function = np.poly1d(popt)
y = function(x)
'''

print(popt)
psigma = np.sqrt(np.diag(pcov))
print(psigma)

# error tube
ylower = function(x,popt[0]+psigma[0],popt[1]+psigma[1],popt[2]-psigma[2])
yupper = function(x,popt[0]-psigma[0],popt[1]-psigma[1],popt[2]+psigma[2])
plt.fill_between(x,ylower,yupper,color='grey',alpha=0.5)

plt.plot(xdata, ydata, label='data')
plt.plot(x,y, label='fit')
plt.legend(loc='best')
plt.show()
#plt.savefig(os.path.splitext(file)[0]+".svg")
