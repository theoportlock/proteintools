import sympy
from Bio.PDB import Selection
from Bio.PDB import PDBParser
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

infile = "plusN80C/ntta_bfacts.pdb"
outfile = "plusN80C/cleandf.csv"

p = PDBParser()
structures = p.get_structure("NttA", infile)
#NttA = structures[0][" "]
NttA = structures[0]["B"]

atoms = list(NttA.get_atoms())
justhn = list()
for atom in atoms:
    if atom.get_name()=="HN":
        justhn.append(atom)
        
cleandf = pd.DataFrame(columns=["xvals","yvals","zvals","bfac"])
for i,j in enumerate(justhn):
    coord = j.get_coord()
    fac = j.get_bfactor()
    cleandf.loc[i] = [coord[0],coord[1],coord[2],fac]

cleandf.to_csv(outfile)
