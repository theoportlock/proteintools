#!/usr/bin/env python3
import sys
from Bio import SeqIO
from Bio.Alphabet import generic_dna, generic_protein
from Bio.Blast import NCBIWWW, NCBIXML

sequence = SeqIO.read(sys.argv[1], "fasta")

reshandle = NCBIWWW.qblast("blastn", "nt", sequence.seq)
blast_result = NCBIXML.parse(reshandle)
            
for b in blast_result:
    for alignment in b.alignments:
        for hsp in alignment.hsps:
            print('Align')
            print('Sequence:', alignment.title)
            print('length:', alignment.length)
            print('e value:', hsp.expect)
            print(hsp.query[0:75] + '...')
            print(hsp.match[0:75] + '...')
            print(hsp.sbjct[0:75] + '...')
            print("")
