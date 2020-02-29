#!/usr/bin/env python
import numpy as np
import pandas as pd
import sys
import sigmoid
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

df = pd.read_csv(sys.argv[1])
xdata = df["x"]
ydata = df["y"]

plt.plot(xdata, ydata, 'o', label='data')
x = np.linspace(-1, 2000, 50)

for i in np.linspace(100,1200,num=2):
    for j in np.linspace(0,1, num=2):
        for k in np.linspace(80,120,num=2):
            popt, pcov = curve_fit(sigmoid.a, xdata, ydata, p0=[i, j, k])
            if pcov.any( > 4):
                pass
            else:
                y = sigmoid.a(x, *popt)
                plt.plot(x,y, label=popt)

plt.ylim(0, 1.05)
plt.legend(loc='best')
plt.savefig("test.svg")
