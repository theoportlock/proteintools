#!/usr/bin/env python3
import numpy as np
import matplotlib
import sys
import pandas as pd
import matplotlib.pyplot as plt
import os
import sympy
from scipy.optimize import curve_fit
from matplotlib import cm

conc_of_analyte = 0.4

# Fitting scripts preamble
def make_f2opt(lambdified): return lambda *args : lambdified(*args)
# hyperbolic tan
A,B,X,Y = sympy.symbols("a,b,x,y")
eq = sympy.Eq(Y, B*sympy.tanh(B*X))
eqy = sympy.solve(eq,Y)[0]
function = sympy.lambdify((X,A,B),eqy)
eqy2opt = make_f2opt(function)

# Load data
df = []
files = ["0.csv","1.csv","2.csv","3.csv","4.csv","5.csv","6.csv","7.csv","8.csv","9.csv"]
for i,x in enumerate(files):
    df.append(pd.read_csv(x))
    df[i]["Molar Excess"]=i
    df[i]["Concentration of titrant (mM)"]= conc_of_analyte * i
'''
for x in range(len(sys.argv)-1):
    df.append(pd.read_csv(sys.argv[x+1]))
    df[x]["Molar Excess"]=x
'''

# Merge datasets
big_df = pd.concat(df,ignore_index=True)
x = 'Assign F1'
y = 'Position F1'

gb = big_df.groupby(x)
colour = big_df[x].unique()
for i in big_df[x].unique():
    gbdf = gb.get_group(i)
    gbdf["Normalised" + y] = np.abs(gbdf[y] - gbdf.loc[gbdf["Molar Excess"]==0][y].values)
    xdata = gbdf["Concentration of titrant (mM)"]
    ydata = gbdf["Normalised" + y]
    # curve_fit
    if len(gbdf) > 2:
        try:
            popt, pcov = curve_fit(eqy2opt, xdata, ydata, p0=[1, 1])
            fitx = np.linspace(0, 3.6, 50)
            fity = function(fitx, *popt)
            #colour=cm.rainbow(np.linspace(0, 1, len(big_df[x].unique())))
            plt.plot(fitx,fity,c=colour) 
            plt.scatter(xdata,ydata,marker="+",c=colour)
        except RuntimeError:
            print("fit failed")

'''
plt.ylabel(y) 
plt.xlabel(x)
'''
plt.tight_layout()
plt.show()
#plt.savefig("output.svg")
