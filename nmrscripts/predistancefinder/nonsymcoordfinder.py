#from sympy import symbols, lambdify, pi, exp, solve, Eq, sqrt
import numpy as np
import math
import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(X, A, B):
    return (1/(A*np.sqrt(2*np.pi))) * np.exp(-0.5*((X-B)/A)**2)

datafile = "cleandf.csv"
df = pd.read_csv(datafile)

x = "xvals"
y = "bfac"

popt, pcov = curve_fit(func, df[x], df[y], p0=[5, 2])

x2 = np.linspace(-30, 50, 100)
y2 = func(x2, *popt)

print(popt)

psigma = np.sqrt(np.diag(pcov))
print(psigma)
'''
ylower = func(x2,popt[0]+psigma[0],popt[1]+psigma[1])
yupper = func(x2,popt[0]-psigma[0],popt[1]-psigma[1],popt[2]-psigma[2])
plt.fill_between(x2,ylower,yupper,color='grey',alpha=0.5)
'''
plt.scatter(df[x], df[y])
plt.plot(x2, y2)
plt.ticklabel_format(style='plain')
