#!/usr/bin/env python3
import sys
import pandas as pd
import matplotlib.pyplot as plt
import os

file = sys.argv[1]
df = pd.read_csv(file,header=[1,2],encoding='UTF-16',sep="\t")
a = df.columns.get_level_values(0)
b = df.columns.get_level_values(1)
df.columns = [a.to_series().mask(lambda x: x.str.startswith('Unnamed')).ffill(), b]

x = list(df)[0]
y = list(df)[1]

plt.plot(df[x], df[y])
plt.ylabel("Absorbance at 260 nm ") 
plt.xticks(rotation=90)
plt.xlabel("Elution Volume / " + x[1])
plt.tight_layout()
plt.savefig(os.path.splitext(file)[0]+".svg")
