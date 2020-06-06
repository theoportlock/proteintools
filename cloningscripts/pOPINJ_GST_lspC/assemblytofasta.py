from pydna.dseqrecord import Dseqrecord
from Bio import SeqIO

genome = SeqIO.read("GCF_000211115.1_ASM21111v2.fna","fasta")
records = list(SeqIO.parse("GCF_000211115.1_ASM21111v2.fna", "fasta"))

fullgenome = ""
for i in records:
    fullgenome += i.seq
    
genome = Dseqrecord(fullgenome,circular=True)
SeqIO.write(genome, "130b.fasta", "fasta")
