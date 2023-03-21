import pymol
import os
from numpy import nan
import sys
import pandas as pd
from pymol import cmd, stored, math

pymol.finish_launching()
cmd.load(sys.argv[1])

mol=os.path.splitext(sys.argv[1])[0]
sourcecsv = sys.argv[2]

df = pd.read_csv(sourcecsv)
resi = "Number"
df[resi] = df[resi].astype('int')
val = "pymol"

obj = cmd.get_object_list(mol)[0]

cmd.alter(mol,"b=0.0")

for row in df.index:	
    cmd.alter("resi %s"%df[resi][row], "b=%s"%df[val][row])
cmd.save(mol+"_bfacts.pdb")
