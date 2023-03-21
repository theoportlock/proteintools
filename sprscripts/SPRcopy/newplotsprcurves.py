#!/usr/bin/env python3
# Added the baseline adjust script but didnt work as well
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy
from scipy.optimize import curve_fit
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.signal import find_peaks

file = "highestconcen.csv"
dfo = pd.read_csv(file,header=None)
x = list(dfo)[0]
y = list(dfo)[1]
df = dfo[[x,y]].copy()

def baseline_als(y, lam, p, niter=10):
    # Baseline Correction for Raman Spectra Using Improved Asymmetric Least Squares
    L = len(y)
    D = sparse.diags([1,-2,1],[0,-1,-2], shape=(L,L-2))
    D = lam * D.dot(D.transpose())
    w = np.ones(L)
    W = sparse.spdiags(w, 0, L, L)
    for i in range(niter):
        W.setdiag(w)
        Z = W + D
        z = spsolve(Z, w*y)
        w = p * (y > z) + (1-p) * (y < z)
    return z

df["baseline_y"] = baseline_als(df[list(df)[1]], 1000, 0.001, niter=10)

plt.plot(df[x], df["baseline_y"])
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
#plt.savefig("curves.svg")
