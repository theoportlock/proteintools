#!/usr/bin/env python3
import pandas as pd
from Bio.PDB import Selection
from Bio.PDB import PDBParser
from Bio.PDB.NeighborSearch import NeighborSearch

actives = "15nNttA/ntta_activeairs"
structfile = "15nNttA/nttamtsl_bfacts.pdb"
outfile = "15nNttA/ntta_passiveairs"

'''
actives = "15nLspC/lspc_activeairs"
structfile = "15nLspC/lspctitrspin.pdb"
outfile = "15nLspC/lspc_passiveairs"
'''

with open(actives, "r") as f:
    airs = f.read()

rsnlist = airs.split(", ")
print(rsnlist)

p = PDBParser()
structures = p.get_structure("TEMP",structfile)
structure = structures[0]
atoms = Selection.unfold_entities(structure, 'A')

s = set()
for i in rsnlist:
    print(int(i))
    target_atom = structure[" "][int(i)]["HN"]
    ns = NeighborSearch(atoms)
    result = ns.search(target_atom.coord, 3)
    for j in result:
        s.add(j.get_parent().id[1])
        #print(s)

for i in rsnlist:
    s.discard(int(i))

out = ""
for i in s:
    out += str(i)
    out += ", "

print("final = ",out[:-2])

with open(outfile,"w") as f:
    f.write(out[:-2])
