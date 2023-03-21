#!/usr/bin/env python3
import sys
from Bio import SeqIO, SearchIO
from Bio.Blast import NCBIWWW, NCBIXML

sequence = SeqIO.read(sys.argv[1], "fasta")
with NCBIWWW.qblast("blastn", "nt", sequence.seq) as reshandle:
    with open("results.xml", "w") as xml_file:
        xml_file.write(reshandle.read())

#blast_result = SearchIO.read(reshandle, "blast-xml")
#SearchIO.write(blast_result, 'results.xml', 'blast-xml')

blast_qresult = SearchIO.read("results.xml", 'blast-xml')
records = []
for hit in blast_qresult:
    records.append(hit[0].hit)
SeqIO.write(records, "results.fa", "fasta")
