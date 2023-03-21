#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
from Bio.PDB import Selection
from Bio.PDB import PDBParser

infile = "nttamtsl_bfacts.pdb"
outfile = ""

p = PDBParser()
structures = p.get_structure("complex",infile)

NttA = structures[0]["B"]
LspC = structures[0]["A"]
        
nttaarray = [i.id[1] for i in NttA]
lspcarray = [i.id[1] for i in LspC]
final = pd.DataFrame(index=lspcarray,columns=nttaarray)
for i in nttaarray:
    for j in lspcarray:
        final.loc[j,i] = NttA[i]["CA"]-LspC[j]["CA"]

print(final)
final.to_csv("test.csv")
        
out = final.apply(pd.to_numeric, errors='ignore')

#plt.imshow(out,extent=[nttaarray[0],nttaarray[-1],lspcarray[0],lspcarray[-1]])
plt.imshow(out,extent=[nttaarray[0],nttaarray[-1],lspcarray[-1],lspcarray[0]],cmap='afmhot')
#plt.yticks(out.index)
#plt.xticks(out.columns)
plt.show()
