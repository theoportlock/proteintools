#!/usr/bin/env python3
import math
import numpy as np
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import sympy
from scipy.optimize import curve_fit

df = pd.read_csv("ratiodata.csv")

'''
should be correct
t = 9e-3
k = 1.23e-32
wh = 800e6
# estimated from Nickanthis website and MW (lspc is 7.278)
tc = 6.086e-9
'''

t = 9e-3
k = 1.23e-47
wh = 800e6
# estimated from Nickanthis website and MW
tc = 16e-9
r2 = math.pi/(df["N_G31C_MTSL_VITC.csvF1LW"].mean())
print(df["N_G31C_MTSL_VITC.csvF1LW"].mean())

# Calculate calibration curve and fit
RATIO, T, R2 , R2SP = sympy.symbols("RATIO, T , R2, R2SP")
eq = sympy.Eq(RATIO, (R2*sympy.exp(-R2SP * T))/(R2 + R2SP))
eqy = sympy.solve(eq, R2SP)[0]
r, K, WH, TC = sympy.symbols("r, K, WH, TC")
eqdist = sympy.Eq(r, ((K/eqy)*(4*TC + (3*TC)/(1 + (WH**2)*(TC**2))))**(1/6))
eqdisty = sympy.solve(eqdist, r)[0]
eqdistysubs = eqdisty.subs({
    T:t,
    K:k,
    WH:wh,
    R2:r2,
    TC:tc})
function = sympy.lambdify(RATIO,eqdistysubs,modules=['numpy','sympy'])
testratio = np.linspace(0.1,0.95,30)
testdistance = []
for i in testratio:
    testdistance.append(function(i))

df["r"] = df.apply(lambda row: function(row.loc["Norm_Iox/Ired"])*1e10,axis=1)
print(df)
#print(df)
df.to_csv("distances.csv")
#plt.scatter(df["Number"],df["r"])
#plt.scatter(df["Norm_Iox/Ired"],df["r"])
#plt.scatter(testratio,[i*1e10 for i in testdistance])
#plt.scatter(df["Iox/Ired"],df["r"]*1e10)

plt.show()
#plt.savefig("PREdistance.svg")

# Output the tbl file - Won't look good on the structure as there are a lot of missing datapoints, use the ratios for printing
restraint_file = ""
for i in df.index:
    if df["Norm_Iox/Ired"][i] < 0.8:
        restraint_file += "assign (resid 56 and name CA and segid A) (resid {} and name HN and segid B) {} 5.0 5.0\n".format(df["Number"][i],df["r"][i])
    else:
        restraint_file += "assign (resid 56 and name CA and segid A) (resid {} and name HN and segid B) 25.0 5.0 200.0\n".format(df["Number"][i])
#print(restraint_file)
with open("G56C.tbl","w") as f:
    f.write(restraint_file)
