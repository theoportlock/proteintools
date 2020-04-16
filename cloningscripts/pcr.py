#!/usr/bin/env python3
import pandas as pd
from pydna.dseqrecord import Dseqrecord
from Bio.SeqRecord import SeqRecord
from pydna import amplify
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import generic_dna, generic_protein

lgenome = SeqIO.read("lgenome.fasta", "fasta")
lgenome = Dseqrecord(lgenome,circular=True)

protein = "ntta"
df = pd.read_csv('primers.csv',usecols = ["Name","Complete sequence"])
primers = df.loc[(df["Name"]==protein+" F") | (df["Name"]==protein+" R")]["Complete sequence"].values

fprimer = Seq(primers[0])
rprimer = Seq(primers[1])
rprimer_rec = SeqRecord(rprimer,id="rev")
fprimer_rec = SeqRecord(fprimer,id="fwd")
result = amplify.Anneal((fprimer_rec,rprimer_rec),lgenome) 
