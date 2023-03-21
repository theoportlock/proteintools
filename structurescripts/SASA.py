import pymol
import os
import sys
import pandas as pd
from pymol import cmd, stored

pymol.finish_launching()

cmd.set('dot_solvent', 1)
cmd.set('dot_density', 3)

cmd.load(sys.argv[1])
stored.residues = []
cmd.iterate('name ca', 'stored.residues.append(resi)')

sasa_per_residue = []
for i in stored.residues:
    lst=[i,cmd.get_area('resi %s' % i)]
    sasa_per_residue.append(lst)

column_names = ["Residue_Number", "SASA"]
df = pd.DataFrame(sasa_per_residue, columns = column_names)
df.set_index("Residue_Number",inplace=True)

df.to_csv(os.path.splitext(sys.argv[1])[0]+"_SASA.csv")
