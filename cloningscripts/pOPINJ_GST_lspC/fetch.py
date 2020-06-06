#!/usr/bin/env python3
from Bio import SeqIO
from pydna.genbank import Genbank

gb = Genbank("zn.tportlock@gmail.com")

genome = gb.nucleotide("GCA_000211115")
SeqIO.write(genome, "genome.fasta", "fasta")
