import sys
import pandas as pd
from Bio.PDB import Selection
from Bio.PDB import PDBParser

# load new b factors
csvfile = "/home/theoportlock/thesis/chapters/6-cn_complex/figures/PRE/15nNttA/plusG56C/ratiodata.csv"
df = pd.read_csv(csvfile)
resi = "Number"
bfactorvalue = "pymol"

# load structure
#pdbfile = sys.argv[1]
pdbfile = "/home/theoportlock/thesis/chapters/6-cn_complex/figures/PRE/15nNttA/plusG56C/ntta.pdb"
p = PDBParser()
structures = p.get_structure("",pdbfile)
structure = structures[0]

'''
# select HN
atoms = list(structure.get_atoms())
selected_atom_type = list()
for atom in atoms:
    if atom.get_name()=="HN":
        selected_atom_type.append(atom)
'''
        
for i in df.index:
    structure['B'][i]['N'].set_bfactor(df[bfactorvalue][i])
    print(structure['B'][i]['N'].get_bfactor())

# export new structure
from Bio.PDB import PDBIO
outfile = 'bfacts-' + pdbfile
io = PDBIO()
io.set_structure(structure['B'])
io.save("outfile.pdb")
