#!/usr/bin/env python3
import sys
from Bio import SeqIO, SearchIO
from Bio.Blast import NCBIWWW, NCBIXML

sequence = SeqIO.read(sys.argv[1], "fasta")
reshandle = NCBIWWW.qblast("blastn", "nt", sequence.seq)

#blast_result = NCBIXML.parse(reshandle)
blast_result = SearchIO.read(reshandle, "blast-xml")
SearchIO.write(blast_result, 'results.xml', 'blast-xml')
