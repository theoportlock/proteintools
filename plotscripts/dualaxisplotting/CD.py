#!/usr/bin/env python
import pandas as pd
import sys
import matplotlib.pyplot as plt

directory = "2019-10-09 HRCTD HisTrap 3L prep.csv"

df = pd.read_csv(directory)

df = df.ewm(com=5000).mean()
x = df['volume (ml)']
y = df['Absorbance (mAU)']
plt.plot(x,y)
plt.xlabel('Volume (mL)')
plt.ylabel('Absorbance (mAu)')

plt.show()
#plt.savefig("result.svg")
