#!/usr/bin/env python
"""
Created on Mon Dec  9 16:30:41 2019

@author: bendorgan

###########################################
edited by peo naughtcock

run with python blot_plot.py <filename>.csv
###########################################
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

directory=sys.argv[1]

plt.rcParams['figure.dpi'] = 300

blot_df = pd.read_csv(directory)

ax = blot_df.plot.bar(x='Solublising agent', y='Mean (% sol)', width=0.7, yerr='StDev', error_kw=dict(lw=1, capsize=3, capthick=1), rot=0, legend=False)
ax.set_ylabel("% Extracted", fontsize=12)
ax.set_xlabel("Solublising agent", fontsize=12)

plt.savefig("result.png")
