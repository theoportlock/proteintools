#!/usr/bin/env python3
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file = sys.argv[1]
df = pd.read_csv(file,header=[1,2],sep="\t")
a = df.columns.get_level_values(0)
b = df.columns.get_level_values(1)
df.columns = [a.to_series().mask(lambda x: x.str.startswith('Unnamed')).ffill(), b]

print(df.info())

fig, ax = plt.subplots(1,1)

x = list(df)[0]
y = list(df)[1]

ax.plot(df[x], df[y])
ax.set(ylabel=y) 
plt.xticks(rotation=90)
plt.xlabel(x)
plt.tight_layout()
plt.savefig("output.svg")
