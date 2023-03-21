#!/usr/bin/env python3
import numpy as np
import matplotlib
import sys
import pandas as pd
import matplotlib.pyplot as plt
import os
import sympy
from scipy.optimize import curve_fit
from matplotlib import cm

# Load data
dfformatted = []
files = ["N_G31C_MTSL_VITC.csv","N_G31C_MTSL.csv"]
for i, x in enumerate(files):
    df = pd.read_csv(x)
    result = df['Assign F1'].str.split('(\d+)([A-Z][a-z]+)H',expand=True)
    result = result.loc[:,[1,2]]
    result.rename(columns={1:'Number', 2:'Type'}, inplace=True)
    df["Number"] = result["Number"]
    df["Type"] = result["Type"]
    df.rename(columns={"Line Width F1 (Hz)":x+"F1LW"}, inplace=True)
    df.rename(columns={"Height":x}, inplace=True)
    dfformatted.append(df.loc[:,["Number","Type",x,x+"F1LW"]])

# Merge datasets
#big_df = pd.concat(dfformatted,axis=1,join='inner').reindex(dfformatted[0].index).reset_index()
big_df = dfformatted[0].loc[:,["Number","Type",files[0],files[0]+"F1LW"]].merge(dfformatted[1].loc[:,["Number",files[1]]],left_on="Number",right_on="Number")
big_df["Number"].astype(np.float64)

# for filling in the gaps
#print(s.reindex(range(s.index.min(),s.index.max()+1)))

# Calculate ratios
big_df["Iox/Ired"] = big_df[files[1]].abs() / big_df[files[0]].abs()
big_df["Norm_Iox/Ired"] = big_df["Iox/Ired"]/big_df["Iox/Ired"].max().astype(np.float64)
big_df["pymol"] = 1-big_df["Norm_Iox/Ired"]
print(big_df)
#big_df.to_csv("ratiodata.csv")

#plt.plot(big_df["Number"].astype(np.int),big_df["Norm_Iox/Ired"])
plt.bar(big_df["Number"].astype(np.int),big_df["Norm_Iox/Ired"])
#plt.bar(big_df["Number"].astype(np.int),big_df["Iox/Ired"])
plt.savefig("Histogram.svg")
#plt.show()
