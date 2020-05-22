#!/usr/bin/env python3
import sys
import pandas as pd
import matplotlib.pyplot as plt
import os

# load data
file = "highestconcen.csv"
dfo = pd.read_csv(file,header=None)
x = list(dfo)[0]
y = list(dfo)[1]
df = dfo[[x,y]].copy()

# Curve smoothing
chnval = 0.06
df["chn"] = df[list(df)[1]].pct_change(periods = 50)
df["chn"] = df[df["chn"] < chnval]["chn"]
df.dropna(inplace=True)
df["chn"] = df[df["chn"] > -chnval]["chn"]
df.dropna(inplace=True)
df["chn"] = df[list(df)[1]].diff(periods = 5)
df["chn"] = df[df["chn"] < 0.9]["chn"]
df.dropna(inplace=True)
df["chn"] = df[df["chn"] > -0.9]["chn"]
df.dropna(inplace=True)

# Plotting
plt.plot(df[x], df[y])
#plt.xlabel(x)
#plt.ylabel(y) 
plt.tight_layout()
plt.show()
#plt.savefig("curves.svg")
