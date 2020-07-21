#!/usr/bin/env python3
import math
import numpy as np
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import sympy
from scipy.optimize import curve_fit

"assign (resid 56 and name HZ and segid B) (resid 53 and name HN and segid A) 21.0 9.0 9.0"
restraint_file = ""

df = pd.read_csv("ratiodata.csv")

t = 9e-3
k = 1.23e-32
omega_H = 800e6
# estimated from Nickanthis website and MW
tau_C = 6.086e-9

# Real R2
r2df = pd.read_csv("../../../../../4-ntta_structure/figures/nttarelaxation/t2params.csv")
df = df.merge(r2df,left_on="Number",right_on="Residue Number")
df["R2"] = df["DecayRate"]
print(df)

# Estimate R2 from reduced spectra
#df["R2"] =  1/df["N_G31C_MTSL_VITC.csv"]
#df["R2"] = df.apply(lambda row: math.exp(row["N_G31C_MTSL_VITC.csv"]),axis=1)
#df["R2"] = df.apply(lambda row: math.pi/row["N_G31C_MTSL_VITC.csvF1LW"],axis=1)
#df["R2"] = df.apply(lambda row: math.log(row["N_G31C_MTSL_VITC.csv"]),axis=1)

# Calculate R2SP
A,B,X,Y = sympy.symbols("a,b,x,y")
eq = sympy.Eq(A, (X*sympy.exp(-Y*B))/(X+Y))
eqy = sympy.solve(eq,Y)[0]
function = sympy.lambdify((X,A,B),eqy)
df["R2SP"] = df.apply(lambda row: eqy.subs({A:row["Iox/Ired"],B:t,X:row["R2"]}).evalf(), axis=1)
R,K,R2SP,WH,TC = sympy.symbols("r,k,r2sp,wh,tc")
eqdist = sympy.Eq(R, ((K/R2SP)*(4*TC + (3*TC)/(1 + (WH**2)*(TC**2))))**(1/6))
eqy = sympy.solve(eqdist,R)[0]

# Calculate r
df["r"] = df.apply(lambda row: eqy.subs({K:k,R2SP:row["R2SP"],WH:omega_H,TC:tau_C}).evalf(), axis=1)
print(df)
#df.to_csv("distances.csv")

#plt.scatter(df["Number"],df["r"]*1e8)
plt.scatter(df["Norm_Iox/Ired"],df["r"]*1e10)
plt.show()
#plt.savefig("PREdistance.svg")
