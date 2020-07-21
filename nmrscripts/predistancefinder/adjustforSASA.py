#!/usr/bin/env python3
import pandas as pd
from Bio.PDB import Selection
from Bio.PDB import PDBParser
from Bio.PDB.NeighborSearch import NeighborSearch

'''
# nttapassive
sasadir = "15nNttA/ntta_buriedresn"
airdir = "15nNttA/ntta_passiveairs"
outdir = "15nNttA/ntta_passiveairs_adj"
'''
# nttaactive
sasadir = "../SASA/ntta_buriedresn"
airdir = "15nNttA/ntta_activeairs"
outdir = "15nNttA/ntta_activeairs_adj"
'''
# lspcpassive
sasadir = "15nLspC/lspc_buriedresn"
airdir = "15nLspC/lspc_passiveairs"
outdir = "15nLspC/lspc_passiveairs_adj"
'''
'''
# lspcactive
sasadir = "15nLspC/lspc_buriedresn"
airdir = "15nLspC/lspc_activeairs"
outdir = "15nLspC/lspc_activeairs_adj"
'''

with open(airdir, "r") as f:
    airs = f.read()

with open(sasadir, "r") as f:
    sasa = f.read()

rsnlist = set(airs.split(","))
sasalist = set(sasa.split(","))

print("csi list: ",rsnlist)
print("sasa list: ",sasalist)

for i in sasalist:
    rsnlist.discard(i)

out = ""
for i in rsnlist:
    out += i
    out += ","

print("final = ",out[:-1])

with open(outdir,"w") as f:
    f.write(out[:-1])
