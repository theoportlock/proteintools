#!/usr/bin/env python
import pandas as pd
import sys
import matplotlib.pyplot as plt

directory = sys.argv[1]

df = pd.read_csv(directory)

df = df.ewm(com=5000).mean()
x = df['volume (ml)']
y = df['Absorbance (mAU)']
plt.plot(x,y)
plt.xlabel('Volume (mL)')
plt.ylabel('Absorbance (mAu)')

plt.savefig("result.png")
