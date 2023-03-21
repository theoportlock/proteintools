#!/usr/bin/env python3
'''
A script that finds the open reading frames in a fasta file
'''
import sys
from Bio import SeqIO, Seq
from pydna.dseq import Dseq

record = SeqIO.read(open(sys.argv[1]), "fasta")
readingframes = [Seq.translate(record.seq[i:], table='Standard', stop_symbol='*', to_stop=False, cds=False) for i in range(3)]

results = []
for frame in readingframes:
    for peptide in frame.split('*'): #Split translation over stopcodons
        if len(peptide[peptide.find("M"):]) > 100:
            results.append(peptide[peptide.find("M"):])

for i in results:
    print(i)

with open('ORF.txt', 'w') as output: 
    for peptide in results:
        output.write("{}\t{}\n".format(len(peptide), peptide))
