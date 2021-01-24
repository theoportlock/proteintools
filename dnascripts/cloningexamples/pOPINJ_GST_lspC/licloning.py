import pandas as pd
from pydna.dseq import Dseq
from pydna.dseqrecord import Dseqrecord
from pydna import amplify
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Restriction import Restriction
from Bio.Alphabet import generic_dna, generic_protein

genome = SeqIO.read("130b.fasta", "fasta")
genome = Dseqrecord(genome,circular=True)

protein = "LspC-GST-fixed"
#protein = "10421"

df = pd.read_csv('primers.csv',usecols = ["Name","Complete sequence"])
primers = df.loc[(df["Name"]==protein+" F") | (df["Name"]==protein+" R")]["Complete sequence"].values

fprimer = Seq(primers[0])
rprimer = Seq(primers[1])
rprimer_rec = SeqRecord(rprimer,id="rev")
fprimer_rec = SeqRecord(fprimer,id="fwd")

result = amplify.pcr((fprimer_rec,rprimer_rec),genome) 
pcr = result.seq
SeqIO.write(SeqRecord(pcr,id="LspC-GST"), "LspC-GST.fasta", "fasta")

record = SeqIO.read("addgene-plasmid-26045-sequence-12221.gbk", "genbank")
plasseq = Dseq(str(record.seq),circular=True)

Fover = Dseq("AAGTTCTGTTTCAGGG") #CCCG
Rover = Dseq("TGGTCTAGAAAGCT") #TTAT removed first base 

plasseq = plasseq.cut(Restriction.KpnI,Restriction.HindIII)[1].fill_in()

print(pcr.find(Fover))
print(pcr.find(Rover.rc()))
print(plasseq.find(Fover))
print(plasseq.find(Rover.rc()))

#TAATACGACTCACTATAGGG - T7

#print("cutplasseq ",plasseq)
linearvector = plasseq[plasseq.find(Rover.rc()):plasseq.find(Fover)]
pcranneal= pcr[pcr.find(Fover):pcr.find(Rover.rc())]

completevector = linearvector + pcranneal
finishedvector = Dseqrecord(completevector.looped())
SeqIO.write(finishedvector, "pOPINJ-lspcper.fasta", "fasta")

import orffinder
orf_list = orffinder.find_orfs_with_trans(finishedvector.seq,15,100)
for start, end, strand, pro in orf_list:
    print("%s...%s - length %i, strand %i, %i:%i" % (pro[:30], pro[-3:], len(pro), strand, start, end))
