#!/usr/bin/env python3
from Bio import SeqIO
from pydna.genbank import Genbank

gb = Genbank("zn.tportlock@gmail.com")

lgenome = gb.nucleotide("NC_002942.5")
SeqIO.write(lgenome, "lgenome.fasta", "fasta")
ntta = gb.nucleotide("LN901282")
SeqIO.write(ntta, "ntta.fasta", "fasta")
