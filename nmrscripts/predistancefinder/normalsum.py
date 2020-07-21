#!/usr/bin/env python3
'''
Finds the KD and makes a pretty figure
'''
import numpy as np
import matplotlib
import sys
import pandas as pd
import matplotlib.pyplot as plt
import os
import sympy
from scipy.optimize import curve_fit
from matplotlib import cm

A,B,X,Y = sympy.symbols("a,b,x,y")
eq = sympy.Eq(Y, ((1/(A*sympy.sqrt(2*sympy.pi)))*sympy.exp(-0.5*((X-B)/A)**2)))
eqy = sympy.solve(eq,Y)[0]
singlefunction = sympy.lambdify((X,A,B),eqy)
df = pd.read_csv("cleandf.csv")

summed_normal_distribution_function = 0
count = 0
for i in df.index:
    if df["bfac"][i] > 0:
        count += 1
        normal_distribution_function = eqy.subs({A:df["bfac"][i]*30,B:df["xvals"][i]})
        function = sympy.lambdify((X),normal_distribution_function)
        plt.scatter(df["xvals"][i],0)
        #x = np.linspace(-100, 250, 50000)
        #y = function(x)
        #plt.plot(x,y)
        summed_normal_distribution_function = normal_distribution_function + summed_normal_distribution_function

print(summed_normal_distribution_function)
function = sympy.lambdify((X),summed_normal_distribution_function)
x = np.linspace(-100, 250, 50000)
y = function(x)/count

plt.plot(x,y)
plt.tight_layout()
plt.show()
#plt.savefig("normal.svg")

'''
smallerrordf = df.loc[df["errB"]<1].copy()
print(smallerrordf["Predited Kd (mM)"].values.mean(),"pm",smallerrordf["Predited Kd (mM)"].values.std())
'''
