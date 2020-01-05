from Bio.Seq import Seq
from Bio.Alphabet import *
import pandas as pd

df = pd.read_csv("ProteinDatabase.csv")
test = Seq(df["DNAseq"][0], generic_dna).transcribe().translate()
print(test)
#for a,b in enumerate(df["DNAseq"]):
#    df["AAseq"][a]=Seq(b, generic_dna).transcribe()
