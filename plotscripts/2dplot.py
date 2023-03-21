#!/usr/bin/env python
import sys
import pandas as pd
import matplotlib.pyplot as plt
import os

#df = pd.read_csv(sys.argv[1])
df = pd.read_csv("analysis_mean.csv")
x = list(df)[0]
y = list(df)[1]

plt.bar(df[x], df[y])
plt.ylabel(y) 
plt.xlabel(x)
plt.tight_layout()
plt.show()
#plt.savefig(os.path.splitext(sys.argv[1])[0]+".svg")
