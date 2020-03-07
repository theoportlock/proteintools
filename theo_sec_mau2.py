#!/usr/bin/env python3
import sys
import pandas as pd
import matplotlib.pyplot as plt
<<<<<<< HEAD
import numpy as np

file = sys.argv[1]
df = pd.read_csv(file,header=[1,2],sep="\t")
=======
import os

file = sys.argv[1]
df = pd.read_csv(file,header=[1,2],encoding='UTF-16',sep="\t")
>>>>>>> 0d008dabe5a551c7c043a69eda750b55f2c1db0f
a = df.columns.get_level_values(0)
b = df.columns.get_level_values(1)
df.columns = [a.to_series().mask(lambda x: x.str.startswith('Unnamed')).ffill(), b]

<<<<<<< HEAD
print(df.info())

=======
>>>>>>> 0d008dabe5a551c7c043a69eda750b55f2c1db0f
fig, ax = plt.subplots(1,1)

x = list(df)[0]
y = list(df)[1]

ax.plot(df[x], df[y])
ax.set(ylabel=y) 
plt.xticks(rotation=90)
plt.xlabel(x)
plt.tight_layout()
<<<<<<< HEAD
plt.savefig("output.svg")
=======
plt.savefig(os.path.splitext(file)[0]+".svg")
>>>>>>> 0d008dabe5a551c7c043a69eda750b55f2c1db0f
