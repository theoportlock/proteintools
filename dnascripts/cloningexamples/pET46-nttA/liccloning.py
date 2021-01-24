import pandas as pd
from pydna.dseq import Dseq
from pydna.dseqrecord import Dseqrecord
from pydna import amplify
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Restriction import Restriction
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
nttapcr = result.products[1].reverse_complement().seq.lower()

record = SeqIO.read("pet46.fasta", "fasta", generic_dna)
plasseq = Dseq(str(record.seq),circular=True)

linearvector = Dseqrecord(plasseq[plasseq.find("ccgggcttctcctc"):plasseq.find("gacgacgac")])
linearntta = Dseqrecord(nttapcr[nttapcr.find("gacgacgac"):nttapcr.find("ccgggcttctcctc")])
completevector = linearvector + linearntta
finishedvector = completevector.looped()
SeqIO.write(finishedvector, "ntta-pet46.fasta", "fasta")

import orffinder
orf_list = orffinder.find_orfs_with_trans(finishedvector.seq,15,100)
for start, end, strand, pro in orf_list:
    print("%s...%s - length %i, strand %i, %i:%i" % (pro[:30], pro[-3:], len(pro), strand, start, end))
