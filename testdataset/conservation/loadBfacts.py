import pymol
from numpy import nan
import os
import sys
import pandas as pd
from pymol import cmd, stored, math

pymol.finish_launching()
cmd.load(sys.argv[1])

mol=os.path.splitext(sys.argv[1])[0]
sourcecsv = sys.argv[2]

df = pd.read_csv(sourcecsv)

resi = list(df)[0]
df[resi] = df[resi].astype('int')
val = list(df)[1]


obj=cmd.get_object_list(mol)[0]

cmd.alter(mol,"b=0.0")

def normal(x,mn,mx):
    return round((x-mn)/(mx - mn),4)

mn = df[val].min()
mx = df[val].max()

for row in df.index:	
    newval = normal(df[val][row],mn,mx)
    cmd.alter("resi %s"%df[resi][row], "b=%s"%newval)
cmd.spectrum("b","blue_red",minimum=0,maximum=1)
cmd.save(mol+"_bfacts.pdb")
