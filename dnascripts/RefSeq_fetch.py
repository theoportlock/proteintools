#!/usr/bin/env python3
from Bio import SeqIO
from pydna.genbank import Genbank

signin = input("input user email: ")
gb = Genbank(signin)
gene_name = input("input RefSeq: ")
gene = gb.nucleotide(gene_name)
SeqIO.write(gene, gene_name + ".fa", "fasta")
