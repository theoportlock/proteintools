import pymol
import os
import sys
import pandas as pd
from pymol import cmd, stored, math

pymol.finish_launching()

cmd.load(sys.argv[1])

mol=os.path.splitext(sys.argv[1])[0]
soucecsv = sys.argv[2]
df = pd.read_csv(sourcecsv)

obj=cmd.get_object_list(mol)[0]

cmd.alter(mol,"b=0.0")

for resid in df:	
        cmd.alter("%s and resi %s"%(mol,resid), "b=%s"%df[resid])

cmd.save(mol+"_bfacts.pdb")
