#!/usr/bin/env python3
from Bio import SeqIO
from pydna.genbank import Genbank

gb = Genbank("zn.tportlock@gmail.com")

#genome = gb.nucleotide("NC_002942.5")
genome = gb.nucleotide("NZ_CAFM00000000.1")
print(genome)
#SeqIO.write(genome, "lgenome.fasta", "fasta")
#ntta = gb.nucleotide("LN901282")
#SeqIO.write(ntta, "ntta.fasta", "fasta")
