#!/usr/bin/env python3
import numpy as np
import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os

def sigmoid(x, a, b, c):
     y = a / (1 + np.exp((b-x)/c))
     return y

file = "analysis.csv"
df = pd.read_csv(file)
x = list(df)[0]
y = list(df)[1]

popt, pcov = curve_fit(sigmoid,df[x],df[y],p0=[300,0.001,0.0002])
x2 = np.linspace(0,0.000325, 50)
y2 = sigmoid(x2, *popt)
print(popt)

plt.scatter(df[x], df[y])
plt.plot(x2, y2)
plt.ylabel(y) 
plt.xticks(rotation=90)
plt.xlabel(x)
#plt.show()
plt.savefig("sigmoid.svg")
