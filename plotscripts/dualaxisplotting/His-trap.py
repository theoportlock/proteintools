#!/usr/bin/env python
'''
###########################################
edited by peo naughtcock

run with python His-trap.py <filename>.csv
###########################################
'''

import pandas as pd
import sys
import matplotlib.pyplot as plt

directory = sys.argv[1]

chrom_df = pd.read_csv(directory)

x = chrom_df['volume (ml)']
y = chrom_df['Absorbance (mAU)']
plt.plot(x,y)
plt.xlabel('Volume (mL)')
plt.ylabel('Absorbance (mAu)')

plt.savefig("result.png")

