#!/usr/bin/env python3

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def sigmoid(x, a, b, c):
     y = c / (1 + np.exp(-b*(x-a)))
     return y

def normal(x,a,b,c,d):
    y = d*np.exp(-c*(a-x)**2)+b
    return y

'''
#for sig
xdata = np.array([400, 600, 800, 1000, 1200, 1400, 1600])
ydata = np.array([0, 0, 0.13, 0.35, 0.75, 0.89, 0.91])
'''

print("loading file...")
file = sys.argv[1]
#encoding = 'UTF-16'
df = pd.read_csv(file,header=[1,2],sep="\t")
a = df.columns.get_level_values(0)
b = df.columns.get_level_values(1)
df.columns = [a.to_series().mask(lambda x: x.str.startswith('Unnamed')).ffill(), b]
print("done\n")

#for norm
xdata = df[list(df)[0]]
ydata= df[list(df)[1]]

print(xdata)
popt, pcov = curve_fit(normal, xdata, ydata, p0=[1000, 0.01, 0.0001,1.2])
print(popt)

x = np.linspace(0, 2000, 50)
y = normal(x, *popt)

fig, ax = plt.subplots(1,1)
ax.plot(x, y)
plt.plot(xdata, ydata, 'o', label='data')
plt.plot(x,y, label='fit')
ax.set(ylabel=y) 
plt.xticks(rotation=90)
plt.xlabel(x)
plt.tight_layout()
plt.savefig(os.path.splitext(file)[0]+".svg")
